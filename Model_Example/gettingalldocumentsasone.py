import os
import shutil

News = []
News_divisions = os.listdir("Data")
News_divisions.remove("README.TXT")
print(News_divisions)
os.chdir("Data")
for dir in News_divisions:
    os.chdir(dir)
    files = os.listdir(".")
    for file in files:
        f = open(file, "r")
        if f.mode == "r":
            contents = f.read()
            News.append(contents)
        f.close()
    print(os.getcwd())
    os.chdir("../")
f = open("Combined.txt", "w+")
f.write(contents)
f.close()