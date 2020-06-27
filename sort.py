import os,shutil

folders={
    'videos':['.mp4'],
    'audios':['.mp3','.wav'],
    'images':['.jpg','.png','.jpeg'],
    'documents':['.doc','.xlsx','.xls','.pdf','.zip','.rar','.ppt','.txt'],
    'programming':['.c','.cpp','.py']
}

def rename_folder():
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory,folder))==True:
            os.rename(os.path.join(directory,folder),os.path.join(directory,folder.lower()))
def create_move(ext,filename):
    find=False
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory,folder_name))
            shutil.move(os.path.join(directory,filename),os.path.join(directory,folder_name))
            find=True
            break
    if find==False:
        if other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory,other_name))
        shutil.move(os.path.join(directory,filename),os.path.join(directory,other_name))            


directory=input("Enter the location: ")
all_files=os.listdir(directory)
other_name=input("Enter the location of other: ")
for i in all_files:
    if os.path.isfile(os.path.join(directory,i))==True:
        create_move(i.split(".")[-1],i)