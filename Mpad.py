
from tkinter import *
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

root =Tk()
root.geometry('800x600+100+100')
root.title("Mpad Editor")
root.wm_iconbitmap('icons/icon.ico')
############################# MAIN MENU #################################

mainMenu = Menu() 

file = Menu(mainMenu, tearoff=False)
edit  = Menu(mainMenu, tearoff=False)
view  = Menu(mainMenu, tearoff=False)
theme = Menu(mainMenu, tearoff=False)

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

statusbar = Label(root, text="Status Bar",anchor='se',padx=20)
statusbar.pack(side=BOTTOM, fill=X)

textChanged = False
def changed(event):
    global textChanged
    if txtEditor.edit_modified():
        textChanged = True
        words = len(txtEditor.get(1.0, 'end-1c').split(" "))
        charachters = len(txtEditor.get(1.0,'end-1c'))
        statusbar.config(text=f"Chrachters: {charachters}   |   Words: {words}")
    txtEditor.edit_modified(False)
txtEditor.bind('<<Modified>>', changed)

txtEditor.configure(padx=5,pady=5)

############################# END OF STATUS NBAR ###########################


############################ MAIN MENU FUNCTIONALITY ################################# 

URL = ''
### NEW FILE FUNCTIONALITY 
def newFile(event):
    global URL
    URL = ''
    txtEditor.delete(1.0, END)

####  FILES COMMMANDS
file.add_command(label="New", compound=LEFT, accelerator="Ctrl+N", command=newFile)

 ## OPEN FILE FUNCTIONALITY
