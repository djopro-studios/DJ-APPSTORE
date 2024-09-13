from .__version__ import __version__
import os
import sys
import requests
import json
from PIL import Image
import zipfile
import pefile
import tarfile
import subprocess
import urllib3
import shutil

URL = requests.get("https://raw.githubusercontent.com/djopro-studios/DJ-APPSTORE/server-api-upd-side/server-api-universal").text.strip().replace("%0A", "")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

########### COLORS #############
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m' # called to return to standard terminal text color
BACKGROUND_BLACK = '\033[40m'
BACKGROUND_RED = '\033[41m'
BACKGROUND_GREEN = '\033[42m'
BACKGROUND_YELLOW = '\033[43m' # orange on some systems
BACKGROUND_BLUE = '\033[44m'
BACKGROUND_MAGENTA = '\033[45m'
BACKGROUND_CYAN = '\033[46m'
BACKGROUND_LIGHT_GRAY = '\third-party033[47m'
BACKGROUND_DARK_GRAY = '\033[100m'
BACKGROUND_BRIGHT_RED = '\033[101m'
BACKGROUND_BRIGHT_GREEN = '\033[102m'
BACKGROUND_BRIGHT_YELLOW = '\033[103m'
BACKGROUND_BRIGHT_BLUE = '\033[104m'
BACKGROUND_BRIGHT_MAGENTA = '\033[105m'
BACKGROUND_BRIGHT_CYAN = '\033[106m'
BACKGROUND_WHITE = '\033[107m'
##########################################

def is_valid_tar(tar_path):
    try:
        # Open the tar file in read mode
        with tarfile.open(tar_path, 'r') as tar:
            # List all files inside the tar archive
            tar.getmembers()  # If this works, the tar file is valid
        return True
    except (tarfile.TarError, IOError):
        return False
    
def is_valid_image_pillow(file_name):
    try:
        with Image.open(file_name) as img:
            img.verify()
            return True
    except (IOError, SyntaxError):
        return False

def is_valid_apk(apk_path):
    try:
        with zipfile.ZipFile(apk_path, 'r') as zip_ref:
            # Check if the APK file can be opened
            return zip_ref.testzip() is None
    except zipfile.BadZipFile:
        return False

def is_valid_pe(exe_path):
    try:
        pe = pefile.PE(exe_path)
        # If the file loads without error, it's a valid PE file
        return True
    except pefile.PEFormatError:
        return False

def help_cmd():
    print()
    print(""" == All commands and arguments ==

- help : show all arguments and commands
- connect : connect to your DJAPPSTORE Account and save your connection
- new_account : create a new account
- disconnect : disconnect from your account and erase your last connection
- deploy : deploy apps on the store
- remove_app : erase app from the store
- update : update the program
- fix : fix & reinstall the program
          
[ NOTE ] This program auto update every execution
          
""")
    
def connect_cmd():
    print("[-] Checking for connection saved", end='\r', flush=True)
    if not os.path.exists(f"{os.path.dirname(__file__)}/token"):
        open(f"{os.path.dirname(__file__)}/token","w").write("")
        
    print("[\] Checking for connection saved", end='\r', flush=True)
    file = open(f"{os.path.dirname(__file__)}/token","r")
    print("[|] Checking for connection saved", end='\r', flush=True)
    if file.read() == "":
        file.close()
        print(GREEN + "[OK]" + RESET + " Checking for connection saved")
        print()
        usrname = input("Username : ")
        psword = input("Password : ")
        print()
        print("[-] Connecting to your account", end='\r', flush=True)
        account = requests.get(f"{URL}/connect",data={"name":usrname,"pswrd":psword},verify=False)
        print("[\] Connecting to your account", end='\r', flush=True)
        if account.status_code == 200:
            print("[|] Connecting to your account", end='\r', flush=True)
            json_dt = json.loads(account.text)
            print("[/] Connecting to your account", end='\r', flush=True)
            if json_dt["success"] == 0:
                print(YELLOW + "[!]" + RESET + " Connecting to your account")
                if json_dt["error"] == "pswd_incorrect":
                    print(RED + "Error : Password Incorrect" + RESET)
                    exit()
                elif json_dt["error"] == "NameAccount_404":
                    print(RED + "Error : Account Not Found" + RESET)
                    exit()
            else:
                if json_dt["verified"] == 1:
                    print(GREEN + "[OK]" + RESET + " Connecting to your account")
                    print("[-] Saving your connection", end='\r', flush=True)
                    file = open(f"{os.path.dirname(__file__)}/token","w")
                    print("[\] Saving your connection", end='\r', flush=True)
                    file.write(json_dt["id_creator"])
                    print(GREEN + "[OK]" + RESET + " Saving your connection")
                    file.close()
                    exit()
                else:
                    print(YELLOW + "[!]" + RESET + " Connecting to your account")
                    print(RED + "Error : Account must be verified" + RESET)
                    exit()
        else:
            print(YELLOW + "[!]" + RESET + " Checking for connection saved")
            print(f"Error : Bad Request Code {account.status_code}" + RESET)
            exit()
    else:
        print(YELLOW + "[!]" + RESET + " Checking for connection saved")
        print(RED + "Error : Another account already connected" + RESET)
        exit()

