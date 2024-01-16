def change_pass(passwdfile):
    import codecs
    import getpass
    
    def change_pw(passwdfile):
        '''Function to change the password'''
     
        with open(passwdfile, 'r') as file: #opening in the read mode
            lines = file.readlines()
        
        #Taking all the input from the users        
        user_name = input("Enter user name: ")
        
        # For existing password
        password = getpass.getpass("Enter password: ")
        password = codecs.encode(password, "rot13")
        
        #For new password
        new_password = getpass.getpass("Enter new password: ")
        new_password = codecs.encode(new_password, "rot13")
        
        #Re-enter the password to confirm it
        confirm_password = getpass.getpass("Confirm new password: ")
        confirm_password = codecs.encode(confirm_password, "rot13")
        
        for num, info in enumerate(lines):
            data = info.strip()
            data_1 = data.split(":") #splitting the data and making it into a list
            un = data_1[0] #username in index 0
            rn = data_1[1]#realname in index 1
            pw = data_1[2]#password in index 2
            
            #Comparing the passwords
            if user_name == un:
                
                if password == pw:
                    
                    if new_password != password:
                        
                        if new_password == confirm_password:
                            lines[num] = f"{un}:{rn}:{new_password}\n" 
                            print("Password Changed!")
                        
                        else:
                            print("Confirm password correctly!")
                            
                    else:
                        print("Password cannot be same as before!")
                        
                else:
                    print("Password not correct!")
                    
        
        with open(passwdfile, "w") as file: #opening the file in write mode to write the changed data
                file.writelines(lines)
            
    change_pw("passwd (1).txt")        
        