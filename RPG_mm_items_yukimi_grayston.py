#RPG mm items - Yukimi Grayston

#This code stores the list of items and dictionary of descriptions of the items
#as well as the functions for printing them 

#list of items
items = ['key', 'room code', 'small treasure chest', 'large treasure']

#item descriptions 
item_desc = { 'key' : {
    'use' : 'unlocks door',
    'value' : '0 gp ',
    },
        'room code' : {
    'use' : 'unlocks treasure room',
    'value' : '0 gp',
    },
        'small treasure chest' : {
    'use' : 'none',
    'value' : '100 gp',
    },
              'large treasure ' : {
    'use' : 'none',
    'value' : '1000 gp, 15 gems',
    },
              }


def p_item(items):
"""prints items to console"""
    for item in items:
        print(item.title())

def p_item_desc(item_desc):
"""prints item descriptions to console"""
    for item, desc in item_desc.items():
        print(f"\n{item.title()}")
        print(f"Use: {desc['use']}")
        print(f"Value: {desc['value']}")

