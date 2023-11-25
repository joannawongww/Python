from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# connect to database
engine = create_engine("mysql://cf-python:password@localhost/task_database")

# generate Session class an bind to engine (database connection obj)
Session = sessionmaker(bind=engine)

# initalize session object
session = Session()

# generate declarative base class
Base = declarative_base()

# definition for Recipe model


class Recipe(Base):
    __tablename__ = 'final_recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # quick representation of recipe id, name & difficulty
    def __repr__(self):
        return "\nID: " + str(self.id) + "\nName: " + str(self.name) + "\nDifficulty: " + str(self.difficulty)

    # string format of recipe details
    def __str__(self):
        return (
            "\nID: " + str(self.id) +
            "\nName: " + str(self.name) +
            "\nIngredients: " + str(self.ingredients) +
            "\nCooking Time(mins): " + str(self.cooking_time) +
            "\nDifficulty: " + str(self.difficulty) +
            "\n" + 20*("=")
        )

    # calculate difficulty of recipe
    def calculate_difficulty(self):
        ingredients_num = len(self.ingredients.split(", "))
        if self.cooking_time < 10 and ingredients_num < 4:
            self.difficulty = 'Easy'

        elif self.cooking_time < 10 and ingredients_num >= 4:
            self.difficulty = 'Medium'

        elif self.cooking_time >= 10 and ingredients_num < 4:
            self.difficulty = 'Intermediate'

        elif self.cooking_time >= 10 and ingredients_num >= 4:
            self.difficulty = 'Hard'

        return self.difficulty

    # get ingredients string as list
    def return_ingredients_as_list(self):
        # no ingredients will return empty list
        if self.ingredients == "":
            return []
        # split ingredients into list
        else:
            return self.ingredients.split(", ")


# create table
Base.metadata.create_all(engine)

# before create main menu, establish 5 functions

# funct 1: create recipe


def create_recipe():

    # get user input on name
    name = str(input("Name of recipe: "))

    # check name length
    if len(name) > 50:
        print("Name must not exceed 50 characters.")
        return

    # get user input on cooking time
    cooking_time = (input("Cooking time in mins: "))

    # check cooking time number
    if not cooking_time.isnumeric():
        print("\nError occured. Only numbers are allowed.")
        return

    # get user input on ingredients
    ingredients = []
    ingredients_number = (input("Number of ingredients in Recipe: "))

    # check ingredient number
    if not ingredients_number.isnumeric():
        print("Only numbers are allowed.")
        return

    # convert ingredient number to integer
    ingredients_number = int(ingredients_number)

    # run loop to add ingredients to list
    for ingredient in range(ingredients_number):
        ingredient = input("Enter each ingredient 1 by 1: ")
        ingredients.append(ingredient)

    # convert ingredients into string
    ingredients = ", ".join(ingredients)

    # create new object from Recipe model
    recipe_entry = Recipe(
        name=name, cooking_time=int(cooking_time), ingredients=ingredients)
    # calculate difficulty of recipe entry
    recipe_entry.calculate_difficulty()

    # add recipe to database
    session.add(recipe_entry)

    # save changes
    session.commit()

    # inform user recipe created
    print("\nRecipe added to database.")

# function 2 to view all recipes


def view_all_recipes():
    recipes = session.query(Recipe).all()

    # if no recipes in database
    if len(recipes) == 0:
        print("No recipes found")
        return

    # if recipes found, print recipe
    else:
        for recipe in recipes:
            print(recipe)

# function 3 to search recipes by ingredient


def search_by_ingredients():
    # check if any entries in table
    recipe_count = session.query(Recipe).count()

    # if no entries found in table
    if recipe_count == 0:
        print("No recipes found.")
        return

    # entries found in table
    else:
        # get ingredients
        results = session.query(Recipe.ingredients).all()

        # empty list
        all_ingredients = []

        # split ingredients and add to list
        for item in results:
            temporary_list = item[0].split(", ")

            # check for duplicate before add to list
            for item in temporary_list:
                if item not in all_ingredients:
                    all_ingredients.append(item)

        # add number to ingredient, start number from 1
        all_ingredients_list = list(enumerate(all_ingredients, 1))

        # display number & ingredient list
        for index, tup in enumerate(all_ingredients_list):
            print(str(tup[0]+1) + ". " + tup[1])

        # user input ingredient number
        ingredient_num = input(
            "\nEnter ingredient number (separate by space): ").split()

        # empty list for searched ingredient
        search_ingredients = []

        for i in ingredient_num:
            if not i.isnumeric():
                print("Only numbers are allowed.")
                return
            else:
                i = int(i)
                ingredient = all_ingredients_list[i-1][1]
                search_ingredients.append(ingredient)

        # empty list for conditions
        conditions = []

        # loop to search conditions
        for ingredient in search_ingredients:
            # search string
            like_term = "%" + ingredient + "%"
            conditions.append(Recipe.ingredients.like(like_term))

        # retrieve recipes from database based on conditions
        filtered_recipe = session.query(Recipe).filter(*conditions).all()

        for recipe in filtered_recipe:
            print(recipe)

