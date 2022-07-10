import requests
from colorama import Fore, init

init()

class liinks():
    def __init__(self):

        self.targets = open("targets.txt").read().splitlines()
        self.valid = open("valid.txt", "a+")
    
    def check(self):
        for targets in self.targets:
            checkusername = requests.post(f"https://www.liinks.co/i/graphql", json={"operationName":"getIsUserSlugUnique","variables":{"slug":targets},"query":"mutation getIsUserSlugUnique($slug: String!) {\n  isUserSlugUnique(slug: $slug)\n}\n"})
          
            if ("true" in checkusername.text):
                print(f"[{Fore.GREEN}+{Fore.WHITE}] {targets} is not taken!")
            #elif ("false" in checkusername.text):
              #  print(f"[{Fore.RED}+{Fore.WHITE}] {targets} is taken!")

if __name__ == "__main__":
    liinksChecker = liinks()
    liinksChecker.check()
    
    #Discord: Obstacles#5096
