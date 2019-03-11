#!/usr/bin/env python2.7

import os
import re
import sys
import urllib
import random
import ConfigParser
from time import gmtime, strftime, sleep

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'

def clearScr():
    os.system('clear')

def yesOrNo():
    return (raw_input("Continue Y / N: ") in yes)

spyderPrompt = "spyder ~# "
alreadyInstalled = "Already Installed"
'''
Config
'''
installDir = os.path.dirname(os.path.abspath(__file__)) + '/'
configFile = installDir + "/spydrs.cfg"
print(installDir)
config = ConfigParser.RawConfigParser()
config.read(configFile)

toolDir = installDir + config.get('spydrs', 'toolDir')
logDir = installDir + config.get('spydrs', 'logDir')
yes = config.get('spydrs', 'yes').split()

color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
random.shuffle(color_random)

d3=os.system("curl http://ipinfo.io/ip")
os.system("clear && clear && clear")
logo = color_random[0] + ''' 
        .d8888. 88"""Yb db      db 88888b.  88""Yb  .d8888.
        88'  YP 88   dP  `8b  d8'   8I  dY  88   db 88'  YP
        `8bo.   88___Yb   `8bd8'    8I   dY 88  db  `8bo.
          `Y8b. 88"""       88      8I   dY 88"Yb     `Y8b.
        db   8D 88          88      8I  dY  88  YP  db   8D
        `8888Y' 88          YP     88888b.  88   YI `8888Y'                               
     '''
menu = color.OKGREEN + '''
    {1}--Whois lookup
    {2}--Traceroute
    {3}--DNS Lookup
    {4}--Reverse DNS Lookup
    {5}--GeoIP Lookup
    {6}--Port Scan
    {7}--Reverse IP Lookup
    {8}--Subdomain Finder
    {9}--Control Panel Finder
    {10}-Upload File Finder
    {11}-Get server Info
    {12}-XssPy
    {99}-Exit                                                                                                                   
 '''

# find admin panels
def findPanels():
	site = raw_input('Enter target: ')
	print "[~] Finding admin panels"
	adminList = ['admin/', 'site/admin', 'admin.php/', 'up/admin/', 'central/admin/', 'whm/admin/', 'whmcs/admin/', 'support/admin/', 'upload/admin/', 'video/admin/', 'shop/admin/', 'shoping/admin/', 'wp-admin/', 'wp/wp-admin/', 'blog/wp-admin/', 'admincp/', 'admincp.php/', 'vb/admincp/', 'forum/admincp/', 'up/admincp/', 'administrator/',
		     'administrator.php/', 'joomla/administrator/', 'jm/administrator/', 'site/administrator/', 'install/', 'vb/install/', 'dimcp/', 'clientes/', 'admin_cp/', 'login/', 'login.php', 'site/login', 'site/login.php', 'up/login/', 'up/login.php', 'cp.php', 'up/cp', 'cp', 'master', 'adm', 'member', 'control', 'webmaster', 'myadmin', 'admin_cp', 'admin_site', 'adminpanel/']
	clearScr()
	for admin in adminList:
		try:
		    if urllib.urlopen(site + admin).getcode() == 200:
			print " [*] Found admin panel -> ", site + admin
		except IOError:
		    pass
        quit()

#get server info
def getServerBanner():
        serverip = raw_input('Enter Server IP: ')
        clearScr()
        try:
            s = 'http://' + serverip
            httpresponse = urllib.urlopen(s)
            print ' [*] Server header -> ', httpresponse.headers.getheader(
                'server')
        except:
            print('[*] Server header ->  Not Found')
        quit()

def findUp():
        site = raw_input('Enter target: ')
        upList = ['up.php', 'up1.php', 'up/up.php', 'site/up.php', 'vb/up.php', 'forum/up.php', 'blog/up.php', 'upload.php',
                  'upload1.php', 'upload2.php', 'vb/upload.php', 'forum/upload.php', 'blog/upload.php', 'site/upload.php', 'download.php']
        clearScr()
        print "[~] Finding Upload"
	for up in upList:
	    try:
		if (urllib.urlopen(site + up).getcode() == 200):
		    html = urllib.urlopen(site + up).readlines()
		    for line in html:
		        if re.findall('type=file', line):
		            print " [*] Found upload -> ", site + up
	    except IOError:
	        pass
        quit()

class XssPy:
    def __init__(self):
        self.installDir = toolDir + "XssPy"
        self.gitRepo = "https://github.com/faizann24/XssPy.git"

        if not self.installed():
            self.install()
        clearScr()
        target = raw_input("   Enter Target: ")
        self.run(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))

    def run(self, target):
        try:
            os.system("python %s/XssPy.py -u %s" %
                      (self.installDir, target))
        except KeyboardInterrupt:
            pass
        quit()


