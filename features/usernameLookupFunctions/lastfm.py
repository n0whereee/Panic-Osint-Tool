from config.settings import *

def lookupLastfm(username):
    url = f"https://www.last.fm/user/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def lastfmResult(username):
    lastfm = lookupLastfm(username=username)

    if lastfm:
        lastfmUrl = f"https://www.last.fm/user/{username}"
        lastfmFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Last.fm      :{Style.RESET_ALL} {lastfmUrl}"
    else:
        lastfmFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Last.fm{Style.RESET_ALL}"

    return lastfmFound