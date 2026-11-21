from config.settings import *

def lookupDuolingo(username):
    url = f"https://www.duolingo.com/2017-06-30/users?username={username}"

    r = requests.get(
        url,
        timeout=10
    )

    if r.status_code in succesStatus:
        data = r.json()
        taken = data.get("users")

        if taken == []:
            return False
        else:
            return True
    else:
        return False

def duolingoResult(username):
    duolingo = lookupDuolingo(username=username)

    if duolingo:
        duolingoUrl = f"https://www.duolingo.com/2017-06-30/users?username={username}"
        duolingoFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Duolingo     :{Style.RESET_ALL} {duolingoUrl}"
    else:
        duolingoFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Duolingo{Style.RESET_ALL}"

    return duolingoFound