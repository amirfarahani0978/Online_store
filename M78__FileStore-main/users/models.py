from core.models import DBModel
import re
from rich.console import Console
from rich.table import Table
import psycopg2
from configs import DB_CONNECTION
HOST = DB_CONNECTION["DBNAME"]
USER = DB_CONNECTION["USER"]
PASSWORD = DB_CONNECTION["PASSWORD"]
class User(DBModel):  # User model
    TABLE = 'users'
    PK = 'id'

    def __init__(self, full_name, last_name, phone,email, national_id, age, password, id=None) -> None:
        self.full_name = full_name
        self.last_name = last_name
        self.phone = phone
        self.email= email
        self.age = age
        self.national_id = national_id
        self.password = password
        if id:self.id=self.__class__.PK
    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self, number):
        pattern=re.compile(r'[0][9][0-9]{9}|[+989]{4}[0-9]{9}')
        result = pattern.finditer(number)
        for  i in result:
            print(i.group())
            self._phone = i.group()
    @property
    def full_name(self):
        return self._full_name
    @full_name.setter
    def full_name(self,name):
        pattern = re.compile(r'^[a-zA-Z-]{4,14}$')
        result = pattern.finditer(name)
        for  i in result:
            print(i.group())
            self._full_name = (i.group())
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self ,mail):
        pattern=re.compile(r'([a-zA-Z0-9-]+)(\@g?mail)(\.com)')
        result = pattern.finditer(mail)
        for  i in result:
            print(i.group())
            self._email = (i.group())
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self,name):
        pattern = re.compile(r'^[a-zA-Z-]{4,14}$')
        result = pattern.finditer(name)
        for  i in result:
            print(i.group())
            self._last_name = (i.group())
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,name):
        pattern = re.compile(r'^[0-9]{1,2}$')
        result = pattern.finditer(name)
        for  i in result:
            print(i.group())
            self._age = (i.group())
    @property
    def national_id(self):
        return self._national_id
    @national_id.setter
    def national_id(self,name):
        pattern = re.compile(r'^[0-9]{10}$')
        result = pattern.finditer(name)
        for  i in result:
            print(i.group())
            self._national_id = (i.group())
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,name):
        pattern = re.compile(r'^[a-zA-z0-9]{8,10}$')
        result = pattern.finditer(name)
        for  i in result:
            print(i.group())
            self._password = (i.group())
    def insert(self):
        try:
            conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
            cur = conn.cursor()
            command = """
            INSERT INTO users(first_name , last_name,phone,email, national_id, age, pasword ) 
            VALUES(%s,  %s, %s, %s , %s , %s,%s)
            RETURNING user_id
            """
            cur.execute(command, (self.full_name, self.last_name, self.phone,self.email ,self.national_id, self.age , self.password))
            row = cur.fetchone()
            self.id = row[0]
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
    def sign_in(username , pasword):
        try:
            conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
            cur = conn.cursor()
            command = f"""
            select first_name , pasword from users
            where first_name = '{username}' and pasword ='{pasword}'
            """
            cur.execute(command)
            row = cur.fetchone()
            # self.id = row[0]
            cur.close()
            # commit the changes
            print(row)
            return row
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
def show():
    try:
        table_public =[]
        conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
        cur = conn.cursor()
        command = f"""
        select * from files
        group by files_id
        """
        cur.execute(command)
        rows = cur.fetchall()
        # for row in rows:
        #     table_public.append(row)
        # print(row[1])
        table = Table(title=" !!! My Files !!!", title_style="white")
        # styles = ("cyan", "green")

        table.add_column("File_id", justify="magenta", style="cyan", no_wrap=True)
        table.add_column("Name", justify="magenta", style="magenta")
        table.add_column("price", justify="magenta", style="magenta")
        table.add_column("Date", justify="magenta", style="green")
        for row in rows:
            table.add_row(str(row[0]) , str(row[1]) ,str(row[2]) , str(row[3]))

        console = Console()
        console.print(table)
        # row = cur.fetchone()
        # self.id = row[0]
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
class Manager(DBModel): 
    def __init__(self , username , password) -> None:
        self.username  = username
        self.password = password
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,admin):
        if admin == "admin":
            self._password = admin
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,admin):
        if admin == "admin":
            self._username = admin
    def sign_in(username , pasword):
        try:
            conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
            cur = conn.cursor()
            command = f"""
            select first_name , pasword from users
            where first_name = '{username}' and pasword ='{pasword}'
            """
            cur.execute(command)
            # row = cur.fetchone()
            # self.id = row[0]
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
    def add_file(name_file ,price, date_file):
        try:
            conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
            cur = conn.cursor()
            command = f"""
            INSERT INTO files(name ,price, date) 
            VALUES(%s, %s , %s)
            RETURNING files_id
            """
            cur.execute(command , (name_file,price , date_file))
            # row = cur.fetchone()
            # self.id = row[0]
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        
def commeent(file_id,username , email , description):
    try:
        conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
        cur = conn.cursor()
        command = f"""
        INSERT INTO comments(file_id,first_name,email , description) 
        VALUES(%s,%s, %s , %s)
        """
        cur.execute(command , (file_id,username , email , description))
        # row = cur.fetchall()
        # self.id = row[0]
        cur.close()
        # commit the changes
        conn.commit()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def finding(username):
    try:
        conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
        cur = conn.cursor()
        command = f"""
            select first_name ,email from users
            where first_name = '{username}'
            """
        cur.execute(command)
        row = cur.fetchone()
        # self.id = row[0]
        cur.close()
        # commit the changes
        # conn.commit()
        return row[1]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def show_coment():
    try:
        conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
        cur = conn.cursor()
        command = f"""
        select * from comments
        order by comment_id
        """
        cur.execute(command)
        rows = cur.fetchall()
        # for row in rows:
        #     table_public.append(row)
        # print(row[1])
        table = Table(title=" !!! Comment !!!", title_style="white")
        # styles = ("cyan", "green")

        table.add_column("Comment_id", justify="magenta", style="cyan", no_wrap=True)
        table.add_column("File_id", justify="magenta", style="magenta")
        table.add_column("First_name", justify="magenta", style="magenta")
        table.add_column("Description", justify="magenta", style="green")
        for row in rows:
            table.add_row(str(row[0]) , str(row[1]) , str(row[2]) , str(row[4]))

        console = Console()
        console.print(table)
        # row = cur.fetchone()
        # self.id = row[0]
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def ordering(user_id , order_date):
    try:
        conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
        cur = conn.cursor()
        command = f"""
        INSERT INTO orders(user_id,order_date) 
        VALUES(%s,%s)
        """
        cur.execute(command, (user_id ,order_date))
        # row = cur.fetchall()
        # self.id = row[0]
        cur.close()
        # commit the changes
        conn.commit()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def find_user_id(username):
    table = []
    try:
        conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
        cur = conn.cursor()
        command = f"""
            select user_id ,first_name  from users
            where first_name = '{username}'
            """
        cur.execute(command)
        rows = cur.fetchone()
        for row in rows:
            table.append(row)
        id = table[0]
        cur.close()
        # commit the changes
        # conn.commit()
        return id
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def find_order_id(user_id):
    table =[]
    try:
        conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
        cur = conn.cursor()
        command = f"""
            select order_id,user_id ,order_date  from orders
            where user_id = '{user_id}'
            """
        cur.execute(command)
        rows = cur.fetchone()
        for row in rows:
            table.append(row)
        id = table[0]
        cur.close()
        # commit the changes
        # conn.commit()
        return id
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def ordering_item(order_id , file_id):
    try:
        conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
        cur = conn.cursor()
        command = f"""
        INSERT INTO order_item(order_id,file_id) 
        VALUES(%s,%s)
        """
        cur.execute(command, (order_id ,file_id))
        # row = cur.fetchall()
        # self.id = row[0]
        cur.close()
        # commit the changes
        conn.commit()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def show_ordering(user_id):
    table =[]
    try:
        conn = psycopg2.connect(f"dbname={HOST} user={USER} password={PASSWORD}")
        cur = conn.cursor()
        command = f"""
        select first_name , user_id , order_id from users
        join  orders  using (user_id)
        join  order_item  using (order_id)
        where first_name ='{user_id}'
        """
        cur.execute(command)
        rows = cur.fetchall()
        # for row in rows:
        #     table.append(row)
        # print(table)
        table = Table(title=" !!! Comment !!!", title_style="white")
        # styles = ("cyan", "green")

        table.add_column("Name", justify="magenta", style="cyan", no_wrap=True)
        table.add_column("User_d", justify="magenta", style="magenta")
        table.add_column("OrderID", justify="magenta", style="magenta")
        for row in rows:
            table.add_row(str(row[0]) , str(row[1]) , str(row[2]))

        console = Console()
        console.print(table)
        # row = cur.fetchone()
        # self.id = row[0]
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()