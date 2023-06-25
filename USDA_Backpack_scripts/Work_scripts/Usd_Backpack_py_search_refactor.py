import os
import shutil
import re
import fnmatch
import fileinput
from pathlib import Path
import pprint

# define master file paths
file_path = ""
new_file_path = ""




# define default file vars
file_dir = ""
file_name = ""
file_drive = ""


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

# Open Shoud be and With open
texture_file_types = [line.rstrip() for line in open('conf_files/Image_file_types.txt')]
usd_file_types = [line.rstrip() for line in open('conf_files/usd_file_formats.txt')]
usd_file_types.remove(".usda")
Geo_file_types = [line.rstrip() for line in open('conf_files/Image_file_types.txt')]


Hou_dir = ""
iconver_exe = "iconvert.exe"


def debug_printer(*args, is_on:bool=False, debugt_funct:str="No funtion Decleard", print_at_start:str=None, print_at_end:str=None): # will get more functions in the future // file exists , parent foulder, referneces found in files etc
    def print_str_int_type(string):
        print(string)
    def print_list_array_dict_type(print_thing):
        pprint.pprint(print_thing)

    type_execute = {
        "<class 'str'>":print_str_int_type,
        "<class 'int'>":print_str_int_type,
        "<class 'list'>": print_list_array_dict_type,
        "<class 'dict'>": print_list_array_dict_type,
    }

    if is_on:
        print("Current Function: ",debugt_funct)
        if print_at_start != None:
            print(print_at_start)
        for things in args:
            type_execute[str(type(things))](things)
        if print_at_end != None:
            print(print_at_end)
        print("-"*80)


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
        else:
            IO_file_copy_dic[sorce]=copy_dic[sorce]  
    for files in udim_work_dic:
        print("files in the work dic", files)
        print(os.listdir(os.path.dirname(os.path.abspath(files))))
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
            print("file to copy  ",IO_dic[sorce])
            if  os.path.exists(IO_dic[sorce]): 
                os.remove(IO_dic[sorce])
                print("file existed, remove file ",IO_dic[sorce])
                shutil.copy(sorce, IO_dic[sorce])
            else:
                Path(os.path.abspath(os.path.dirname(IO_dic[sorce]))).mkdir(parents=True, exist_ok=True)
                print("dir_created", os.path.abspath(os.path.dirname(IO_dic[sorce])))
                shutil.copy(sorce, IO_dic[sorce])
            print(" file copyied f/t", sorce, "  //  ", IO_dic[sorce],".\n")


    def convert_to_rat(IO_dic,usd_dic):
        for sorce_file in IO_dic: 
            in_file = os.path.abspath(IO_dic[sorce_file])
            if in_file.endswith(".hdr"):
                print("hdr_files_will_not_be_converted", in_file)
            else:
                print("rat conf files:",in_file)
                cmd_iconvert_command = "-g off  -d float  " + in_file +"  " + in_file.replace(in_file.split("/")[-1].split(".")[-1],'rat')
                cmd_command = '"'+Hou_dir+iconver_exe+'" '+ cmd_iconvert_command  #TODO this needs to be multi thread
                os.system(cmd_command)
                os.remove(in_file)
            
        for file in usd_dic:
            work_file = os.path.abspath(file)
            print("recursive files ", work_file)
            with fileinput.input(inplace=True,files=(work_file)) as f:
                for line in f:
                    if any(ext in line for ext in texture_file_types) and ":file" in line and not line.split("@")[-2].endswith(".hdr"):      
                        print(line.replace(line.split("@")[-2].split(".")[-1], "rat"))

                    else:
                        print(line)

