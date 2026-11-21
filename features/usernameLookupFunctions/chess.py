from config.settings import *

def lookupChess(username):
    url = f"https://api.chess.com/pub/player/{username}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if r.status_code in succesStatus:
        return True
    else:
        return False

def chessResult(username):
    chess = lookupChess(username=username)

    if chess:
        chessUrl = f"https://www.chess.com/member/{username}"
        chessFound = f"{bracketOpen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketClosed2}{Fore.GREEN} Chess.com    :{Style.RESET_ALL} {chessUrl}"
    else:
        chessFound = f"{bracketOpen2}{Fore.RED}×{Style.RESET_ALL}{bracketClosed2}{Fore.RED} Chess.com{Style.RESET_ALL}"

    return chessFound