import shelve
import os
import shutil
import datetime

##Silinen dosyayı Bulur

path = "C:\\Users\\cs\\Desktop\\AtlamaBotu"
fileNames = os.listdir(path)


db = shelve.open('backup.db')
for key in db:  # Iterate to display database objects
    if fileNames.__contains__(db[key])  == False:
        print(db[key] + " adlı Dosya Ana Dosyadan Silinmiştir.")
        try :
            f = open("Changes.txt", "a+")
        except:
            f = open('Changes.txt', 'w+')


        f.write(str(datetime.datetime.now().time()))
        f.write(db[key] + " adli Dosya Ana Dosyadan Silinmistir. \n")
db.close()