from config.settings import *
from config.banners import *

def extractMetadata():
        os.system("cls")
        slow(analyzeBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketOpen}!{bracketClosed} {Fore.RED}Metadata extractor{Style.RESET_ALL}")
        print("")
        rawPath = input(f"{bracketOpen}>{bracketClosed} {Fore.RED}Image -> {Style.RESET_ALL}")

        try:
            imagePath = cleanPath(rawPath)

            if not os.path.isfile(imagePath):
                print("")
                print(f"{bracketOpen}{Fore.WHITE}!{Style.RESET_ALL}{bracketClosed}{Fore.RED} Image not found :{Style.RESET_ALL} {image}")
                time.sleep(2)
                return

            image = PIL.Image.open(imagePath)
            rawExif = image._getexif()

            if not rawExif:
                print("")
                print(f"{bracketOpen}{Fore.WHITE}!{Style.RESET_ALL}{bracketClosed}{Fore.RED} No metadata found{Style.RESET_ALL}")
                time.sleep(2)
                return

            exifData = {}

            for k, v in image._getexif().items():
                tag = PIL.ExifTags.TAGS.get(k)
                if tag:
                    exifData[tag] = v

            make = exifData.get("Make", "None")
            model = exifData.get("Model", "None")
            software = exifData.get("Software", "None")
            date = exifData.get("DateTime", "None")
            originalDate = exifData.get("DateTimeOriginal", "None")
            gpsInfo = exifData.get("GPSInfo")

            if not gpsInfo:            
                lat = None
                long = None
            else:
                try:
                    lat = convertGps(gpsInfo[2], gpsInfo[1])
                    long = convertGps(gpsInfo[4], gpsInfo[3])
                except Exception:
                    lat = None
                    long = None

            print(f"{bracketOpen}~{bracketClosed} {Fore.RED}Searching for metadata... {Style.RESET_ALL}")
            time.sleep(1)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Make           :{Style.RESET_ALL} {make}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Model          :{Style.RESET_ALL} {model}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Software       :{Style.RESET_ALL} {software}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Recorded       :{Style.RESET_ALL} {originalDate}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Last modified  :{Style.RESET_ALL} {date}")
            time.sleep(0.05)
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Latitude       :{Style.RESET_ALL} {lat}")
            time.sleep(0.05) 
            print(f"{bracketOpen2}{Fore.RED}+{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Longitude      :{Style.RESET_ALL} {long}")
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

        except Exception:
            print("")
            print(f"{bracketOpen}{Fore.WHITE}!{Style.RESET_ALL}{bracketClosed}{Fore.RED} Metadata could not be extracted{Style.RESET_ALL}")
            time.sleep(2)
        