import os, shutil, sys
import ctypes
from colorama import init, Fore
from os import path

init(autoreset=True)

version="Auto Rp Install v0.3"

ctypes.windll.kernel32.SetConsoleTitleW(version)

def resource_path(relative_path):
    # Получаем абсолютный путь к ресурсам.
    try:
        # PyInstaller создает временную папку в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#path file

change_log=resource_path("ChangeLog.arp")


f_change = open(change_log, 'r+')
for i in (f_change):
    if i != "   ":
        if "+" in i:
            print(Fore.GREEN + i.replace('\n', ''))
        elif "-" in i:
            print(Fore.RED + i.replace('\n', ''))
        else:
            print(i.replace('\n', ''))

def get_rp_name(rp_path):
    while True:
        n=rp_path.find('\\')
        rp_path=rp_path[n+1:]
        if "\\" not in rp_path:
            break
    return rp_path

def zip_or_not(rp_name):
    if rp_name[-4:] == '.zip' or rp_name[-4:] == '.rar':
        return True
    else:
        return False
    
def print_installed(installed):
    if "1" in installed:
        print(Fore.GREEN+"Wild рп установлен!")
    if "2" in installed:
        print(Fore.GREEN+"Akrien Beta рп установлен!")
    if "3" in installed:
        print(Fore.GREEN+"Akrien Premium рп установлен!")
    if "4" in installed:
        print(Fore.GREEN+"Celestial рп установлен!")
    if "5" in installed:
        print(Fore.GREEN+"DeadCode рп установлен!")
    if "6" in installed:
        print(Fore.GREEN+"Nursultan NextGen рп установлен!")
    
print("\n"+"wild = 1 | akrien beta = 2 | akrien premium = 3 | celka = 4 | deadcode = 5 | nurik_next = 6")
choise=input("Выбери в какие читы устанавливаються рп(пример: 1245): ")
rp_path=input("\n"+"Путь до рп: ")


if path.exists(rp_path):
    rp_name=get_rp_name(rp_path)
    wild="C://.wildclient//client//resourcepacks//"
    akrien_beta="C://AkrienAntiLeak//beta//game//resourcepacks//"
    akrien_premium="C://AkrienAntiLeak//clients//AkrienPremium//game//resourcepacks//"
    celka='C://Celka//client//resourcepacks//'
    deadcode='C://DeadCode//resourcepacks//'
    nurik_next="C://NurikNext//client//resourcepacks//"

###Эту залупу бы по функциям раскидать, потом ебану крч, пускай пока так будет

### делаю вывод через отдельную переменную, а не сразу при установке, для того чито бы оно не засоряло консоль(что бы оно не пролетало во время установки, 
# а сразу устанавливало), 
# и было удобно смотреть где рп повторен, где установлен и т.д.
    installed=str
    if zip_or_not(rp_name) == False:
        if '1' in choise:
            if not path.exists(wild+rp_name):
                shutil.copytree(rp_path, wild+rp_name)
                installed+="1"
            else:
                print(Fore.YELLOW+"Wild уже есть этот рп")
        if '2' in choise:
            if not path.exists(akrien_beta+rp_name):
                shutil.copytree(rp_path, akrien_beta+rp_name)
                installed+="2"
            else:
                print(Fore.YELLOW+"Akrien Beta уже есть этот рп")
        if '3' in choise:
            if not path.exists(akrien_premium+rp_name):
                shutil.copytree(rp_path, akrien_premium+rp_name)
                installed+="3"
            else:
                print(Fore.YELLOW+"Akrien Premium уже есть этот рп")
        if '4' in choise:
            if not path.exists(celka+rp_name):
                shutil.copytree(rp_path, celka+rp_name)
                installed+="4"
            else:
                print(Fore.YELLOW+"Celestial уже есть этот рп")
        if '5' in choise:
            if not path.exists(deadcode+rp_name):    
                shutil.copytree(rp_path, deadcode+rp_name)
                installed+='5'
            else:
                print(Fore.YELLOW+"DeadCode уже есть этот рп")
        if '6' in choise:
            if not path.exists(nurik_next+rp_name):
                shutil.copytree(rp_path, nurik_next+rp_name)
                installed+='6'
            else:
                print(Fore.YELLOW+"Nurik NextGen уже есть этот рп")
    else:
        if '1' in choise:
            if not path.exists(wild+rp_name):
                shutil.copy2(rp_path, wild)
                installed+="1"
            else:
                print(Fore.YELLOW+"Wild уже есть этот рп")
        if '2' in choise:
            if not path.exists(akrien_beta+rp_name):
                shutil.copy2(rp_path, akrien_beta)
                installed+="2"
            else:
                print(Fore.YELLOW+"Akrien Beta уже есть этот рп")
        if '3' in choise:
            if not path.exists(akrien_premium+rp_name):
                shutil.copy2(rp_path, akrien_premium)
                installed+="3"
            else:
                print(Fore.YELLOW+"Akrien Premium уже есть этот рп")
        if '4' in choise:
            if not path.exists(celka+rp_name):
                shutil.copy2(rp_path, celka)
                installed+="4"
            else:
                print(Fore.YELLOW+"Celestial уже есть этот рп")
        if '5' in choise:
            if not path.exists(deadcode+rp_name):    
                shutil.copy2(rp_path, deadcode)
                installed+="5"
            else:
                print(Fore.YELLOW+"DeadCode уже есть этот рп")
        if '6' in choise:
            if not path.exists(nurik_next+rp_name):
                shutil.copy2(rp_path, nurik_next)
                installed+="6"
            else:
                print(Fore.YELLOW+"Nurik NextGen уже есть этот рп")



    ctypes.windll.kernel32.SetConsoleTitleW(f"Все рп установлены! | {version}")

    print(Fore.GREEN + "Готово")

    print_installed(installed)
else:
    print(Fore.RED + "Такого рп нет!")

input('Нажмите Enter для выхода\n')