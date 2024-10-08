from AnnModel import *
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import tkinter.messagebox


# root=Tk()
# root.geometry("700x350")
# fr1 =Frame(root)
# bt1=Button(fr1,text='new data', width='30',height='2',bg='black',fg='white',font="20")
# bt2=Button(fr1,text='predict', width='30',height='2',bg='black',fg='white', font="20")

# fr1.pack(pady=100)
# bt1.pack(pady=5)
# bt2.pack(pady=15)
# mainloop()



win = Tk()
obj=AnnModel() 
#  # Set the geometry of tkinter frame
win.geometry("700x350")
file=""

def open_file():
    file = filedialog.askopenfilename(initialdir = "/" ,filetypes=[('All files', '*.*')])
    print("file path is " ,file)
    label["text"]=file

def predict_image():
    img_path = label["text"]
    pred = obj.predectation(img_path)
    label["text"]=pred

ttk.Button( text="Browse",width='30', command=open_file).pack(pady=50)
label = Label(win, text="", font=('Georgia 13'),width=50)
label.pack(pady=50)
bt1=Button(text="submit",width='30',height='2',bg='black',fg='white',font="20", command = predict_image )
bt1.pack(pady=5,padx=50)


win.mainloop()

 # if file=="":
    #     tkinter.messagebox.showerror(title="error", message="please selct file")    
    # else :





















# Create an instance of tkinter frame
# win = Tk()

#  # Set the geometry of tkinter frame
# win.geometry("700x350")

# def open_file():
#     file = filedialog.askopenfilename(initialdir = "/" ,filetypes=[('All files', '*.*')])
#     print("file path is " ,file)








# def browse_button():
#     filename = filedialog.askdirectory()
#     print(filename)
#     return filename


# root = Tk()
# v = StringVar()
# button2 = Button(text="Browse", command=browse_button).grid(row=0, column=3)

# mainloop()
#    if file:
#       content = file.read()
#       file.close()
#       print("%d characters in this file" % len(content))

# # Add a Label widget
# label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'), command = filedialog)
# label.pack(pady=10)

# Create a Button
# ttk.Button( text="Browse", command=open_file).pack(pady=50)

# win.mainloop()

# button = ttk. Button (labelFrame, text = "Browse A File", command = fileDialog)
# button.grid (column = 1, row = 1)
# filename = filedialog.askopenfilename (initialdir = "/", title = "Select A File", filetype = (("jpeg", "*.jpg ",('All Files', '*.*')))

# # ttk.Button( text="Browse", command=open_file).pack(pady=50)

# win.mainloop()

