from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open(r'images\chatbot.jpeg')
        img_chat=img_chat.resize((250,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='blue',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=18,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label1.grid(row=0,column=0,padx=5,sticky=W)
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=35,font=('arial',14,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send",command=self.send,font=('arial',14,'bold'),width=8,bg='blue',fg='white')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear",command=self.clear,font=('arial',16,'bold'),width=8,bg='green',fg='white')
        self.clear.grid(row=1,column=0,padx=5,pady=10,sticky=W)
        
        self.msg=''
        self.label2=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label2.grid(row=1,column=1,padx=5,sticky=W)

    #############Function Declaration##############
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('') 
    
    
    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)

        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label2.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label2.config(text=self.msg,fg='red')

        if(self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
        elif(self.entry.get()=='Hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')
        elif(self.entry.get()=='How are you?'):
            self.text.insert(END,'\n\n'+'Bot: Fine and you')
        elif(self.entry.get()=='Fantastic'):
            self.text.insert(END,'\n\n'+'Bot: Nice to hear')
        elif(self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Bot: Thank you for chatting')
        
        else:
             self.text.insert(END,'\n\n'+"Bot: Sorry I didn't get it")
        


if __name__=='__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()