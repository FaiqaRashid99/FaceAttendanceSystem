import re
from tkinter import*
from tkinter import ttk,messagebox
from wsgiref import validate
from PIL import Image, ImageTk  #pip install pillow
from tkinter import messagebox
import pymysql

# from images.lgin import Login_Window
# from login import Login_Window
# import pyttsx3

# def main():
#     win=Tk()
#     app=Register(win)
#     win.mainloop()      #for stoping window from closing on its own


class Register:
        def __init__(self,root):
                self.root=root
                self.root.title("Register")
                self.root.geometry("1366x768")#1366x768   960x540
                self.root.state("zoomed")

        #background image
                img0=Image.open(r'images\bg5.gif')
                self.bg=ImageTk.PhotoImage(img0)
                bg_lbl=Label(self.root,image=self.bg)
                bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #left image
                img1=Image.open(r'images\lf2.jpg')
                self.lf=ImageTk.PhotoImage(img1)
                lf_lbl=Label(self.root,image=self.lf)
                lf_lbl.place(x=88,y=100,width=400,height=500)
        #registration frame
                frame1=Frame(self.root,bg="white")
                frame1.place(x=480,y=100,width=700,height=500)

                title=Label(frame1,text="REGISTER HERE" ,font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
                
                # 1 ####################################################################################################

                fname=Label(frame1,text="First name" ,font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
                self.txt_fname=Entry(frame1,font=("times new roman",15),bg=("lightgray"))
                self.txt_fname.place(x=50,y=130,width=250)
                        #Bind and Validate:
                validate_fname=self.root.register(self.checkname)  #register is an inbuilt function in python
                self.txt_fname.config(validate="key",validatecommand=(validate_fname,"%P"))

                lname=Label(frame1,text="Last name" ,font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
                self.txt_lname=Entry(frame1,font=("times new roman",15),bg=("lightgray"))
                self.txt_lname.place(x=370,y=130,width=250)
                        #Bind and Validate:
                validate_lname=self.root.register(self.checkname)  #register is an inbuilt function in python
                self.txt_lname.config(validate="key",validatecommand=(validate_lname,"%P"))

                # 2 ######################################################################################################

                contact=Label(frame1,text="Contact Number" ,font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
                self.txt_contact=Entry(frame1,font=("times new roman",15),bg=("lightgray"))
                self.txt_contact.place(x=50,y=200,width=250)
                        

                email=Label(frame1,text="Email" ,font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
                self.txt_email=Entry(frame1,font=("times new roman",15),bg=("lightgray"))
                self.txt_email.place(x=370,y=200,width=250)
                       
                # 3 ######################################################################################################

                question=Label(frame1,text="Security Question" ,font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
                self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
                self.cmb_quest['values']=("Select","Your Favoruit Book Name","Your first pet name","Your Birth Place","Your Best Friend Name")
                self.cmb_quest.place(x=50,y=270,width=250)
                self.cmb_quest.current(0)

                answer=Label(frame1,text="Answer" ,font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
                self.txt_ans=Entry(frame1,font=("times new roman",15),bg=("lightgray"))
                self.txt_ans.place(x=370,y=270,width=250)

                # 4 ######################################################################################################

                password=Label(frame1,text="Password" ,font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
                self.txt_password=Entry(frame1,font=("times new roman",15),bg=("lightgray"))
                self.txt_password.place(x=50,y=340,width=250)
                        
                cpassword=Label(frame1,text="Confirm Password" ,font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
                self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg=("lightgray"))
                self.txt_cpassword.place(x=370,y=340,width=250)

                # 5 ######################################################################################################

                self.var_chk=IntVar()  #checkbox ki value get kernay k liye function is "variable" not textvariable ooook
                chk=Checkbutton(frame1,text="I Agree The Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white", font=("times new roman",12)).place(x=50,y=380) #onvalue mean jb ye checkbox click ho ga to is ki 1 value ho gi of off value ho ga to is ki value 0 ho gi
                self.chk_lbl=Label(frame1,text="",font=("times new roman",14),fg='red',bg=("lightgray"))
                self.chk_lbl.place(x=300,y=380,width=325)

                self.btn_img=ImageTk.PhotoImage(file="F:\\FYP folder\\r1.JPG")
                btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420) #bd=border

                self.btn_login=ImageTk.PhotoImage(file="F:\\FYP folder\\signin1.JPG")
                btn_login=Button(frame1,image=self.btn_login,bd=0,cursor="hand2",command=self.login_window).place(x=370,y=420,height=56)
                
                #############################################################################################
        # def login_window(self):
        #         self.new_window=Toplevel(self.root)
        #         self.app=Login_Window(self.new_window)    #,command=self.login_window


        def clear(self):
                self.txt_fname.delete(0,END)
                self.txt_lname.delete(0,END)
                self.txt_contact.delete(0,END)
                self.txt_email.delete(0,END)
                self.cmb_quest.current(0)
                self.txt_ans.delete(0,END)
                self.txt_password.delete(0,END)
                self.txt_cpassword.delete(0,END)

        def register_data(self):
                if self.txt_fname.get()=="":
                        messagebox.showerror("Error","PLease enter your first name",parent=self.root)
                elif self.txt_lname.get()=="":
                        messagebox.showerror("Error","PLease enter your last name",parent=self.root)
                elif self.txt_contact.get()=="" or len(self.txt_contact.get())!=11:
                        messagebox.showerror("Error","PLease enter the valid contact having length=11",parent=self.root)
                elif self.txt_email.get()=="":
                        messagebox.showerror("Error","PLease enter your Email",parent=self.root)          
                elif self.cmb_quest.get()=="Select":
                        messagebox.showerror("Error","Kindly select the question",parent=self.root)
                elif self.txt_ans.get()=="" :
                        messagebox.showerror("Error","PLease enter the security answer",parent=self.root)
                elif self.txt_password.get()=="" :
                        messagebox.showerror("Error","Password is necessary for security, please enter the password",parent=self.root)
                elif self.txt_cpassword.get()=="" :
                        messagebox.showerror("Error","Re Enter the password for further confirmation",parent=self.root)
                elif self.txt_password.get()!=self.txt_cpassword.get():
                        messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
                elif self.txt_email.get()!=None and self.txt_password.get()!=None:
                        x=self.checkemail(self.txt_email.get())
                        y=self.checkpassword(self.txt_password.get())
                if x==True and y==True:
                        if self.var_chk.get()==0:
                                self.chk_lbl.config(text='Please agree our terms & conditions',fg='red')
                        else:
                                self.chk_lbl.config(text='Checked',fg='green')
                                try:
                                        con=pymysql.connect(host="localhost",user="root", password="", database="fatsys")
                                        cur=con.cursor() #cursor() helps to execute queries
                                        cur.execute("select * from employee where email=%s",self.txt_email.get())
                                        row=cur.fetchone() # this will fetch the data from table if its email is similar to entered email
                                        # print(row)
                                        if row!=None:
                                                messagebox.showerror("Error","The user already exists, please try with another email",parent=self.root)
                                        else:
                                                cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                                (self.txt_fname.get(),
                                                self.txt_lname.get(),
                                                self.txt_contact.get(),
                                                self.txt_email.get(),
                                                self.cmb_quest.get(),
                                                self.txt_ans.get(),
                                                self.txt_password.get()
                                                ))
                                                con.commit() #saves changes in database as it is
                                                con.close()
                                                messagebox.showinfo("Success","Successfully Registered!",parent=self.root)
                                                self.clear()

                                except Exception as es:
                                        messagebox.showerror("Error",f"Error due to {str[es]}",parent=self.root)





##########################  VALIDATION FUNCTIONS #######################################################

#call back function: entry field me enter hotay sath us ko validate kre
        def checkname(self,name):
                if name.isalnum():   # isalnum= for validating digits + characters
                        return True
                if name=="":
                        return True
                else:
                        messagebox.showerror("Invalid","Not Allowed "+name[-1])
                        return False
        def checkcontact(self,contact):
                if contact.isdigit():
                        return True
                if len(str(contact))==0:
                        return True
                else:
                        messagebox.showerror("Invalid","Not Allowed "+contact[-1])
                        return False
        
        def checkpassword(self,password):
                if len(password)<=21: #max length must not exeed 21
                        if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
                                return True
                        else:
                                messagebox.showinfo('Alert','Password must contain minimum one Capital letter,a digit and a spacial character')
                                return False
                else:
                        messagebox.showerror("Inavalid", "Length of password must not exceed from 21" )
                        return False

        def checkemail(self,email):
                if len(email)>7: #max length must not exeed 21
                        if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                                return True
                        else:
                                messagebox.showinfo('Alert','Invalid Email, please enter valid email (example: abc@gmail.com')
                                return False
                else:
                        messagebox.showerror("Inavalid", "Length of email must not be less than 8" )
                        return False
                        
        
############################  LOGIN CLASS HERE ##########################################################


        def login_window(self):
                # self.new_window=Toplevel(self.root)#for opening a new window
                self.root.title("Login")
                self.root.geometry("1366x768")
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
                fname=Label(frame1,text="UserName" ,font=("times new roman",15,"bold"),bg="white",fg="black").place(x=70,y=150)
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
                elif self.lgin_fname.get()=="Faiqa" and self.lgin_password.get()=="Audacious99":
                        messagebox.showerror("Success","You have successfully loged In")
                else:
                        con=pymysql.connect(host="localhost",user="root",password="", database="fas")
                        cur=con.cursor()
                        cur.execute("select* from employee where email=%s and password=%s",(
                                self.txt_email.get(),
                                self.txt_password.get()
                                )
                        )
                        row=cur.fetchone()
                        if row==None:
                                messagebox.showerror("Error","Invalid username or password")
                        else:
                                open_main=messagebox.askyesno("yes/no", "Access only admin") ## ager login as admin yes he then open a new window i.e main window face recognition wali
                                if open_main>0:
                                        self.new_window=Toplevel(self.new_window)
               
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
                        con=pymysql.connect(host="localhost",user="root",password="", database="fatsys")
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
                        con=pymysql.connect(host="localhost",user="root",password="", database="fatsys")
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

if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()