class line_runner():
    #TODO needs to be rewritten to take all trypes of files 
    def build_file_pathing(line,curent_file): # TODO this function needs to be rewritten to take in the curent work file 
        print("line_runner_build_file_pathing_args", line, curent_file)
        
        old_rel_path = "@" + (line.strip().split("@"))[-2] + "@"
        
        
        sorce_rel_file = line.split("@")[-2]
        sorce_abs_file = os.path.abspath(curent_file.replace(curent_file.split("\\")[-1],sorce_rel_file))
        
        new_work_file_path = os.path.abspath(sublayer_usda_files+"\\"+curent_file.split("\\")[-2] + "\\" + curent_file.split("\\")[-1])
        
        new_abs_file_path = os.path.abspath(sublayer_files+"\\"+sorce_abs_file.split("\\")[-2] + "\\" + sorce_abs_file.split("\\")[-1])
        new_rel_file_path2 = os.path.relpath(new_abs_file_path, new_work_file_path).replace("\\","/")[1:]
        new_rel_path_line = "@" + new_rel_file_path2 + "@"
        print("paths",new_rel_path_line)
        
        print("")
        return new_rel_path_line, old_rel_path, new_abs_file_path, sorce_abs_file


    def run_true_line(file_to_run_true, new_file_write, function_set):
        
        """This function Truns True a file in and writes the output in to the coresponding list

        Args:
            file_to_run_true (String): this is the file that you want to be searched true
            new_file_write (String): this is the new file you are trying to write out 
            function_set (int): this is a varible that selects the functions to runn (1: all texture files types, 2: all usd files (exept usda), 3:usda files, 9:all)
        """    
        print("")
        print("line_runner file to run true   ",file_to_run_true)


        for line in file_to_run_true:
            
            if any(ext in line for ext in texture_file_types) and ":file" in line: 
                print("line_runner_run_true_line ", file_to_run_true.name)
                print(texture_file_types)
                print("tex file found ", line)
                result = line_runner.build_file_pathing(line,file_to_run_true.name)
                
                IO_file_sorce_dic[result[3]] = result[2]
                new_file_write.write(line.replace(result[1], result[0]))    

                
            elif any(ext in line for ext in usd_file_types) and not "@usda": # this function exists because it will be important to report all non usda usd files in order to show the files that might not be resolved in the ui 

                result = line_runner.build_file_pathing(line)
                IO_file_sorce_dic[result[3]] = result[2]
                new_file_write.write(line.replace(result[1], result[0])) 


            elif "usda@" in line:
                
                print("line runner usda found  ")
                print("line runner curent work file ", file_to_run_true.name)
                print("line runner file taht gets created ", new_file_write.name)
                file_to_copy = os.path.abspath(file_to_run_true.name.replace(os.path.abspath(file_to_run_true.name).split("\\")[-1], line.split("@")[-2]))
                print("original abs path test" ,file_to_copy)
                new_abs_path = os.path.abspath(sublayer_usda_files+"\\"+file_to_copy.split("\\")[-2] + "\\" + file_to_copy.split("\\")[-1])
                print("new abs path for copy",new_abs_path)
                print("work line  ", line)
                new_rel_path = os.path.relpath(new_abs_path, new_file_write.name)[1:]
                print("new_rel_path ", new_rel_path)
                new_line = line.replace(line.split("@")[-2],new_rel_path.replace("\\","/"))
                print("new line", new_line)
                new_file_write.write(new_line)
                

            else:
                new_file_write.write(line)

# function to recursivle search true all usda files TODO add function for handling usd files ( usd cat )
# Rebuild V1
def recurve_usda_search(file, debug:bool=False):
    all_found_files = []
    def _recurve_usda_search_inner_search(file,debug):
        usdas_found_in_this_file = []
        with open(file, "r") as current_file:
            # go true all the lines  in the usda file
            for line in current_file:
                # find all the usda files in the master file
                if "usda@" in line:
                    os.chdir(os.path.dirname(os.path.abspath(file)))
                    # build full file path for the files to copy from the relative path
                    # file_to_copy = os.path.abspath((line.strip().split("@"))[-2]).replace('/','\\') # this function sperates the usda path out off the line
                    # appendie_dict.append(os.path.abspath((line.strip().split("@"))[-2]).replace('/','\\')) # this function sperates the usda path out off the line
                    usdas_found_in_this_file.append(os.path.abspath((line.strip().split("@"))[-2]).replace('/', '\\')) # this function sperates the usda path out off the line
                    all_found_files.append(os.path.abspath((line.strip().split("@"))[-2]).replace('/', '\\'))
        debug_printer(file,usdas_found_in_this_file, is_on=debug,debugt_funct="_recurve_usda_search_inner_search", print_at_start= "recrusive search found  : ")
        # recursevly search true all found usda files
        for files in usdas_found_in_this_file:
            _recurve_usda_search_inner_search(files,debug)
    _recurve_usda_search_inner_search(file,debug)
    return all_found_files# TODO make shure function returns all files





