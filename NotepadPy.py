from tkinter import *
from tkinter import filedialog

filename = None

def newFile():
	global filename
	filename  = "Untitled"
	text.delete(0.0, END)

def saveFile():
	global filename
	filename = "Untitled"
	t = text.get(0.0,END)
	f = open(filename,"w")
	f.write(t)
	f.close()

def saveAs():
	f = filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title = "OOPS...",message = "Unable to save file !!!!")

def openFile():
	f = filedialog.askopenfile(mode = 'r')
	t = f.read()
	text.delete(0.0,END)
	text.insert(0.0,t)


root = Tk()
root.title("NotepadPy")
root.minsize(width = 500,height = 500)
root.maxsize(width = 500,height = 500)

text = Text(root,width = 500,height  = 500)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label = 'New',command = newFile)
filemenu.add_command(label = 'Open',command = openFile)
filemenu.add_command(label = 'Save',command = saveFile)
filemenu.add_command(label = 'Save As',command = saveAs)
filemenu.add_separator()
filemenu.add_command(label = 'Quit',command = root.quit)
menubar.add_cascade(label = 'File', menu = filemenu)


root.config(menu = menubar)
root.mainloop()
