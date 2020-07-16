import os
from pathlib import Path

main_dict = {
    'Executables': ('.exe',),
    'Documents'  : ('.pdf', '.txt', '.iso'),
    'Images'     : ('.png', '.jpeg', '.gif'),
    'Archives'   : ('.zip', '.rar', '.7z'),
    'Music'      : ('.mp3', '.wav'),
    'Videos'     : ('.mp4', '.AVI', '.mkv')
    }

def main():
    
    p = Path(os.getcwd())
    
    for folder_name, file_formats in main_dict.items():
        
        if not os.path.exists(folder_name): os.mkdir(folder_name)

        for file_format in file_formats:
            for file in list(map(str, list(p.glob('*' + file_format)))):
                source = p / file
                destination = p / folder_name / file
                os.replace(str(source.cwd()), str(destination.cwd()))

                
if __name__ == '__main__':
    print("Current location:", os.getcwd())
    main()
    input("Sorting is finished.")
