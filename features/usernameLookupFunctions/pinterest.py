from config.settings import *

def lookupPinterest(username):
    url = f"https://pinterest.com/{username}"
    profileName = "profile-name"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        data = r.text

        return profileName in data
    else:
        return False

def pinterestResult(username):
    pinterest = lookupPinterest(username=username)

    if pinterest:
        pinterestUrl = f"https://pinterest.com/{username}"
        pinterestFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Pinterest    :{Style.RESET_ALL} {pinterestUrl}"
    else:
        pinterestFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Pinterest{Style.RESET_ALL}"

    return pinterestFound