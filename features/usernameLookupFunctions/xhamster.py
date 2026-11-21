from config.settings import *

def lookupXhamster(username):
    url = f"https://xhamster.com/users/profiles/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def xhamsterResult(username):
    xhamster = lookupXhamster(username=username)

    if xhamster:
        xhamsterUrl = f"https://xhamster.com/users/profiles/{username}"
        xhamsterFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Xhamster     :{Style.RESET_ALL} {xhamsterUrl}"
    else:
        xhamsterFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Xhamster{Style.RESET_ALL}"

    return xhamsterFound