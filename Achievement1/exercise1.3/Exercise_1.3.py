recipes_list = []
ingredients_list = []

# function to take input from user on recipe


def take_recipe():
    name = str(input("Name of recipe: "))
    cooking_time = int(input("Cooking time (mins): "))
    ingredients = (input("Ingredients: ").split(", "))
    recipe = {'name': name, 'cooking_time': cooking_time,
              'ingredients': ingredients}
    return recipe


# Ask user how many recipes they would like to enter
n = int(input('How many recipes would you like to enter: '))

# Check if ingredient present else add into list
for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)


# Determine recipe difficulty level
for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Easy'

    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Medium'

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Intermediate'

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Hard'

# Display recipe
for recipe in recipes_list:
    print()
    print("Recipe: ", recipe['name'])
    print("Cooking time (min): ", recipe['cooking_time'])
    print("Ingredients: ")
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print("Difficulty level: ", recipe['difficulty'])

# Display all ingredients


def print_ingredients():
    print()
    ingredients_list.sort()
    print('Ingredients available across all recipes')
    print('--------------------------------------')
    for ingredient in recipe['ingredients']:
        print(ingredient)


print_ingredients()
