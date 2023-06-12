


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