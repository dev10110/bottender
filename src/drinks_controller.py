

from recipes import MENU


class DrinksController:

    def __init__(self):

        self.drinks = ["Vodka", "None", "None", "None"]
        self.menu = MENU
        return

    def set_drinks(self, drinks):
        if len(drinks) != len(self.drinks):
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

    def get_ingredient_availability(self, drink):
        count = 0
        for ing in drink.ingredients:
            if ing in self.drinks:
                count +=1

        return count/len(drink.ingredients)


    def get_menu(self):

        # return sorted(self.menu, key=lambda d: self.get_ingredient_availability(d), reverse=True)
        return sorted(self.menu, key=lambda d: d.name, reverse=False)