def new_account_cmd():
    print("[-] Checking for connection saved", end='\r', flush=True)
    if not os.path.exists(f"{os.path.dirname(__file__)}/token"):
        open(f"{os.path.dirname(__file__)}/token","w").write("")
        
    print("[\] Checking for connection saved", end='\r', flush=True)
    file = open(f"{os.path.dirname(__file__)}/token","r")
    print("[|] Checking for connection saved", end='\r', flush=True)
    if file.read() == "":
        file.close()
        print(GREEN + "[OK]" + RESET + " Checking for connection saved")
        print()
        usrname = input("Username : ")
        psword = input("Password : ")
        email = input("Email : ")
        print()
        print("[-] Creating a new account", end='\r', flush=True)
        account = requests.get(f"{URL}/add_account",data={"name":usrname,"email":email,"pswrd":psword},verify=False)
        print("[\] Creating a new account", end='\r', flush=True)
        if account.status_code == 200:
            print("[|] Creating a new account", end='\r', flush=True)
            json_dt = json.loads(account.text)
            if json_dt["success"] == 0:
                if json_dt["error"] == "AccountName_Taken":
                    print(YELLOW + "[!]" + RESET + " Creating a new account")
                    print(RED + "Error : Name Account is already taken" + RESET)
                    exit()
                else:
                    print(YELLOW + "[!]" + RESET + " Creating a new account")
                    print(f"Error : JSON {json_dt['error']}" + RESET)
                    exit()
            else:
                print(GREEN + "[OK]" + RESET + " Creating a new account")
                print("[-] Saving your connection", end='\r', flush=True)
                file = open(f"{os.path.dirname(__file__)}/token","w")
                print("[\] Saving your connection", end='\r', flush=True)
                file.write(json_dt["id_creator"])
                print("[|] Saving your connection", end='\r', flush=True)
                file.close()
                print(GREEN + "[OK]" + RESET + " Saving your connection")
        else:
            print(YELLOW + "[!]" + RESET + " Checking for connection saved")
            print(f"Error : Bad Request Code {account.status_code}" + RESET)
            exit()
    else:
        print(YELLOW + "[!]" + RESET + " Checking for connection saved")
        print(RED + "Error : Another account already connected" + RESET)
        exit()

def disconnect_cmd():
    print("[-] Deleting your connection", end='\r', flush=True)
    if not os.path.exists(f"{os.path.dirname(__file__)}/token"):
        open(f"{os.path.dirname(__file__)}/token","w").write("")
        print(GREEN + "[OK]" + RESET + " Deleting your connection")
    else:
        os.remove(f"{os.path.dirname(__file__)}/token")
        open(f"{os.path.dirname(__file__)}/token","w").write("")
        print(GREEN + "[OK]" + RESET + " Deleting your connection")

