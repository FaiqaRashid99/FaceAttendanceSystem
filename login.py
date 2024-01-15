from email.mime import message
from multiprocessing.dummy.connection import Connection
from operator import index
import re
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk    #pip install Pillow
from tkinter import messagebox
import pymysql
from main2 import Home2
from register import Register

###############################################################################################################

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()      #for stoping window from closing on its own




##############################################################################################################

class Login_Window:

    def __init__(self,root):           #window's name= root
        self.root=root                 #initialization
        self.root.title("Login")
        self.root.geometry("1366x768") #1366x768 960x540
        self.root.state("zoomed")

       
         #=======Background Image=======#
        img0=Image.open(r"images\bg5.gif")
        self.bg=ImageTk.PhotoImage(img0)
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
         #left image
        img3=Image.open(r"images\lf2.jpg")
        self.lf=ImageTk.PhotoImage(img3)
        lf_lbl=Label(self.root,image=self.lf)
        lf_lbl.place(x=270,y=100,width=400,height=500)

        #Login frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=670,y=100,width=380,height=500)

        title=Label(frame1,text="Log In" ,font=("times new roman",20,"bold"),bg="white",fg="blue").place(x=150,y=100)

        #label
        fname=Label(frame1,text="User Email" ,font=("times new roman",15,"bold"),bg="white",fg="black").place(x=70,y=150)
        self.lgin_fname=Entry(frame1,font=("times new roman",15),bg=("lightgray"))
        self.lgin_fname.place(x=50,y=180,width=250)
       
        password=Label(frame1,text="Password" ,font=("times new roman",15,"bold"),bg="white",fg="black").place(x=75,y=230)
        self.lgin_password=Entry(frame1,font=("times new roman",15),bg=("lightgray"))
        self.lgin_password.place(x=50,y=260,width=250)

       
      

        #======Icon images======
        img1=Image.open(r"images\loginIcon1.jpeg")
        img1=img1.resize((25,25),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=720,y=250,width=25,height=25)

        img2=Image.open(r"images\lockIcon1.jpeg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lblimg1.place(x=720,y=330,width=25,height=25)

        img4=Image.open(r"images\loginIcon2.jpeg")
        img4=img4.resize((100,100),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lblimg1=Label(image=self.photoimage4,bg="white",borderwidth=0)
        lblimg1.place(x=810,y=100,width=100,height=100)

        #Login Button
        img5=Image.open(r"images\loginbutton.jpeg")
        img5=img5.resize((200,75),Image.ANTIALIAS)
        self.btn_img=ImageTk.PhotoImage(img5)
        btn=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.login).place(x=80,y=290, width=200) #bd=border


        #Register Button
        registerbtn=Button(frame1,text="Create New Account?",command=self.register_window,font=("times new roman",15,"bold"),borderwidth=0,fg="black",bg="white")
        registerbtn.place(x=35,y=380,width=185)

        #Forgot Password
        forgotbtn=Button(frame1,text="Forgot Password?",command=self.forgot_password_window,font=("times new roman",15,"bold"),borderwidth=0,fg="black",bg="white")
        forgotbtn.place(x=30,y=420,width=160)
    
    
    
    #Register Window in login form:
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    #Login Form Validation:
    def login(self):
        if self.lgin_fname.get()=="" or self.lgin_password.get()=="":
            messagebox.showerror("Error","All fields are required")
        # elif self.lgin_fname.get()=="Faiqa" and self.lgin_password.get()=="Audacious@99":
        #     messagebox.showerror("Success","You have successfully loged In")
        else:
             con=pymysql.connect(host="localhost",user="root",password="", database="fas")
             cur=con.cursor()
             cur.execute("select* from employee where email=%s and password=%s",(
                 self.lgin_fname.get(),
                 self.lgin_password.get()
                 )
             )
             row=cur.fetchone()
             if row==None:
                 messagebox.showerror("Error","Invalid username or password")
             else:
                 open_main=messagebox.askyesno("yes/no", "Access only admin") ## ager login as admin yes he then open a new window i.e main window face recognition wali
                 if open_main>0:

                    #  self.new_window=Toplevel(self.new_window)
                    #  self.app=index(self.new_window)  
                
                     self.new_window=Toplevel(self.root)
                     self.app=Home2(self.new_window)
                 else:
                        if open_main: # if "no" is clicked
                                return
        con.commit()
        con.close()
                    
#################################################################################################################
# FUNCTIONS:
#################################################################################################################


#Reset password
    def reset_pass(self):
            if self.cmb_quest.get()=="Select":
                    messagebox.showerror("Error","Select the security question",parent=self.root2)
            elif self.cmb_quest.get()=="":
                    messagebox.showerror("Error","Please enter the answer",parent=self.root2)
            elif self.txt_newpass.get()=="":
                    messagebox.showerror("Error","Please enter new password",parent=self.root2)
            else:
                    con=pymysql.connect(host="localhost",user="root",password="", database="fas")
                    cur=con.cursor()
                    query=("select * from employee where email=%s and question=%s and answer=%s")
                    value=(self.lgin_fname.get(), self.cmb_quest.get(), self.txt_ans.get())
                    cur.execute(query,value)
                    row=cur.fetchone()
                    if row==None:
                         messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
                    else:
                        query=("update employee set password=%s where email=%s")
                        value=(self.txt_newpass.get(),self.lgin_fname.get())
                        cur.execute(query,value)

                        con.commit()
                        con.close()
                        messagebox.showinfo("Notice","Your password has been reset successfully, now you can login with new password",parent=self.root2)
                        self.root2.destroy()
                   



#Forgot password
    def forgot_password_window(self):
        if self.lgin_fname.get()=="":
                messagebox.showerror("Error","please enter the email to reset password")
        else:
                con=pymysql.connect(host="localhost",user="root",password="", database="fas")
                cur=con.cursor()
                query=("select * from employee where email=%s")
                value=(self.lgin_fname.get())
                cur.execute(query,value)
                row=cur.fetchone()
                # print(row)
                if row==None:
                        messagebox.showerror("Error","please enter the valid username")
                else:
                        con.close()
                        self.root2=Toplevel()#for opening a new window
                        self.root2.title("Forgot Password")
                        self.root2.geometry("340x450+610+170")
                        l=Label(self.root2,text="Forgot Password",font=("times new roman",18,"bold"),fg="red",bg="white")
                        l.place(x=0,y=10,relwidth=1)

                        #security question answer from registeration class
                        question=Label(self.root2,text="Security Question" ,font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=80)
                        self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state="readonly",justify=CENTER)
                        self.cmb_quest['values']=("Select","Your Favoruit Book Name","Your first pet name","Your Birth Place","Your Best Friend Name")
                        self.cmb_quest.place(x=50,y=110,width=250)
                        self.cmb_quest.current(0)

                        answer=Label(self.root2,text="Security Answer" ,font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=150)
                        self.txt_ans=Entry(self.root2,font=("times new roman",15),bg=("lightgray"))
                        self.txt_ans.place(x=50,y=180,width=250)

                        #new password fild
                        new_password=Label(self.root2,text="New Password" ,font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=220)
                        self.txt_newpass=Entry(self.root2,font=("times new roman",15),bg=("lightgray"))
                        self.txt_newpass.place(x=50,y=250,width=250)

                        #RESET button
                        btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg=("green"))
                        btn.place(x=150,y=290)

##########################  VALIDATION FUNCTIONS #######################################################

#call back function: entry field me enter hotay sath us ko validate kre
#     def checkname(self,name):
#         if name.isalnum():   # isalnum= for validating digits + characters
#                 return True
#         if name=="":
#                 return True
#         else:
#          messagebox.showerror("Invalid","Not Allowed"+name[-1])




if __name__=="__main__":
    main()
    # root=Tk()
    # app=Login_Window(root)
    # root.mainloop()