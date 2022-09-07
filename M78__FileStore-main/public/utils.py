from getpass import getpass
from configs import INFO as information
from users.models import User , show , Manager,finding ,commeent , show_coment , ordering , find_user_id , find_order_id ,ordering_item ,show_ordering
from users.models import show
from core.router import Config
import logging
import datetime
def about_us():
    print(
        f"""Store name : {information["name"]}
            Description : {information["description"]}
        """
    )
def files():
    print("files")
def sign_in():
    username= input("Username : ")
    pasword = getpass("Password : ")
    # print(type(User.sign_in(username , pasword)))
    if User.sign_in(username , pasword):
        Config.status_sign_in = username
        logging.basicConfig(filename="C:/Users/Amir/Desktop/Maktab/maktab/week13/HW13/M78__FileStore-main/core/log.log" , filemode='a' ,level=logging.INFO)
        logging.info(f"This {username} sign in")
        print("Sucessfully !!!")
        logging.basicConfig(filename="C:/Users/Amir/Desktop/Maktab/maktab/week13/HW13/M78__FileStore-main/core/log.log" , filemode='a'  ,level=logging.INFO)
        logging.info(f"This {username} can to sign in")
    else: 
        print('Unsucessfuuly')
        logging.basicConfig(filename="C:/Users/Amir/Desktop/Maktab/maktab/week13/HW13/M78__FileStore-main/core/log.log" , filemode='a' ,level=logging.INFO)
        logging.warning(f"This {username} try to sign in")

def Login():
    name = input("Name : ")
    last_name = input("Last_Name : ")
    phone=input("Phone : ")
    email= input("Email : ")
    national_id = input("National_id : ")
    age = input("Age : ")
    pasword = input("Password : ")
    user= User(name , last_name , phone , email , national_id , age,pasword)
    user.insert()
    logging.basicConfig(filename="C:/Users/Amir/Desktop/Maktab/maktab/week13/HW13/M78__FileStore-main/core/log.log" , filemode='a' ,level=logging.INFO)
    logging.info(f"This {name} create new account")
def salam(name):
    print("Hello ", name)
def sign_out():
    name = Config.status_sign_in
    Config.status_sign_in = False
    logging.basicConfig(filename="C:/Users/Amir/Desktop/Maktab/maktab/week13/HW13/M78__FileStore-main/core/log.log" , filemode='a' ,level=logging.INFO)
    logging.info(f"This {name} sign_out ")
def show_file():
    print(show())
def manager():
    username = input("Username : ")
    pasword = input("Password : ")
    manger = Manager(username , pasword)
    Config.status_sign_in = username
def add_file():
    if Config.status_sign_in:
        name_file = input("Name of your file : ")
        date_file  =input("Date of your file : ")
        price = int(input("Price of your file : "))
        Manager.add_file(name_file ,price,date_file)
        print("Succesfuly!!!")
        show_file()
        logging.basicConfig(filename="C:/Users/Amir/Desktop/Maktab/maktab/week13/HW13/M78__FileStore-main/core/log.log" , filemode='a' ,level=logging.INFO)
        logging.info(f"This {name_file} add")
def comment():
    if Config.status_sign_in:
        file_id = int(input("enter file_id for commnet : "))
        username=Config.status_sign_in 
        email=find(username)
        description= input("Your description : ")
        commeent(file_id , username , email,description)
        if commeent(file_id , username , email , description):
            print("succesfully!!!")
            show_comment()
            logging.basicConfig(filename="C:/Users/Amir/Desktop/Maktab/maktab/week13/HW13/M78__FileStore-main/core/log.log" , filemode='a' ,level=logging.INFO)
            logging.info(f"This {username} comment the file")
        else:
            print("Unsuccesfully!!!")
            logging.basicConfig(filename="C:/Users/Amir/Desktop/Maktab/maktab/week13/HW13/M78__FileStore-main/core/log.log" , filemode='a')
            logging.warning(f"This {username} can't comment the file")
def order():
    username=Config.status_sign_in 
    id = find_user_id(username)
    time=datetime.datetime.now()
    ordering(id ,time)
    if ordering(id ,time):
        logging.basicConfig(filename="C:/Users/Amir/Desktop/Maktab/maktab/week13/HW13/M78__FileStore-main/core/log.log" , filemode='a' ,level=logging.INFO)
        logging.info(f"This {id} order the file")
        order_id =find_order_id(id)
        print(order_id)
        print(type(order_id))
        file_id =int(input("File id : "))
        order_item(order_id ,file_id)
        if order_item(order_id ,file_id):
            print("succesfuly!!!")
    else:
        print("Unsuccesfully")
        logging.basicConfig(filename="C:/Users/Amir/Desktop/Maktab/maktab/week13/HW13/M78__FileStore-main/core/log.log" , filemode='a' ,level=logging.INFO)
        logging.warning(f"This {id} can't order the file")
def find(username):
    mail = finding(username)
    return mail
def show_comment():
    show_coment()
def order_item(order_id , file_id):
    ordering_item(order_id , file_id)
    if ordering_item(order_id , file_id):
        print("Succesfully!!!")
def show_order():
    user_name = input("username : ")
    show_ordering(user_name)
