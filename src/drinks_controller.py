

from recipes import MENU


class DrinksController:

    def __init__(self):

        self.drinks = ["Vodka", 
                "None", 
                "None",
                "None",
                "None",
                "None",
                "None",
                "None"]
        self.menu = MENU
        return

    def set_drinks(self, drinks):
        if len(drinks) != len(self.drinks):
            print(len(drinks))
            print(len(self.drinks))
            print("NOT CORRECT NUMBER OF DRINKS - REJECTING SETUP")
            return False

        for i in range(len(self.drinks)):
            self.drinks[i] = drinks[i]
        
        return True

    def get_all_ingredients(self):
        

        ing = ["None"]

        for d in self.menu:
            ing.extend(d.ingredients.keys())

        ing = sorted(list(set(ing)))
        
        
        return ing