# function to find all files in all usda files and write new usda files 
def search_true_usda_files(usda_files): 
    for file in usda_files:
        print("text", file)
        new_file_pos = os.path.abspath(sublayer_usda_files+file.split("\\")[-2]+"\\" +file.split("\\")[-1])
        new_usda_file_dir = os.path.dirname(new_file_pos)
        if  os.path.exists(new_file_pos): 
            print("exists")
            os.remove(new_file_pos)
            print("file existed and was replaced : ",new_file_pos)
            new_file_write = open(os.path.abspath(new_file_pos),"w")
        else:
            Path(new_usda_file_dir).mkdir(parents=True, exist_ok=True)
            new_file_write = open(os.path.abspath(new_file_pos),"w")
            print("dir was missing and file was created :",new_file_pos)
        print("created usda file : ",new_file_pos)


        opend_file_old = open(file, "r")

        new_file_path = os.path.abspath(sublayer_usda_files+file.split("\\")[-2]+"\\" +file.split("\\")[-1])
        #new_file_write = open(new_file_path,"w")
        all_written_usda_files.append(new_file_path)

        line_runner.run_true_line(opend_file_old,new_file_write, 5)
        print("search_true_usda_files work file   ",opend_file_old)
        new_file_write.close()


# function to find all files present in a usda file



# Function that bilds the master usda file 
def write_new_master_usda_file(old_master_usda_file, new_master_usda_file):
    
    old_file = open(old_master_usda_file)
    new_file_write = open(new_master_usda_file,"w")
    all_written_usda_files.append(new_master_usda_file)
    line_runner.run_true_line(old_file,new_file_write, 5)
    old_file.close()
    new_file_write.close()


# def Call_py_search(sorce_path,Destination_path,Hou_bin_foulder: str= "C:/Program Files/Side Effects Software/Houdini 19.5.605/bin/",Rat_Convert: bool=True):
#
#     global file_path
#     global new_file_path
#     global file_dir
#     global file_name
#     global file_drive
#     global sublayer_files
#     global sublayer_usda_files
#     global Hou_dir
#
#     if os.path.exists(Hou_bin_foulder):
#         Hou_dir = Hou_bin_foulder
#     else:
#         Hou_dir = "C:/Program Files/Side Effects Software/Houdini 19.5.605/bin/"
#
#     sublayer_files = os.path.split(Destination_path)[0].replace('/','\\') + "\\usd_tex\\IO_files"
#     sublayer_usda_files = os.path.split(Destination_path)[0].replace('/','\\') + "\\usd_tex\\usda\\"
#     file_path = sorce_path
#     new_file_path = Destination_path
#     file_dir = os.path.split(sorce_path)[0]
#     file_name = sorce_path.split("/")[-1]
#     file_drive = sorce_path.split("/")[-0]
#
#     recurve_usda_search(sorce_path)
#     search_true_usda_files(master_layer_usda_sorce)
#
#     write_new_master_usda_file(sorce_path,Destination_path)
#
#     refactor_copy_dic(IO_file_sorce_dic)
#     file_manager.copy_files(IO_file_copy_dic)
#     if Rat_Convert:
#         file_manager.convert_to_rat(IO_file_copy_dic,all_written_usda_files)
#

def Call_py_search(sorce_path,Destination_path,Hou_bin_foulder: str= "C:/Program Files/Side Effects Software/Houdini 19.5.605/bin/",Rat_Convert: bool=True):

    global file_path
    global new_file_path
    global file_dir
    global file_name
    global file_drive
    global sublayer_files
    global sublayer_usda_files
    global Hou_dir

    if os.path.exists(Hou_bin_foulder):
        Hou_dir = Hou_bin_foulder
    else:
        Hou_dir = "C:/Program Files/Side Effects Software/Houdini 19.5.605/bin/"

    sublayer_files = os.path.split(Destination_path)[0].replace('/','\\') + "\\usd_tex\\IO_files"
    sublayer_usda_files = os.path.split(Destination_path)[0].replace('/','\\') + "\\usd_tex\\usda\\"
    file_path = sorce_path
    new_file_path = Destination_path
    file_dir = os.path.split(sorce_path)[0]
    file_name = sorce_path.split("/")[-1]
    file_drive = sorce_path.split("/")[-0]

    recurve_usda_search(sorce_path)
    search_true_usda_files(master_layer_usda_sorce)

    write_new_master_usda_file(sorce_path,Destination_path)

    refactor_copy_dic(IO_file_sorce_dic)
    file_manager.copy_files(IO_file_copy_dic)
    if Rat_Convert:
        file_manager.convert_to_rat(IO_file_copy_dic,all_written_usda_files)


# find all the files present in the master usd file and then ask the user if the non usda files shoud be converted
found_usds = recurve_usda_search("E:/Tools/USDA_backpack/test_cases/usd_backpack_test_cases/Simple_tester/Sceene/main_sccene_render2.usda",debug=True)

# convert usd files to usda and search true them then append to found_usdas list

# find all non usd files present in the found usda files
# nextb = search_true_usda_files(found_usds)
# print(nextb)
# pprint.pprint(found_usds)


