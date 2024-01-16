def login_account(passwdfile):    
    import codecs
    import getpass

    def user_login(passwdfile):
        '''function to let user login into their account'''
        
        with open(passwdfile, "rt") as file: #opening the file in read write mode
            lines = file.readlines() #reading line by line
            
        def user_input(text):
            '''function that prompts user to give the input'''
            while True: 
                user_inp  = input(text) 
                if user_inp:
                    return user_inp
                
    #Asking user for input
        username  = user_input("\nEnter username: ") 
        
        password = getpass.getpass("Enter password: ")
        password = codecs.encode(password, "rot_13") 
        
        for data in lines:
            data = data.strip() #removes unnessesary spaces
            data_list  = data.split(":") #splitting turned the data into the list 
            if username == data_list[0] and password == data_list[2]: 
                print("\nlogin successful")
                return

        print("\n user not found")    
                  
                
    user_login(passwdfile)              