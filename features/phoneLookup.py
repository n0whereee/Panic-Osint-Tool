from config.settings import *
from config.banners import *

def lookupPhone():
        os.system("cls")
        slow(lookupBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketOpen}!{bracketClosed} {Fore.RED}Phone lookup{Style.RESET_ALL}")
        print("")
        phone = input(f"{bracketOpen}>{bracketClosed} {Fore.RED}Phone number (with country code) -> {Style.RESET_ALL}")

        try:
            phoneNumber = phonenumbers.parse(phone)

            phoneTypes = {
                0: "Fixed Line",
                1: "Mobile",
                2: "Fixed Line or Mobile",
                3: "Toll free",
                4: "Premium Rate",
                5: "Shared Cost",
                6: "VoIP",
                7: "Personal Number",
                8: "Pager",
                9: "Universal Access Number",
                10: "Voicemail",
            }

            phoneType = phoneTypes.get(number_type(phoneNumber), "Unknown")

            valid = is_valid_number(phoneNumber)
            international = format_number(phoneNumber, PhoneNumberFormat.INTERNATIONAL)
            national = format_number(phoneNumber, PhoneNumberFormat.NATIONAL)

            timeList = timezone.time_zones_for_number(phoneNumber)
            timeZone = timeList[0] if timeList else "Unknown"

            region = region_code_for_number(phoneNumber)
            location = geocoder.description_for_number(phoneNumber, 'en')
            provider = carrier.name_for_number(phoneNumber, 'en')

            print(f"{bracketOpen}~{bracketClosed} {Fore.RED}Searching for information... {Style.RESET_ALL}")
            time.sleep(1)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Valid                : {Style.RESET_ALL}{valid}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} International number : {Style.RESET_ALL}{international}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} National number      : {Style.RESET_ALL}{national}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Type                 : {Style.RESET_ALL}{phoneType}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Timezone             : {Style.RESET_ALL}{timeZone}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Country              : {Style.RESET_ALL}{location}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Region               : {Style.RESET_ALL}{region}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Provider             : {Style.RESET_ALL}{provider}")
            time.sleep(0.05)
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)

            print("")
            print(f"{bracketOpen}{Fore.WHITE}01{Style.RESET_ALL}{bracketClosed}{Fore.RED} Main Menu{Style.RESET_ALL}")
            print(f"{bracketOpen}{Fore.WHITE}02{Style.RESET_ALL}{bracketClosed}{Fore.RED} Exit{Style.RESET_ALL}")
            print("")

            Command = input(f"""{Fore.RED} ┌──({Fore.WHITE}{winUsername}{Fore.RED})─[{Fore.WHITE}~/{system}/{pcName}{Fore.RED}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")

            if Command == "1" or Command == "01":
                pass
            elif Command == "2" or Command == "02":
                sys.exit()
            else:
                pass

        except Exception as e:
            print("")
            print(f"{bracketOpen}{Fore.WHITE}!{Style.RESET_ALL}{bracketClosed}{Fore.RED} Failed to lookup phone :{Style.RESET_ALL} {e}")
            time.sleep(2)
        