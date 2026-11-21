from config.settings import *

def lookupCfx(username):
    url = f"https://forum.cfx.re/u/check_username.json?username={username}"

    r = requests.get(
        url,
        timeout=10
    )

    if r.status_code in succesStatus:
        data = r.json() 

        if data.get("available"):
            return False
        else:
            return True
    else:
        return False

def cfxResult(username):
    cfx = lookupCfx(username=username)

    if cfx:
        cfxUrl = f"https://forum.cfx.re/u/{username}"
        cfxFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} FiveM / RedM :{Style.RESET_ALL} {cfxUrl}"
    else:
        cfxFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} FiveM / RedM{Style.RESET_ALL}"

    return cfxFound