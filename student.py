from ast import Constant
from logging import exception
from operator import ge
from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk    #pip install Pillow
from tkinter import messagebox
import pymysql
import cv2
from tkinter import filedialog
import os

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Home")
        self.root.geometry("1366x768")
        self.root.state("zoomed")


        #=================Variables===========
        
        self.var_prog=StringVar()
        self.var_course=StringVar()
        self.var_batch=StringVar()
        self.var_semester=StringVar()
        self.var_std_name=StringVar()
        self.var_std_reg=StringVar()
        self.var_email=StringVar()
        self.var_phoneno=StringVar()
        self.var_teacher=StringVar()
        self.var_gender=StringVar()
        self.var_id=IntVar()

        # add_data
        #--------Background Image---------#
        img0=Image.open(r"images\bg5.gif")
        img0=img0.resize((1366,710),Image.ANTIALIAS)
        self.photoimg0=ImageTk.PhotoImage(img0)

        bg_lbl=Label(self.root,image=self.photoimg0)
        bg_lbl.place(x=0,y=0,width=1366,height=710)

        #--------Title--------#
        title_lbl=Label(bg_lbl,text="STUDENT DETAILS",font=("times new roman",35,"bold"),bg="darkgreen",fg="white")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        main_frame=Frame(bg_lbl,bd=2)
        main_frame.place(x=10,y=55,width=1330,height=630)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",14,"bold"))
        left_frame.place(x=10,y=5,width=640,height=610)

        img_left=Image.open(r"images\stupage.jpeg")
        img_left=img_left.resize((630,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=630,height=130)



        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",14,"bold"))
        right_frame.place(x=660,y=5,width=650,height=610)

        #current course information
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",14,"bold"))
        current_course_frame.place(x=5,y=135,width=630,height=125)
        
        #Program
        dep_label=Label(current_course_frame,text="Program",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_prog,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Program","BS","MS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",14,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","CS","IT","SE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Batch
        batch_label=Label(current_course_frame,text="Batch",font=("times new roman",14,"bold"),bg="white")
        batch_label.grid(row=1,column=0,padx=10,sticky=W)

        batch_combo=ttk.Combobox(current_course_frame,textvariable=self.var_batch,font=("times new roman",12,"bold"),state="readonly")
        batch_combo["values"]=("Select Batch","F18","S19","F19","S20","F20","S21","F21","S22")
        batch_combo.current(0)
        batch_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",14,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Student information
        student_info_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",14,"bold"))
        student_info_frame.place(x=5,y=260,width=630,height=320)

        #Student reg no
        studentReg_label=Label(student_info_frame,text="Student Reg#",font=("times new roman",14,"bold"),bg="white")
        studentReg_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentReg_entry=ttk.Entry(student_info_frame,textvariable=self.var_std_reg,width=20,font=("times new roman",14,"bold"))
        studentReg_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student name
        studentName_label=Label(student_info_frame,text="Student Name:",font=("times new roman",14,"bold"),bg="white")
        studentName_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        studentReg_entry=ttk.Entry(student_info_frame,textvariable=self.var_std_name,width=20,font=("times new roman",14,"bold"))
        studentReg_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Student Email
        studentEmail_label=Label(student_info_frame,text="Student Email:",font=("times new roman",14,"bold"),bg="white")
        studentEmail_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        studentEmail_entry=ttk.Entry(student_info_frame,textvariable=self.var_email,width=20,font=("times new roman",14,"bold"))
        studentEmail_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Student phoneno
        studentPhoneno_label=Label(student_info_frame,text="Student Phoneno:",font=("times new roman",14,"bold"),bg="white")
        studentPhoneno_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        studentPhoneno_entry=ttk.Entry(student_info_frame,textvariable=self.var_phoneno,width=20,font=("times new roman",14,"bold"))
        studentPhoneno_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #Teacher Name
        teacherName_label=Label(student_info_frame,text="Teacher name:",font=("times new roman",14,"bold"),bg="white")
        teacherName_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        teacherName_entry=ttk.Entry(student_info_frame,textvariable=self.var_teacher,width=20,font=("times new roman",14,"bold"))
        teacherName_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        #Gender
        gender_label=Label(student_info_frame,text="Student Gender:",font=("times new roman",14,"bold"),bg="white")
        gender_label.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        gender_combo=ttk.Combobox(student_info_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=5,column=1,padx=2,pady=10,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(student_info_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=7,column=0)
        
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(student_info_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=7,column=1)

        Sid_label=Label(student_info_frame,text="Student ID:",font=("times new roman",11),bg="white")
        Sid_label.grid(row=7,column=3,padx=3,pady=3,sticky=W)
        Sid_entry=ttk.Entry(student_info_frame,textvariable=self.var_id,width=20,font=("times new roman",11))
        Sid_entry.grid(row=7,column=4,padx=3,pady=3,sticky=W)

        #Button Frame
        btn_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=0,width=640,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="darkgreen",fg="white")
        save_btn.grid(row=0,column=0) 

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="darkgreen",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="darkgreen",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="darkgreen",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=35,width=640,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=31,font=("times new roman",13,"bold"),bg="darkgreen",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=31,font=("times new roman",13,"bold"),bg="darkgreen",fg="white")
        update_photo_btn.grid(row=0,column=1)

        #--------Search System--------#
        self.var_com_search=StringVar() #for combo box
        self.var_search=StringVar()     #for entry field


        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",14,"bold"))
        search_frame.place(x=5,y=80,width=640,height=110)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",14,"bold"),bg="darkgreen",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("Select","RegNo","stdName")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=("times new roman",14,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",command=self.search_data,width=12,font=("times new roman",13,"bold"),bg="darkgreen",fg="white")
        search_btn.grid(row=1,column=2)

        showAll_btn=Button(search_frame,text="Show All",command=self.fetch_data,width=12,font=("times new roman",13,"bold"),bg="darkgreen",fg="white")
        showAll_btn.grid(row=1,column=3)

        #========Table Frame=========#
        table_frame=Frame(right_frame,bd=1,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=200,width=640,height=380)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("st_id","dep","course","year","sem","reg","name","email","phoneno","teacher","gender","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("st_id",text="St_ID")
        self.student_table.heading("dep",text="Program")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("reg",text="StName")
        self.student_table.heading("name",text="RegNo")
        self.student_table.heading("email",text="StEmail")
        self.student_table.heading("phoneno",text="StPhoneno")
        self.student_table.heading("teacher",text="TName")
        self.student_table.heading("gender",text="StGender")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        #=============Function buttons============
    def add_data(self):
        if self.var_prog.get()=="Select Program" or self.var_std_name.get()=="" or self.var_std_reg.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
            try:
                    conn=pymysql.connect(host="localhost",user="root", password="", database="fatsys")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student(program,course,batch,semester,stdName,RegNo,email,phoneNo,teacher,gender,photosample) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_prog.get(),
                        self.var_course.get(),
                        self.var_batch.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_std_reg.get(),
                        self.var_email.get(),
                        self.var_phoneno.get(),
                        self.var_teacher.get(),
                        self.var_gender.get(),
                        self.var_radio1.get()
                        ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Your details has successfully been added")
            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)

