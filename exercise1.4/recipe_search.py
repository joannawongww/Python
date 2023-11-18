import pickle

# function to display recipe


def display_recipe(recipe):
    print()
    print("Recipe: ", recipe['name'])
    print("Cooking time (min): ", recipe['cooking_time'])
    print("Ingredients: ")
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print("Difficulty level: ", recipe['difficulty'])

# function to search ingredient


def search_ingredients(data):
    # add index number
    numbered_ingredients = list(enumerate(data['all_ingredients']))

    print("All ingredients in recipe: ")
    for ingredient in numbered_ingredients:
        print(ingredient[0], ingredient[1])

    try:
        ingredient_number = int(
            input('Enter ingredient number to search for: '))
        ingredient_searched = numbered_ingredients[ingredient_number][1]
    except:
        print('Incorrect input')
    else:
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                print("Recipe: " + recipe["name"])
                print("Cooking Time: " + str(recipe["cooking_time"]))
                print("Ingredients: " + ", ".join(recipe["ingredients"]))
                print("Difficulty: " + recipe["difficulty"])


filename = input("Enter name of file: ")

try:
    file = open(filename, 'rb')
    data = pickle.load(file)
except FileNotFoundError:
    print("File is not found")
except:
    print("Unexpected error")
else:
    file.close()
    search_ingredients(data)
