#RPG modules and maps - Yukimi Grayston 

#this code will ask the user what menu they want to see then print it


#importing functions 
from RPG_mm_characters_yukimi_grayston import characters, cr_stats, actions,p_character as cr, p_cr_stats as crs, p_cr_actions as cra
from RPG_mm_items_yukimi_grayston import items,item_desc, p_item as pi, p_item_desc as pid
from tabulate import tabulate 


#function names
#pi : items, pid : item description, cr : character,
#crs : character stats, cra : character actions

print("Characters \nItems \nLocations")

options = "\nPlease enter the menu you would like to view(character/items/location): "
options += "\nEnter 'quit' when you would like to finish "

#asks user what they want to see
while True:
    menu = input(options)
    #stops asking when user types quit
    if(menu) == 'quit':
        break
    
    else:
        if(menu) == 'character': 
            cr(characters)
            cr_info = input("Would you like to see stats or actions? (stats/actions): ")
                
            if(cr_info) == 'stats':
                crs(cr_stats)
            elif(cr_info) == 'actions':
                cra(actions)
            else:
                menu()
        if(menu) == 'items':
            pi(items)
            i_info = input("Would you like to see the item informrtion? (item_desc): ")
            
            if(i_info) == 'item_desc':
                pid(item_desc)
        if(menu) == 'location':
            print(tabulate([['beginning room', 'key'],['code room', 'door code'], ['goblin room', 'enemys'],['fork in the road', 'none'],['left room', 'small treasure'],                 
            ['middle room', 'trap'],['right room', 'trapped door' ]], headers=['Room','Item'], tablefmt='orgtbl'))
            
            
                
        
                
                
      
        
