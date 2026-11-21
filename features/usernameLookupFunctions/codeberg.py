from config.settings import *

def lookupCodeberg(username):
    url = f"https://codeberg.org/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def codebergResult(username):
    codeberg = lookupCodeberg(username=username)

    if codeberg:
        codebergUrl = f"https://codeberg.org/{username}"
        codebergFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Codeberg     :{Style.RESET_ALL} {codebergUrl}"
    else:
        codebergFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Codeberg{Style.RESET_ALL}"

    return codebergFound