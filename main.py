from features.usernameLookup import *
from features.ipLookup import *
from features.phoneLookup import *
from features.metadataExtractor import *

#Menu 1
def main():
    while True:
        os.system("cls")
        slow(banner)

        command = input(f"""{Fore.RED} ┌──({Fore.WHITE}{winUsername}{Fore.RED})─[{Fore.WHITE}~/{system}/{pcName}{Fore.RED}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")
                
        if command == "1" or command == "01":
            lookupUsername()
        elif command == "2" or command == "02":
            lookupIp()
        elif command == "3" or command == "03":
            lookupPhone()
        elif command == "4" or command == "04":
            extractMetadata()

main()