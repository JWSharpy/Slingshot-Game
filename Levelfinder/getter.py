def getMenuOption(debug = False):
    if debug: print ("getMenuOption Function")

    goodInput = False
    
    while not goodInput:
        option = input("Please select an option: ")
        option = option.lower()
        
        if (option == "q" or 
            option == "quit" or 
            option == "x" or 
            option == "exit"): 
                option = "q"
                goodInput = True 
        elif (option == "1" or 
            option == "one" or 
            option == "Levels"): 
                option = "1"
                goodInput = True 
        elif (option == "2" or 
            option == "two" or 
            option == "Decription"): 
                option = "2"
                goodInput = True 
        else:
            print("Please make a valid choice")
            
    return option


