import os

location = os.getcwd()

print("Current location:", location)

main_dict = {
    'Executables': '.exe',
    'Documents'  : ('.pdf', '.txt', '.iso'),
    'Images'     : ('.png', '.jpeg', '.gif'),
    'Archives'   : ('.zip', '.rar', '.7z'),
    'Music'      : ('.mp3', '.wav'),
    'Videos'     : ('.mp4', '.AVI', '.mkv')
    }

def main():
    
    for folder_name in main_dict:
        
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        
        if type(main_dict[folder_name]) is tuple:
            for file_format in main_dict[folder_name]:
                for file_name in os.listdir():    
                    if file_name.endswith(file_format):
                        os.replace(os.getcwd() + '\\' + file_name,
                                   os.getcwd() + '\\' + folder_name
                                   + '\\' + file_name)

        else:
            file_format = main_dict[folder_name]
            for file_name in os.listdir():
                if file_name.endswith(file_format):
                    os.replace(os.getcwd() + '\\' + file_name,
                               os.getcwd() + '\\' + folder_name
                               + '\\' + file_name)

if __name__ == '__main__':
    main()
    input("Sorting is finished.")
