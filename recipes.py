

class Drink:
    def __init__(self, id,  name, ingredients):
        self.id = id    
        self.name = name
        self.ingredients = ingredients # each ingredient is 1 oz measure


moscow_mule = Drink("moscow_mule", "Moscow Mule", 
    {"Vodka": 2, 
     "Ginger Beer": 4,
     "Lime Juice": 0.5
    }
)

martini = Drink("martini", "Martini", 
    {"Vodka": 2,
     "Dry Vermouth": 0.5
    }
)

MENU = [moscow_mule, martini]