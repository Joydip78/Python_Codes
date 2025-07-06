import os

folder_path = r"J:\All_Codes\New folder"  # e.g., 'C:/Users/You/Documents/rename'
# folder_path = "J:/All_Codes/New folder"   {optional usable}
# folder_path = "J:\\All_Codes\\New folder"   {optional usable}


prefix = "Set_"  # Change this to the desired prefix
i = 0
for folder_name in os.listdir(folder_path):
    old_path = os.path.join(folder_path, folder_name)
    x = len(folder_name)
    f = str(folder_name)
    if x == 8:
        new_foldername = prefix + "0" + f[6:]
    if x == 9:
        new_foldername = prefix + f[6:]
    if x > 9:
        if f[8] ==" ":
            new_foldername = prefix + "0" + f[6:]
        else:
            new_foldername = prefix + f[6:]
    print(new_foldername)

    # {for renaming file name we need to use this condition check also}
    # if os.path.isfile(old_path):
    #     new_filename = prefix + "0" + i

    new_path = os.path.join(folder_path, new_foldername)
    os.rename(old_path, new_path)
print("Renaming complete.")
