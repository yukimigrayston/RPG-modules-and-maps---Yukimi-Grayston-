#RPG mm characters - Yukimi Grayston

#this code stores all of the character dictionaries and functions to print the dictionaries

#character dictionary 
characters = {'fighter' : {
    'damage type' : 'meelee',
    } ,
              'mage' : {
    'damage type' : 'magic',
    },
              'druid' : {
    'damage type' : 'nature/magic',
    },
              }
#character stats 
cr_stats = { 'fighter' : {
                'health' : '80',
                'speed' : '25',
                'armor' : 'heavy',
                },
              'mage' : {
                'health' : '50',
                'speed' : '30',
                'armor' : 'none',
                },
              'druid' : {
                'health' : '40',
                'speed' : '35',
                'armor' : 'light',
                },
             }

#character actions 
actions = { 'fighter' : {
    'action_1' : 'sword attack: 50 dmg',
    'action_2' : 'sheild defense: blocks 50 dmg',
    },
            'mage' : {
    'action_1' : 'magic missle: 20 dmg per missle',
    'action_2' : 'fire ball: 50 fire damage',
    },
            'druid':  {
    'action_1' : 'vine trap: 30 dmg, stuns enemy',
    'action_2' : 'heal: heals 40 hp',
    },
            }

def p_character(character):
"""prints characters to console"""
    for character, damage_type in characters.items():
        print(f"\n{character.title()}")
        print(f"Damage Type: {damage_type['damage type']}")

def p_cr_stats(cr_stats):
"""prints character stats to console"""
    for cr, stats in cr_stats.items():
        print(f"\n{cr.title()}")
        print(f"Stats: {stats['health']}") 
        print(f"Stats: {stats['speed']}") 
        print(f"Stats: {stats['armor']}")
        
def p_cr_actions(cr_actions):
"""prints character actions to console"""
    for cr, action in actions.items():
        print(f"\n{cr.title()}")
        print(f"Action 1 - {action['action_1']}") 
        print(f"Action 2 -  {action['action_2']}") 
      

