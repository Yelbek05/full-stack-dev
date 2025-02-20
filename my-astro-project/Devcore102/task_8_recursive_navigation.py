import os 
import glob

#specific directory 
directory = '/home/abstract/full-stack-dev/Devcore102'

#dir = os.getcwd() #path for the directories

def print_directory_structure(directory, is_root = True):
    #recurecively ouputing all the fules and folders through the given path 
    if is_root:
        print("Directories: ")
    for filename in glob.glob(os.path.join(directory, '**'), recursive=True):
        print(f"Globe: {filename}")
        
    #Cheching subdirectory is whether is encountered or not
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print(f"Subdirectory {item_path}")
            #recursively check subdirectories
            print("/Subdirectories")
            print_directory_structure(item_path, is_root=False)

def search_file(directory):
    print("Files: ")
    py_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root, file))
    return py_files

def calculate_total_size(directory):
    total_size = 0
    
#size of the files in specific directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
    return (total_size)

if os.path.exists(directory):
    print_directory_structure(directory)
    py_files = search_file(directory)
    for py_file in py_files:
        print(py_file)
    total_size = calculate_total_size(directory)

    print(f"Total size of files of .py files {total_size} bytes")
else:
    print(f"Directory {directory} does not exist")
