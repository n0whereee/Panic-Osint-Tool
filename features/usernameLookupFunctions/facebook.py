from config.settings import *

def lookupFacebook(username):
    url = f"https://www.facebook.com/{username}"
    follower = "Follower"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        data = r.text

        return follower in data
    else:
        return False

def facebookResult(username):
    facebook = lookupFacebook(username=username)

    if facebook:
        facebookUrl = f"https://www.facebook.com/{username}"
        facebookFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Facebook     :{Style.RESET_ALL} {facebookUrl}"
    else:
        facebookFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Facebook{Style.RESET_ALL}"

    return facebookFound