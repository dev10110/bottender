

class Drink:
    def __init__(self, id,  name, ingredients, recommended=False, sort_priority=0, garnish=None):
        self.id = id    
        self.name = name
        self.ingredients = ingredients # each ingredient is 1 oz measure
        self.recommended = recommended
        self.sort_priority = sort_priority
        self.garnish = garnish


# moscow_mule = Drink("moscow_mule", "Moscow Mule", 
#     {"Vodka": 2, 
#      "Ginger Beer": 4,
#      "Lime Juice": 0.5
#     }
# )

# martini = Drink("martini", "Martini", 
#     {"Vodka": 2,
#      "Dry Vermouth": 0.5
#     }
# )

##  **************************************
##  *********** BOTTENDER 1.0 ************
##  **************************************
# tequila_sunrise=Drink("tequila_sunrise","Tequila Sunrise", {"Grenadine":0.75, "Tequila": 1.5, "Orange Juice": 6})
# tequila_tropical=Drink("tequila_tropical","Tequila Tropical", {"Tequila": 1.5, "Pineapple Juice": 6})
# cantarito=Drink("cantarito","Cantarito", {"Tequila": 1.5, "Orange Juice": 6})
# tequila_cranberry=Drink("tequila_cranberry","Tequila Cranberry", {"Tequila": 1.5, "Cranberry Juice": 6})
# mexican_mule=Drink("mexican_mule","Mexican Mule", {"Tequila": 1.5, "Ginger Beer": 6})
# moscow_mule=Drink("moscow_mule","Moscow Mule", {"Vodka": 1.5, "Ginger Beer": 6})
# screwdriver=Drink("screwdriver","Screwdriver", {"Vodka": 1.5, "Orange Juice": 6})
# vodka_cranberry=Drink("vodka_cranberry","Vodka Cranberry", {"Vodka": 1.5, "Cranberry Juice": 6})
# vodka_spritz=Drink("vodka_spritz","Vodka Spritz", {"Vodka": 1.5, "Cranberry Juice": 3})
# almost_cosmo=Drink("almost_cosmo","Almost Cosmo", {"Vodka": 1.5, "Cranberry Juice": 3,"Orange Juice": 3})
# bahama_mama=Drink("bahama_mama","Bahama Mama", {"Grenadine":0.75, "Malibu": 1.5, "Pineapple Juice": 5})
# malibu_bay_breeze=Drink("malibu_bay_breeze","Malibu Bay Breeze", {"Malibu": 1.5, "Cranberry Juice": 3, "Pineapple Juice": 3})
# malibu_sunset=Drink("malibu_sunset","Malibu Sunset", {"Grenadine":0.75, "Malibu": 1, "Cranberry Juice": 3,"Orange Juice": 3})
# malibu_pineapple=Drink("malibu_pineapple","Malibu Pineapple", {"Malibu": 1.5, "Pineapple Juice": 6})
# malibu_cranberry=Drink("malibu_cranberry","Malibu Cranberry", {"Malibu": 1.5, "Cranberry Juice": 6})

# MENU = [
# tequila_sunrise,
# tequila_tropical,
# cantarito,
# tequila_cranberry,
# mexican_mule,
# moscow_mule,
# screwdriver,
# vodka_cranberry,
# vodka_spritz,
# almost_cosmo,
# bahama_mama,
# malibu_bay_breeze,
# malibu_sunset,
# malibu_pineapple,
# malibu_cranberry
# ]


##  **************************************
##  *********** BOTTENDER 2.0 ************
##  **************************************


# gold_rush=Drink("gold_rush","Gold Rush", {"Bourbon": 2, "Honey Syrup": 1, "Lemon Juice":0.75})
# old_fashioned_paloma=Drink("old_fashioned_paloma","Old Fashioned Paloma",{"Bourbon":1.5, "Grapefruit Soda":4,"Honey Syrup":0.5,"Lemon Juice":0.25})
# original_margarita=Drink("original_margarita","Original Margarita",{"Tequila":2, "Margarita Mix":1.5, "Honey Syrup":0.5})
# pineapple_margarita=Drink("pineapple_margarita","Pineapple Margarita",{"Tequila":1.5, "Pineapple Juice":4, "Margarita Mix":0.75})
# classic_paloma=Drink("classic_paloma","Classic Paloma",{"Tequila":2, "Grapefruit Soda":3.5,"Honey Syrup":0.5})
# greyhound=Drink("greyhound","Greyhound",{"Vodka":2, "Grapefruit Soda":3.5,"Honey Syrup":0.5})
# pineapple_screwdriver=Drink("pineapple_screwdriver","Pineapple Screwdriver",{"Vodka":2,"Pineapple Juice":4})
# the_joseph=Drink("the_joseph","The Joseph",{"Grapefruit Soda":4.0, "Honey Syrup":1.0})
# the_joseph_v2=Drink("the_joseph_v2","The Joseph V2",{"Pineapple Juice":4.0, "Honey Syrup":1.0})
# honey_shot =Drink("honey_shot","Honey Shot",{"Honey Syrup":0.5})
# test_drink = Drink("test_drink", "Test Drink", {"Vodka": 0.5, "Pineapple Juice": 0.5})

# MENU = [
#     gold_rush,
#     old_fashioned_paloma,
#     original_margarita,
#     pineapple_margarita,
#     classic_paloma,
#     greyhound,
#     pineapple_screwdriver,
#     the_joseph_v2,
#     honey_shot
#     #test_drink
# ]


## *********************************8
## ************* BOTTENDER 2.1 *************
####

# vodka_gimlet=Drink("vodka_gimlet","Vodka Gimlet", {"Vodka":2, "Lime Juice":1, "Simple Syrup":0.25})
# moscow_mule2=Drink("moscow_mule2","Moscow Mule", {"Vodka":1.5, "Lime Juice":0.5})
# cosmopolitan=Drink("cosmopolitan","Cosmopolitan", {"Vodka":1, "Cranberry Juice":1, "Cointreau":0.5,"Lemon Juice":0.5,"Simple Syrup":0.25})
# vodka_cranberry=Drink("vodka_cranberry","Vodka Cranberry", {"Vodka":1.5, "Cranberry Juice":4, "Lime Juice":0.5})
# lemon_drop=Drink("lemon_drop","Lemon Drop", {"Vodka":1.5, "Cointreau":0.5, "Lemon Juice":0.5, "Simple Syrup":0.25})
# spiced_n_pineapple=Drink("spiced_n_pineapple","Spiced & Pineapple", {"Spiced Rum":1.5, "Pineapple Juice":4, "Lime Juice":0.25})
# pineapple_screwdriver=Drink("pineapple_screwdriver","Pineapple Screwdriver", {"Vodka":2, "Pineapple Juice":4})

# MENU = [vodka_gimlet,
# moscow_mule2,
# cosmopolitan,
# vodka_cranberry,
# lemon_drop,
# spiced_n_pineapple,
# pineapple_screwdriver
# ]

