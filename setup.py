import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Lucifer\AppData\Local\Programs\Python\Python37\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Lucifer\AppData\Local\Programs\Python\Python37\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="2.ico")]


cx_Freeze.setup(
    name = "COVID-19 Tracker",
    options = {"build_exe": {"packages":["tkinter","os","bs4","requests","plyer","threading"], "include_files":["2.ico",'tcl86t.dll','tk86t.dll']}},
    version = "0.01",
    description = "Tkinter,Web scraping Application",
    executables = executables,
    author = "Girish Kumar Goyal"
    )