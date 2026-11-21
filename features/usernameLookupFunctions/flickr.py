from config.settings import *

def lookupFlickr(username):
    url = f"https://www.flickr.com/people/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def flickrResult(username):
    flickr = lookupFlickr(username=username)

    if flickr:
        flickrUrl = f"https://www.flickr.com/people/{username}"
        flickrFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Flickr       :{Style.RESET_ALL} {flickrUrl}"
    else:
        flickrFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Flickr{Style.RESET_ALL}"

    return flickrFound