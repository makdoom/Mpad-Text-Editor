
from tkinter import *
from tkinter import ttk
from tkinter import font, colorchooser

root =Tk()
root.geometry('800x600+100+100')
root.title("Mpad Editor")

############################# MAIN MENU #################################

mainMenu = Menu() 

file = Menu(mainMenu, tearoff=False)
edit  = Menu(mainMenu, tearoff=False)
view  = Menu(mainMenu, tearoff=False)
theme = Menu(mainMenu, tearoff=False)
themeChoice = StringVar()
color_dict = {
        'Light Default' : ('#000000','#ffffff'),
        'Light Plus' : ('#474747','#e0e0e0'),
        'Dark' : ('#c4c4c4','#2d2d2d'),
        'Red' : ('#2d2d2d','#ffe8e8'),
        'Monokai' : ('#d3b774','#474747'),
        'Night Blue' : ('#ededed','#6b9d2c')
}

# Cascade
mainMenu.add_cascade(label="File", font="lucida",menu=file)
mainMenu.add_cascade(label="Edit", font="lucida",menu=edit)
mainMenu.add_cascade(label="View", font="lucida",menu=view)
mainMenu.add_cascade(label="Themes", font="lucida",menu=theme)

############################# END OF MAIN MENU ###########################


#############################  TOOL BAR #################################

toolbar = Label(root)
toolbar.pack(side=TOP, fill=X)

###font Box
fontTuples = font.families()
font_family = StringVar()
fontBox = ttk.Combobox(toolbar, width=30, textvar= font_family, state='readonly')
fontBox['values'] = fontTuples
fontBox.current(fontTuples.index('Fira Code Medium'))
fontBox.grid(row=0,column=0,padx=5)

### Size Box
size = IntVar()
fontSize = ttk.Combobox(toolbar, width=14,textvar=size, state='readonly')
fontSize['values'] = tuple(range(8,80,2))
fontSize.current(2)
fontSize.grid(row=0, column=1, padx=5)

###Bold Button
boldIcon = PhotoImage(file='icons/bold.png')
boldBtn = Button(toolbar, image=boldIcon)
boldBtn.grid(row=0, column=2,padx=3)

italicIcon = PhotoImage(file='icons/italic.png')
italicBtn = Button(toolbar, image=italicIcon,height=22,width=22)
italicBtn.grid(row=0, column=3,padx=3)

underlineIcon = PhotoImage(file='icons/underline.png')
underlineBtn = Button(toolbar, image=underlineIcon,height=22,width=22)
underlineBtn.grid(row=0, column=4,padx=3)


###Font color button
fontColorIcon = PhotoImage(file='icons/fontColor.png')
fontColorBtn = Button(toolbar, image=fontColorIcon,height=23,width=23)
fontColorBtn.grid(row=0, column=5,padx=5)

### Aligne left 
alignLeftIcon = PhotoImage(file='icons/left.png')
alignLeftBtn = Button(toolbar, image=alignLeftIcon)
alignLeftBtn.grid(row=0, column=6,padx=3)

##align center
alignCenterIcon = PhotoImage(file='icons/center.png')
alignCenterBtn = Button(toolbar, image=alignCenterIcon,height=22,width=22)
alignCenterBtn.grid(row=0, column=7,padx=3)

###align right
alignRightIcon = PhotoImage(file='icons/right.png')
alignRightBtn = Button(toolbar, image=alignRightIcon,height=22,width=22)
alignRightBtn.grid(row=0, column=8,padx=3)


############################# END OF TOOL BAR  ###########################

############################# TEXT EDITOR #################################

txtEditor = Text(root)
txtEditor.config(wrap='word', relief=FLAT)
txtEditor.focus_set()

scroll_Bar =Scrollbar(root)
scroll_Bar.pack(side=RIGHT, fill=Y)
txtEditor.pack(fill='both', expand=TRUE)
scroll_Bar.config(command=txtEditor.yview)
txtEditor.config(yscrollcommand=scroll_Bar.set)

# Font Family and Font size FUNCTIONALITY
currentFontFamily = 'Fira Code Medium'
currentFontSize = 12

### to change the font 
def changeFont(root):
    global currentFontFamily
    currentFontFamily = font_family.get()
    txtEditor.configure(font=(currentFontFamily,currentFontSize))
fontBox.bind('<<ComboboxSelected>>', changeFont)

##to chnage the size
def changeSize(root):
    global currentFontSize
    currentFontSize = size.get()
    txtEditor.configure(font=(currentFontFamily, currentFontSize))
fontSize.bind('<<ComboboxSelected>>', changeSize)

