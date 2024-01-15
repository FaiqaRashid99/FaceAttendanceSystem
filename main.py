from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import pymysql
from chatBot import ChatBot
from faceRecognition import face_recognition
from login import Login_Window   
from student import Student
from tkinter import messagebox
import os
import numpy as np
import cv2

class Home:
    def __init__(self,root):
        self.root=root
        self.root.title("Home")
        self.root.geometry("1366x768")
        self.root.state("zoomed")

          #--------Background Image---------#
        img0=Image.open(r"images\bg5.gif")
        self.bg=ImageTk.PhotoImage(img0)
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #--------Title--------#
        title_lbl=Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        #--------Student Details Button--------#

        img1=Image.open("images\studetails.jpeg")
        img1=img1.resize((220,220),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(bg_lbl,image=self.photoimg1,cursor="hand2",command=self.student_details)
        b1.place(x=130,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Black")
        b1_1.place(x=130,y=320,width=220,height=40)

        #-----Detect Face--------#
        img2=Image.open(r"images\detectface.jpeg")
        img2=img2.resize((220,220),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_lbl,image=self.photoimg2,cursor="hand2",command=self.faceRecogn)
        b1.place(x=570,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Face Detector",cursor="hand2", command=self.faceRecogn,font=("times new roman",15,"bold"),bg="white",fg="Black")
        b1_1.place(x=570,y=320,width=220,height=40)

        #-------Attendance Face Button-------#
        img3=Image.open(r"images\faceAttendance.jpeg")
        img3=img3.resize((220,220),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(bg_lbl,image=self.photoimg3,cursor="hand2")
        b1.place(x=1000,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Black")
        b1_1.place(x=1000,y=320,width=220,height=40)

        

         #---------chat bot-------#
        img5=Image.open(r"images\chatbot.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2",command=self.openChatBot)
        b1.place(x=350,y=400,width=220,height=220)

        b1_1=Button(bg_lbl,text="ChatBot",command=self.openChatBot,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Black")
        b1_1.place(x=350,y=600,width=220,height=40)


        #---------Exit-------#
        img6=Image.open(r"images\exit.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_lbl,image=self.photoimg6,cursor="hand2")
        b1.place(x=780,y=400,width=220,height=220)

        b1_1=Button(bg_lbl,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="Black")
        b1_1.place(x=780,y=600,width=220,height=40)

 #---------Admin Login-------#
    
        b1_1=Button(bg_lbl,text="Admin Login",cursor="hand2",command=self.openLogin,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=1050,y=600,width=200,height=40)

    
    

   ################# Face Recognition ########################################
    # def face_recog(self):
    #         def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
    #             gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #             features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

    #             coord=[]

    #             for(x,y,w,h) in features:
    #                 cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
    #                 id,predict=clf.predict(gray_image[y:y+h,x:x+w])
    #                 confidence=int((100*(1-predict/300)))

    #                 conn=pymysql.connect(host="localhost",user="root", password="", database="fas")
    #                 my_cursor=conn.cursor()

    #                 my_cursor.execute("select Name from student where st_id="+str(id))
    #                 i=my_cursor.fetchone()
    #                 i="+".join(i)

    #                 my_cursor.execute("select reg_no from student where st_id="+str(id))
    #                 r=my_cursor.fetchone()
    #                 r="+".join(r)

    #                 my_cursor.execute("select dep from student where st_id="+str(id))
    #                 d=my_cursor.fetchone()
    #                 d="+".join(d)



    #                 if confidence>77:
    #                     cv2.putText(img,f"Reg_no:{r}",(x,y-55),cv2.FONT_HARSHEY_COMPLEX,0.8,(255,255,255),3)
    #                     cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HARSHEY_COMPLEX,0.8,(255,255,255),3)
    #                     cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HARSHEY_COMPLEX,0.8,(255,255,255),3)

    #                 else:
    #                     cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
    #                     cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HARSHEY_COMPLEX,0.8(255,255,255),3)

    #                 coord=[x,y,w,h]

    #             return coord
            
    #         def recognize(img,clf,faceCascade):
    #             coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
    #             return img
            
    #         faceCascade=cv2.CascadeClassifier()     #copy xml file path and pass in cascadeclassifier
    #         clf=cv2.face.LBPHFaceRecognizer_create()
    #         clf.read("classifier.xml")

    #         video_cap=cv2.VideoCapture(0)

    #         while True:
    #             ret,img=video_cap.read()
    #             img=recognize(img,clf,faceCascade)
    #             cv2.imshow("Welcome to face recognition",img)

    #             if cv2.waitKey(1)==13:
    #                 break
    #             video_cap.release()
    #             cv2.destroyAllWindows





        #==========Functions Buttons=========
    def open_images(self):
        os.startfile("data")

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def openChatBot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)
    def openLogin(self):
        self.new_window=Toplevel(self.root)
        self.app=Login_Window(self.new_window)
    def faceRecogn(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)
        
  



if __name__=="__main__":
    root=Tk()
    app=Home(root)
    root.mainloop()