def openFile(event=None):
    global URL
    URL = filedialog.askopenfilename(initialdir=os.getcwd(), title='Open File', filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
    try:
        with open(URL, 'r') as fptr:
            txtEditor.delete(1.0, END)
            txtEditor.insert(1.0, fptr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    root.title(os.path.basename(URL)) 
file.add_command(label="Open", compound=LEFT, accelerator="Ctrl+O", command=openFile)

### SAVE FILE
def saveFile(event=None):
    global URL
    try:
        if URL:
            content = str(txtEditor.get(1.0, END))
            with open(URL,'w', encoding='utf-8') as fptr:
                fptr.write(content)
        else:
            URL = filedialog.asksaveasfile(mode='w',defaultextension='.txt', title='Open File', filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
            content2 = txtEditor.get(1.0, END)
            URL.write(content2)
            URL.close()
    except:
        return

file.add_command(label="Save", compound=LEFT, accelerator="Ctrl+S",command=saveFile)

### SAVE AS FUNCITNALITY
def saveAsFile(event=None):
    global URL
    try:
        content = txtEditor.get(1.0, END)
        URL = filedialog.asksaveasfile(mode='w',defaultextension='.txt', title='Open File', filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
        URL.write(content)
        URL.close()
    except:
        return
file.add_command(label="Save As", compound=LEFT, accelerator="Ctrl+Alt+S", command=saveAsFile)

### EXIT FUCNTINALITY
def exitFunc(event=None):
    global URL, textChanged
    print(textChanged)
    try:
        if textChanged:
            msgBox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if msgBox == True:
                if URL:
                    content = txtEditor.get(1.0, END)
                    with open(URL,'w',encoding='utf-8') as fptr:
                        fptr.writ(content)
                        root.destroy()
                else:
                    content2 = str(txtEditor.get(1.0, END))
                    URL = filedialog.asksaveasfile(mode='w',defaultextension='.txt', title='Open File', filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
                    URL.write(content2)
                    URL.close()
                    root.destroy()
            elif msgBox == False:
                root.destroy()
        else:
            root.destroy()
    except:
        return

file.add_command(label="Exit", compound=LEFT, accelerator="Ctrl+Q",command=exitFunc)

# EDIT COMMANDS
edit.add_command(label="Copy", compound=LEFT, accelerator="Ctrl+C",command=lambda:txtEditor.event_generate('<Control c>') )
edit.add_command(label="Cut", compound=LEFT, accelerator="Ctrl+X",command=lambda:txtEditor.event_generate('<Control x>') )
edit.add_command(label="Paste", compound=LEFT, accelerator="Ctrl+V",command=lambda:txtEditor.event_generate('<Control v>') )
edit.add_command(label="Clear All", compound=LEFT, accelerator="Ctrl+Alt+S",command=lambda:txtEditor.delete(1.0, END) )

### FIND FUNCTINALITY 
def findText(event=None):
    find_dialogue = Toplevel()
    find_dialogue.geometry('400x200')
    find_dialogue.title('Find & Replace')
    find_dialogue.resizable(0,0)

    def find():
        global txtEditor
        word = findInput.get()
        txtEditor.tag_remove('match','1.0', END)
        matches = 0
        if word:
            startPos = '1.0'
            while True:
                startPos = txtEditor.search(word, startPos, stopindex=END)
                # print(startPos)
                if not startPos:
                    break
                endPos =f"{startPos}+{len(word)}c"
                txtEditor.tag_add('match', startPos, endPos)
                matches+=1
                startPos =endPos
                txtEditor.tag_config('match',foreground='red',background='yellow')

    def replace():
        word = findInput.get()
        repText = replaceInput.get()
        content= txtEditor.get(1.0, END)
        newContent = content.replace(word, repText)
        txtEditor.delete(1.0,END)
        txtEditor.insert(1.0,newContent)


    #Find Frame
    findFrame = LabelFrame(find_dialogue, text='Find & Replace ')
    findFrame.pack(pady=20)

    #label
    findlbl = Label(findFrame, text='Find: ')
    replacelbl = Label(findFrame, text='Replace: ')

    #entry boxes
    findInput = Entry(findFrame, width=30)
    replaceInput = Entry(findFrame, width=30)

    #button
    findBtn = Button(findFrame, text='Find ', command=find)
    replaceBtn = Button(findFrame, text='Replace', command=replace)

    #packing
    findlbl.grid(row=0, column=0,padx=5,pady=5)
    replacelbl.grid(row=1, column=0,padx=5,pady=5)
    findInput.grid(row=0, column=1,padx=5,pady=5)
    replaceInput.grid(row=1, column=1,padx=5,pady=5)
    findBtn.grid(row=2,column=0, padx=8,pady=5)
    replaceBtn.grid(row=2,column=1, padx=8,pady=5)
    find_dialogue.mainloop()

edit.add_command(label="Find", compound=LEFT, accelerator="Ctrl+F",command=findText)


# VIEW COMMANDS
showToolbar = BooleanVar()
showToolbar.set(True)
showStatusbar = BooleanVar()
showStatusbar.set(True)

def hideTool():
    global showToolbar
    if showToolbar:
        toolbar.pack_forget()
        showToolbar=False
    else:
        txtEditor.pack_forget()
        statusbar.pack_forget()
        toolbar.pack(side=TOP, fill=X)
        txtEditor.pack(fill='both',expand=True)
        statusbar.pack(side=BOTTOM)
        showToolbar=True

def hideStatus():
    global showStatusbar
    if showStatusbar:
        statusbar.pack_forget()
        showStatusbar=False
    else:
        statusbar.pack(side=BOTTOM)
        showStatusbar=True
    
view.add_checkbutton(label="Tool bar" ,variable=showToolbar,onvalue=True, offvalue=False, command=hideTool)
view.add_checkbutton(label="Status bar",variable=showStatusbar,onvalue=True, offvalue=False,command=hideStatus)


themeChoice = StringVar()
color_dict = {
        'Light Default' : ('#000000','#ffffff'),
        'Light Plus' : ('#474747','#e0e0e0'),
        'Dark' : ('#c4c4c4','#2d2d2d','#ffffff'),
        'Red' : ('#2d2d2d','#ffe8e8'),
        'Monokai' : ('#d3b774','#474747'),
        'Purple' : ('#ffffff','#5f27cd','')
}
def changeTheme():
    choosenTheme = themeChoice.get()
    colorTuple = color_dict.get(choosenTheme)
    fgColor, bgColor = colorTuple[0],colorTuple[1]
    if choosenTheme == 'Dark' or choosenTheme == 'Purple':
        txtEditor.config(insertbackground='white')
    txtEditor.configure(background=bgColor, fg=fgColor)


# COLOR THEME
for i in color_dict:
    theme.add_radiobutton(label=i, variable=themeChoice,compound=LEFT,command=changeTheme)
    
### VIEW BUTTON
############################# END OF MAIN MENU FUNCTIONALITY ###########################

###Binding shortcut keys
root.bind('<Control-n>',newFile)
root.bind('<Control-o>',openFile)
root.bind('<Control-s>',saveFile)
root.bind('<Control-Alt-s>',saveAsFile)
root.bind('<Control-q>',exitFunc)
root.bind('<Control-f>',findText)

root.config(menu=mainMenu)
root.mainloop()