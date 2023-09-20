from tkinter import *


wind_scr = Tk()
wind_scr.title('LOGIN PAGE')
wind_scr.config(bg='#0B5A81')

f = ('Times', 14)
var = StringVar()
var.set('male')



right_frame = Frame(wind_scr, bd=2, bg='#CCCCCC',relief=SOLID, padx=10, pady=10)

Label(right_frame, text="Enter Name", bg='#CCCCCC',font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(right_frame, text="Enter Email", bg='#CCCCCC',font=f).grid(row=1, column=0, sticky=W, pady=10)

Label(right_frame,text="Contact Number", bg='#CCCCCC',font=f).grid(row=2, column=0, sticky=W, pady=10)

Label(right_frame,text="Select Gender", bg='#CCCCCC',font=f).grid(row=3, column=0, sticky=W, pady=10)

Label(right_frame,text="Enter Password", bg='#CCCCCC',font=f).grid(row=5, column=0, sticky=W, pady=10)

Label(right_frame,text="Re-Enter Password", bg='#CCCCCC',font=f).grid(row=6, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(right_frame,bg='#CCCCCC',padx=10, pady=10,)


reg_name = Entry(right_frame, font=f)

reg_email = Entry(right_frame, font=f)

reg_mobile = Entry(right_frame, font=f)


male_rb = Radiobutton(gender_frame, text='Male',bg='#CCCCCC',variable=var,value='male',font=('Times', 10),)

female_rb = Radiobutton(gender_frame,text='Female',bg='#CCCCCC',variable=var,value='female',font=('Times', 10),)

others_rb = Radiobutton(gender_frame,text='Others',bg='#CCCCCC',variable=var,value='others',font=('Times', 10),)

reg_pwd = Entry(right_frame, font=f,show='*')

pwd_again = Entry(right_frame, font=f,show='*')

reg_btn = Button(right_frame, width=15, text='Register', font=f, relief=SOLID,cursor='hand2',command=None)


reg_name.grid(row=0, column=1, pady=10, padx=20)
reg_email.grid(row=1, column=1, pady=10, padx=20) 
reg_mobile.grid(row=2, column=1, pady=10, padx=20)
reg_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
reg_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.pack()

gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
others_rb.pack(expand=True, side=LEFT)


wind_scr.mainloop()
