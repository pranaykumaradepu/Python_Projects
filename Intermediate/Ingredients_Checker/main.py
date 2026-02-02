# Ingredients Checker
recipes =  {
    'bread' : {'flour', 'water'},
    'cake' : {'flour', 'sugar', 'eggs'},
    'cookies' : {'flour', 'butter', 'sugar'},
    'pie' : {'flour', 'butter', 'sugar', 'eggs'},
    }
def available_recipes(recipe_name):

    return recipes.get(recipe_name, set())  



def main():
    print('*** Welcome to Ingredients Checker ***')

    user_input = input('Recipes Available : Bread, Cake, Cookies, Pie\nEnter your choice to check ingredients : ').lower().strip()

    if user_input in recipes:
        recipe_ingredients = available_recipes(user_input)

        # Removes spaces and converts to lowercase and stores in a set
        user_avalible_ingredients = {
                        ingredient.strip().lower()
                        for ingredient in input("Enter available ingredients (comma separated): ").split(',')
                    }

        missing_ingredients = recipe_ingredients - user_avalible_ingredients

        extra_ingredients = user_avalible_ingredients - recipe_ingredients

        print('--- Ingredient Check Result ---')

        print(f"The total ingredients for recipe : {', '.join(sorted(recipe_ingredients))}")

        if missing_ingredients:
            print(f"Missing ingredients : {', '.join(sorted(missing_ingredients))}")
        else:
            print('You have all the ingredients needed.')

        if extra_ingredients:     
            print(f"Extra ingredients : {', '.join(sorted(extra_ingredients))}")
        else:
            print('You have no extra ingredients.')
        
        print('Thank You...')
    
    else:
        print('Invalid choice. Please select a valid recipe.')

if __name__ == '__main__':
    main()