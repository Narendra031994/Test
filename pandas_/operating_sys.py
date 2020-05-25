import os
print(os.environ.get('home'))

os.getcwd()
lis = os.listdir()
lis
for i in lis:
    path  = os.path.join(os.getcwd(),i)
    print(path)
    print(os.path.split(i))
    print(os.path.isfile(i))
    print("check if this is dir :",os.path.isdir(i))

os.chdir(r"C:\Users\Naren\Documents")
os.getcwd()

os.path.isdir(os.getcwd()) # should be true

os.mkdir('Naren_test')
os.listdir()
os.rmdir('Naren_test')
os.listdir()

file = open('Folder.jpg',mode = 'rb')
rd = file.read()
print(rd)
file.close()


# str functions

strr = "Narendra"
strr.upper()
strr.lower()
strr.isspace()
strr.isdigit()
strr.``