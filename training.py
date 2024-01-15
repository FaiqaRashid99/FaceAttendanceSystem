from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk 
import numpy as np
import os
import cv2

class Train:
    def __init__(self,root):
        self.root=root
        self.root.title("train data")
        self.root.geometry("1366x768+0+0")

        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="darkgreen",fg="white")
        title_lbl.place(x=0,y=0,width=1366,height=55)

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



if __name__=='__main__':
    root=Tk()
    obj=Train(root)
    root.mainloop()