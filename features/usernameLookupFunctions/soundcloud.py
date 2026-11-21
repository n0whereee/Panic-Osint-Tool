from config.settings import *

def lookupSoundcloud(username):
    url = f"https://soundcloud.com/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def soundcloudResult(username):
    soundcloud = lookupSoundcloud(username=username)

    if soundcloud:
        soundcloudUrl = f"https://soundcloud.com/{username}"
        soundcloudFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Soundcloud   :{Style.RESET_ALL} {soundcloudUrl}"
    else:
        soundcloudFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Soundcloud{Style.RESET_ALL}"

    return soundcloudFound