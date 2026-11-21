from config.settings import *

def lookupRoblox(username):
    url = "https://users.roblox.com/v1/usernames/users"
    json={
        "usernames": [username],
        "excludeBannedUsers": False
    }

    r = requests.post(
        url,
        json=json,
        timeout=10
    )

    if r.status_code in succesStatus:
        data = r.json() 
        taken = data.get("data")

        if taken == []:
            return False
        else:
            userId = taken[0].get("id")

            return userId
    else:
        return False

def robloxResult(username):
    roblox = lookupRoblox(username=username)

    if roblox:
        robloxUrl = f"https://www.roblox.com/users/{roblox}/profile"
        robloxFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Roblox       :{Style.RESET_ALL} {robloxUrl}"
    else:
        robloxFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Roblox{Style.RESET_ALL}"

    return robloxFound