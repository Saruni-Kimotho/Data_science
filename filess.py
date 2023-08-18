#go to desktop
#create a folder and call it "files"
#open notepad and type the following text
# 1. This is a simple text file
# 2. We will use it to learn about file 
# 3. handling in python
# save the file as "files.txt" inside the
#files folder on the desktop
# open your ide eg vs code and create a file
# named "files.py" and save it inside the files
# folder on the desktop
# type the followingcodes

#file context manager
with open('files1.txt', 'w')as file_handle:
    file_handle.write('this the new content ')
    
with open('files1.txt', 'r')as file_handle:
    content = file_handle.read()
    print(content)
    
    
