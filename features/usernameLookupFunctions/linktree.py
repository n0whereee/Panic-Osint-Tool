from config.settings import *

def lookupLinktree(username):
    url = f"https://linktr.ee/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def linktreeResult(username):
    linktree = lookupLinktree(username=username)

    if linktree:
        linktreeUrl = f"https://linktr.ee/{username}"
        linktreeFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Linktree     :{Style.RESET_ALL} {linktreeUrl}"
    else:
        linktreeFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Linktree{Style.RESET_ALL}"

    return linktreeFound