from config.settings import *

def lookupErome(username):
    url = f"https://www.erome.com/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def eromeResult(username):
    erome = lookupErome(username=username)

    if erome:
        eromeUrl = f"https://www.erome.com/{username}"
        eromeFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Erome.com    :{Style.RESET_ALL} {eromeUrl}"
    else:
        eromeFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Erome.com{Style.RESET_ALL}"

    return eromeFound