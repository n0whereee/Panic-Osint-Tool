from config.settings import *

def lookupMinecraft(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"

    r = requests.get(
        url,
        timeout=10
    )

    if r.status_code in succesStatus:
        data = r.json()
        userId = data.get("id")

        return userId
    else:
        return False

def minecraftResult(username):
    minecraft = lookupMinecraft(username=username)

    if minecraft:
        minecraftUrl = f"https://namemc.com/profile/{minecraft}"
        minecraftFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Minecraft    :{Style.RESET_ALL} {minecraftUrl}"
    else:
        minecraftFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Minecraft{Style.RESET_ALL}"

    return minecraftFound