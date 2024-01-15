def pizza_total_price(tuesday, pizza_number,customer_delivery,order_from_app):
    '''calculation of total price of pizza based on various conditions.
        
        parameters: Tuesday: (boolean data-type) True if it's tuesday, else false.
                    pizza_number: (Integer data-type) Total number of pizza ordered by customer.
                    customer_delivery: (boolean data-type) True if customer wants delivery, else false.
                    order_from_app: (boolean data-type) True if customer is ordering using BPP app, else false.
        
        Returns the total price of pizza after applying all the conditions. (Float data-type)            '''
    
    Pizza_cost = 12.00
    Discount_on_Tuesdays = 0.50 #(50%) 
    #(Constant values given in the question)
    
    #Applying Tuesday Discount if the day is tuesday.(50% off)
    if tuesday:
        total_price = pizza_number *(Pizza_cost*(1-Discount_on_Tuesdays)) 
        #applying discount formula
    else:
        total_price = pizza_number *Pizza_cost
        #if no discount, number of pizza should be multiplied with total cost(eg: if 6 pizzas, 12*6=£72 )
        
    
    Delivery_Cost = 2.50
    if pizza_number >= 5 and customer_delivery:
        total_price = total_price + 0 #No delivery charge
    #if customer orders 5 or more pizzas, there is no delivery cost. If not, £2.50 delivery cost is added.(shown below)
    else:
        total_price = total_price + Delivery_Cost
    
    
    Discount_using_App = 0.25 
    #if the customer orders using BPP app, 25% of total price is applied as discount.
    if order_from_app:
        total_price = total_price * (1-Discount_using_App)
    
    
    return total_price

   
   
    # Now,taking input from user
while True:
    pizza_number = int(input("Number of pizzas you wish to order? : "))
    if pizza_number > 0:
        break 
    #if user inputs positive number, the condition is true and the loop breaks. Else,(given below)
    else:
        print("Invalid input.Please enter right numbers") #if less than zero      
    

while True:
    tuesday = input("Is it Tuesday today? (y/n/yes/no): ")
    tuesday = tuesday.lower()
    if tuesday == "yes" or tuesday =="no" or tuesday=="y" or tuesday=="n":
        tuesday = (tuesday =="yes" or tuesday =="y")
        break 
    #if the user says yes or y to tuesday, the condition is true,(1 is stored in tuesday, which is true) and the loop breaks. else,(given below)
    else:
        print("Invalid input. Please enter 'yes','no','y' or 'n'.")


while True:
    customer_delivery = input("Do you want your order to be delivered? (yes/no/y/n): ")
    customer_delivery = customer_delivery.lower()
    if customer_delivery == "yes" or customer_delivery =="no" or customer_delivery =="y" or customer_delivery=="n":
        customer_delivery = (customer_delivery =="yes" or customer_delivery == "y")
        break
    else:
        print("Invalid input. Please enter 'yes','no','y' or 'n'.")
   
while True:
    order_from_app = input("Are you ordering using BPP app? (yes/no/y/n): ")
    order_from_app = order_from_app.lower()
    if order_from_app =="yes" or order_from_app == "no" or order_from_app=="y" or order_from_app=="n":
        order_from_app = (order_from_app =="yes" or order_from_app =="y")
        break
    else:
        print("Invalid input. Please enter 'yes','no','y' or 'n'.")

#calling the function to calculate the total price
total_price = pizza_total_price(tuesday, pizza_number,customer_delivery,order_from_app)

#displaying total price of the pizza. 
print(f"Your Total Price is: £{total_price:.2f}" ) 
#(.2f displays only 2 numbers after decimal point(in order to avoid multiple numbers after decimal which could confuse the customer)

