from colorama import Fore, Back, Style, init
import requests
import os
import sys
import platform
import time
from phonenumbers import geocoder, carrier, timezone
from phonenumbers import is_valid_number, is_possible_number, region_code_for_number, number_type
from phonenumbers import format_number, PhoneNumberFormat
import phonenumbers
import re
import PIL.Image
import PIL.ExifTags

init(convert=True)

bracketOpen = f"{Fore.RED}[{Style.RESET_ALL}"
bracketClosed = f"{Fore.RED}]{Style.RESET_ALL}"

bracketOpen2 = f"{Fore.WHITE}[{Style.RESET_ALL}"
bracketClosed2 = f"{Fore.WHITE}]{Style.RESET_ALL}"

pcName = platform.node()
winUsername = os.getlogin()

isWindows = os.name == "nt"
system = "Windows" if isWindows else "Linux"

succesStatus = [200, 201, 204, 304]

osintTitle = "O S I N T"

usernameLookup = f"{bracketOpen}01{bracketClosed} Username lookup"
ipLookup = f"{bracketOpen}02{bracketClosed} IP lookup"
phoneLookup = f"{bracketOpen}03{bracketClosed} Phone lookup"
metadataExtraction = f"{bracketOpen}04{bracketClosed} Metadata extractor"
exitTool = f"{bracketOpen}05{bracketClosed} Exit"

def cleanPath(inp: str) -> str:
    m = re.match(r'^\s*&?\s*["\']?(.*?)["\']?\s*$', inp)
    return m.group(1) if m else inp.strip().strip('"').strip("'")

def convertGps(coord, ref):
    try:
        degrees = float(coord[0])
        minutes = float(coord[1])
        seconds = float(coord[2])

        decimal = degrees + (minutes / 60) + (seconds / 3600)

        if ref in ["S", "W"]:
            decimal = -decimal

        return decimal
    except Exception:
        return None

def slow(banner):
    delai = 0.03
    lignes = banner.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)