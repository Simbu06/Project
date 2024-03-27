import os
import shutil

path=input("Enter the Path :")
files=os.listdir(path)

if "Videos" not in files:
    os.makedirs(path+"/Videos")
if "Audio" not in files:
    os.makedirs(path+"/Audio")
if "Images" not in files:
    os.makedirs(path+"/Images")
if "Documents" not in files:
    os.makedirs(path+"/Documents")
if "Programs" not in files:
    os.makedirs(path+"/Programs")
if "Software" not in files:
    os.makedirs(path+"/Software")
    
for file in files:
    if '.mp4' in file or '.mov' in file or '.mkv' in file or '.webm' in file:
        shutil.move(path+"/"+file,path+"/Videos")
    elif '.mp3' in file or '.aac' in file or '.m4a' in file:
        shutil.move(path+"/"+file,path+"/Audio")
    elif '.png' in file or '.jpeg' in file or '.jpg' in file:
        shutil.move(path+"/"+file,path+"/Images")
    elif '.pdf' in file or '.docx' in file or '.pptx' in file or '.doc' in file:
        shutil.move(path+"/"+file,path+"/Documents")
    elif '.py' in file or '.c' in file or '.cpp' in file or '.java' in file:
        shutil.move(path+"/"+file,path+"/Programs")
    elif '.exe' in file:
        shutil.move(path+"/"+file,path+"/Software")