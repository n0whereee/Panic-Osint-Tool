from config.banners import *
from features.usernameLookupFunctions.discord import *
from features.usernameLookupFunctions.tiktok import *
from features.usernameLookupFunctions.instagram import *
from features.usernameLookupFunctions.snapchat import *
from features.usernameLookupFunctions.facebook import *
from features.usernameLookupFunctions.x import *
from features.usernameLookupFunctions.pinterest import *
from features.usernameLookupFunctions.flickr import *
from features.usernameLookupFunctions.kick import *
from features.usernameLookupFunctions.spotify import *
from features.usernameLookupFunctions.soundcloud import *
from features.usernameLookupFunctions.lastfm import *
from features.usernameLookupFunctions.audiomack import *
from features.usernameLookupFunctions.bandlab import *
from features.usernameLookupFunctions.roblox import *
from features.usernameLookupFunctions.minecraft import *
from features.usernameLookupFunctions.cfx import *
from features.usernameLookupFunctions.github import *
from features.usernameLookupFunctions.gitlab import *
from features.usernameLookupFunctions.codeberg import *
from features.usernameLookupFunctions.linktree import *
from features.usernameLookupFunctions.gunslol import *
from features.usernameLookupFunctions.chess import *
from features.usernameLookupFunctions.duolingo import *
from features.usernameLookupFunctions.pornhub import *
from features.usernameLookupFunctions.xhamster import *
from features.usernameLookupFunctions.erome import *
from features.usernameLookupFunctions.characterai import *

def lookupUsername():
        os.system("cls")
        slow(lookupBanner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketOpen}!{bracketClosed} {Fore.RED}Username lookup{Style.RESET_ALL}")
        print("")
        username = input(f"{bracketOpen}>{bracketClosed} {Fore.RED}Username -> {Style.RESET_ALL}")

        time.sleep(0.05)
        print(f"{bracketOpen}~{bracketClosed} {Fore.RED}Searching for username...{Style.RESET_ALL}")

        try:
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(discordResult(username=username))
            print(tiktokResult(username=username))
            print(instagramResult(username=username))
            print(snapchatResult(username=username))
            print(facebookResult(username=username))
            print(xResult(username=username))
            print(pinterestResult(username=username))
            print(flickrResult(username=username))
            print(kickResult(username=username))
            print(spotifyResult(username=username))
            print(soundcloudResult(username=username))
            print(lastfmResult(username=username))
            print(audiomackResult(username=username))
            print(bandlabResult(username=username))
            print(robloxResult(username=username))
            print(minecraftResult(username=username))
            print(cfxResult(username=username))
            print(githubResult(username=username))
            print(gitlabResult(username=username))
            print(codebergResult(username=username))
            print(linktreeResult(username=username))
            print(gunslolResult(username=username))
            print(chessResult(username=username))
            print(duolingoResult(username=username))
            print(pornhubResult(username=username))
            print(xhamsterResult(username=username))
            print(eromeResult(username=username))
            print(characteraiResult(username=username))
            time.sleep(0.05)
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

            print("")
            print(f"{bracketOpen}{Fore.WHITE}01{Style.RESET_ALL}{bracketClosed}{Fore.RED} Main Menu{Style.RESET_ALL}")
            print(f"{bracketOpen}{Fore.WHITE}02{Style.RESET_ALL}{bracketClosed}{Fore.RED} Exit{Style.RESET_ALL}")
            print("")

            command = input(f"""{Fore.RED} ┌──({Fore.WHITE}{winUsername}{Fore.RED})─[{Fore.WHITE}~/{system}/{pcName}{Fore.RED}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")

            if command == "1" or command == "01":
                pass
            elif command == "2" or command == "02":
                sys.exit()
            else:
                pass

        except Exception as e:
            print("")
            print(f"{bracketOpen}{Fore.WHITE}!{Style.RESET_ALL}{bracketClosed}{Fore.RED} Failed to lookup username :{Style.RESET_ALL} {e}")
            time.sleep(2)
        