from config.settings import *

def lookupSnapchat(username):
    url = f"https://www.snapchat.com/add/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def snapchatResult(username):
    snapchat = lookupSnapchat(username=username)

    if snapchat:
        snapchatUrl = f"https://www.snapchat.com/add/{username}"
        snapchatFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Snapchat     :{Style.RESET_ALL} {snapchatUrl}"
    else:
        snapchatFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Snapchat{Style.RESET_ALL}"

    return snapchatFound