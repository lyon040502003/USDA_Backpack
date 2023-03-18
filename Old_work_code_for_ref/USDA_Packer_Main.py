import os
import shutil


# define file paths

file_path = "E:/Tools/USD/File_Sorce/Master_usda.usda"
new_file_path = "E:/temp/dell/usd_test2.usda"

# define default file vars
file_dir = os.path.split(file_path)[0]
file_name = file_path.split("/")[-1]
file_drive = file_path.split("/")[-0]

# define list off found files in master layer
copy_master_dir = os.path.split(file_path)[0].replace('/','\\') + "\\usd_tex"
master_layer_IOfiles_sorce = []
master_layer_IOfiles_destination = []

master_layer_usda_sorce = []
master_layer_usda_destination = []



#open usd
file1 = open(file_path, "r")
file2 = open(new_file_path, "w")




def find_IO_files():
    
    for line in file1:
        if "file" in line:
            os.chdir(file_drive)
            file_to_copy = (os.path.abspath((line.strip().split("@"))[-2]))
            file_destination_dir = copy_master_dir + os.path.split(file_to_copy.split(":")[1])[0] + "\\" + os.path.split(file_to_copy.split(":")[1])[-1]  
            
            
            # out put found files   
            master_layer_IOfiles_sorce.append(file_to_copy)
            master_layer_IOfiles_destination.append(file_destination_dir)  

def find_usda_files():
    for line in file1:
        print(line)
        if "usda" in line:
            os.chdir(file_drive)
            file_to_copy = (os.path.abspath((line.strip().split("@"))[-2]))
            file_destination_dir = copy_master_dir + os.path.split(file_to_copy.split(":")[1])[0] + "\\" + os.path.split(file_to_copy.split(":")[1])[-1]  
            
            
            # out put found files   
            master_layer_usda_sorce.append(file_to_copy)
            master_layer_usda_destination.append(file_destination_dir)  
    print("")
    
 

    recursive_usd_search("E:/temp/dell/usd_test2.usda")
    
       
def create_new_rel_path():
   
    new_rel_file_path = "@." + "/usd_tex/" + file_to_copy.split("\\")[-1] + "@"
    old_line = "@" + (line.strip().split("@"))[-2] + "@"
    file2.write(line.replace(old_line, new_rel_file_path))   


def list_usda_files():
    print("")



def copy_files():
    
    if  os.path.exists(file_destination_dir):
        shutil.copy(file_to_copy, file_destination)
    else:
        os.mkdir(file_destination_dir)
        shutil.copy(file_to_copy, file_destination)
    print("file copyied  " + file_to_copy)
    
    
def write_new_usd():
    
    print("not yet build")  
    
def debug():
    print(master_layer_usda_sorce)
    #print(master_layer_usda_destination)
    
    #print(master_layer_IOfiles_sorce)
    #print(master_layer_IOfiles_destination)

find_usda_files()
#find_IO_files()
#debug()  