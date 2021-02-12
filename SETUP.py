from cx_Freeze import setup, Executable

base = None    

executables = [Executable("SALT.py", base=base)]

packages = ["asyncio", "sys", "auraxium", "tkinter", "colorsys", "pyautogui"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "SALT Auto V6",
    options = options,
    version = "1.0",
    description = 'SALT Auto V6',
    executables = executables
)