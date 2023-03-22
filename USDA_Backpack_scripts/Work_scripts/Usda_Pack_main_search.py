import os
import shutil


# define master file paths
file_path = "E:/Tools/USD/File_Sorce/3_layer_usd/layer_1_usda.usda"
new_file_path = "E:/Tools/USD/OUT_Test/usd_test2.usda"


# open new master file
destination_file = open(new_file_path, "w")


# define default file vars
file_dir = os.path.split(file_path)[0]
file_name = file_path.split("/")[-1]
file_drive = file_path.split("/")[-0]


# deine paths for the new files to go to 
sublayer_files = os.path.split(new_file_path)[0].replace('/','\\') + "\\usd_tex\\IO_files"
sublayer_usda_files = os.path.split(new_file_path)[0].replace('/','\\') + "\\usd_tex\\usda\\"

# dic off all files that need to be copied and the destination where ther have to go to 
IO_file_copy_dic = dict()

# list off all usda files that need checking
master_layer_usda_sorce = []
master_layer_usda_destination = []


#         /// FUNCTIONS ////  


def copy_files(files_to_copy,file_destination):
    
    
    if  os.path.exists(os.path.dirname(file_destination)):
        shutil.copy(files_to_copy, file_destination)
    else:
        os.makedirs(os.path.dirname(file_destination))
        shutil.copy(files_to_copy, file_destination)



# function to recursivle search true all usda files 
def recurve_usda_search(file):

    usd_files = []
    opend_file = open(file, "r")
    # go true all the lines  in the usda file
    for line in opend_file:
        # find all the usda files in the master file
        if "usda@" in line:
        
            os.chdir(os.path.dirname(os.path.abspath(file)))  

            
            # build full file path for the files to copy from the relative path       
            file_to_copy = os.path.abspath((line.strip().split("@"))[-2]).replace('/','\\') 
            # appen to the sorce and target list
            master_layer_usda_sorce.append(file_to_copy.replace('/','\\'))
            


            
            # array to all files in the found
            usd_files.append(file_to_copy)  
            
    # recursevly search true all found usda files
    for files in usd_files:
        recurve_usda_search(files)
    

# function to find all files in all usda files and write new usda files 
def search_true_usda_files(usda_files): 
    for file in usda_files:
        # function that creates the new usda file and its directory #TODO re build this block its guly af
        if  os.path.exists(os.path.dirname(os.path.abspath(sublayer_usda_files+file.split("\\")[-2]+"\\" +file.split("\\")[-1]))):
            try:
                new_file = open(os.path.abspath(sublayer_usda_files+file.split("\\")[-2]+"\\" +file.split("\\")[-1]),"x")
            except:
                os.remove(os.path.abspath(sublayer_usda_files+file.split("\\")[-2]+"\\" +file.split("\\")[-1]))
                new_file = open(os.path.abspath(sublayer_usda_files+file.split("\\")[-2]+"\\" +file.split("\\")[-1]),"x")                
        else:
            os.makedirs(os.path.dirname(os.path.abspath(sublayer_usda_files+file.split("\\")[-2]+"\\" +file.split("\\")[-1])))
            try:
                new_file = open(os.path.abspath(sublayer_usda_files+file.split("\\")[-2]+"\\" +file.split("\\")[-1]),"x")
            except:
                os.remove(os.path.abspath(sublayer_usda_files+file.split("\\")[-2]+"\\" +file.split("\\")[-1]))
                new_file = open(os.path.abspath(sublayer_usda_files+file.split("\\")[-2]+"\\" +file.split("\\")[-1]),"x") 


        opend_file_old = open(file, "r")

        new_file_path = os.path.abspath(sublayer_usda_files+file.split("\\")[-2]+"\\" +file.split("\\")[-1])
        new_file_write = open(new_file_path,"w")

        for line in opend_file_old:
            
            # find all lines that have a file in the line 
            if "file" in line:    
                
                # build abselut path                
                file_to_copy = (os.path.abspath((line.strip().split("@"))[-2]).replace('/','\\'))  
                # create destination dir out off target dir, last foulder in the original dir and the file name
                file_destination_dir = sublayer_files+"\\"+file_to_copy.split("\\")[-2] + "\\" + file_to_copy.split("\\")[-1]
                
                # addes the files sorce and the file destination to the IO file copy dic 
                IO_file_copy_dic[file_to_copy] = file_destination_dir

                
                # generate new line to replace old line in new file 
                new_rel_file_path = "@" + os.path.relpath(file_destination_dir, new_file_path) + "@"
                old_rel_path = "@" + (line.strip().split("@"))[-2] + "@"


                # write the new relative path in to the usda file 
                new_file_write.write(line.replace(old_rel_path, new_rel_file_path))     

            elif "usda@" in line:

                file_to_copy = (os.path.abspath((line.strip().split("@"))[-2]).replace('/','\\')) 
                new_rel_file_path = "@" + os.path.relpath(os.path.abspath(sublayer_usda_files+file_to_copy.split("\\")[-2]+"\\" +file_to_copy.split("\\")[-1]), new_file_path) + "@"


                old_rel_path = "@" + (line.strip().split("@"))[-2] + "@"

                #write the line
                new_file_write.write(line.replace(old_rel_path, new_rel_file_path))

            else:
                new_file_write.write(line)


# TODO gug mal nach ob das ganze hier auch das baut wass es soll  muss das ding überhaupt ? ich bin mir nicht sicher 
# Function that bilds the master usda file 
def write_new_master_usda_file(old_master_usda_file, new_master_usda_file):
    
    print(new_master_usda_file)
    old_file = open(old_master_usda_file)
    new_file_write = open(new_master_usda_file,"w")

    for line in old_file:
        # find all lines that have a file in the line 
        if "file" in line:    
            
            # build abselut path                
            file_to_copy = (os.path.abspath((line.strip().split("@"))[-2]).replace('/','\\'))  
            # create destination dir out off target dir, last foulder in the original dir and the file name
            file_destination_dir = sublayer_files+"\\"+file_to_copy.split("\\")[-2] + "\\" + file_to_copy.split("\\")[-1]
            
            # addes the files sorce and the file destination to the IO file copy dic 
            IO_file_copy_dic[file_to_copy] = file_destination_dir

            
            # generate new line to replace old line in new file 
            new_rel_file_path = "@" + os.path.relpath(file_destination_dir, new_file_path) + "@"
            old_rel_path = "@" + (line.strip().split("@"))[-2] + "@"


            # write the new relative path in to the usda file 
            new_file_write.write(line.replace(old_rel_path, new_rel_file_path))     

        elif "usda@" in line:

            file_to_copy = (os.path.abspath((line.strip().split("@"))[-2]).replace('/','\\')) 
            new_rel_file_path = "@" + os.path.relpath(os.path.abspath(sublayer_usda_files+file_to_copy.split("\\")[-2]+"\\" +file_to_copy.split("\\")[-1]), new_file_path) + "@"


            old_rel_path = "@" + (line.strip().split("@"))[-2] + "@"

            #write the line
            new_file_write.write(line.replace(old_rel_path, new_rel_file_path))

        else:
            new_file_write.write(line)


#      /// Calls ///

recurve_usda_search(file_path)
search_true_usda_files(master_layer_usda_sorce)

write_new_master_usda_file(file_path,new_file_path)

for sorce in IO_file_copy_dic:
    copy_files(sorce,IO_file_copy_dic[sorce])
    #print(sorce, "|", IO_file_copy_dic[sorce])
    

#      /// TEST PINTS ///


#TODO die walk true list sache muss mal ne function werden mein bester 
