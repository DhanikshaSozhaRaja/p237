import os
from os.path import exists

old = "E:\projects of WhiteHatJunior\module5\p237\code.txt"
new = "E:\projects of WhiteHatJunior\module5\p237\sample_code.txt"

file_exists = exists("E:\projects of WhiteHatJunior\module5\p237\sample_code.txt")

if(file_exists == True):
    print("File already exists")
else:
    os.rename(old, new)