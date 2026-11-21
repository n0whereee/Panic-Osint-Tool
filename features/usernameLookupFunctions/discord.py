from config.settings import *

def lookupDiscord(username):
    url = f"https://discord.com/api/v9/unique-username/username-attempt-unauthed"
    checkUsername = {"username": username}

    r = requests.post(
        url,
        json=checkUsername,
        timeout=10
    )

    if r.status_code in succesStatus:
        data = r.json()
        taken = data.get("taken")

        return taken
    else:
        return False

def discordResult(username):
    discord = lookupDiscord(username=username)

    if discord:
        discordFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Discord      :{Style.RESET_ALL} {username}"
    else:
        discordFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Discord{Style.RESET_ALL}"

    return discordFound