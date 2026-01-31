from drink import Drink, DrinkStage

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


# ##  **************************************
# ##  *********** BOTTENDER 2.0 ************
# ##  **************************************
#
#
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
#
# MENU = [
#     gold_rush,
#     old_fashioned_paloma,
#     original_margarita,
#     pineapple_margarita,
#     classic_paloma,
#     greyhound,
#     pineapple_screwdriver,
#     the_joseph_v2,
#     honey_shot,
#     test_drink
# ]
#
#
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
##
##
## paloma = Drink(
##   "paloma",
##   "Paloma",
##   {"Grapefruit Soda": 4.5, "Tequila": 1, "Lime Juice": 0.5},
##   recommended=False,
## )
##
## margarita = Drink(
##   "margarita",
##   "Margarita",
##   {"Cointreau": 1, "Tequila": 1.5, "Lime Juice": 1, "Simple Syrup": 1}
## )
##
## blue_hawaii = Drink(
##   "blue_hawaii",
##   "Blue Hawaiian",
##   {"Malibu": 1, "Dark Rum": 1, "Pineapple Juice": 2, "Lime Juice": 1, "Blue Curacao": 0.75, "Simple Syrup": 0.25}
## )
##
## coconut_marg = Drink(
##   "coconut_marg",
##   "Coconut Marg",
##   {"Cream of Coconut": 1.5, "Cointreau": 0.75, "Tequila": 2, "Lime Juice": 0.75}
## )
##
##
## pina_colada = Drink(
##   "pina_colada",
##   "Pina Colada",
##   {"Dark Rum": 2, "Pineapple Juice": 2, "Cream of Coconut": 1.5, "Lime Juice": 0.5}
## )
##
## bay_breeze = Drink(
##   "bay_breeze",
##   "Bay Breeze",
##   {"Malibu": 1.5, "Pineapple Juice": 2, "Cranberry": 1, "Lime Juice": 0.5}
## )
##
## pineapple_marg = Drink(
##   "pineapple_marg",
##   "Pineapple Marg",
##   {"Pineapple Juice": 2.5, "Cointreau": 1, "Tequila": 1.5, "Lime Juice": 1}
## )
##
## rum_punch = Drink(
##   "rum_punch",
##   "Rum Punch",
##   {"Malibu": 1, "Dark Rum": 1, "Orange Juice": 1, "Pineapple Juice": 2, "Lime Juice": 0.5}
## )
##
## cranberry_soda = Drink(
##   "cranberry_soda",
##   "Cranberry Soda",
##   {"Cranberry": 3, "Grapefruit Soda": 3}
## )
##
## virgin_pina = Drink(
##   "virgin_pina",
##   "Virgin Pina Colada",
##   {"Pineapple Juice": 3, "Cream of Coconut": 2, "Lime Juice": 0.5}
## )
##
## painkiller = Drink(
##   "painkiller",
##   "Painkiller",
##   {"Dark Rum": 1.5, "Orange Juice": 0.75, "Pineapple Juice": 3, "Cream of Coconut": 0.75},
##   hidden=True
## )
##
## blue_marg = Drink(
##   "blue_marg",
##   "Blue Marg",
##   {"Tequila": 1.5, "Lime Juice": 1, "Blue Curacao": 1, "Simple Syrup": 1}
## )
##
##
## MENU = [
##   paloma,
##   margarita,
##   blue_hawaii,
##   coconut_marg,
##   pina_colada,
##   bay_breeze,
##   pineapple_marg,
##   rum_punch,
##   cranberry_soda,
##   virgin_pina,
##   painkiller,
##   blue_marg
## ]
##


###


