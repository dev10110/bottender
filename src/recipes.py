

class Drink:
    def __init__(self, id,  name, ingredients, recommended=False, sort_priority=0, garnish=None, section=None):
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


gold_rush=Drink("gold_rush","Gold Rush", {"Bourbon": 2, "Honey Syrup": 1, "Lemon Juice":0.75})
old_fashioned_paloma=Drink("old_fashioned_paloma","Old Fashioned Paloma",{"Bourbon":1.5, "Grapefruit Soda":4,"Honey Syrup":0.5,"Lemon Juice":0.25})
original_margarita=Drink("original_margarita","Original Margarita",{"Tequila":2, "Margarita Mix":1.5, "Honey Syrup":0.5})
pineapple_margarita=Drink("pineapple_margarita","Pineapple Margarita",{"Tequila":1.5, "Pineapple Juice":4, "Margarita Mix":0.75})
classic_paloma=Drink("classic_paloma","Classic Paloma",{"Tequila":2, "Grapefruit Soda":3.5,"Honey Syrup":0.5})
greyhound=Drink("greyhound","Greyhound",{"Vodka":2, "Grapefruit Soda":3.5,"Honey Syrup":0.5})
pineapple_screwdriver=Drink("pineapple_screwdriver","Pineapple Screwdriver",{"Vodka":2,"Pineapple Juice":4})
the_joseph=Drink("the_joseph","The Joseph",{"Grapefruit Soda":4.0, "Honey Syrup":1.0})
the_joseph_v2=Drink("the_joseph_v2","The Joseph V2",{"Pineapple Juice":4.0, "Honey Syrup":1.0})
honey_shot =Drink("honey_shot","Honey Shot",{"Honey Syrup":0.5})
test_drink = Drink("test_drink", "Test Drink", {"Vodka": 0.5, "Pineapple Juice": 0.5})

MENU = [
    gold_rush,
    old_fashioned_paloma,
    original_margarita,
    pineapple_margarita,
    classic_paloma,
    greyhound,
    pineapple_screwdriver,
    the_joseph_v2,
    honey_shot,
    test_drink
]


