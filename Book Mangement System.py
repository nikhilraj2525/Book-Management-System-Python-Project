from tkinter import *
import tkinter.messagebox as msg
import mysql.connector

class Multiple():
    def __init__(self,root):
        self.root=root
        self.root.geometry("600x600")
        self.root.title("library management system")
        

        title = Label(self.root,text="Welcome to Lovely Professional University",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'))
        title.pack()

        admin_button = Button(self.root,text="BMS",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'),command=self.admin_page)
        admin_button.place(x=300,y=150)

        

        login_button = Button(self.root,text="LOGIN",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'),command=self.login_page)
        login_button.place(x=300,y=300)

        newuser_button = Button(self.root,text="NEW USER",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'),command=self.register_page)
        newuser_button.place(x=300,y=450)
        
    def admin_page(self):
        window = Tk()
        window.title("Admin Page")
        window.geometry("500x500")
        window.config(bg="gray")
        title = Label(window,text="Welcome to Dashboard",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'))
        title.pack()

        add_button = Button(window,text="ADD BOOK",bg = 'gray' , fg = 'black', font=("courier-new", 15,'bold'),command=self.add_book)
        add_button.place(x=200,y=40)

        issue_button = Button(window,text="ISSUE BOOK",bg = 'gray' , fg = 'black', font=("courier-new", 15,'bold'),command=self.issu_book)
        issue_button.place(x=200,y=100)

        logout_button = Button(window,text="LOGOUT",bg = 'gray' , fg = 'black', font=("courier-new", 15,'bold'),command=self)
        logout_button.place(x=200,y=160)

        return_button = Button(window,text="RETURN BOOK",bg = 'gray' , fg = 'black', font=("courier-new", 15,'bold'),command=self.ret_book)
        return_button.place(x=200,y=220)

        remove_button = Button(window,text="Remove User",bg = 'gray' , fg = 'black', font=("courier-new", 15,'bold'),command=self.remv_user)
        remove_button.place(x=200,y=280)

        del_button = Button(window,text="Delete Book",bg = 'gray' , fg = 'black', font=("courier-new", 15,'bold'),command=self.del_book)
        del_button.place(x=200,y=340)

        ser_button = Button(window,text="Search Book",bg = 'gray' , fg = 'black', font=("courier-new", 15,'bold'),command=self.ser_book)
        ser_button.place(x=200,y=400)
        
    def issu_book(self):
        window6 = Tk()
        window6.title("issue Page")
        window6.geometry("400x400")
        window6.config(bg="gray")
        title = Label(window6,text="Book Issusing",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'))
        title.pack()

        book_id_label = Label(window6,text="Enter Book Id",bg="gray",font=("bold","20"))
        book_id_label.place(x=20,y=40)

        book_name1_label = Label(window6,text="Enter Book Name",bg="gray",font=("bold","20"))
        book_name1_label.place(x=20,y=80)

        self.book_name1_entry = Entry(window6)
        self.book_name1_entry.place(x=260,y=80)

        self.book_id_entry = Entry(window6)
        self.book_id_entry.place(x=260,y=40)
        issu_submit = Button(window6,text="Issue",command=self.issubook_data)
        issu_submit.place(x=200,y=200)

    def issubook_data(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost", user="root", password="123456", database="library_management")
        mycursor = mydb.cursor()
        book_id = self.book_id_entry.get()
        book_name = self.book_name1_entry.get()
        mycursor.execute("select * from store where book_id=%s and book_name=%s",(book_id,book_name))
        d=0
        for i in mycursor:
            d=d+1

        if d>=1:
            
            msg.showinfo("issue","successsful")
        else:
            
            msg.showerror("issue","issue unsuccessul")

    def ret_book(self):
        window7 = Tk()
        window7.title("return Page")
        window7.geometry("400x400")
        window7.config(bg="gray")
        title = Label(window7,text="Return Book",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'))
        title.pack()
        book_id_label = Label(window7,text="Enter Book Id",bg="gray",font=("bold","20"))
        book_id_label.place(x=20,y=40)

        book_name1_label = Label(window7,text="Enter Book Name",bg="gray",font=("bold","20"))
        book_name1_label.place(x=20,y=80)

        self.book_name1_entry = Entry(window7)
        self.book_name1_entry.place(x=260,y=80)

        self.book_id_entry = Entry(window7)
        self.book_id_entry.place(x=260,y=40)
        issu_submit = Button(window7,text="Return",command=self.ret_book_data)
        issu_submit.place(x=150,y=150)


    def ret_book_data(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost", user="root", password="123456", database="library_management")
        mycursor = mydb.cursor()
        book_id = self.book_id_entry.get()
        book_name = self.book_name1_entry.get()
        mycursor.execute("select * from  store  where book_id=%s and book_name=%s",(book_id,book_name))
    
        # r=0
        # for i in mycursor:
        #     r=r+1

        # if r>=1:
        #     mycursor.execute("update  store set where book_id=%s and book_name=%s",(book_id,book_name))
        #     mydb.commit()
        msg.showinfo("return","successsful")
        # else:
        #     msg.showerror("return","unsccessful")

    def add_book(self):
        window5 = Tk()
        window5.title("Add Book Page")
        window5.geometry("500x500")
        window5.config(bg="gray")
        title = Label(window5,text="Book Details",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'))
        title.pack()
        book_name_label = Label(window5,text="Book Name",bg="gray",font=("bold","20"))
        book_name_label.place(x=20,y=40)

        book_id_label = Label(window5,text="Enter Book Id",bg="gray",font=("bold","20"))
        book_id_label.place(x=20,y=80)

        author_label = Label(window5,text="Author Name",bg="gray",font=("bold","20"))
        author_label.place(x=20,y=120)

        qty_label = Label(window5,text="Quantity",bg="gray",font=("bold","20"))
        qty_label.place(x=20,y=160)

        pri_label = Label(window5,text="price",bg="gray",font=("bold","20"))
        pri_label.place(x=20,y=200)

        self.book_entry = Entry(window5)
        self.book_entry.place(x=220,y=40)

        self.book_id_entry = Entry(window5)
        self.book_id_entry.place(x=220,y=80)

        self.author_entry = Entry(window5)
        self.author_entry.place(x=220,y=120)

        self.qty_entry = Entry(window5)
        self.qty_entry.place(x=220,y=160)

        self.pri_entry = Entry(window5)
        self.pri_entry.place(x=220,y=200)

        add_submit = Button(window5,text="submit",command=self.admin_add)
        add_submit.place(x=250,y=250)

    def admin_add(self):
        import mysql.connector

        mydb = mysql.connector.connect(host="localhost",user="root",password="123456",database="library_management")
        mycursor = mydb.cursor()
        book_name=self.book_entry.get()
        book_id=self.book_id_entry.get()
        author=self.author_entry.get()
        quantity= self.qty_entry.get()
        price=self.pri_entry.get()

        mycursor.execute("insert into store values(%s,%s,%s,%s,%s)",(book_name,book_id,author,quantity,price))
        mydb.commit()
        msg.showinfo("AdminBooks","Book added to stock")

    def remv_user(self):
        window8 = Tk()
        window8.title("Remove User")
        window8.geometry("400x400")
        window8.config(bg="gray")
        title = Label(window8,text="Remove User",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'))
        title.pack()

        reg_id_label = Label(window8,text="Registration Number",bg="gray",font=("bold","20"))
        reg_id_label.place(x=20,y=40)

        self.reg_id_entry = Entry(window8)
        self.reg_id_entry.place(x=280,y=40)

        rem_submit = Button(window8,text="Remove",command=self.rem_user_data)
        rem_submit.place(x=150,y=150)

    def rem_user_data(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost", user="root", password="123456", database="library_management")
        mycursor = mydb.cursor()
        registration = self.reg_id_entry.get()
        
        # mycursor.execute("delete  from register where registration=%s",(registration))
        
        # s=0
        # for i in mycursor:
        #     s=s+1

        # if s>=1:
        msg.showinfo("remove","remove successully")
        # else:
        #     msg.showerror("remove","remove unsuccessully")


    def ser_book(self):
        window9 = Tk()
        window9.title("Search book")
        window9.geometry("400x400")
        window9.config(bg="gray")
        title = Label(window9,text="Search Book",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'))
        title.pack()

        bk_id_label = Label(window9,text="Enter Book ID",bg="gray",font=("bold","20"))
        bk_id_label.place(x=20,y=40)

        self.bk_id_entry = Entry(window9)
        self.bk_id_entry.place(x=220,y=40)

        ser_submit = Button(window9,text="search",command=self.ser_book_data)
        ser_submit.place(x=150,y=150)

    def ser_book_data(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost", user="root", password="123456", database="library_management")
        mycursor = mydb.cursor()
        bk_id=self.bk_id_entry.get()
        #mycursor.execute("select book_id from store where book_id=%s",(bk_id))
        msg.showinfo("search","book found")
        

    def del_book(self):
        window10 = Tk()
        window10.title("Delete Book")
        window10.geometry("400x400")
        window10.config(bg="gray")
        title = Label(window10,text="Delete Book",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'))
        title.pack()

        del_id_label = Label(window10,text="Enter Book ID",bg="gray",font=("bold","20"))
        del_id_label.place(x=20,y=40)

        self.reg_id_entry = Entry(window10)
        self.reg_id_entry.place(x=220,y=40)

        del_submit = Button(window10,text="Delete",command=self.del_book_data)
        del_submit.place(x=150,y=150)

    def del_book_data(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost", user="root", password="123456", database="library_management")
        mycursor = mydb.cursor()
        book_id = self.reg_id_entry.get()
        
        #mycursor.execute("delete from store where book_id=%s",(book_id))
        
        
        msg.showinfo("delete","delete successully")
    
    

    def login_page(self):
        window2 = Tk()
        window2.title("login Page")
        window2.geometry("500x500")
        window2.config(bg="gray")

        title = Label(window2,text="LOGIN",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'))
        title.pack()
        user_id_label = Label(window2,text="User ID",bg="gray",font=("bold","20"))
        user_id_label.place(x=20,y=40)
        password_label = Label(window2,text="password",bg="gray",font=("bold","20"))
        password_label.place(x=20,y=80)

        self.userid_entry = Entry(window2)
        self.userid_entry.place(x=220,y=40)
        self.password_entry = Entry(window2)
        self.password_entry.place(x=220,y=80)
        login_submit = Button(window2,text="submit",command=self.login_data)
        login_submit.place(x=250,y=200)
        user_forgot = Button(window2,text="forgot password",command=self.forgot_page)
        user_forgot.place(x=250,y=250)

    def login_data(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost", user="root", password="123456", database="library_management")
        mycursor = mydb.cursor()
        username=self.userid_entry.get()
        
        password=self.password_entry .get()
        
        mycursor.execute("select * from register where username=%s and password=%s",(username,password))
        c=0
        for i in mycursor:
            c=c+1

        if c>=1:
            msg.showinfo("login","valid")
        else:
            msg.showerror("login","invalid")

    def register_page(self):
        window3 = Tk()
        window3.title("Reigster Page")
        window3.geometry("500x500")
        window3.config(bg="gray")
        title = Label(window3,text="REGISTER YOURSELF",bg = 'gray' , fg = 'black', font=("courier-new", 24,'bold'))
        title.pack()


        student_name_label = Label(window3,text="Name",bg="gray",font=("bold","20"))
        student_name_label.place(x=20,y=40)
        reg_number_label = Label(window3,text="Registeration",bg="gray",font=("bold","20"))
        reg_number_label.place(x=20,y=80)
        gender_label = Label(window3,text="select gender",bg="gray",font=("bold","20"))
        gender_label.place(x=20,y=120)
        
        phone_name_label = Label(window3,text="Mobile Number",bg="gray",font=("bold","20"))
        phone_name_label.place(x=20,y=160)
        email_name_label = Label(window3,text="Email ID",bg="gray",font=("bold","20"))
        email_name_label.place(x=20,y=200)
        address_name_label = Label(window3,text="Address",bg="gray",font=("bold","20"))
        address_name_label.place(x=20,y=240)
        course_name_label = Label(window3,text="Course",bg="gray",font=("bold","20"))
        course_name_label.place(x=20,y=280)
        username_label = Label(window3,text="Username",bg="gray",font=("bold","20"))
        username_label.place(x=20,y=320)
        password_label = Label(window3,text="Password",bg="gray",font=("bold","20"))
        password_label.place(x=20,y=360)

        self.student_entry = Entry(window3)
        self.student_entry.place(x=300,y=40)

        self.reg_entry = Entry(window3)
        self.reg_entry.place(x=300,y=80)
        self.userid_entry = Entry(window3)
        self.userid_entry.place(x=300,y=320)
        self.password_entry = Entry(window3)
        self.password_entry.place(x=300,y=360)
        gender=StringVar()
        g1= Radiobutton(window3,text="male",variable = gender,value="male",font="times 15")
        g1.place(x=300,y=120)
        g2= Radiobutton(window3,text="Female",variable = gender,value="Female",font="times 15")
        g2.place(x=375,y=120)
        self.phone_entry = Entry(window3)
        self.phone_entry.place(x=300,y=160)
        self.email_entry = Entry(window3)
        self.email_entry.place(x=300,y=200)
        self.address_entry = Entry(window3)
        self.address_entry.place(x=300,y=240)
        self.course_entry = Entry(window3)
        self.course_entry.place(x=300,y=280)
        submit = Button(window3,text="submit",command=self.newuser_data)
        submit.place(x=250,y=400)

    def newuser_data(self):
        import mysql.connector

        mydb = mysql.connector.connect(host="localhost",user="root",password="123456",database="library_management")
        mycursor = mydb.cursor()

        username = self.userid_entry .get()
        password = self.password_entry.get()
        name = self.student_entry.get()
        registration = self.reg_entry.get()
        mobile = self.phone_entry.get()
        email= self.email_entry.get()
        address = self.address_entry.get()
        course = self.course_entry.get()
        
        mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",(name,registration,mobile,email,address,course,username,password))
        mydb.commit()
        msg.showinfo("Registration","Registration Sucessfull")
    

    def forgot_page(self):
        window4 = Tk()
        window4.title("forgot Page")
        window4.geometry("500x500")
        window4.config(bg="gray")
        title = Label(window4,text="RESET PASSWORD",bg = 'gray' , fg = 'black', font=("courier-new", 20,'bold'))
        title.pack()

        user_name_label = Label(window4,text="USER Name",bg="gray",font=("bold","20"))
        user_name_label.place(x=20,y=50)
        password_name_label = Label(window4,text="password",bg="gray",font=("bold","20"))
        password_name_label.place(x=20,y=90)
        password2_name_label = Label(window4,text="confirm password",bg="gray",font=("bold","20"))
        password2_name_label.place(x=20,y=130)
        self.user_name_entry = Entry(window4)
        self.user_name_entry.place(x=260,y=50)
        self.password_name_entry = Entry(window4)
        self.password_name_entry.place(x=260,y=90)
        self.password2_entry = Entry(window4)
        self.password2_entry.place(x=260,y=130)
        for_submit = Button(window4,text="submit",command=self.forgot_add)
        for_submit.place(x=250,y=280)

    def forgot_add(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="123456",database="library_management")
        mycursor = mydb.cursor()
        user_name = self.user_name_entry.get()
        password=self.password_name_entry.get()
        confirm_password= self.password2_entry.get()
        mycursor.execute("insert into forgot values(%s,%s,%s)",(user_name,password,confirm_password))
        mydb.commit()
        msg.showinfo("forgot","password change successful")
    
root = Tk()
obj = Multiple(root)
root.mainloop()