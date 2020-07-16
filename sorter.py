import os
from pathlib import Path
from tkinter improt Tk, messagebox

main_dict = {
    'Executables': ('.exe',),
    'Documents'  : ('.pdf', '.txt', '.iso'),
    'Images'     : ('.png', '.jpeg', '.gif'),
    'Archives'   : ('.zip', '.rar', '.7z'),
    'Music'      : ('.mp3', '.wav'),
    'Videos'     : ('.mp4', '.AVI', '.mkv')
    }

root = Tk()
root.withdraw()
if not messagebox.askyesno("Ask", "Are you sure"): exit()

p = Path(os.getcwd())

for folder_name, file_formats in main_dict.items():
    
    if not os.path.exists(folder_name): os.mkdir(folder_name)

    for file_format in file_formats:
        for file in list(map(str, list(p.glob('*' + file_format)))):
            source = p / file
            destination = p / folder_name / file
            os.replace(str(source.cwd()), str(destination.cwd()))
            
messagebox.showinfo("Info", "Sorting is finished.")
