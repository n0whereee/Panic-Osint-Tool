from config.settings import *

def lookupBandlab(username):
    url = f"https://www.bandlab.com/api/v1.3/users/{username}"

    r = requests.get(
        url,
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def bandlabResult(username):
    bandlab = lookupBandlab(username=username)

    if bandlab:
        bandlabUrl = f"https://www.bandlab.com/{username}"
        bandlabFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Bandlab      :{Style.RESET_ALL} {bandlabUrl}"
    else:
        bandlabFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Bandlab{Style.RESET_ALL}"

    return bandlabFound