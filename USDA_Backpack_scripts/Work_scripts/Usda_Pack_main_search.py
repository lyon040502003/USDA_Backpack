import os
import shutil
import re
import fnmatch
import pprint
import fileinput


# define master file paths
file_path = "E:/Tools/USD/File_Sorce_2/master_usda.usda"
new_file_path = "E:/Tools/USD/OUT_Test/usd_test2.usda"


# open new master file




# define default file vars
file_dir = os.path.split(file_path)[0]
file_name = file_path.split("/")[-1]
file_drive = file_path.split("/")[-0]


# deine paths for the new files to go to 
sublayer_files = os.path.split(new_file_path)[0].replace('/','\\') + "\\usd_tex\\IO_files"
sublayer_usda_files = os.path.split(new_file_path)[0].replace('/','\\') + "\\usd_tex\\usda\\"

# dic off all files that need to be copied and the destination where ther have to go to 
IO_file_sorce_dic = dict()
IO_file_copy_dic = dict()

# list off all usda files that need checking
master_layer_usda_sorce = []
master_layer_usda_destination = []

all_written_usda_files = []

texture_file_types = [line.rstrip() for line in open('USDA_Backpack_scripts/Work_scripts/conf_files/Image_file_types.txt')]
usd_file_types = [line.rstrip() for line in open('USDA_Backpack_scripts/Work_scripts/conf_files/usd_file_formats.txt')]
usd_file_types.remove(".usda")
Geo_file_types = [line.rstrip() for line in open('USDA_Backpack_scripts/Work_scripts/conf_files/Image_file_types.txt')]


Hou_dir = "C:/Program Files/Side Effects Software/Houdini 19.5.435/bin/"
iconver_exe = "iconvert.exe"





#         /// FUNCTIONS ////  

def refactor_copy_dic(copy_dic):
    udim_work_dic = dict()
    udim_files = []
    udim_files_destination = []
    for sorce in copy_dic:
        
        
        if "<UDIM>" in sorce:
            udim_files.append(sorce)  
            udim_files_destination.append(copy_dic[sorce])
            udim_work_dic[sorce]=copy_dic[sorce]            
            
    for files in udim_work_dic:
        filenames = fnmatch.filter(os.listdir(os.path.dirname(files)), '*')
        target_file_dir = os.path.dirname(udim_work_dic[files])
        file_front = files.split("\\")[-1].replace("<UDIM>", "/").split("/")[0]
        file_back = files.split("\\")[-1].replace("<UDIM>", "/").split("/")[1]
        for tex in filenames:
            if re.search(f'{file_front}1[0-9][0-9][0-9]{file_back}', tex):
                IO_file_copy_dic[os.path.join(os.path.dirname(files),tex)] = os.path.join(target_file_dir,tex)








class file_manager():
        
    def copy_files(IO_dic):
        
        for sorce in IO_dic:
            if  os.path.exists(os.path.dirname(IO_dic[sorce])):
                shutil.copy(sorce, IO_dic[sorce])
            else:
                os.makedirs(os.path.dirname(IO_dic[sorce]))
                shutil.copy(sorce, IO_dic[sorce])
            print(" file copyied ", sorce, "  //  ", IO_dic[sorce])
    
    def convert_to_rat(IO_dic,usd_dic):
        for sorce_file in IO_dic: 
            print("test:",sorce_file)
            in_file = IO_dic[sorce_file]
            cmd_iconvert_command = "-g auto  " + in_file +"  " + in_file.replace(in_file.split("/")[-1].split(".")[-1],'rat')
            cmd_command = '"'+Hou_dir+iconver_exe+'" '+ cmd_iconvert_command  #TODO this needs to be multi thread
            os.system(cmd_command)
            os.remove(in_file)
        
        for file in usd_dic:
            with fileinput.input(inplace=True,files=(file)) as f:
                for line in f:
                    if any(ext in line for ext in texture_file_types) and "file" in line: 
                        print(line.replace(line.split("@")[-2].split(".")[-1], "rat"))
                    else:
                        print(line)
                






class line_runner():
    
    def build_file_pathing(line):
                
        file_to_copy = (os.path.abspath((line.strip().split("@"))[-2]).replace('/','\\'))  
        file_destination_dir = sublayer_files+"\\"+file_to_copy.split("\\")[-2] + "\\" + file_to_copy.split("\\")[-1]
        
        new_rel_file_path = "@" + os.path.relpath(file_destination_dir, new_file_path)[1:] + "@"
        old_rel_path = "@" + (line.strip().split("@"))[-2] + "@"
        
        return new_rel_file_path, old_rel_path, file_destination_dir, file_to_copy


    def run_true_line(file_to_run_true, new_file_write, function_set):
        
        """This function Truns True a file in and writes the output in to the coresponding list

        Args:
            file_to_run_true (String): this is the file that you want to be searched true
            new_file_write (String): this is the new file you are trying to write out 
            function_set (int): this is a varible that selects the functions to runn (1: all texture files types, 2: all usd files (exept usda), 3:usda files, 9:all)
        """    
        


        for line in file_to_run_true:
            

            if any(ext in line for ext in texture_file_types) and "file" in line: 
                
                result = line_runner.build_file_pathing(line)
                
                IO_file_sorce_dic[result[3]] = result[2]
                new_file_write.write(line.replace(result[1], result[0]))    

                
            elif any(ext in line for ext in usd_file_types) and not "@usda": # this function exists because it will be important to report all non usda usd files in order to show the files that might not be resolved in the ui 
                result = line_runner.build_file_pathing(line)
                IO_file_sorce_dic[result[3]] = result[2]
                new_file_write.write(line.replace(result[1], result[0])) 


            elif "usda@" in line:


                file_to_copy = (os.path.abspath((line.strip().split("@"))[-2]).replace('/','\\')) 
                new_rel_file_path = "@" + os.path.relpath(os.path.abspath(sublayer_usda_files+file_to_copy.split("\\")[-2]+"\\" +file_to_copy.split("\\")[-1]), new_file_path)[1:] + "@"
                old_rel_path = "@" + (line.strip().split("@"))[-2] + "@"

                new_file_write.write(line.replace(old_rel_path, new_rel_file_path))

            else:
                new_file_write.write(line)



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
    opend_file.close()

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
        all_written_usda_files.append(new_file_path)

        line_runner.run_true_line(opend_file_old,new_file_write, 5)
        new_file.close()


# Function that bilds the master usda file 
def write_new_master_usda_file(old_master_usda_file, new_master_usda_file):
    
    old_file = open(old_master_usda_file)
    new_file_write = open(new_master_usda_file,"w")
    all_written_usda_files.append(new_master_usda_file)
    line_runner.run_true_line(old_file,new_file_write, 5)
    old_file.close()
    new_file_write.close()



        

    

#      /// Calls ///


def calls():
    
    recurve_usda_search(file_path)
    search_true_usda_files(master_layer_usda_sorce)

    write_new_master_usda_file(file_path,new_file_path)
    refactor_copy_dic(IO_file_sorce_dic)
    
    
    file_manager.copy_files(IO_file_copy_dic)
    file_manager.convert_to_rat(IO_file_copy_dic,all_written_usda_files)
    
    

calls()

#      /// TEST PINTS ///

