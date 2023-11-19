import random
import json
import sys

class RecipeSuggester:
    def __init__(self):
        self.recipes = self.load_recipes()

    def load_recipes(self):
        try:
            with open('recipes.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Recipe file not found.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error loading recipes: {e}", file=sys.stderr)
            sys.exit(1)

    def save_recipes(self):
        with open('recipes.json', 'w') as file:
            json.dump(self.recipes, file)

    def add_recipe(self, name, ingredients):
        self.recipes[name] = ingredients
        self.save_recipes()

    def suggest_recipe(self, available_ingredients):
        possible_recipes = [name for name, ingredients in self.recipes.items() 
                            if all(ingredient in available_ingredients for ingredient in ingredients)]
        return random.choice(possible_recipes) if possible_recipes else "No matching recipe found."

def main():
        
    try:
        suggester = RecipeSuggester()
        while True:
            print("\n1. Get recipe suggestion\n2. Add new recipe\n3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                ingredients = input("Enter available ingredients (comma separated): ").split(',')
                print("Suggested recipe:", suggester.suggest_recipe(ingredients))
            elif choice == '2':
                name = input("Enter recipe name: ")
                ingredients = input("Enter ingredients (comma separated): ").split(',')
                suggester.add_recipe(name, ingredients)
                print("Recipe added successfully.")
            elif choice == '3':
                break
            else:
                print("Invalid choice.")
    except KeyboardInterrupt:
        sys.exit(0)  # Graceful exit on Ctrl+C
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
