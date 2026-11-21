from config.settings import *

def lookupGitlab(username):
    url = f"https://gitlab.com/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def gitlabResult(username):
    gitlab = lookupGitlab(username=username)

    if gitlab:
        gitlabUrl = f"https://gitlab.com/{username}"
        gitlabFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Gitlab       :{Style.RESET_ALL} {gitlabUrl}"
    else:
        gitlabFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Gitlab{Style.RESET_ALL}"

    return gitlabFound