# tequila_tropical=Drink("tequila_tropical","Tequila Tropical", {"Tequila": 1.5, "Pineapple Juice": 6})
# cantarito=Drink("cantarito","Cantarito", {"Tequila": 1.5, "Orange Juice": 6}, description="is this a cantarito")
# tequila_cranberry=Drink("tequila_cranberry","Tequila Cranberry", {"Tequila": 1.5, "Cranberry Juice": 6})
# mexican_mule=Drink("mexican_mule","Mexican Mule", {"Tequila": 1.5, "Ginger Beer": 6})
# moscow_mule=Drink("moscow_mule","Moscow Mule", {"Vodka": 1.5, "Ginger Beer": 6})
# screwdriver=Drink("screwdriver","Screwdriver", {"Vodka": 1.5, "Orange Juice": 6})
# vodka_cranberry=Drink("vodka_cranberry","Vodka Cranberry", {"Vodka": 1.5, "Cranberry Juice": 4})
# almost_cosmo=Drink("almost_cosmo","Almost Cosmo", {"Vodka": 1.5, "Cranberry Juice": 3,"Orange Juice": 3})
# malibu_bay_breeze=Drink("malibu_bay_breeze","Malibu Bay Breeze", {"Malibu": 1.5, "Cranberry Juice": 3, "Pineapple Juice": 3})
# malibu_pineapple=Drink("malibu_pineapple","Malibu Pineapple", {"Malibu": 1.5, "Pineapple Juice": 6})
# malibu_cranberry=Drink("malibu_cranberry","Malibu Cranberry", {"Malibu": 1.5, "Cranberry Juice": 6})
# gold_rush=Drink("gold_rush","Gold Rush", {"Bourbon": 2, "Syrup": 1, "Lemon Juice":0.75})
# old_fashioned_paloma=Drink("old_fashioned_paloma","Old Fashioned Paloma",{"Bourbon":1.5, "Grapefruit Soda":4,"Syrup":0.5,"Lemon Juice":0.25})
# old_fashioned=Drink("old_fashioned","Old Fashioned",{"Bourbon":1.5,  "Syrup":0.5})
# classic_paloma=Drink("classic_paloma","Classic Paloma",{"Tequila":2, "Grapefruit Soda":3.5,"Syrup":0.5})
# greyhound=Drink("greyhound","Greyhound",{"Vodka":2, "Grapefruit Soda":3.5,"Syrup":0.5})
# pineapple_screwdriver=Drink("pineapple_screwdriver","Pineapple Screwdriver",{"Vodka":2,"Pineapple Juice":4})
# the_joseph_v2=Drink("the_joseph_v2","The Joseph V2",{"Pineapple Juice":4.0, "Syrup":1.0})
# syrup_shot =Drink("syrup_shot","Syrup Shot",{"Syrup":0.5})
# vodka_gimlet=Drink("vodka_gimlet","Vodka Gimlet", {"Vodka":2, "Lemon Juice":1, "Syrup":0.25})
# vodka_cranberry=Drink("vodka_cranberry","Vodka Cranberry", {"Vodka":1.5, "Cranberry Juice":4, "Lemon Juice":0.5})
# spiced_n_pineapple=Drink("spiced_n_pineapple","Spiced & Pineapple", {"Rum":1.5, "Pineapple Juice":4, "Lemon Juice":0.25})
# pineapple_screwdriver=Drink("pineapple_screwdriver","Pineapple Screwdriver", {"Vodka":2, "Pineapple Juice":4}, description="this is a description")


# MENU = [tequila_tropical,
# cantarito,
# tequila_cranberry,
# mexican_mule,
# moscow_mule,
# screwdriver,
# vodka_cranberry,
# almost_cosmo,
# malibu_bay_breeze,
# malibu_pineapple,
# malibu_cranberry,
# gold_rush,
# old_fashioned,
# old_fashioned_paloma,
# classic_paloma,
# greyhound,
# pineapple_screwdriver,
# the_joseph_v2,
# syrup_shot,
# vodka_gimlet,
# vodka_cranberry,
# spiced_n_pineapple,
# ]


# ###########
# ### BOTTENDER ENTREPRENEURSHIP
# ##########
#
# MENU = [tequila_tropical,
# cantarito,
# screwdriver,
# pineapple_screwdriver,
# ]


# #####################################
# ### BOTTENDER House Warming Jan 2026
# #####################################

