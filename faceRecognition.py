from tkinter import*
from tkinter import ttk
import cv2
# import mysql.connector
from PIL import Image,ImageTk    #pip install Pillow
from tkinter import messagebox

import pymysql
class face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.title("Face Recognition")
        self.root.geometry("1366x768+0+0")

        #Title
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1500,height=45)
        
        #1st image
        img_top=Image.open(r"images\bgg2.jpeg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=630)

       
        #2nd image
        img_bottom=Image.open(r"images\studetails.jpeg")
        img_bottom=img_bottom.resize((950,630),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=630)

        #button
        b1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1.place(x=370,y=555,width=200,height=40)


    #==========Face Recognition===========

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=pymysql.connect(host="localhost",user="root", password="", database="fatsys")
                my_cursor=conn.cursor()

                my_cursor.execute("select stdName from student where st_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select RegNo from student where st_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select course from student where st_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)



                if confidence>77:
                    cv2.putText(img,f"Reg_no:{r}",(x,y-55),cv2.FONT_HARSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HARSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Course:{d}",(x,y-5),cv2.FONT_HARSHEY_COMPLEX,0.8,(255,255,255),3)

                else:
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HARSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier()     #copy xml file path and pass in cascadeclassifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows



if __name__=="__main__":
    root=Tk()
    app=face_recognition(root)
    root.mainloop()