# ## *********************************8
# ## ************* BOTTENDER 2.1 *************
# ####
# 
# # vodka_gimlet=Drink("vodka_gimlet","Vodka Gimlet", {"Vodka":2, "Lime Juice":1, "Simple Syrup":0.25})
# # moscow_mule2=Drink("moscow_mule2","Moscow Mule", {"Vodka":1.5, "Lime Juice":0.5})
# # cosmopolitan=Drink("cosmopolitan","Cosmopolitan", {"Vodka":1, "Cranberry Juice":1, "Cointreau":0.5,"Lemon Juice":0.5,"Simple Syrup":0.25})
# # vodka_cranberry=Drink("vodka_cranberry","Vodka Cranberry", {"Vodka":1.5, "Cranberry Juice":4, "Lime Juice":0.5})
# # lemon_drop=Drink("lemon_drop","Lemon Drop", {"Vodka":1.5, "Cointreau":0.5, "Lemon Juice":0.5, "Simple Syrup":0.25})
# # spiced_n_pineapple=Drink("spiced_n_pineapple","Spiced & Pineapple", {"Spiced Rum":1.5, "Pineapple Juice":4, "Lime Juice":0.25})
# # pineapple_screwdriver=Drink("pineapple_screwdriver","Pineapple Screwdriver", {"Vodka":2, "Pineapple Juice":4})
# 
# # MENU = [vodka_gimlet,
# # moscow_mule2,
# # cosmopolitan,
# # vodka_cranberry,
# # lemon_drop,
# # spiced_n_pineapple,
# # pineapple_screwdriver
# # ]
# 
# 
# #SAKE 
# 
# spicy_passionfruit_sakerita = Drink(
#     "spicy_passionfruit_sakerita",
#     "Spicy Passionfruit Sakerita",
#     {"Passionfruit Syrup": 1.0, "Sake":2.0, "Yuzu":0.5, "Cointreau":0.25},
#     recommended=True,
#     sort_priority=17,
#     section="Sake",
#     garnish="Add an Jalapeno!",
#     )
# 
# sake_southside = Drink(
#     "sake_southside",
#     "Sake Southside",
#     {"Honey Syrup":1, "Sake":2, "Yuzu":0.5},
#     recommended=False,
#     sort_priority=16,
#     section="Sake",
#     garnish = "Enjoy with some Mint!"
# )
# 
# classic_sakerita = Drink(
#     "classic_sakerita",
#     "Classic Sakerita",
#     {"Sake":2, "Yuzu":1, "Cointreau":0.5},
#     recommended=False,
#     sort_priority=15,
#     garnish="Squeeze in some Lime!",
#     section="Sake"
# )
# guava_sakerita = Drink(
#     "guava_sakerita",
#     "Guava Sakerita",
#     {"Guava Syrup":1, "Sake":2, "Yuzu":0.5, "Cointreau":0.25},
#     garnish="Squeeze in some Lime!",
#     recommended=False,
#     sort_priority=14,
#     section="Sake"
# )
# 
# #SHOCHU
# 
# yuzu_chuhai = Drink(
#     "yuzu_chuhai",
#     "Yuzu_Chuhai",
#     {"Shochu":1.5, "Yuzu":0.5, "Honey Syrup":1, "Club Soda":2},
#     recommended=False,
#     sort_priority=13,
#     section="Shochu",
#     garnish="Squeeze in some Lime!"
# )
# 
# tropical_melon_chuhai = Drink(
#     "tropical_melon_chuhai",
#     "Tropical Melon Chuhai",
#     {"Shochu":1.5, "Guava Syrup":0.5, "Passionfruit Syrup":0.5, "Midori":0.5, "Club Soda":2},
#     recommended=True,
#     sort_priority=12,
#     garnish="Squeeze in some Lime!",
#     section="Shochu"
# )
# 
# matcha_shochu = Drink(
#     "matcha_shochu",
#     "Matcha Shochu",
#     {"Matcha Syrup":2, "Shochu":2},
#     recommended=False,
#     sort_priority=11,
#     garnish="Squeeze in some Lime!",
#     section="Shochu"
# )
# japanese_sidecar = Drink(
#     "japanese_sidecar",
#     "Japanese Sidecar",
#     {"Shochu":1.75, "Honey Syrup":0.25, "Yuzu":0.5, "Cointreau":0.75},
#     recommended=True,
#     sort_priority=10,
#     garnish="Add a few drops of bitters!",
#     section="Shochu")
# 
# #GIN
# matcha_gin_fizz = Drink(
#     "matcha_gin_fizz",
#     "Matcha Gin Fizz",
#     {"Matcha Syrup":1.5, "Gin":1.5, "Club Soda": 3},
#     recommended=False,
#     sort_priority=9,
#     garnish="Squeeze in some Lime!",
#     section="Gin")
# 
# raspberry_black_tea_gin_fizz = Drink(
#     "raspberry_black_tea_gin_fizz",
#     "Raspberry Black Tea Gin Fizz",
#     {"Raspberry Black Tea":2, "Gin":1.5, "Club Soda":2},
#     recommended=True,
#     sort_priority=8,
#     garnish="Squeeze in some Lime!",
#     section="Gin")
# 
# green_tea_gimlet = Drink(
#     "green_tea_gimlet",
#     "Green Tea Gimlet",
#     {"Matcha Syrup":1.5, "Gin":1.5, "Yuzu":0.5},
#     recommended=False,
#     sort_priority=7,
#     garnish="Top with some Mint!",
#     section="Gin")
# 
# #MIDORI
# midori_sour = Drink(
#     "midori_sour",
#     "Midori Sour",
#     {"Midori":2, "Club Soda":3, "Yuzu": 0.5},
#     recommended=False,
#     sort_priority=6,
#     section="Midori",
#     garnish="Drop in a cherry!"
# )
# japanese_slipper = Drink(
#     "japanese_slipper",
#     "Japanese Slipper",
#     {"Midori":2, "Cointreau":1, "Yuzu":0.5},
#     recommended=True,
#     sort_priority=5,
#     section="Midori",
#     garnish="Drop in a cherry!"
# )
# 
# #NON-ALCOHOLIC
# 
# raspberry_black_tea = Drink(
#     "raspberry_black_tea",
#     "Raspberry Black Tea",
#     {"Raspberry Black Tea": 4},
#     recommended=False,
#     sort_priority=4,
#     garnish="Squeeze in some Lime!",
#     section="Non-alcoholic"
# )
# 
# guava_soda = Drink(
#     "guava_soda",
#     "Guava Soda",
#     {"Guava Syrup":1, "Club Soda":3.5},
#     recommended=False,
#     sort_priority=3,
#     garnish="Enjoy!",
#     section="Non-alcoholic"
# )
# passionfruit_soda = Drink(
#     "passionfruit_soda",
#     "Passionfruit Syrup",
#     {"Passionfruit Syrup":1, "Club Soda":3.5},
#     recommended=False,
#     sort_priority=2,
#     section="Non-alcoholic",
#     garnish="Enjoy!"
# )
# 
# MENU = [
#     spicy_passionfruit_sakerita,
#     sake_southside,
#     classic_sakerita,
#     passionfruit_soda,
#     guava_soda,
#     raspberry_black_tea,
#     japanese_slipper,
#     midori_sour,
#     green_tea_gimlet,
#     raspberry_black_tea_gin_fizz,
#     matcha_gin_fizz,
#     japanese_sidecar,
#     matcha_shochu,
#     tropical_melon_chuhai,
#     yuzu_chuhai,
#     guava_sakerita,
#     honey_shot,
# ]
