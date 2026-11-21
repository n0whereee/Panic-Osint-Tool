from config.settings import *

def lookupX(username):
    url = f"https://x.com/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def xResult(username):
    x = lookupX(username=username)

    if x:
        xUrl = f"https://x.com/{username}"
        xFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} X            :{Style.RESET_ALL} {xUrl}"
    else:
        xFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} X{Style.RESET_ALL}"

    return xFound