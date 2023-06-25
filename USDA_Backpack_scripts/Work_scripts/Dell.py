


# for prim in stage.Traverse():
#     print(prim.GetPath())
#     print("info", stage.GetPrimAtPath(prim.GetPath()).GetTypeName()) 
#     if stage.GetPrimAtPath(prim.GetPath()).GetTypeName() == "DomeLight":
#         texture_input_file = stage.GetPrimAtPath(prim.GetPath()).GetAttribute('inputs:texture:file').Get()
#         if texture_input_file:
#             print()
#             print("testb",str(prim.GetPrimStack()[-1]).split(",")[-2].split("'")[-2])

#             print(prim.GetAttribute('inputs:texture:file').Get())
#             print("SDF_path", prim.GetPath())
#             print("Type", prim.GetAttribute('inputs:texture:file').GetTypeName()) 
#             print("In File", prim.GetAttribute('inputs:texture:file').Get())
#             prim.GetAttribute('inputs:texture:file').Set("dz")
#             print("In File", prim.GetAttribute('inputs:texture:file').Get())
#             print()
        


# for prim in stage.Traverse():
#     texture_input_file = stage.GetPrimAtPath(prim.GetPath()).GetAttribute('inputs:texture:file').Get()
#     if texture_input_file != None:
#         print(prim.GetPath())
#         print(texture_input_file)




usd_work_files = {
    "parent_usd_file": {
        "own_paths" : ["old_path","new_path"]
        "inner_usda_files": [["usd_file_path", "in_file_line", "new_file_paht"]]
        "inner_usd_files": [["usd_file_path", "in_file_line", "new_file_paht"]]
        "inner_IO_Files": [["IO_file_path", "in_file_line", "new_IOfile_paht"]]
    }
}


class usd_work_file():
    def __int__(self,own_paths:list,inner_usda_files:list,inner_usd_files:list,inner_IO_Files:list, usd_extendtion:str):
        self.own_paths = own_paths
        self.inner_usd_files = inner_usd_files
        self.inner_IO_Files = inner_IO_Files
        self.usd_extendtion = usd_extendtion



