import rooms

def start():
    print(
    """
    
        _   ___  ___   _   _  _ ___    ___   _   _ ___ ___ _____ 
       /_\ | _ \/ __| /_\ | \| | __|  / _ \ | | | | __/ __|_   _|
      / _ \|   / (__ / _ \| .` | _|  | (_) || |_| | _|\__ \ | |  
     /_/ \_\_|_\ \___/_/ \_\_|\_|___| \__\_\ \___/|___|___/ |_|  
                                                            
    """)
    print("         A short adventure (in progress)")
    print("   Based on Divinity Original Sin 2 characters by Larian Studios.")
    print("     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")

def intro():
    print(
        """  You wake up in a scream, panting. 
        You had a nightmare where you and Fane were attacked by a bunch of voidwokens.
        After that there is memories of a fight. You with your crossbow. Fane with his spells.
        You feel a sudden wave of pain on your left side and clench your jaw and tighten your hands, clawing the bed.
        Was that really a nightmare?
        You look around. You're in a bed but it's not yours. It looks familiar. 
        A sweet intoxicating smell lingers in the air.
        The smell triggers your memories. You have been here before... It's Fane's house! But where is he?
        ...
        Might want to start moving. You sit on the bed.
        ...""")
    bedchamber()



##############  ITEMS    

character_inventory = {}

def add_to_inventory(character_inventory, added_items):

    
    for new_item in added_items:
        if new_item not in character_inventory:
            character_inventory.update({new_item: 0})

def delete_inventory(character_inventory, deleted_items):
    del character_inventory[key]
    
key = ['lever']    

### this is not finished and it sucks but it's not extremely relevant and doesn't affect the code functioning sooooo


#####################


# BEDCHAMBER
def bedchamber():

    print(
        """You are in Fane's bedchamber.
        Dark curtains cover the windows letting only a faint light come in. You can't see outside. 
        Squinting, you see some old paintings in golden frames decorating the wall. There is mouldings all over the walls and ceiling.
        If the baroque aesthetic had existed in your world, you would use that word to describe this room.
        There is a bear skin rug in the center of the bedchamber. A hunting trophy from your last trip to Arx. You can see a trap door peeking from under it.
        To your right there is a door. It seems to lead outside.\n\n""")
    print("""What do you do? (1 or 2)
        1.) Check the trapdoor.
        2.) Venture outside. \n""")
        

    answer = input(">")

    if "1" in answer:
        print(lab_intro)
        laboratory()
    elif "2" in answer and "lever" not in character_inventory:
        print("It seems to be locked through some weird lever mechanism. It won't bulge.\n Let's try the trapdoor.")
        laboratory()
    elif "2" in answer and "lever" in character_inventory:
        print("""You pull the lever out of your pocket. It seems to fit perfectly in the door!
        You try to move it and it smoothly turns around. You start hearing noises. Cogwheels. Is there cogwheels *inside* the door?
        The noises stop with one last *click*. The door opens and you walk outside.\n""")
        outside()
    else:
        print("That's not acceptable. Please type the proper input so we can continue.")
        bedchamber()

# LABORATORY 

lab_intro = """You lift the trapdoor. Stone stairs that never seem to end. You follow them and encounter a slightly open door.
    You go in and find yourself in an empty, dimly lit room. The stone walls seeem to have witnessed many centuries pass.
    There is shelves filled with books and weird objects that sparkle and make strange sounds. The floor is covered with more books and boxes filled with ingredients.
    You see Fane's empty desk at the end of the room. He is not there. His desk is filled with paper filled with scribbles. You see a polished crate.
    Complicated drawings and maps decorate the wall. You see a shelf with carved wooden details but you can't see what's on top of it.\n\n"""

def laboratory():
  
    print("""What do you do? (1, 2 or 3)
        1.) Check the crate.
        2.) Investigate the shelf.
        3.) Go back upstairs.\n""")

    answer = input(">")
  
    if answer == "1":

        print("""A pretty wooden crate sits on top of the desk.
        You open the crate. It's filled with ingredients. An emerald leather pouch grabs your attention.\n""")
        print("""What do you do? (1 or 2)
        1.) Check the pouch.
        2.) Leave it be.\n""") 
        
        answer = input(">")

        if "1" in answer:
            print("You open the leather pouch. It's filled with herbs.\nThe smell is nauseating and you start to feel dizzy. You close the pouch and let it be.")
            laboratory()
        elif "2" in answer:
            print("You leave the crate be. Fane would probably not like having you go through his personal stuff.")
            laboratory()
            
        else:
            print("That's not acceptable. Please type the proper input so we can continue.") 
            laboratory()
    elif answer == "2": 
        print("""You get closer to the shelf. It looks elvish made. Can it be... Livewood? You shake your head in disbelief.
        You take a look on what is on top. Contraptions than shine and whistle. A globe filled with smoke that keeps changing colour.
        A device catches your eye. Is it a wand? 'It is too thick' you think. It is wooden, threaded with silver... 'A lever'?
        The door upstairs looked like it could fit a lever. Isn't it worth a try?
        You put the lever in your pocket.\n\n""")
        add_to_inventory(character_inventory, key)
        laboratory()
    elif answer == "3":
        print("""You decide to go back upstairs. Maybe you missed something?""")
        bedchamber()

# OUSSIDE
def outside():
  
    print("""The sunlight blinds you at first.
    After a while, you look around. You wouldn't have imagined Fane to have had such a gorgeous garden as this.
    Pretty ironic for an undead to care about something as ephemeral as flowers. But now is not the time for these musings.
    Where the hell did he go? You inspect your surroundings. 
    You notice footprints leading to the back of the house. On the other hand, the manor gate is open, which also seems suspicious.
    Where do you head? (1 or 2)
    1.) You follow the footprints. 
    2.) You head outside the estate.\n\n""") 
    

    answer = input(">")

    if answer == "1":
        print("To be continued...")
            ### backyard()

    elif answer == "2":
        print("To be continued...")
            ### road/hill/whatfuggenever
            
    else:
        print("How. Many. Times?! Insert proper input. (: ") 



start()
intro()