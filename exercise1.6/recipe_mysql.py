import mysql.connector

# Connect to user
conn = mysql.connector.connect(
    host='localhost', user='cf-python', passwd='password'
)

# initialize cursor object from conn
cursor = conn.cursor()

# create & use new database
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

# create new table Recipes
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
               id INT PRIMARY KEY AUTO_INCREMENT,
               name VARCHAR(50),
               ingredients VARCHAR(255),
               cooking_time INT,
               difficulty VARCHAR(20)
)''')

# Main menu


def main_menu(conn, cursor):
    choice = ""
    while (choice != 'quit'):
        print(20*"=" + "\nMain Menu" + '\n' + 20*'=')
        print(" 1. Create new recipe ")
        print(" 2. Search recipe by ingredient ")
        print(" 3. Update existing recipe ")
        print(" 4. Delete recipe ")
        print(" 5. View all recipes ")
        print(" \nEnter 'quit' to exit program" + '\n')
        choice = input("Enter your choice: ")
        print(20*"=")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            view_all_recipes(conn, cursor)

# function to create recipe


def create_recipe(conn, cursor):
    recipe_ingredients = []
    name = str(input("Name of recipe: "))
    cooking_time = int(input("Cooking time in mins: "))
    ingredients = str(
        input("Enter ingredients (separate with comma & space): "))
    recipe_ingredients.append(ingredients)
    difficulty = calculate_difficulty(cooking_time, recipe_ingredients)

    # convert ingredient list into comma-separated string
    ingredients_str = ', '.join(recipe_ingredients)

    # insert recipe into table
    sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    val = (name, ingredients_str, cooking_time, difficulty)
    cursor.execute(sql, val)

    # commit change
    conn.commit()

    print("\nRecipe saved into database")

# function to calculate recipe difficulty based on cooking time and no. of ingredients


def calculate_difficulty(cooking_time, recipe_ingredients):
    if cooking_time < 10 and len(recipe_ingredients) < 4:
        difficulty = 'Easy'

    elif cooking_time < 10 and len(recipe_ingredients) >= 4:
        difficulty = 'Medium'

    elif cooking_time >= 10 and len(recipe_ingredients) < 4:
        difficulty = 'Intermediate'

    elif cooking_time >= 10 and len(recipe_ingredients) >= 4:
        difficulty = 'Hard'

    return difficulty


def search_recipe(conn, cursor):
    all_ingredients = []

    # cursor fetch ingredients
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    for ingredients_list in results:
        for recipe_ingredients in ingredients_list:
            recipe_ingredients_list = recipe_ingredients.split(", ")
            all_ingredients.extend(recipe_ingredients_list)

    # remove duplicates
    all_ingredients = list(dict.fromkeys(all_ingredients))

    # add number to ingredient
    all_ingredients_list = list(enumerate(all_ingredients))

    print("All ingredients: ")

    for index, tup in enumerate(all_ingredients_list):
        print(str(tup[0]+1) + ". " + tup[1])

    try:
        ingredient_num = input(
            "\nEnter ingredient number you want to select: ")
        ingredient_index = int(ingredient_num) - 1
        ingredient_searched = all_ingredients_list[ingredient_index][1]
    except:
        print('Unexpected error.')
    else:
        print('\n' + 20*"=" +
              '\nBelow recipes with selected ingredient: ' + '\n' + 20*'=')

        sql = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
        val = ('%' + ingredient_searched + '%', )

        cursor.execute(sql, val)

        recipe_results = cursor.fetchall()

        for row in recipe_results:
            print('\nID: ', row[0])
            print('Name: ', row[1])
            print('Ingredients: ', row[2])
            print('Cooking Time(mins): ', row[3])
            print('\nDifficulty level: ', row[4])

# to update recipe


def update_recipe(conn, cursor):
    view_all_recipes(conn, cursor)

    # user input ID of recipe to be updated
    recipe_id_update = int((input("Enter ID of recipe to update: ")))

    # user input column to update
    column_update = str(input(
        "What do you want to update? (select 'name', cooking_time' or 'ingredients') "))

    # user input new value to update
    updated_value = input('Enter new value for update: ')

    if column_update == 'name':
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s",
                       (updated_value, recipe_id_update))
        print('\nRecipe name updated')

    elif column_update == 'cooking_time':
        cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s",
                       (updated_value, recipe_id_update))
        cursor.execute("SELECT * FROM Recipes WHERE id = %s",
                       (recipe_id_update, ))
        recipe_to_update = cursor.fetchall()

        name = recipe_to_update[0][1]
        ingredients = tuple(recipe_to_update[0][2].split(','))
        cooking_time = recipe_to_update[0][3]

        updated_difficulty = calculate_difficulty(cooking_time, ingredients)
        print("Recipe difficulty updated: ", updated_difficulty)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s",
                       (updated_difficulty, recipe_id_update))
        print("Recipe difficulty updated.")

    elif column_update == 'ingredients':
        cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s",
                       (updated_value, recipe_id_update))
        cursor.execute("SELECT * From Recipes WHERE id = %s",
                       (recipe_id_update, ))
        recipe_to_update = cursor.fetchall()

        name = recipe_to_update[0][1]
        ingredients = tuple(recipe_to_update[0][2].split(','))
        cooking_time = recipe_to_update[0][3]

        updated_difficulty = calculate_difficulty(cooking_time, ingredients)
        print("Recipe difficulty updated: ", updated_difficulty)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s",
                       (updated_difficulty, recipe_id_update))
        print("Recipe difficulty updated.")
        conn.commit()


# to view all recipes
def view_all_recipes(conn, cursor):
    print('List of Recipes: ')

    # get all recipes
    cursor.execute('SELECT * FROM Recipes')
    recipe_results = cursor.fetchall()

    if len(recipe_results) == 00:
        print('\nNo recipe found.')
        return
    else:
        for row in recipe_results:
            print("")
            print('ID: ', row[0])
            print('Name: ', row[1])
            print('Ingredients: ', row[2])
            print('Cooking Time(mins): ', row[3])
            print('Difficulty level: ', row[4])
            print("")

# to delete recipe


def delete_recipe(conn, cursor):
    view_all_recipes(conn, cursor)

    recipe_id_delete = (input("Enter Recipe ID to delete: "))

    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id_delete, ))

    conn.commit()
    print("Recipe deleted.")


main_menu(conn, cursor)
print("The End.")