def deploy_cmd():
    print("[-] Checking for connection saved", end='\r', flush=True)
    if not os.path.exists(f"{os.path.dirname(__file__)}/token"):
        open(f"{os.path.dirname(__file__)}/token","w").write("")
        
    print("[\] Checking for connection saved", end='\r', flush=True)
    file = open(f"{os.path.dirname(__file__)}/token","r")
    print("[|] Checking for connection saved", end='\r', flush=True)
    if file.read() == "":
        file.close()
        print(YELLOW + "[!]" + RESET + " Checking for connection saved")
        print(RED + "Error : No saved connection found" + RESET)
        exit()
    else:
        print(GREEN + "[OK]" + RESET + " Checking for connection saved")
        print()
        print(" - Choose your platform supported app:")
        print()
        print("[1] Android")
        print("[2] Windows")
        print("[3] PaxOS9")
        print()
        platform = int(input("Choose > "))
        if platform < 1 or platform > 3:
            print(RED + "Error : Choise not found" + RESET)
            exit()
        print()
        print(" - Complete the app details :")
        name = str(input("App Name : "))
        print("Description " + CYAN + "[MultiLine | press Ctrl+D (or Ctrl+Z for Windows) to stop typing] " + YELLOW + "(^Z and ^D will be automatically erased)" + RESET)
        lines = []
        description = ""
        while True:
            try:
                line = input(GREEN + "> " + RESET)
                lines.append(line)
            except EOFError:
                break
            
        
        if len(lines) != 0:
            for txt in lines:
                txt.replace("^Z","")
                txt.replace("^D","")

                description = f"{description}\n{txt}"
        
        icon_path = str(input("Icon Path (.png only supported) : "))
        if not is_valid_image_pillow(icon_path):
            print(RED + "Error : Not a valid image" + RESET)
            exit()
        else:
            if open(icon_path, "rb").read(4) != b"\x89PNG":
                print(RED + "Error : Only .png file are supported" + RESET)
                exit()
        
        file_path = str(input("App File : "))

        if not os.path.exists(file_path):
            print(RED + "Error : File Not Found" + RESET)
            exit()
        else:
            if platform == 1:
                if not is_valid_apk(file_path):
                    print(RED + "Error : File APK not valid" + RESET)
                    exit()
            elif platform == 2:
                if not is_valid_pe(file_path):
                    print(RED + "Error : File .EXE not valid" + RESET)
                    exit()
            elif platform == 3:
                if not is_valid_tar(file_path):
                    print(RED + "Error : File .TAR not valid" + RESET)
                    exit()
        print()
        print("[-] Deploying your app", end='\r', flush=True)
        data_form_deploy ={
            "name":name,
            "description":description,
        } 
        data_files_deploy = {
            "icon": open(icon_path,"rb"),
            "appfile": open(file_path,"rb")
        }
        cookies_data = {
            "id_creator":str(open(f"{os.path.dirname(__file__)}/token","r").read())
        }
        requete = None
        if platform == 1:
            print("[\] Deploying your app", end='\r', flush=True)
            requete = requests.get(f"{URL}/add_app/android",verify=False,data = data_form_deploy,files=data_files_deploy,cookies=cookies_data)
        elif platform == 2:
            print("[\] Deploying your app", end='\r', flush=True)
            requete = requests.get(f"{URL}/add_app/windows",verify=False,data = data_form_deploy,files=data_files_deploy,cookies=cookies_data)
        elif platform == 3:
            print("[\] Deploying your app", end='\r', flush=True)
            requete = requests.get(f"{URL}/add_app/paxo",verify=False,data = data_form_deploy,files=data_files_deploy,cookies=cookies_data)
        
        print("[|] Deploying your app", end='\r', flush=True)
        if requete.status_code == 200:
            if json.loads(requete.text)["success"] == 0:
                if json.loads(requete.text)["error"] == "AccountID_404":
                    print(YELLOW + "[!]" + RESET + " Deploying your app")
                    print(RED + "Error : Account not Found" + RESET)
                    exit()
                elif json.loads(requete.text)["error"] == "Unverified_Account":
                    print(YELLOW + "[!]" + RESET + " Deploying your app")
                    print(RED + "Error : Account not Verified" + RESET)
                    exit()
                elif json.loads(requete.text)["error"] == "NameApp_Taken":
                    print(YELLOW + "[!]" + RESET + " Deploying your app")
                    print(RED + "Error : App Name is already taken" + RESET)
                    exit()
            
            else:
                print(GREEN + "[OK]" + RESET + " Deploying your app")