################################ FETCH DATA ##############################################
    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root", password="", database="fatsys")
        my_cursor=conn.cursor()
        my_cursor.execute("select* from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit
        conn.close() 
############################## get cursor #############################################
#table me kisi line k data per click kren to wo sara data student form me fill ho jana chahiye 
# us k liye hum pehlay cursor ka focus len ge or phir table me mojood wo content hasil kren ge

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus) # item is used to get content from table
        data=content["values"]

        self.var_prog.set(data[1]),
        self.var_course.set(data[2]),
        self.var_batch.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_std_reg.set(data[6]),
        self.var_email.set(data[7]),
        self.var_phoneno.set(data[8]),
        self.var_teacher.set(data[9]),
        self.var_gender.set(data[10]),
        self.var_radio1.set(data[11]),
        self.var_id.set(data[0])


######################## FUNCTION FOR UPDATE ##################################
    def update_data(self):
        if self.var_prog.get()=="Select Program" or self.var_std_name.get()=="" or self.var_std_reg.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
            try:
                updatee=messagebox.askyesno("Update ","Do you want to update this student's details?",parent=self.root)
                if updatee>0:  #if yes button is clicked
                    conn=pymysql.connect(host="localhost",user="root", password="", database="fatsys")
                    my_cursor=conn.cursor()
                    sql="Update student set program=%s,course=%s,batch=%s,semester=%s,stdName=%s,email=%s,phoneNo=%s,teacher=%s,gender=%s,photosample=%s where RegNo=%s"
                    val=(self.var_prog.get(),
                        self.var_course.get(),
                        self.var_batch.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_email.get(),
                        self.var_phoneno.get(),
                        self.var_teacher.get(),
                        self.var_gender.get(),
                        self.var_radio1.get(),
                        self.var_std_reg.get())
                    my_cursor.execute(sql,val)
                else:
                    if not updatee: #if "no" button is clicked
                        return
                messagebox.showinfo("success","Student's details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except exception as es:
                messagebox.showerror("Error",f"Error due to {str[es]}",parrent=self.root)

############################ DELETE FUNCTION ###########################################
    def delete_data(self):
        if self.var_std_reg.get()=="":
            messagebox.showerror("Error","Registration number must not be empty",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Data","Do you want to delete this student data",parent=self.root)
                if delete>0:
                    conn=pymysql.connect(host="localhost",user="root", password="", database="fatsys")
                    my_cursor=conn.cursor()
                    sql="delete from student where RegNo=%s"
                    val=(self.var_std_reg.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete: #if "no" button is clicked
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted")

            except exception as es:
                messagebox.showerror("Error",f"Error due to {str[es]}",parrent=self.root)

############################ DELETE FUNCTION ###########################################
    def reset_data(self):
        self.var_prog.set("Select Program")
        self.var_course.set("Select Course")
        self.var_batch.set("Select Batch")
        self.var_semester.set("Select Semester")
        self.var_std_reg.set("")
        self.var_std_name.set("")
        self.var_email.set("")
        self.var_phoneno.set("")
        self.var_teacher.set("")
        self.var_gender.set("Select Gender")
        self.var_radio1.set("")


############################ search data ########################################3
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","please select option & enter what you want to search")
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root", password="", database="fatsys")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%" +str(self.var_search.get())+"%'")
                # my_cursor.execute("SELECT * FROM student WHERE RegNo=%s OR stdName=%s")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except exception as es:
                messagebox.showerror("Error",f"Error due to {str[es]}",parrent=self.root)


###################### Data set generation + taking photo sample ######################
    def generate_dataset(self):
                if self.var_prog.get()=="Select Program" or self.var_std_name.get()=="" or self.var_std_reg.get()=="":
                    messagebox.showerror("Error","All fields are Required",parent=self.root)
                else:
                
                        ########### Load predefined data on face frontal from opencv ##############
                            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                            def face_cropped(img):
                                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                faces=face_classifier.detectMultiScale(gray,1.3,5)  # scaling factor= 1.3
                                                                                    # minimum neighbour= 5
                                for (x,y,w,h)in faces:# x axis, y axis, width, height
                                    face_cropped=img[y:y+h, x:x+w]  # for x axis and y axis of image k kitni crop ho gi
                                    return face_cropped

                            # OPEN WEB CAM
                            cap=cv2.VideoCapture(0)   #web camera's by default value=0 koi or camera open kerna he to write 1
                            img_id=0
                            while True:
                                ret,my_frame=cap.read()
                                if face_cropped(my_frame) is not None:
                                    img_id += 1
                                    face=cv2.resize(face_cropped(my_frame),(450,450)) #passport size
                                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                    file_name_path="data/user."+format(self.var_id.get())+"."+str(img_id)+".jpg"
                                    cv2.imwrite(file_name_path,face)
                                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                    cv2.imshow("capture image",face)
                                    

                                if cv2.waitKey(1)==13 or int(img_id)==10:
                                        # 13: if "ENTER" is pressed, or images 50 k equal ho gai hain then it will get closed
                                    break
                            cap.release()
                            cv2.destroyAllWindows()
                            messagebox.showinfo("Result","Generating data sets completed.....")

  

    # def generate_dataset(self):
    #     if self.var_prog.get()=="Select Program" or self.var_std_name.get()=="" or self.var_std_reg.get()=="":
    #         messagebox.showerror("Error","All fields are Required",parent=self.root)
    #     else:
    #         try:
    #             conn=pymysql.connect(host="localhost",user="root", password="", database="fatsys")
    #             my_cursor=conn.cursor()
    #             my_cursor.execute("select * from student")
    #             myresult=my_cursor.fetchall()
    #             id=0
    #             for x in myresult:
    #                 id+=1
    #                 sql="Update student set program=%s,course=%s,batch=%s,semester=%s,stdName=%s,RegNo=%s,email=%s,phoneNo=%s,teacher=%s,gender=%s,photosample=%s where st_id=%i"
    #                 val=(self.var_prog.get(),
    #                     self.var_course.get(),
    #                     self.var_batch.get(),
    #                     self.var_semester.get(),
    #                     self.var_std_name.get(),
    #                     self.var_std_reg.get(),
    #                     self.var_email.get(),
    #                     self.var_phoneno.get(),
    #                     self.var_teacher.get(),
    #                     self.var_gender.get(),
    #                     self.var_radio1.get(),
    #                     self.var_id.get()==id+1
    #                     )
    #                 my_cursor.execute(sql,val)
    #                 conn.commit()
    #                 self.fetch_data()
    #                 self.reset_data()
    #                 conn.close()
    #             ########### Load predefined data on face frontal from opencv ##############
    #                 face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #                 def face_cropped(img):
    #                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #                     faces=face_classifier.detectMultiScale(gray,1.3,5)  # scaling factor= 1.3
    #                                                                         # minimum neighbour= 5
    #                     for (x,y,w,h)in faces:# x axis, y axis, width, height
    #                         face_cropped=img[y:y+h, x:x+w]  # for x axis and y axis of image k kitni crop ho gi
    #                         return face_cropped

    #                 # OPEN WEB CAM
    #                 cap=cv2.VideoCapture(0)   #web camera's by default value=0 koi or camera open kerna he to write 1
    #                 img_id=0
    #                 while True:
    #                     ret,my_frame=cap.read()
    #                     if face_cropped(my_frame) is not None:
    #                         img_id += 1
    #                         face=cv2.resize(face_cropped(my_frame),(450,450)) #passport size
    #                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
    #                         file_name_path="data/user."+format(self.var_id.get())+"."+str(img_id)+".jpg"
    #                         cv2.imwrite(file_name_path,face)
    #                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
    #                         cv2.imshow("capture image",face)
                            

    #                     if cv2.waitKey(1)==13 or int(img_id)==10:
    #                             # 13: if "ENTER" is pressed, or images 50 k equal ho gai hain then it will get closed
    #                         id+=1
    #                         break
    #                 cap.release()
    #                 cv2.destroyAllWindows()
    #                 messagebox.showinfo("Result","Generating data sets completed.....")
                    
    #         except exception as es:
    #             messagebox.showerror("Error",f"Error due to {str[es]}",parrent=self.root)

   
if __name__=="__main__":
    root=Tk()
    app=Student(root)
    root.mainloop()