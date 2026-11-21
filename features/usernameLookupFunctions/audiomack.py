from config.settings import *

def lookupAudiomack(username):
    url = f"https://audiomack.com/{username}"
    follower = "Followers"

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

def audiomackResult(username):
    audiomack = lookupAudiomack(username=username)

    if audiomack:
        audiomackUrl = f"https://audiomack.com/{username}"
        audiomackFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Audiomack    :{Style.RESET_ALL} {audiomackUrl}"
    else:
        audiomackFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Audiomack{Style.RESET_ALL}"

    return audiomackFound