# function 4 to edit recipe


def edit_recipe():
    # check if any entries in table
    recipe_count = session.query(Recipe).count()

    # if no entries found in table
    if recipe_count == 0:
        print("No recipes found.")
        return

    # retrieve recipe id and name
    results = session.query(Recipe.id, Recipe.name).all()

    # print recipes to user
    for recipe_id, recipe_name in results:
        print("\nID: " + str(recipe_id) + "\nName: " + str(recipe_name))

    # user input recipe ID to edit recipe
    recipe_id_to_edit = input("Enter recipe ID to edit: ")

    # check if user enter number
    if not recipe_id_to_edit.isnumeric():
        print("Only numbers allowed.")
        return

    # convert to integer
    recipe_id_to_edit = int(recipe_id_to_edit)

    # finds recipe by ID
    recipe_to_edit = session.query(Recipe).filter(
        Recipe.id == recipe_id_to_edit).one()

    # display recipe to user
    print("")
    print("Recipe details: ")
    print("1) Name: " + recipe_to_edit.name)
    print("2) Cooking Time: " + str(recipe_to_edit.cooking_time))
    print("3) Ingredients: " + recipe_to_edit.ingredients)
    print("")

    # user input attribute number to edit
    attribute_number = input("Enter attribute number to edit: ")

    # check user input
    if not attribute_number.isnumeric():
        print("Only numbers allowed.")
        return

    # user wants to edit name
    if attribute_number == "1":
        # user input new name
        new_name = str(input("Enter new name: "))

        # check name length
        if len(new_name) > 50:
            print("Not more than 50 characters.")
            new_name = str(input("Enter new name: "))

        # update name to database
        recipe_to_edit.name = new_name

    # user wants to edit cooking time
    elif attribute_number == "2":
        # user input new cooking time
        new_cooking_time = (input("Enter new cooking time (mins): "))

        # check cooking time is number
        if not new_cooking_time.isnumeric():
            print("Only numbers are allowed.")
            new_cooking_time = int(input("Enter new cooking time (mins): "))

        # update new cooking time
        recipe_to_edit.cooking_time = int(new_cooking_time)

    # user wants to edit ingredients list
    elif attribute_number == "3":
        # user input new ingredients
        new_ingredients = input(
            "Enter new ingredients list (separated by comma and space): ")
        recipe_to_edit.ingredients = new_ingredients

    # recalculate difficulty
    recipe_to_edit.calculate_difficulty()

    # commit changes
    session.commit()

    # inform user recipe updated
    print("Recipe updated.")

# function 5 to delete recipe


def delete_recipe():
    # check if any entries in table
    recipe_count = session.query(Recipe).count()

    # if no entries found in table
    if recipe_count == 0:
        print("No recipes found.")
        return

    # retrieve recipe id and name
    results = session.query(Recipe.id, Recipe.name).all()

    # print recipes to user
    for recipe_id, recipe_name in results:
        print("\nID: " + str(recipe_id) + "\nName: " + str(recipe_name))

    # user input recipe ID to edit recipe
    recipe_id_to_delete = input("\nEnter recipe ID to delete: ")

    # check if user enter number
    if not recipe_id_to_delete.isnumeric():
        print("Only numbers allowed.")
        return

    # convert to integer
    recipe_id_to_delete = int(recipe_id_to_delete)

    # finds recipe by ID
    recipe_id_to_delete = session.query(Recipe).filter(
        Recipe.id == recipe_id_to_delete).one()

    # ask user if confirm deletion
    print("\nConfirm delete recipe? (Yes/No): ")

    # user input yes/no
    confirmation = input("")

    # if user input yes
    if confirmation == "Yes":
        session.delete(recipe_id_to_delete)
        session.commit()
        print("\nRecipe deleted.")
    # if user input no
    elif confirmation == "No":
        print("\nUser does not want delete recipe. Return to Main Menu")

# main menu


def main_menu():
    choice = ""
    # display menu for user to pick choice
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

        # check user choice
        if choice == "1":
            create_recipe()
        elif choice == "2":
            search_by_ingredients()
        elif choice == "3":
            edit_recipe()
        elif choice == "4":
            delete_recipe()
        elif choice == "5":
            view_all_recipes()

        # user pick quit
        elif choice == 'quit':
            print("Program ends.")
            session.close()
            engine.dispose()

        # user choice not found
        else:
            print("Invalid option.")
            main_menu()


main_menu()
