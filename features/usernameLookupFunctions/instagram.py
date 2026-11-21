from config.settings import *

def lookupInstagram(username):
    url = f"https://www.instagram.com/{username}"
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

def instagramResult(username):
    instagram = lookupInstagram(username=username)

    if instagram:
        instagramUrl = f"https://www.instagram.com/{username}"
        instagramFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Instagram    :{Style.RESET_ALL} {instagramUrl}"
    else:
        instagramFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Instagram{Style.RESET_ALL}"

    return instagramFound