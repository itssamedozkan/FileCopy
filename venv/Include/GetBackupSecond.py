import shelve
import os
import shutil
import datetime
path = "C:\\Users\\cs\\Desktop\\AtlamaBotu"
copypath = 'C:\\Users\cs\\Desktop\\Engine_exhaust'

fileNames = os.listdir(path)

#Ekleme Olması durumu
for files in fileNames:
    f = shelve.open('backup.db')
    islem = False
    for key in f:  # Iterate to display database objects
        if f[key] == files:
            islem = True
            break
    if islem == False:
        print(files)

        try:
            c = open("Changes.txt", "a+")
        except:
           c = open('Changes.txt', 'w+')

        c.write(str(datetime.datetime.now().time()) + " ")
        c.write(f[key] + " adli Dosya Ana Dosyaya Eklenmistir. \n")

        newPath = shutil.copy(path+"\\"+files, copypath)
    f.close()


