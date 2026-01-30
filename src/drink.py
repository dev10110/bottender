"""
    Data structures for stages of the drink recipes. 
    The "instruction" is a string displayed to the user at that stage.
    The "button" text is the label for the button to proceed.
    The "pours" is a dict of {ingredient: amount} to be poured at that stage, i.e., AFTER the button is pressed. 
    At the end of the pour, the page will automatically refresh to either the next stage or back to the home page.
"""
class DrinkStage:
    def __init__(self, instruction, pours, button="Next"):
        self.instruction = instruction
        self.pours = pours  # dict of {ingredient: amount}
        self.button = button

"""
    The Drink class represents a cocktail recipe, with its many stages. 
    The ingredients dict is auto-derived from the stages.
"""
class Drink:
    def __init__(
        self,
        id,
        name,
        stages, 
        recommended=False,
        sort_priority=0,
        garnish=None,
        section=None,
        hidden=False,
        secret_menu=False,
        description="",
    ):
        self.id = id
        self.name = name
        self.stages = stages
        self.recommended = recommended
        self.sort_priority = sort_priority
        self.garnish = garnish
        self.hidden = hidden
        self.description = description
        self.secret_menu = secret_menu
        self.section = section
        self.ingredients = self._derive_ingredients_from_stages(self.stages)

    def _derive_ingredients_from_stages(self, stages):
        """Return an aggregated ingredient dict from a list of stages.
        """
        if not stages:
            return {}

        agg = {}
        for s in stages:
            pours = getattr(s, 'pours', {})

            for k, v in pours.items():
                # ensure numeric aggregation
                if k in agg:
                    agg[k] += v
                else:
                    agg[k] = v

        print("Aggregate ingredients for drink", self.id, ":", agg)
        return agg