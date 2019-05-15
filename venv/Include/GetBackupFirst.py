import shelve
import os


path = "C:\\Users\\cs\\Desktop\\AtlamaBotu"

f = shelve.open('backup.db')
fileNames = os.listdir(path)
counter = 0
for i in fileNames:
    f[str(counter)] = fileNames[counter]
    counter += 1
f.close()


db = shelve.open('backup.db')
for key in sorted(db):  # Iterate to display database objects
    print(key, '\t=>', db[key])
db.close()