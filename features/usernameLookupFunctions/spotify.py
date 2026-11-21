from config.settings import *

def lookupSpotify(username):
    url = f"https://open.spotify.com/user/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def spotifyResult(username):
    spotify = lookupSpotify(username=username)

    if spotify:
        spotifyUrl = f"https://open.spotify.com/user/{username}"
        spotifyFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Spotify      :{Style.RESET_ALL} {spotifyUrl}"
    else:
        spotifyFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Spotify{Style.RESET_ALL}"

    return spotifyFound