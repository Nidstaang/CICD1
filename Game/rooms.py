# BEDCHAMBER
def bedchamber():

    print(
        """You find yourself in Fane's bedchamber. Dark curtains cover the windows letting only a faint light come in. You can't see outside. 
        Squinting, you see some old paintings in golden frames decorating the wall. There is mouldings all over the walls and ceiling.
        If the baroque aesthetic had existed in your world, you would use that word to describe this room.
        There is a bear skin rug in the center of the bedchamber. A hunting trophy from your last trip to Arx. You can see a trap door peeking from under it.
        To your right there is a door. It seems to lead outside.""")
    print("""What do you do? (1 or 2)
        1.) Check the trapdoor.
        2.) Venture outside. """)
        
    
    answer = input(">")

    if "1" in answer:
        laboratory()
    elif "2" in answer:
        print("It seems to be locked through some weird lever mechanism. It won't bulge.")
    else:
        print("That's not acceptable. Please type the proper input so we can continue.")

# LABORATORY 
def laboratory():
  
    print("""You lift the trapdoor. Stone stairs that never seem to end. You follow them and encounter a slightly open door.
    You go in and find yourself in an empty, dimly lit room. The stone walls seeem to have witnessed many centuries pass.
    There is shelves filled with books and weird objects that sparkle and make strange sounds. The floor is covered with more books and boxes filled with ingredients.
    You see Fane's empty desk at the end of the room. He is not there. His desk is filled with paper filled with scribbles. You see a polished crate.
    Complicated drawings and maps decorate the wall. You see a shelf with carved wooden details but you can't see what's on top of it.""")
  
    print("""What do you do? (1 or 2)
        1.) Check the crate.
        2.) Investigate the shelf.""")

    answer = input(">")
  
    if answer == "1":

        print("""A pretty wooden crate sits on top of the desk.
        You open the crate. It's filled with ingredients. An emerald leather pouch grabs your attention.""")
        print("""What do you do? (1 or 2)
        1.) Check the pouch.
        2.) Leave it be.""") 
        
        answer = input(">")

        if "1" in answer:
            print("You open the leather pouch. It's filled with herbs.\nThe smell is nauseating and you start to feel dizzy. \n")
        
        elif "2" in answer:
            print("You leave the crate be. Fane would probably not like having you go through his personal stuff.")
            
        else:
            print("That's not acceptable. Please type the proper input so we can continue.") 


# OUSSIDE GIRL
def outside():
  
    print("""The sunlight blinds you at first.
    After a while, you look around. You wouldn't have imagined Fane to have had such a gorgeous garden as this.
    Pretty ironic for an undead to care about something as ephemeral as flowers. But now is not the time for these musings.
    Where the hell did he go? You inspect your surroundings. 
    You notice footprints leading to the back of the house. On the other hand, the manor gate is open, which also seems suspicious.
    Where do you head? (1 or 2)
    1.) You follow the footprints. 
    2.) You head outside the estate.""") 
    

    answer = input(">")

    if answer == "1":
        print("To be continued...")
            ### backyard()

    elif answer == "2":
        print("To be continued...")
            ### road/hill/whatfuggenever
            
    else:
        print("How. Many. Times?! Insert proper input. (: ") 