def remove_app_cmd():
    print("[-] Checking for connection saved", end='\r', flush=True)
    if not os.path.exists(f"{os.path.dirname(__file__)}/token"):
        open(f"{os.path.dirname(__file__)}/token","w").write("")
        
    print("[\] Checking for connection saved", end='\r', flush=True)
    file = open(f"{os.path.dirname(__file__)}/token","r")
    print("[|] Checking for connection saved", end='\r', flush=True)
    if file.read() == "":
        file.close()
        print(YELLOW + "[!]" + RESET + " Checking for connection saved")
        print(RED + "Error : No saved connection found" + RESET)
        exit()
    else:
        print(GREEN + "[OK]" + RESET + " Checking for connection saved")
        print()
        print(" - Choose your platform supported app:")
        print()
        print("[1] Android")
        print("[2] Windows")
        print("[3] PaxOS9")
        print()
        platform = int(input("Choose > "))
        if platform < 1 or platform > 3:
            print(RED + "Error : Choise not found" + RESET)
            exit()
        print()
        name = str(input("Name APP to remove : "))
        print()
        print("[-] Removing your app", end='\r', flush=True)
        data_form_deploy ={
            "name":name,
        } 
        cookies_data = {
            "id_creator":str(open(f"{os.path.dirname(__file__)}/token","r").read())
        }
        requete = None
        if platform == 1:
            print("[\] Removing your app", end='\r', flush=True)
            requete = requests.get(f"{URL}/remove_app/android",verify=False,data = data_form_deploy,cookies=cookies_data)
        elif platform == 2:
            print("[\] Removing your app", end='\r', flush=True)
            requete = requests.get(f"{URL}/remove_app/windows",verify=False,data = data_form_deploy,cookies=cookies_data)
        elif platform == 3:
            print("[\] Removing your app", end='\r', flush=True)
            requete = requests.get(f"{URL}/remove_app/paxo",verify=False,data = data_form_deploy,cookies=cookies_data)
        
        print("[|] Removing your app", end='\r', flush=True)
        if requete.status_code == 200:
            if json.loads(requete.text)["success"] == 0:
                if json.loads(requete.text)["error"] == "AccountID_404":
                    print(YELLOW + "[!]" + RESET + " Removing your app")
                    print(RED + "Error : Account not Found" + RESET)
                    exit()
                elif json.loads(requete.text)["error"] == "Unverified_Account":
                    print(YELLOW + "[!]" + RESET + " Removing your app")
                    print(RED + "Error : Account not Verified" + RESET)
                    exit()
                elif json.loads(requete.text)["error"] == "AppName_404":
                    print(YELLOW + "[!]" + RESET + " Removing your app")
                    print(RED + "Error : App Name not Found" + RESET)
                    exit()
                elif json.loads(requete.text)["error"] == "AccountID_NotAllowed":
                    print(YELLOW + "[!]" + RESET + " Removing your app")
                    print(RED + "Error : You are not allowed to remove other creator apps" + RESET)
                    exit()
            
            else:
                print(GREEN + "[OK]" + RESET + " Removing your app")
        else:
            print(YELLOW + "[!]" + RESET + " Checking for connection saved")
            print(f"Error : Bad Request Code {requete.status_code}" + RESET)
            exit()

def update_cmd():
    print("[\] Checking Updates", end='\r', flush=True)
    if True:
        print("[|] Checking Updates", end='\r', flush=True)
        recent_version = requests.get(URL,verify=False)
        print("[/] Checking Updates", end='\r', flush=True)
        if recent_version.status_code == 200:
            print("[-] Checking Updates", end='\r', flush=True)
            if json.loads(recent_version.text)["v_deployer"] > __version__:
                print(GREEN + "[OK]" + RESET + " Checking Updates")
                print("[-] Updating the CLI", end='\r', flush=True)
                #upd_data = requests.get(f"{URL}/updates_file/cli.py",verify=False)
                print("[\] Updating the CLI", end='\r', flush=True)
                if True:
                    print("[|] Updating the CLI", end='\r', flush=True)
                    
                    ###################################################

                    result = subprocess.run(["git", "clone", "-b", "DJADeployer", "https://github.com/djopro-studios/DJ-APPSTORE"], capture_output=True, text=True)

                    if result.returncode == 0:
                        print("[/] Updating the CLI", end='\r', flush=True)
                        os.chdir(f"{os.getcwd()}/DJ-APPSTORE") 
                        result = subprocess.run(["pip","install","."], capture_output=True, text=True)

                        if result.returncode == 0:
                            print(GREEN + "[OK]" + RESET + " Updating the CLI")
                            os.chdir(f"{os.getcwd()}/..") 
                            print(f"Note : Just delete the folder DJ-APPSTORE in the {os.getcwd()}")
                            exit()
                        else:
                            print(YELLOW + "[!]" + RESET + " Updating the CLI")
                            print(RED + "Error : ", result.stderr + RESET)

                    else:
                        print(YELLOW + "[!]" + RESET + " Updating the CLI")
                        print(RED + "Error : ", result.stderr + RESET)

                    ###################################################
                else:
                    print(YELLOW + "[!]" + RESET + " Updating the CLI")
                    print(RED + "Error : Bad Request / Internet Connexion" + RESET)
                    exit()
            else:
                print(GREEN + "[OK]" + RESET + " Checking Updates")
                exit()
        else:
            print(YELLOW + "[!]" + RESET + " Checking Updates")
            print(RED + "Error : Bad Request / Internet Connexion" + RESET)
            exit()
    else:
        print(YELLOW + "[!]" + RESET + " Checking Updates")
        print(RED + "Error : Bad Request / Internet Connexion" + RESET)
        exit()

