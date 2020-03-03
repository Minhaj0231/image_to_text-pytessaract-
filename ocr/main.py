import ocr

import os

allFiles = os.listdir("images")


for file in allFiles:

    print("start")
    print(ocr.imgToString(file))
    print("end")


# print(allFiles)



