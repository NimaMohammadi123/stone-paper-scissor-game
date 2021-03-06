from tkinter import *
from random import randint
win = Tk()


#by NIMA MOHAMMADI

select = {
    1:"سنگ",
    2:"قیچی",
    3:"کاغذ",
}

def stone():
    comp = randint(1,3)
    lbl["text"]= "انتخاب حریف :"+select[comp]
    if comp == 2:
        lblResultUser["text"] =int(lblResultUser["text"]) +1
    elif comp == 3:
        lblResultComputer["text"] = int (lblResultComputer["text"]) +1
        
def scissors():
    comp = randint(1,3)
    lbl["text"]= "انتخاب حریف : "+select[comp]
    if comp == 3:
        lblResultUser["text"] =int(lblResultUser["text"]) +1
    elif comp == 1:
        lblResultComputer["text"] = int (lblResultComputer["text"]) +1        

def paper():
    comp = randint(1,3)
    lbl["text"]= "انتخاب حریف : "+select[comp]
    if comp == 1:
        lblResultUser["text"] =int(lblResultUser["text"]) +1
    elif comp == 2:
        lblResultComputer["text"] = int (lblResultComputer["text"]) +1
        
def reset():
     lblResultComputer["text"] = "0"
     lblResultUser["text"] = "0"
     lbl["text"] = "انتخاب کنید"
            
win.title("سنگ . کاغذ . قیچی")
win.minsize(300,400)

win.rowconfigure([0,1] , weight=1)
win.columnconfigure(0 , weight=1)

lbl = Label(master=win , text="انتخاب کنید ", background="#fff"
          , height=2 , font=("none", 18,"bold"))
lbl.grid(row=0 , column=0 ,sticky="nwe")

frmBtn = Frame(master=win , height = 100 , background="red")


frmBtn.rowconfigure(0 , weight=1)
frmBtn.columnconfigure([0,1,2] , weight=1)

stoneButton = Button(master=frmBtn , text="سنگ" , height=3 , font =("none", 16 , "bold"),command=stone).grid(row = 0 ,column = 0 , sticky = "nwes" , padx=2 , pady=3)
paperButton = Button(master=frmBtn , text="کاغذ" , height=3, font =("none", 16 , "bold"),command=paper).grid(row = 0 ,column = 1 , sticky = "nwes", padx=2 , pady=3)
scissorButton = Button(master=frmBtn , text="قیچی" , height=3, font =("none", 16 , "bold"),command=scissors).grid(row = 0 ,column = 2 , sticky = "nwes", padx=2 , pady=3)

frmBtn.grid(row=1 , column=0 ,sticky="wen");

frmResult = Frame(master=win , height=200)

frmResult.rowconfigure(0 , weight=1)
frmResult.columnconfigure([0,1] , weight=1)

lblResultNameUser = Label(master=frmResult , text="امتیاز شما " , relief = "ridge").grid (row= 0 , column=0 ,sticky = "nswe")
lblResultNameComputer = Label(master=frmResult , text="امتیاز حریف " ,relief = "ridge").grid (row= 0 , column=1 ,sticky = "nswe")

lblResultUser =Label (master = frmResult , text = "0" , background="blue" ,fg= "#fff" ,height=3, font=("none" ,  40 , "bold"))
lblResultUser.grid(row = 1 , column = 0 , sticky="nswe")
lblResultComputer =Label (master = frmResult , text = "0" , background="green" ,fg= "#fff",height=3, font=("none" ,  40 , "bold"))
lblResultComputer.grid(row = 1 , column = 1 , sticky="nswe")

frmResult.grid(row=2 , column=0 , sticky="nswe")

BtnReset = Button (text= " برو از اول" , font=("none", 18 , "bold") , relief="ridge", command=reset).grid (row=3 , column=0 , sticky="nswe")

win.mainloop()
