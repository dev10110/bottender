

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


tequila_sunrise=Drink("tequila_sunrise","Tequila Sunrise", {"Grenadine":0.75, "Tequila": 1.5, "Orange Juice": 6})
tequila_tropical=Drink("tequila_tropical","Tequila Tropical", {"Tequila": 1.5, "Pineapple Juice": 6})
cantarito=Drink("cantarito","Cantarito", {"Tequila": 1.5, "Orange Juice": 6})
tequila_cranberry=Drink("tequila_cranberry","Tequila Cranberry", {"Tequila": 1.5, "Cranberry Juice": 6})
mexican_mule=Drink("mexican_mule","Mexican Mule", {"Tequila": 1.5, "Ginger Beer": 6})
moscow_mule=Drink("moscow_mule","Moscow Mule", {"Vodka": 1.5, "Ginger Beer": 6})
screwdriver=Drink("screwdriver","Screwdriver", {"Vodka": 1.5, "Orange Juice": 6})
vodka_cranberry=Drink("vodka_cranberry","Vodka Cranberry", {"Vodka": 1.5, "Cranberry Juice": 6})
vodka_spritz=Drink("vodka_spritz","Vodka Spritz", {"Vodka": 1.5, "Cranberry Juice": 3})
almost_cosmo=Drink("almost_cosmo","Almost Cosmo", {"Vodka": 1.5, "Cranberry Juice": 3,"Orange Juice": 3})
bahama_mama=Drink("bahama_mama","Bahama Mama", {"Grenadine":0.75, "Malibu": 1.5, "Pineapple Juice": 5})
malibu_bay_breeze=Drink("malibu_bay_breeze","Malibu Bay Breeze", {"Malibu": 1.5, "Cranberry Juice": 3, "Pineapple Juice": 3})
malibu_sunset=Drink("malibu_sunset","Malibu Sunset", {"Grenadine":0.75, "Malibu": 1, "Cranberry Juice": 3,"Orange Juice": 3})
malibu_pineapple=Drink("malibu_pineapple","Malibu Pineapple", {"Malibu": 1.5, "Pineapple Juice": 6})
malibu_cranberry=Drink("malibu_cranberry","Malibu Cranberry", {"Malibu": 1.5, "Cranberry Juice": 6})

MENU = [
tequila_sunrise,
tequila_tropical,
cantarito,
tequila_cranberry,
mexican_mule,
moscow_mule,
screwdriver,
vodka_cranberry,
vodka_spritz,
almost_cosmo,
bahama_mama,
malibu_bay_breeze,
malibu_sunset,
malibu_pineapple,
malibu_cranberry
]