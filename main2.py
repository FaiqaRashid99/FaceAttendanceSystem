from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import pymysql
from chatBot import ChatBot   
from student import Student
from tkinter import messagebox
import os
import numpy as np
import cv2

class Home2:
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

        title_lbl2=Label(bg_lbl,text="For Admin only",font=("times new roman",28,"bold"),bg="green",fg="yellow")
        title_lbl2.place(x=0,y=660,width=1500,height=45)

       
         #---------Photos-------#
        img5=Image.open(r"images\face-detection.png")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2",command=self.open_images)
        b1.place(x=350,y=200,width=220,height=220)

        b1_1=Button(bg_lbl,text="Student Photos",cursor="hand2",command=self.open_images,font=("times new roman",15,"bold"),bg="gray",fg="Black")
        b1_1.place(x=350,y=400,width=220,height=40)


        #---------Train Data-------#
        img6=Image.open(r"images\trainData.png")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_lbl,image=self.photoimg6,cursor="hand2")
        b1.place(x=780,y=200,width=220,height=220)

        b1_1=Button(bg_lbl,text="Train Data",cursor="hand2",command=self.train_classifier,font=("times new roman",15,"bold"),bg="gray",fg="Black")
        b1_1.place(x=780,y=400,width=220,height=40)

    #==========Functions Buttons=========
    def open_images(self):
        os.startfile("data")

    # ===============Training Function ===============
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # convert image to Gray scale image
            imageNp=np.array(img,'uint8')  #uint8 is a datatype for image.   #convert grid 
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp) #for showing window
            cv2.waitKey(1)==13 #if "enter" is clicked window will close
        ids=np.array(ids) #converting ids to numpy array       Numpy array make our performance faster

        # =============Train the classifier And save=============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")



if __name__=="__main__":
    root=Tk()
    app=Home2(root)
    root.mainloop()


     