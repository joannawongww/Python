## Exercise 1.1

### Tasks

- Explain variables and data types in Python
- Summarize use of objects in PYthon
- Create data structure for Recipe app

#### Below are the steps for the task, done in IPython shell:

##### Step 1-2: Create structure for first recipe:

Step 1-2: Create structure for first recipe:
`recipe_1 = {'Name': 'Tea', 'Cooking Time': 5, 'Ingredients': 'Tea leaves', 'Sugar', 'Water'}`

- Have chosen dictionary as data structure due to its flexibility
- Each entry separated by comma and entered as key:value pair
- Provides a key-value structure, which is suitable for recipe with Name, Cooking Time and Ingredients as key.
- No restriction for immutable data types for values
- Able to store Name as str, Cooking Time as int and Ingredients as list.

Step 3: Create outer structure called all_recipes
`all_recipes = []`

- Have chosen list for all_recipes
- all_recipes need to be sequential and able to store multiple recipes.
- lists are able to keep the order of elements which is required

Step 4: Generate 4 more recipes and append to all_recipes
`recipe_2 = {'Name': 'Ginger Tea', 'Cooking time': 5, 'Ingredients': ['Ginger', 'Sugar', 'Water']}`

`recipe_3 = {'Name': 'Coffee', 'Cooking time': 5, 'Ingredients': ['Coffee Powder', 'Milk', 'Water', 'Sugar']}`

`recipe_4 = {'Name': 'Hot Cocoa', 'Cooking time': 5, 'Ingredients': ['Cocoa Powder', 'Water', 'Sugar']}`

`recipe_5 = {'Name': 'Lemon Tea', 'Cooking time': 10, 'Ingredients': ['Lemon', 'Tea Leaves', 'Water', 'Honey]}`

`all_recipes.apend(recipe_2)`
`all_recipes.apend(recipe_3)`
`all_recipes.apend(recipe_4)`
`all_recipes.apend(recipe_5)`

Step 5: Print ingredients of each recipe as 5 different lists in IPython
`print(all_recipes[0]['Ingredients])`
`print(all_recipes[1]['Ingredients])`
`print(all_recipes[2]['Ingredients])`
`print(all_recipes[3]['Ingredients])`
`print(all_recipes[4]['Ingredients])`
