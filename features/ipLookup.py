from config.settings import *
from config.banners import *

def lookupIp():
        os.system("cls")
        slow(mapBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketOpen}!{bracketClosed} {Fore.RED}IP lookup{Style.RESET_ALL}")
        print("")
        targetIp = input(f"{bracketOpen}>{bracketClosed} {Fore.RED}IP -> {Style.RESET_ALL}")

        try:
            request = requests.get(f"http://ip-api.com/json/{targetIp}")
            data = request.json()

            status = "Valid" if data.get('status') == "success" else "Invalid"
            country = data.get('country', "None")
            countryCode = data.get('countryCode', "None")
            region = data.get('regionName', "None")
            zipCode = data.get('zip', "None")
            city = data.get('city', "None")
            latitude = data.get('lat', "None")
            longitude = data.get('lon', "None")
            timezone = data.get('timezone', "None")
            isp = data.get('isp', "None")
            org = data.get('org', "None")
            asHost = data.get('as', "None")

            print(f"{bracketOpen}~{bracketClosed} {Fore.RED}Searching for information...{Style.RESET_ALL}")
            time.sleep(1)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Status       :{Style.RESET_ALL} {status}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Country      :{Style.RESET_ALL} {country}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Country code :{Style.RESET_ALL} {countryCode}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Region       :{Style.RESET_ALL} {region}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} City         :{Style.RESET_ALL} {city}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Zip code     :{Style.RESET_ALL} {zipCode}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Latitude     :{Style.RESET_ALL} {latitude}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Longitude    :{Style.RESET_ALL} {longitude}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Timezone     :{Style.RESET_ALL} {timezone}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Isp          :{Style.RESET_ALL} {isp}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Org          :{Style.RESET_ALL} {org}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} As host      :{Style.RESET_ALL} {asHost}")
            time.sleep(0.05)
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

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
            print(f"{bracketOpen}{Fore.WHITE}!{Style.RESET_ALL}{bracketClosed}{Fore.RED} Failed to lookup IP :{Style.RESET_ALL} {e}")
            time.sleep(2)
        