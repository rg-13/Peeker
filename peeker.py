import argparse
import json
import os
import sys
import time

import requests
from fake_useragent import UserAgent

UA = UserAgent()
Agent = UA.random

""" Quick Admin Page Finder AKA Peeker.
    By RG13 """

class AdminPageFinder:
    def __init__(self, url, admin_list):
        self.url = url
        self.admin_list = []
        self.admin_list = admin_list
        self.agents = UA.random
    

    def help(self):
        self.art()
        print("""
        Quick Admin Page Finder
        Usage:
        python3 admin_finder.py -u <url> -a <admin_list>
        """)

    def art(self):
        """ RG13 ASCII """
        ascii = """
 ____    ____       _     __     
/\  _`\ /\  _`\   /' \  /'__`\   
\ \ \L\ \ \ \L\_\/\_, \/\_\L\ \  
 \ \ ,  /\ \ \L_L\/_/\ \/_/_\_<_ 
  \ \ \\ \\ \ \/, \ \ \ \/\ \L\ \
   \ \_\ \_\ \____/  \ \_\ \____/
    \/_/\/ /\/___/    \/_/\/___/ 
                                 
        """
        print(ascii)
        self.help()

    def random_user_agent(self):
        return self.agents

    def load_admin_list(self, list):
        with open(list, 'r') as f:
            try:
                self.admin_list = json.load(f)
            except:
                print("[-] Error loading admin list")
                sys.exit(1)


    def find_admin_page(self, admin_list):
        if not admin_list:
            print("[-] Error loading admin list")
            sys.exit(1)
        for admin in admin_list:
            try:
                r = requests.get(self.url + "/"+ admin, headers={'User-Agent': self.random_user_agent()})
                if r.status_code == 200:
                    print("[+] Admin page found: " + self.url + admin)
                    sys.exit(1)
            except:
                pass
        print("[-] Admin page not found")
        sys.exit(1)
    
    def args(self):
        parser = argparse.ArgumentParser(description='Admin Page Finder')
        parser.add_argument('-u', '--url', help='URL to scan', required=True)
        parser.add_argument('-l', '--list', help='Admin list file', required=True)
        args = parser.parse_args()
        self.url = args.url
        self.load_admin_list(args.list)
        self.run()
    
    def run(self):
        self.find_admin_page(self.admin_list)




if __name__ == "__main__":
    AdminPageFinder().args()
    sys.exit(1)
