import re
import os
import pathlib

dir_path = r"C:/TEST/"
os.chdir(dir_path)
for folder_name in os.listdir(dir_path) :
    if not os.path.isdir(os.path.join(dir_path, folder_name)):
        continue
    new_name = re.sub(" ?\[(\d{6}|DL.|別.*?)\]", "", folder_name, flags=re.IGNORECASE)
    #Prevent duplicated name when there are more than two version exist.
    info = folder_name.replace(new_name, "")
    info = re.sub("\[\d{6}\]$", "", info)
    new_name = re.sub("^((?P<session_1>\(C\d{1,3}\))? ?(\[(?P<author>.*?)\])? ?(?P<name>[^\[\(]*)) ?(\[DL.\])? ?(?P<session_2>\(C\d{1,3}\))?",
                      "\g<author>---ForSplit---\g<session_1>\g<session_2>    \g<name>",
                      new_name, 
                      flags=re.IGNORECASE)
    new_name = new_name.strip()

    if re.search("---ForSplit---", new_name): 
        author, new_name = new_name.split("---ForSplit---", 1)
        if author == "":
            continue
        new_name = new_name.strip()
            
        pathlib.Path(author).mkdir(parents=True, exist_ok=True) 
        
        parent_folder = os.path.join(dir_path, author)
        new_name = os.path.join(parent_folder, new_name)
        if os.path.isdir(new_name) :
            new_name += info
        os.rename(folder_name, new_name)
os.system(r"del /s g*.txt")