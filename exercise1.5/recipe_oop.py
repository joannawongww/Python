class Recipe:

    all_ingredients = []

    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = None

    # get recipe name
    def get_name(self):
        return self.name

    # set recipe name
    def set_name(self, name):
        self.name = name

    # get cooking time
    def get_cooking_time(self):
        return self.cooking_time

    # set cooking time
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    # add ingredients
    def add_ingredients(self, *args):
        for ingredient in args:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()

    # get ingredients
    def get_ingredients(self):
        return self.ingredients

    # calculate recipe difficulty
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = 'Easy'

        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = 'Medium'

        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = 'Intermediate'

        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
            self.difficulty = 'Hard'

        return self.difficulty

    # get difficulty
    def get_difficulty(self):
        # Getter for the difficulty, calculates if not already done
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    # search ingredient in recipe, return True or False

    def search_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            return True
        else:
            return False

    # update ingredients and add to class if not present
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)

    # string representation to print entire recipe
    def __str__(self):
        output = "\nName: " + str(self.name) + \
            "\nCooking Time: " + str(self.cooking_time) + " mins" + \
            "\nDifficulty: " + str(self.get_difficulty()) + \
            "\nIngredients: " + str(self.ingredients)
        return output

 # sesarch recipe that contains a specific ingreident


def recipe_search(recipes_list, ingredient):
    data = recipes_list
    searched_term = ingredient
    for recipe in data:
        if recipe.search_ingredient(searched_term):
            print(recipe)


# main code
tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)

coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)

cake = Recipe(
    "Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)

banana_smoothie = Recipe(
    "Banana Smoothie", ["Banana", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)

recipes_list = [tea, coffee, cake, banana_smoothie]

for recipe in recipes_list:
    print("")
    print("---------------------------------------------------------------")
    print("Recipe: ")
    print(recipe)


print("")
print("---------------------------------------------------------------")
print("Recipes containing ingredient: Water")
recipe_search(recipes_list, "Water")

print("")
print("---------------------------------------------------------------")
print("Recipes containing ingredient: Sugar")
recipe_search(recipes_list, "Sugar")

print("")
print("---------------------------------------------------------------")
print("Recipes containing ingredient: Banana")
recipe_search(recipes_list, "Banana")
