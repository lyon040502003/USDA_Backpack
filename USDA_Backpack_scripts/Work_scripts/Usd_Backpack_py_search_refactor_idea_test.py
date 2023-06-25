import os
import shutil
import re
import fnmatch
import fileinput
from pathlib import Path
import pprint



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
class usd_work_file(object):
    def __init__(self,own_paths:list=[],inner_usda_files:list="",inner_usd_files:list=[],inner_IO_Files:list=[], usd_extendtion:str="", all_inner_files:dict={}):
        self.own_path = own_paths
        self.all_inner_files = all_inner_files
        self.inner_usd_files = inner_usd_files
        self.inner_IO_Files = inner_IO_Files
        self.usd_extendtion = usd_extendtion

    def order_all_inner_file_list(self,conf_file:str=""):


        for item in self.all_inner_files:


            print(self.all_inner_files[item])



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
    usd_info_dicts = {}
    Export_dict = {}
    def _recurve_usda_search_inner_search(file,debug):
        usdas_found_in_this_file = []
        # print(file)
        usd_info_dicts[os.path.abspath(file)] ={}

        with open(file, "r") as current_file:
            os.chdir(os.path.dirname(os.path.abspath(file)))
            current_line_index = 1
            for line in current_file:
                if "@" in line:
                    if "." in os.path.abspath((line.strip().split("@"))[-2]).replace('/', '\\').split("\\")[-1]:
                        usd_info_dicts[os.path.abspath(file)][current_line_index] = os.path.abspath((line.strip().split("@"))[-2]).replace('/', '\\')
                        if "usda@" in line:
                            usdas_found_in_this_file.append(os.path.abspath((line.strip().split("@"))[-2]).replace('/', '\\'))
                current_line_index += 1
        for files in usdas_found_in_this_file:
            _recurve_usda_search_inner_search(files,debug)

    _recurve_usda_search_inner_search(file,debug)

    for usd in usd_info_dicts:
        Export_dict[usd]=usd_work_file()
        Export_dict[usd].own_path = usd
        Export_dict[usd].all_inner_files =  usd_info_dicts[usd]

    if debug:
        for usd in Export_dict:
            print("current Function recurve_usda_search:")
            print(Export_dict[usd].own_path)
            pprint.pprint((Export_dict[usd].all_inner_files))
            print("-"*80)
            print("\n")

    return Export_dict



class backpack_conf():
    def __init__(self, conf_file:str="conf_files/Usd_Backpack.env"):
        self.main_config = {}

        with open(conf_file,) as config:
            lines = config.read().rstrip().replace("\n","").split(":")[:-1]
            os.chdir(os.path.dirname(os.path.abspath(conf_file)))
            for val in lines:
                key, val = val.replace('"',"").split("=")
                val = val.strip()
                key = key.strip()
                print(os.path.abspath(val))

                # TODO read in the list files and then build up the dict
                self.main_config[key] = val
    def print_config(self):

        pprint.pprint(self.main_config)



# find all the files present in the master usd file and then ask the user if the non usda files shoud be converted

base_config = backpack_conf()

base_config.print_config()

found_usds = recurve_usda_search(
    "E:/Tools/USDA_backpack/test_cases/usd_backpack_test_cases/Simple_tester/Sceene/main_sccene_render2.usda",
    debug=False)


for usd in found_usds:
    found_usds[usd]

