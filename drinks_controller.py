

class DrinksController:

    def __init__(self):

        self.drinks = ["Drink 1", "Drink 2", "Drink 3", "Drink 4"]

        return

    def set_drinks(self, drinks):
        if len(drinks) != len(self.drinks):
            print("NOT CORRECT NUMBER OF DRINKS - REJECTING SETUP")
            return False

        for i in range(len(self.drinks)):
            self.drinks[i] = drinks[i]
        
        return True
