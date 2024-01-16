import sys
import adduser
import deluser
import login
import changepass #importing the modules

passwdfile = sys.argv[1] #assigning the file to a variable
while True:
        #asking the user what they want to do
        print("What do you want to do?")
        print("1. Create new account")
        print("2. Delete account")
        print("3. Change password")
        print("4. Log in")
        print("Press Enter to exit:)")

        user_choice = int(input("Enter your choice (1/2/3/4): ")) #taking user input for the choice
        
        if user_choice == 1:
            adduser.add_account(passwdfile)
        elif user_choice == 2:
            deluser.del_account(passwdfile)
        elif user_choice == 3:
            changepass.change_pass(passwdfile)
        elif user_choice == 4:
            login.login_account(passwdfile)
            break
        else:
            print(f"{user_choice} is not valid!. please choose between (1/2/3/4)")
            #if user inputs any other number except 1,2,3 or 4
        