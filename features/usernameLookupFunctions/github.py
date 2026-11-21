from config.settings import *

def lookupGithub(username):
    url = f"https://api.github.com/users/{username}"

    r = requests.get(
        url,
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def githubResult(username):
    github = lookupGithub(username=username)

    if github:
        githubUrl = f"https://github.com/{username}"
        githubFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Github       :{Style.RESET_ALL} {githubUrl}"
    else:
        githubFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Github{Style.RESET_ALL}"

    return githubFound