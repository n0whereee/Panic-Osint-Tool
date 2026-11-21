from config.settings import *

def lookupPornhub(username):
    url = f"https://www.pornhub.com/users/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def pornhubResult(username):
    pornhub = lookupPornhub(username=username)

    if pornhub:
        pornhubUrl = f"https://www.pornhub.com/users/{username}"
        pornhubFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Pornhub      :{Style.RESET_ALL} {pornhubUrl}"
    else:
        pornhubFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Pornhub{Style.RESET_ALL}"

    return pornhubFound