# Bold Button FUNCTIONALITY
def toBold():
    txtProperties = font.Font(font=txtEditor['font'])
    if txtProperties.actual()['weight'] == 'normal':
        txtEditor.configure(font=(currentFontFamily, currentFontSize,'bold'))
    if txtProperties.actual()['weight'] == 'bold':
        txtEditor.configure(font=(currentFontFamily, currentFontSize,'normal'))
boldBtn.configure(command=toBold)

# Italic Button FUNCTIONALITY
def toItalic():
    txtProperties = font.Font(font=txtEditor['font'])
    if txtProperties.actual()['slant'] == 'roman':
        txtEditor.configure(font=(currentFontFamily, currentFontSize,'italic'))
    if txtProperties.actual()['slant'] == 'italic':
        txtEditor.configure(font=(currentFontFamily, currentFontSize,'roman'))
italicBtn.configure(command=toItalic)

# underline Button FUNCTIONALITY
def toUnderline():
    txtProperties = font.Font(font=txtEditor['font'])
    if txtProperties.actual()['underline'] == 0:
        txtEditor.configure(font=(currentFontFamily, currentFontSize,'underline'))
    if txtProperties.actual()['underline'] == 1:
        txtEditor.configure(font=(currentFontFamily, currentFontSize, 'normal'))
underlineBtn.configure(command=toUnderline)

## font color choooser
def colorChooser():
    color = colorchooser.askcolor()
    txtEditor.configure(fg=color[1])
fontColorBtn.configure(command=colorChooser) 
##############  ALIGN FUNCTIONALITY ################

###LEFT ALIGN
def leftAlign():
    content = txtEditor.get(1.0, 'end')
    txtEditor.tag_config('left',justify=LEFT)
    txtEditor.delete(1.0, END)
    txtEditor.insert(INSERT, content, 'left')
alignLeftBtn.configure(command=leftAlign)

###cemnter ALIGN
def centerAlign():
    content = txtEditor.get(1.0, 'end')
    txtEditor.tag_config('center',justify=CENTER)
    txtEditor.delete(1.0, END)
    txtEditor.insert(INSERT, content, 'center')
alignCenterBtn.configure(command=centerAlign)

###rIGHT ALIGN
def rightAlign():
    content = txtEditor.get(1.0, 'end')
    txtEditor.tag_config('right',justify=RIGHT)
    txtEditor.delete(1.0, END)
    txtEditor.insert(INSERT, content, 'right')
alignRightBtn.configure(command=rightAlign)

txtEditor.configure(font=("Fira Code Medium", 12))

############################# END OF TEXT EDITOR ###########################

############################# STATUS NBAR #################################

statusbar = Label(root, text="Status Bar")
statusbar.pack(side=BOTTOM, fill=X)

def changed(event):
    if txtEditor.edit_modified():
        textChnaged = True
        words = len(txtEditor.get(1.0, 'end-1c').split(" "))
        charachters = len(txtEditor.get(1.0,'end-1c'))
        statusbar.config(text=f"Chrachters: {charachters}   Words: {words}")
    txtEditor.edit_modified(False)
txtEditor.bind('<<Modified>>', changed)

txtEditor.configure(padx=5,pady=5)

############################# END OF STATUS NBAR ###########################


############################ MAIN MENU FUNCTIONALITY ################################# 


####  FILES COMMMANDS
file.add_command(label="New", compound=LEFT, accelerator="Ctrl+N")
file.add_command(label="Open", compound=LEFT, accelerator="Ctrl+O")
file.add_command(label="Save", compound=LEFT, accelerator="Ctrl+S")
file.add_command(label="Save As", compound=LEFT, accelerator="Ctrl+Shift+S")
file.add_command(label="Exit", compound=LEFT, accelerator="Ctrl+Q")

# EDIT COMMANDS
edit.add_command(label="Copy", compound=LEFT, accelerator="Ctrl+C" )
edit.add_command(label="Cut", compound=LEFT, accelerator="Ctrl+X")
edit.add_command(label="Paste", compound=LEFT, accelerator="Ctrl+V")
edit.add_command(label="Clear All", compound=LEFT, accelerator="Ctrl+Alt+S")
edit.add_command(label="Find", compound=LEFT, accelerator="Ctrl+F")

# VIEW COMMANDS
view.add_checkbutton(label="Title bar"  )
view.add_checkbutton(label="Status bar")

# COLOR THEME 
for i in color_dict:
    theme.add_checkbutton(label=i, variable=themeChoice,compound=LEFT)
############################# END OF MAIN MENU FUNCTIONALITY ###########################


root.config(menu=mainMenu)
root.mainloop()