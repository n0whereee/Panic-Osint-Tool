from config.settings import *

def lookupGunslol(username):
    url = f"https://guns.lol/{username}"
    pageViews = "page_views"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        data = r.text

        return pageViews in data
    else:
        return False

def gunslolResult(username):
    gunslol = lookupGunslol(username=username)

    if gunslol:
        gunslolUrl = f"https://guns.lol/{username}"
        gunslolFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Guns.lol     :{Style.RESET_ALL} {gunslolUrl}"
    else:
        gunslolFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Guns.lol{Style.RESET_ALL}"

    return gunslolFound