dark_n_stormy = Drink(
    id="dark_n_stormy",
    name="Dark 'n Stormy",
    description="Rum, ginger beer, and lime",
    section="Classics",
    stages=[
        DrinkStage(
            instruction="Place the cup.",
            pours={"Ginger Beer": 4.0},
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Add some ice, and place back the cup.",
            pours={"Rum": 2.0},
            button_text="Continue",
        ),
        DrinkStage(
            instruction="Garnish with a lime wedge. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)
manhattan = Drink(
    id="manhattan",
    name="Manhattan",
    description="Bourbon, vermouth, bitters, topped with a cherry",
    section="Classics",
    stages=[
        DrinkStage(
            instruction="Place the cup.",
            pours={"Bourbon": 2.0, "Vermouth": 1.0},
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Shake with ice, strain into glass.",
            pours={},
            button_text="Continue",
        ),
        DrinkStage(
            instruction="Add a few drops bitters, and garnish with a cherry. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

smoky_paloma = Drink(
    id="smoky_paloma",
    name="Smoky Paloma",
    description="Mezcal, grapefruit soda, and lime",
    section="Classics",
    stages=[
        DrinkStage(
            instruction="Place the cup. (Salt the rim if desired)",
            pours={
                "Mezcal": 2.0,
                "Lime": 0.5,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Add ice, and place back the cup.",
            pours={
                "Grapefruit Soda": 4.0,
            },
            button_text="Continue",
        ),
        DrinkStage(
            instruction="Garnish with a slice of grapefruit. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

midnight_oil = Drink(
    id="midnight_oil",
    name="Midnight Oil",
    description="Dark rum, cold brew coffee, honey, and bitters",
    section="Experiments",
    stages=[
        DrinkStage(
            instruction="Place the cup.",
            pours={
                "Rum": 2.0,
                "Cold Brew": 2.0,
                "Honey": 0.5,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Shake with ice and strain into a glass. Garnish with an orange twist. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

orchard_ember = Drink(
    id="orchard_ember",
    name="Orchard Ember",
    description="Bourbon, spiced apple cider, fresh ginger, and lime",
    section="Experiments",
    stages=[
        DrinkStage(
            instruction="Place the cup.",
            pours={
                "Bourbon": 2.0,
                "Cider": 3.0,
                "Lime": 0.5,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Add ice and garnish with some muddled fresh ginger. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

spicy_mezcalita = Drink(
    id="spicy_mezcalita",
    name="Spicy Pina Mezcalita",
    description="Mezcal, pineapple juice, lime, and jalapeno",
    section="Experiments",
    stages=[
        DrinkStage(
            instruction="Place the cup. (Salt the rim if desired)",
            pours={
                "Mezcal": 2.0,
                "Pineapple Juice": 2.0,
                "Lime": 0.5,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Shake with ice and strain. Garnish with jalapenos. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

stone_fence = Drink(
    id="stone_fence",
    name="Stone Fence",
    description="Bourbon, spiced apple cider, and bitters",
    secret_menu=True,
    section="Secret",
    stages=[
        DrinkStage(
            instruction="Place the cup.",
            pours={
                "Bourbon": 2.0,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Add some ice and place back the cup.",
            pours={"Cider": 4.0},
            button_text="Continue",
        ),
        DrinkStage(
            instruction="Add a few dashes of bitters. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

mezcal_mule = Drink(
    id="mezcal_mule",
    name="Mezcal Mule",
    description="Mezcal, ginger beer, lime, and fresh ginger",
    secret_menu=True,
    section="Secret",
    stages=[
        DrinkStage(
            instruction="Place the cup.",
            pours={
                "Mezcal": 2.0,
                "Lime": 0.5,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Add ice and place back the cup.",
            pours={"Ginger Beer": 4.0},
            button_text="Continue",
        ),
        DrinkStage(
            instruction="Garnish with some fresh ginger. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

coffee_cider = Drink(
    id="coffee_cider",
    name="Coffee Cider",
    description="Rum, cold brew, spiced apple cider, and some cinnamon",
    secret_menu=True,
    section="Secret",
    stages=[
        DrinkStage(
            instruction="Place the cup.",
            pours={
                "Rum": 1.5,
                "Cold Brew": 2.0,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Add ice and place back the cup.",
            pours={"Cider": 2.0},
            button_text="Continue",
        ),
        DrinkStage(
            instruction="Garnish with a sprinkle of cinnamon. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)


rum_runner = Drink(
    id="rum_runner",
    name="Rum Runner",
    description="Rum, pineapple juice, lime, and honey",
    secret_menu=True,
    section="Secret",
    stages=[
        DrinkStage(
            instruction="Place the cup.",
            pours={
                "Rum": 2.0,
                "Pineapple Juice": 2.0,
                "Lime": 0.75,
                "Honey": 0.5,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Shake with ice and strain into a glass. Garnish with a pineapple wedge. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

bitter_apple = Drink(
    id="bitter_apple",
    name="Bitter Apple",
    description="Vermouth, spiced apple cider, ginger beer, and bitters",
    secret_menu=True,
    section="Secret",
    stages=[
        DrinkStage(
            instruction="Place the cup.",
            pours={
                "Vermouth": 1.5,
                "Cider": 2.0,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Add ice and place back the cup.",
            pours={"Ginger Beer": 2.0},
            button_text="Continue",
        ),
        DrinkStage(
            instruction="Add a few dashes of bitters. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

oaxacan_morning = Drink(
    id="oaxacan_morning",
    name="Oaxacan Morning",
    description="Mezcal, cold brew, pineapple juice",
    secret_menu=True,
    section="Secret",
    stages=[
        DrinkStage(
            instruction="Place the cup.",
            pours={
                "Mezcal": 1.5,
                "Cold Brew": 1.5,
                "Pineapple Juice": 1.5,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Shake with ice and strain into a glass. Garnish with a pineapple wedge. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

ginger_fizz = Drink(
    id="ginger_fizz",
    name="Ginger Fizz",
    description="Spiced apple cider, ginger beer",
    section="Mocktails",
    stages=[
        DrinkStage(
            instruction="Place the cup.",
            pours={
                "Cider": 3.0,
                "Lime": 0.5,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Add ice, and place back the cup.",
            pours={
                "Ginger Beer": 3.0,
            },
            button_text="Continue",
        ),
        DrinkStage(
            instruction="Garnish with a slice of ginger. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

tropical_wakeup = Drink(
    id="tropical_wakeup",
    name="Tropical Wakeup",
    description="Pineapple juice, cold brew, and honey",
    section="Mocktails",
    stages=[
        DrinkStage(
            instruction="Place the cup.",
            pours={
                "Pineapple Juice": 3.0,
                "Cold Brew": 2.0,
                "Honey": 0.5,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Shake with ice and strain into a glass. Garnish with a pineapple wedge. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

pomelo_sparkler = Drink(
    id="pomelo_sparkler",
    name="Pomelo Sparkler",
    description="Grapefruit soda, and a spritz of lime",
    section="Mocktails",
    stages=[
        DrinkStage(
            instruction="Place the cup. Optionally salt the rim and add muddled ginger.",
            pours={
                "Lime": 0.5,
            },
            button_text="Start pouring",
        ),
        DrinkStage(
            instruction="Add ice, and place back the cup.",
            pours={
                "Grapefruit Soda": 5.0,
            },
            button_text="Continue",
        ),
        DrinkStage(
            instruction="Garnish with a lime wedge. Enjoy!",
            pours={},
            button_text="Back to menu",
        ),
    ],
)

MENU = [
    dark_n_stormy,
    manhattan,
    smoky_paloma,
    midnight_oil,
    orchard_ember,
    spicy_mezcalita,
    stone_fence,
    mezcal_mule,
    coffee_cider,
    rum_runner,
    bitter_apple,
    oaxacan_morning,
    ginger_fizz,
    tropical_wakeup,
    pomelo_sparkler,
]

SECTIONS = ["Classics", "Experiments", "Mocktails", "Secret"]
