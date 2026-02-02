
# loading data from file
def loading_recipes(file_path):
    try:
        with open(file_path, 'r') as file:
            recipes = file.read()
            return recipes
    except FileNotFoundError:
        print("File not found.")



# displaying recipe names 
def dispaying_recipes(data):
    recipes = data.split('---')
    names = []

    for recipe in recipes:
        lines = recipe.strip().split('\n')
        if lines and lines[0].startswith("Recipe:"):
            name = lines[0].replace("Recipe:","").strip()
            names.append(name)
    return names

# Display ingredients & instructions

def show_recipe(data,recipe_name):
    recipes = data.split('---')

    for recipe in recipes:
        if f'Recipe: {recipe_name}' in recipe:
            print(f'\n{recipe.strip()}')
            break
        print('Recipe not found.')



def main():
    recipe_data = loading_recipes('recipes.txt')

    recipe_names = dispaying_recipes(recipe_data)

    print('Available Recipes:')
    for index,recipe in enumerate(recipe_names,start=1):
        print(f'{index} : {recipe}')
    
    # Ask user to select recipe
    choice = int(input('\nEnter recipe number : '))
    if 1 <= choice <= len(recipe_names):
        selected_recipe = recipe_names[choice-1]
    else:
        print('Invalid choice.')
        return
    
    show_recipe(recipe_data,selected_recipe)

if __name__ == '__main__':
    main()