from screens import*
from getter import*


def SlingShot (debug = False):
    if debug: print ("Welcome to Debug")
    
    print (TitleScreen(debug))
    input ("Press Enter to Continue")
    
    done = False
    
    while not done:
        print(MainMenu(debug))
        choice = getMenuOption(debug)
    
        if choice == "q":
            exit()
        elif choice == "1":
            print (Levels(debug))
            print("\n")
            input ("Press Enter to Continue")
        elif choice == "2":
            print (Decription(debug))
            print("\n")
            input ("Press Enter to Continue")
    
    
SlingShot (False)

