from config.settings import *

def lookupKick(username):
    url = f"https://kick.com/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def kickResult(username):
    kick = lookupKick(username=username)

    if kick:
        kickUrl = f"https://kick.com/{username}"
        kickFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Kick         :{Style.RESET_ALL} {kickUrl}"
    else:
        kickFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Kick{Style.RESET_ALL}"

    return kickFound