print logo
print menu
def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()

           
def  select():
  try:
    choice = input("spydrs~# ")
    if choice == 1:
      d3 = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
 _       ____  ______  _________
| |     / / / / / __ \/  _/ ___/
| | /| / / /_/ / / / // / \__ \ 
| |/ |/ / __  / /_/ _/ / ___/ / 
|__/|__/_/ /_/\____/___//____/                                  
      """)
      os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
      print("")
      quit()
    elif choice == 2:
      d3 = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
 ____ ____   __   ___ ____ ____ _____ __  __ ____ ____ 
(_  _(  _ \ /__\ / __( ___(  _ (  _  (  )(  (_  _( ___)
  )(  )   //(__)( (__ )__) )   /)(_)( )(__)(  )(  )__) 
 (__)(_)\_(__)(__\___(____(_)\_(_____(______)(__)(____)
""")
      os.system("curl https://api.hackertarget.com/mtr/?q=" + d3 )
      print("")
      quit()
    elif choice == 3:
      d3 = raw_input('Enter Domain : ')
      os.system("clear")
      print("""
______ _   _ _____   _                 _                
|  _  | \ | /  ___| | |               | |               
| | | |  \| \ `--.  | |     ___   ___ | | ___   _ _ __  
| | | | . ` |`--. \ | |    / _ \ / _ \| |/ | | | | '_ \ 
| |/ /| |\  /\__/ / | |___| (_) | (_) |   <| |_| | |_) |
|___/ \_| \_\____/  \_____/\___/ \___/|_|\_\\__,_| .__ / 
                                                 | |    
                                                 |_|     
""")
      os.system("curl http://api.hackertarget.com/dnslookup/?q=" + d3 )
      print("")
      quit()    
    elif choice == 4:
	  d3 = raw_input('Enter IP Address - IP Range Or Domain  : ')
	  os.system("clear")
	  print("""
 _____                            ____  _____ _____ 
| __  |___ _ _ ___ ___ ___ ___   |    \|   | |   __|
|    -| -_| | | -_|  _|_ -| -_|  |  |  | | | |__   |
|__|__|___|\_/|___|_| |___|___|  |____/|_|___|_____|
                                                    
	  """)
	  os.system("curl https://api.hackertarget.com/reversedns/?q=" + d3 )
	  print("")
	  quit()
    elif choice == 5:
	  d3 = raw_input('Enter IP Or Domain : ')
	  os.system("clear")
	  print("""
   _____           _____ _____  
  / ____|         |_   _|  __ \ 
 | |  __  ___  ___  | | | |__) |
 | | |_ |/ _ \/ _ \ | | |  ___/ 
 | |__| |  __| (_) _| |_| |     
  \_____|\___|\___|_____|_|     
                                	
	""")
	  os.system("curl http://api.hackertarget.com/geoip/?q=" + d3 )
	  print("")
	  quit()
    elif choice == 6:
      d3 = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
     __                         __                 
  /\ \ \_ __ ___   __ _ _ __   / _\ ___ __ _ _ __  
 /  \/ | '_ ` _ \ / _` | '_ \  \ \ / __/ _` | '_ \ 
/ /\  /| | | | | | (_| | |_) | _\ | (_| (_| | | | |
\_\ \/ |_| |_| |_|\__,_| .__/  \__/\___\__,_|_| |_|
                       |_|                         
      """)
      os.system("curl http://api.hackertarget.com/nmap/?q=" + d3 )
      print("")
      quit()
    elif choice == 7:
	  d3 = raw_input('Enter IP Or Domain : ')
	  os.system("clear")
	  print("""
 ___ ___    _                         
|_ _| _ \  | |   ___ ___|          _____ 
 | ||  _/  | |__/ _ / _ |_/ / | || | '_ \ 
|___|_|    |____\___\___|_\_\ \_,_ | .__/  
                                   |_|     
	  """)
	  os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + d3 )
	  print("")
	  quit()
    elif choice == 8:
          d3 = raw_input('Entre Domain: ')
          path = os.getcwd() 
          os.system('cd ' +  path  + '/modules && python2 sub.py -t %s -l fr ' % d3)    
          quit()
    elif choice == 9:
          findPanels()
    elif choice == 10:
          findUp()
    elif choice == 11:
          getServerBanner()
    elif choice == 12:
          XssPy()
  except(KeyboardInterrupt):
    print ""
select()
