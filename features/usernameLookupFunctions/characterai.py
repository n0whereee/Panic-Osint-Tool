from config.settings import *

def lookupCharacterai(username):
    url = f"https://character.ai/profile/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def characteraiResult(username):
    characterai = lookupCharacterai(username=username)

    if characterai:
        characteraiUrl = f"https://character.ai/profile/{username}"
        characteraiFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Character.ai :{Style.RESET_ALL} {characteraiUrl}"
    else:
        characteraiFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Character.ai{Style.RESET_ALL}"

    return characteraiFound