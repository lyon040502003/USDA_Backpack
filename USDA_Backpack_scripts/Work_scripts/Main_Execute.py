import Usd_Backpack_pxr_Search
import Usd_Backpack_py_search



# define master file paths
file_path = "E:/Tools/USDA_backpack/test_cases/usd_backpack_test_cases/Simple_tester/Sceene/main_sccene_render.usda"
new_file_path = "E:/Tools/USDA_backpack/test_cases/usd_backpack_test_cases/test_out/simple_test_exp_test.usda"






Usd_Backpack_py_search.Call_py_search(file_path,new_file_path,Rat_Convert=True,Hou_bin_foulder="C:/Program Files/Side Effects Software/Houdini 19.5.605/bins/")