def del_account(passwdfile):   
    import codecs
    import getpass

    def del_user(passwdfile):
        '''function to delete the password'''
        
        with open(passwdfile, "rt") as file: #opening the file in read text mode
            lines = file.readlines()
            
        def user_input(text) : 
            '''function that prompts the user to give the input'''
            while True: 
                user_inp  =  input(text) 
                if user_inp:
                    return user_inp
                
    #Asking user for input
        username  = user_input("\nEnter username: ") 
        
        password = getpass.getpass("Enter password: ")
        password = codecs.encode(password, "rot_13") 
        
        remove = False 
        user = False
        
        with open(passwdfile, "w") as file: #opening the file in write mode (writes the file all over again)
            for data in lines:
                data_list  = data.split(":") #splitting the data into a list 
                if data_list[0] == username:
                    user = True
                    if data_list[2]==password:
                        remove = True
                    else:
                        file.write(data) #if username matches, skip that part and write remaining data
                else:
                    file.write(data) #if password matches, skip that part and write remaining data 
                
        if remove == True:
            print("\nuser removed")
        elif user == False:
            print("\nuser not found")  
        elif remove == False:
            print("\npassword not correct")
         
    del_user("passwd (1).txt")                     
        
                
            
        