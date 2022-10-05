def cakes(recipe, available):
    val_list = list()
    for key, value in recipe.items():
        try:        
            val_list.append(available[key] // recipe[key])
        except KeyError:
            return 0
    return min(val_list)



print(cakes({'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, \
    {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000, 'cream': 5000}))

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
    
recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available))