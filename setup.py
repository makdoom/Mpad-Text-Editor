import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Python\Python37-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python\Python37-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("Mpad.py", base=base, icon="icons/icon.ico")]


cx_Freeze.setup(
    name = "Mpad Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icons/icon.ico",'tcl86t.dll','tk86t.dll', 'icons']}},
    version = "1.00",
    description = "Tkinter Application",
    executables = executables
    )