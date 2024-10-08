from tkinter import *

# the main program
root = Tk()
root.geometry("800x500")  # width & height control
root.title("Home")  # name of the page

# lbfr1 =LabelFrame(root,text="this is label frame")
# lbfr1.pack(expand="yes",fill="both")
# lb1=Label(lbfr1,text="this is the label")
# lb1.pack()
ent = Entry(root)
ent.pack()
# btn1 =Button(root,text="Button 1")
# btn1.pack()
# btn1.place(anchor=NW,width=100,height=100,bordermode=OUTSIDE)
#



# fr2 = Frame(root)
# btn2 =Button(fr2,text="Button 2")
# fr3 = Frame(root)
# btn3 =Button(fr3,text="Button 3")
# fr4 = Frame(root)
# btn4 =Button(fr4,text="Button 4")
# btn1.pack()
# btn2.pack()
# btn3.pack()
# btn4.pack()

# fr1.grid(column=1,row=1)
# fr2.grid(column=2,row=1)
# fr3.grid(column=1,row=2)
# fr4.grid(column=2,row=2)


# def btn_print():
#     # print("hello world")
#     name = txt.get("1.0", "end")
#     lb1["text"] = name
# # add button and add some style to it
# ptn1 = Button(fr1,command=btn_print,text="click me",width="10",height="1",font="20",background="red",fg="white",padx=20)
# # command => bass the function to it to execute it when button clicked
# lb1=Label(fr1,text="Click me",width="50",height="5",font="30",background="black",fg="white",padx=20 ,pady=50)
# txt=Text(fr1,width="50",height="5",font="30",background="black",fg="white",padx=20 ,pady=50)
# fr1.pack()
# txt.pack()   # => add the text to the page
# ptn1.pack()  # => add the button to the page
# lb1.pack()  # => add the label to the page
root.mainloop()  # => show