def fix_cmd():
    print(RED + "Error : Comming Soon" + RESET)

################ MAIN ################
def main():
    print(f"""                              
               -------                  
              |       |                 
              |       |                 
              |       |                 
            -------------               
           |  |       |  |              
          |               |             
         |    @@@@@   @    |            
         |     @  @   @    |            
        |      @  @   @     |           
        |      @  @ @ @     |           
       |       @  @ @ @      |          
       |      @@@@@ @@@      |          
       |                     |          
        ---------------------           
      
       +=====================+
       | DJAPPSTORE DEPLOYER |
       +========= V{__version__} ========+

""")


    # FIRST CHECK

    #print(sys.argv[0])
    #if sys.argv[0].lower().find("python"):
    #    print(YELLOW + "[!]" + RESET + " First check")
    #    print(RED + "Error : Use 'pip install .' then use 'djad help'")
    #    exit()
    #else:
    #    print(GREEN + "[OK]" + RESET + " First Check")

    # CHECK UPDATES
    print("[-] Checking Updates", end='\r', flush=True)
    url_upd = requests.get("https://raw.githubusercontent.com/djopro-studios/DJ-APPSTORE/server-api-upd-side/server-api-universal")
    print("[\] Checking Updates", end='\r', flush=True)
    if url_upd.status_code == 200:
        print("[|] Checking Updates", end='\r', flush=True)
        URL = url_upd.text.strip().replace("%0A", "")
        recent_version = requests.get(URL, verify=False)
        print("[/] Checking Updates", end='\r', flush=True)
        if recent_version.status_code == 200:
            print("[-] Checking Updates", end='\r', flush=True)
            if json.loads(recent_version.text)["v_deployer"] > __version__:
                print(GREEN + "[OK]" + RESET + " Checking Updates")
                print("[-] Updating the CLI", end='\r', flush=True)
                # upd_data = requests.get(f"{URL}/updates_file/cli.py", verify=False)
                print("[\] Updating the CLI", end='\r', flush=True)
                if True:
                    print("[|] Updating the CLI", end='\r', flush=True)
                    
                    ###################################################
                    
                    result = subprocess.run(["git", "clone", "-b", "DJADeployer", "https://github.com/djopro-studios/DJ-APPSTORE"], capture_output=True, text=True)

                    if result.returncode == 0:
                        print("[/] Updating the CLI", end='\r', flush=True)
                        os.chdir(f"{os.getcwd()}/DJ-APPSTORE") 
                        result = subprocess.run(["pip","install","."], capture_output=True, text=True)

                        if result.returncode == 0:
                            print(GREEN + "[OK]" + RESET + " Updating the CLI")
                            os.chdir(f"{os.getcwd()}/..") 
                            print(f"Note : Just delete the folder DJ-APPSTORE in the {os.getcwd()}")
                            exit()
                        else:
                            print(YELLOW + "[!]" + RESET + " Updating the CLI")
                            print(RED + "Error : ", result.stderr + RESET)

                    else:
                        print(YELLOW + "[!]" + RESET + " Updating the CLI")
                        print(RED + "Error : ", result.stderr + RESET)

                    ###################################################
                else:
                    print(YELLOW + "[!]" + RESET + " Updating the CLI")
                    print(RED + "Error : Bad Request / Internet Connexion" + RESET)
                    exit()
            else:
                print(GREEN + "[OK]" + RESET + " Checking Updates")
                
        else:
            print(YELLOW + "[!]" + RESET + " Checking Updates")
            print(RED + "Error : Bad Request / Internet Connexion" + RESET)
            exit()
    else:
        print(YELLOW + "[!]" + RESET + " Checking Updates")
        print(RED + "Error : Bad Request / Internet Connexion" + RESET)
        exit()

    if len(sys.argv) == 1:
        print("Execute the command 'djad help' for Help")
        exit()
    elif sys.argv[1].lower() == "help":
        help_cmd()
    elif sys.argv[1].lower() == "connect":
        connect_cmd()
    elif sys.argv[1].lower() == "new_account":
        new_account_cmd()
    elif sys.argv[1].lower() == "disconnect":
        disconnect_cmd()
    elif sys.argv[1].lower() == "deploy":
        deploy_cmd()
    elif sys.argv[1].lower() == "remove_app":
        remove_app_cmd()
    elif sys.argv[1].lower() == "update":
        update_cmd()
    elif sys.argv[1].lower() == "fix":
        fix_cmd()
    else:
        help_cmd()
    
if __name__ == "__main__":
    main()
