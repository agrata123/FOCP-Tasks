def add_account(passwdfile):
    '''Adding a new user account to the password file.

    Parameter:
    - passwdfile: The path to the password file.'''
    import codecs
    import getpass
        
    def add_user(passwdfile):
        
        
        def user_add(username, name, npassword):
            '''Adding a new user entry to the password file.'''
            with open(passwdfile, "a") as file:
                file.write(f"{username}:{name}:{npassword}\n")
            print("User Created.\n") 
            
        def user_input(text) :
            while True: 
                user_inp  =  input(text) 
                if user_inp:
                    return user_inp
                
        #Asking user for input
        username  = user_input("\nEnter new username: ")
        name = user_input("\nEnter real name: ")
        name = str(name).title()  
        
        npassword = getpass.getpass("\nEnter new password: ") 
        #for encryption
        npassword = codecs.encode(npassword,"rot13") 
        
        #cheking if the username already exists
        with open(passwdfile, "r") as file:
            existing_username = []
            for line in file:
                data = line.split(":")[0]
                existing_username.append(data)
    #existing_username = [line.split(":")[0] for line in file.readlines()]
            
            if username in existing_username:
                print("this username already exists")
            else:
                user_add(username, name, npassword)
    #calling the function with file name            
    add_user(passwdfile)                
                    
    
        
    
    