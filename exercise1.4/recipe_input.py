import pickle

# function to take input from user on recipe


def take_recipe():
    name = str(input("Name of recipe: "))
    cooking_time = int(input("Cooking time (mins): "))
    ingredients = (input("Ingredients: ").split(", "))
    difficulty = calc_difficulty(cooking_time, ingredients)
    recipe = {'name': name, 'cooking_time': cooking_time,
              'ingredients': ingredients, 'difficulty': difficulty}
    return recipe


# function to calculate recipe difficulty
def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = 'Easy'

    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = 'Medium'

    elif cooking_time >= 10 and len('ingredients') < 4:
        difficulty = 'Intermediate'

    elif cooking_time >= 10 and len('ingredients') >= 4:
        difficulty = 'Hard'
    return difficulty


filename = (str(input('Enter filename: ')) + ".bin")

try:
    file = open(filename, 'r')
    data = pickle.load(file)
except FileNotFoundError:
    print('Filename not found')
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    print('An unexpected error occurs')
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    file.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

# user to input how many recipes
n = int(input('How many recipes would you like to enter: '))

# Check if ingredient present else add into list
for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if not ingredient in all_ingredients:
            all_ingredients.append(ingredient)
    recipes_list.append(recipe)

# gather updated data
data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

# open binary file and write data to it using pickle module
updated_file = open(filename, 'wb')
pickle.dump(data, updated_file)

updated_file.close()
print('File has been updated')
