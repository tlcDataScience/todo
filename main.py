#To do list

from datetime import datetime

database = {
    datetime.now():
    {
    'todoItem': 'template',
    'current': datetime.now(),
    'IsCompleted': False,
    'Category': 'template2'
    }
}

user_input = input("Enter\t")
while user_input != "Q":
    user_input = input("Enter a command\t")
    if user_input == "Create":
       todoItem = input("Enter a new item todo:\t")
       currentTime = datetime.now()
       IsCompleted = False
       Category = input("Enter category:\t") 

       print(f"""
        Todo_item: {todoItem}
        CreateDateTime: {currentTime}
        IsCompleted: {IsCompleted}
        Category: {Category}
       """)
       database [datetime.now()] = {
           'todoItem': todoItem,
           'CreateDateTime': currentTime,
           'IsCompleted': IsCompleted,
           'Category': Category
       }

    elif user_input == "Display" :
        for i in database:
            print(database[i])    

    elif user_input == "Sort" :
        pass 