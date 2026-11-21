from config.settings import *

def lookupTiktok(username):
    url = f"https://www.tiktok.com/@{username}"
    userInfo = "userInfo"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        data = r.text

        return userInfo in data
    else:
        return False

def tiktokResult(username):
    tiktok = lookupTiktok(username=username)

    if tiktok:
        tiktokUrl = f"https://www.tiktok.com/@{username}"
        tiktokFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Tiktok       :{Style.RESET_ALL} {tiktokUrl}"
    else:
        tiktokFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Tiktok{Style.RESET_ALL}"

    return tiktokFound