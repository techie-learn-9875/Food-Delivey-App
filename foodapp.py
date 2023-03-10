# -*- coding: utf-8 -*-
"""FoodApp.ipynb

#Online Food Ordering Application
import json
import sys
import random

class Restaurent:
    
    Restaurent_name = 'Green Chillyz'
    
    def __init__(self):
        self.food_items ={}
        self.users_dict = {}
        self.odered_item = []

# admin functionallity

    def add_food_item(self):
        
        food_name = input('\nEnter the food name: ')
        food_quantity = input('Enter the food quantity: ')
        food_price = input('Enter food price: ')
        food_discount = input('Enter discount on food: ')
        food_stock = input('Enter food stock: ')
        
        item = {'food_name':food_name,'food_quantity':food_quantity,'food_price':food_price,'food_discount':food_discount,'food_stock':food_stock}
        
        food_ID = len(self.food_items)+1
        self.food_items[food_ID]=item
        
        with open('food_items.json','w') as f:
            json.dump(self.food_items,f)

    def edit_food_item(self):
        Id = input('\nEnter food id to edit food item: ')
        
        with open('food_items.json','r') as f:
            data = json.load(f)
        
        for i,j in data.items():
            if Id == i:
                for k in j:
                    data[i][k]=input('Enter the changed '+k+' : ') 
        print('\nYour food item with food Id '+Id+' updated successfully!')
        
        with open('food_items.json','w') as f:
            json.dump(data,f)

    def view_food_items(self):
        
        with open('food_items.json','r') as f:
            data = json.load(f)
        
        for i,j in data.items():
            print('\nFood ID:',i)
            for k in j:
                print(k +" : "+ j[k])

    def remove_food_item(self):
        
        with open('food_items.json','r') as f:
            data = json.load(f)
        
        self.Id = input('\nEnter food id to remove food item: ')
        try:
          data.pop(self.Id)
        except:
              print('val not exist')
        print('\nYour food item removed successfully! Having Food Id: ',self.Id)
        
        with open('food_items.json','w') as f:
            json.dump(data,f)


# User functionallity

    def User_Registration(self):
        
        self.Full_Name = input('\nEnter your full name: ')
        self.Phone_Number = int(input('Enter your phone number: '))
        self.Email = input('Enter your Mail ID:')
        self.Address = input('Enter your address: ')
        self.Password = input('Enter your password: ')
        
        self.user = {'Full Name':self.Full_Name,'Phone Number':self.Phone_Number,'Email':self.Email,'Address':self.Address,'Password':self.Password}
        
        self.ID = len(self.users_dict)+722000
        self.users_dict[self.ID] = self.user
        
        with open('users_data.json','w') as f:
            json.dump(self.users_dict,f)
        print('\nDear ', self.Full_Name ,'! Your User ID: ', self.ID ,' and Password: ', self.Password ,' generated successfully!')

    def Update_user_profile(self):
        Id = input('\nEnter user ID to edit profile: ')
        
        with open('users_data.json','r') as f:
            data = json.load(f)
        
        for i,j in data.items():
            if Id == i:
                for k in j:
                    data[i][k]=input('Enter the changed '+k+' : ') 
        
        print('\nYour profile with user Id '+Id+' updated successfully!')
        
        with open('users_data.json','w') as f:
            json.dump(data,f)

    def User_login(self):
        self.userID = input('\nEnter User ID: ')
        self.pswd = input('Enter Password: ')
        
        with open('users_data.json','r') as f:
            data = json.load(f)
        
        for i,j in data.items():
            if self.userID == i:
                if j['Password'] == self.pswd:
                    print('\nDear ',j['Full Name'],',You logged in successfully!')
                    
                    while True:
                        self.input = int(input('\n1 --> Place New Order \n2 --> Order History \n3 --> Update Profile \n0 --> Logout'))
                        
                        if self.input == 1:
                            x.place_new_order()
                            add_order = int(input('\nOrder more items \n1 --> Yes \n2 --> No'))
                            
                            if add_order == 1:
                                x.place_new_order()
                        
                        elif self.input == 2:
                            x.Order_history()
                        
                        elif self.input == 3:
                            x.Update_user_profile()
                        
                        elif self.input == 0:
                            print('\nDear',j['Full Name'],', Logged out successfully!')
                            print('\n Thank You!\n  Green Chillyz. Best in Chineese!!\n',Restaurent.Restaurent_name) 
                            sys.exit()
        
                else:
                    print('\nOops! Incorrect Password, Please enter correct password.')
        
        print('\nUser ID is not found, please enter correct user ID or Password.')

    def place_new_order(self):
        
        with open('food_items.json','r') as f:
            data = json.load(f)
        
        print('\nFood items list is shown below: ')    
        
        for i,j in data.items():
                print(i , j['food_name'],' (',j['food_quantity'],')',' [???',j['food_price'],']')
        
        self.order_num = list(input('\nSelect your Food: '))
        self.odered_item = self.order_num

        print('\nYour selected food list is: ')
        
        for i,j in data.items():
            for k in self.order_num:
                if k == i:
                    print(i,data[i]['food_name'],' (',data[i]['food_quantity'],')',' [???',data[i]['food_price'],']')
        
        confirm_order = int(input('\nConfirm this order --> \n1 --> Yes\n2 --> No'))
        order_number = random.randint(10000,99999)
        
        if confirm_order == 1:
            print('Your order is placed successfully, Order ID: ',order_number,'\n Thank You!!')
        
        elif confirm_order == 2:
            print('We are canceling your request. Thank you!')   


    def Order_history(self):
        print('\nYour previous orders list is: ')
        
        with open('food_items.json','r') as f:
            data = json.load(f)
        
        for i,j in data.items():
            for k in self.odered_item:
                if k == i:
                    print(i,data[i]['food_name'],' (',data[i]['food_quantity'],')',' [???',data[i]['food_price'],']')               
    


#Object Creation

x = Restaurent()

print('\nWelcome to ',Restaurent.Restaurent_name, '!!')


#Menu Driven Program

while True:
    
    entry = int(input('\nPlease select your role for '+ Restaurent.Restaurent_name +'\n1 --> Admin \n2 --> User \n0 --> Exit \n Enter Your Choice here : '))
    if entry == 1:
        
        while True:
            admin_intput = int(input('\nSelect preference \n1 --> Add Food Items \n2 --> Edit Food Items \n3 --> View Food Items \n4 --> Remove Food Itmes \n0 --> Exit \n Enter Your Choice here : '))
            
            if admin_intput == 1:
                x.add_food_item()
                new_item = int(input('\nAdd more item: \n1 --> Yes\n2 --> No \n Enter Your Choice here : '))
            
                if new_item == 1:
                    x.add_food_item()
            
            elif admin_intput == 2:
                x.edit_food_item()
            
            elif admin_intput == 3:
                x.view_food_items()
            
            elif admin_intput == 4:
                x.remove_food_item()
            
            elif admin_intput == 0:
                print('\nExit from the application!')                
                break
            
            else:
                print('\nPlease select the valid input from the options.')

    elif entry == 2:
        while True:
            user_input = int(input('\nSelect preference \n1 --> New User Registration \n2 --> User Login \n0 --> Exit \n Enter Your Choice here : '))
            
            if user_input == 1:
                x.User_Registration()
            
            elif user_input == 2:
                x.User_login()

            elif user_input == 0:
                print('\nExit From Application')    
                sys.exit()

            else:
                print('\nPlease Enter valid input')    
                  
    elif entry == 0:
        print(' Thank You!\n  Visit us Again!!\n',Restaurent.Restaurent_name) 
        sys.exit()

1
1

