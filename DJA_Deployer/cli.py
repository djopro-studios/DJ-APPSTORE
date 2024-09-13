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
    if not os.path.exists("token"):
        open("token","w").write("")
        
    print("[\] Checking for connection saved", end='\r', flush=True)
    file = open("token","r")
    print("[|] Checking for connection saved", end='\r', flush=True)
    if file.read() == "":
        file.close()
        print("[OK] Checking for connection saved")
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
                print("[!] Connecting to your account")
                if json_dt["error"] == "pswd_incorrect":
                    print("Error : Password Incorrect")
                    exit()
                elif json_dt["error"] == "NameAccount_404":
                    print("Error : Account Not Found")
                    exit()
            else:
                if json_dt["verified"] == 1:
                    print("[OK] Connecting to your account")
                    print("[-] Saving your connection", end='\r', flush=True)
                    file = open("token","w")
                    print("[\] Saving your connection", end='\r', flush=True)
                    file.write(json_dt["id_creator"])
                    print("[OK] Saving your connection")
                    file.close()
                    exit()
                else:
                    print("[!] Connecting to your account")
                    print("Error : Account must be verified")
                    exit()
        else:
            print("[!] Checking for connection saved")
            print(f"Error : Bad Request Code {account.status_code}")
            exit()
    else:
        print("[!] Checking for connection saved")
        print("Error : Another account already connected")
        exit()

def new_account_cmd():
    print("[-] Checking for connection saved", end='\r', flush=True)
    if not os.path.exists("token"):
        open("token","w").write("")
        
    print("[\] Checking for connection saved", end='\r', flush=True)
    file = open("token","r")
    print("[|] Checking for connection saved", end='\r', flush=True)
    if file.read() == "":
        file.close()
        print("[OK] Checking for connection saved")
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
                    print("[!] Creating a new account")
                    print("Error : Name Account is already taken")
                    exit()
                else:
                    print("[!] Creating a new account")
                    print(f"Error : JSON {json_dt['error']}")
                    exit()
            else:
                print("[OK] Creating a new account")
                print("[-] Saving your connection", end='\r', flush=True)
                file = open("token","w")
                print("[\] Saving your connection", end='\r', flush=True)
                file.write(json_dt["id_creator"])
                print("[|] Saving your connection", end='\r', flush=True)
                file.close()
                print("[OK] Saving your connection")
        else:
            print("[!] Checking for connection saved")
            print(f"Error : Bad Request Code {account.status_code}")
            exit()
    else:
        print("[!] Checking for connection saved")
        print("Error : Another account already connected")
        exit()

def disconnect_cmd():
    print("[-] Deleting your connection", end='\r', flush=True)
    if not os.path.exists("token"):
        open("token","w").write("")
        print("[OK] Deleting your connection")
    else:
        os.remove("token")
        open("token","w").write("")
        print("[OK] Deleting your connection")

def deploy_cmd():
    print("[-] Checking for connection saved", end='\r', flush=True)
    if not os.path.exists("token"):
        open("token","w").write("")
        
    print("[\] Checking for connection saved", end='\r', flush=True)
    file = open("token","r")
    print("[|] Checking for connection saved", end='\r', flush=True)
    if file.read() == "":
        file.close()
        print("[!] Checking for connection saved")
        print("Error : No saved connection found")
        exit()
    else:
        print("[OK] Checking for connection saved")
        print()
        print(" - Choose your platform supported app:")
        print()
        print("[1] Android")
        print("[2] Windows")
        print("[3] PaxOS9")
        print()
        platform = int(input("Choose > "))
        if platform < 1 or platform > 3:
            print("Error : Choise not found")
            exit()
        print()
        print(" - Complete the app details :")
        name = str(input("App Name : "))
        print("Description [MultiLine | press Ctrl+D (or Ctrl+Z for Windows) to stop typing]")
        lines = []
        description = ""
        while True:
            try:
                line = input(">")
                lines.append(line)
            except EOFError:
                break
            
        
        if len(lines) != 0:
            for txt in lines:
                description = f"{description}\n"
        
        icon_path = str(input("Icon Path (.png only supported) : "))
        if not is_valid_image_pillow(icon_path):
            print("Error : Not a valid image")
            exit()
        else:
            if open(icon_path, "rb").read(4) != b"\x89PNG":
                print("Error : Only .png file are supported")
                exit()
        
        file_path = str(input("App File : "))

        if not os.path.exists(file_path):
            print("Error : File Not Found")
            exit()
        else:
            if platform == 1:
                if not is_valid_apk(file_path):
                    print("Error : File APK not valid")
                    exit()
            elif platform == 2:
                if not is_valid_pe(file_path):
                    print("Error : File .EXE not valid")
                    exit()
            elif platform == 3:
                if not is_valid_tar(file_path):
                    print("Error : File .TAR not valid")
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
            "id_creator":str(open("token","r").read())
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
                    print("[!] Deploying your app")
                    print("Error : Account not Found")
                    exit()
                elif json.loads(requete.text)["error"] == "Unverified_Account":
                    print("[!] Deploying your app")
                    print("Error : Account not Verified")
                    exit()
                elif json.loads(requete.text)["error"] == "NameApp_Taken":
                    print("[!] Deploying your app")
                    print("Error : App Name is already taken")
                    exit()
            
            else:
                print("[OK] Deploying your app")

def remove_app_cmd():
    print("[-] Checking for connection saved", end='\r', flush=True)
    if not os.path.exists("token"):
        open("token","w").write("")
        
    print("[\] Checking for connection saved", end='\r', flush=True)
    file = open("token","r")
    print("[|] Checking for connection saved", end='\r', flush=True)
    if file.read() == "":
        file.close()
        print("[!] Checking for connection saved")
        print("Error : No saved connection found")
        exit()
    else:
        print("[OK] Checking for connection saved")
        print()
        print(" - Choose your platform supported app:")
        print()
        print("[1] Android")
        print("[2] Windows")
        print("[3] PaxOS9")
        print()
        platform = int(input("Choose > "))
        if platform < 1 or platform > 3:
            print("Error : Choise not found")
            exit()
        print()
        name = str(input("Name APP to remove : "))
        print()
        print("[-] Removing your app", end='\r', flush=True)
        data_form_deploy ={
            "name":name,
        } 
        cookies_data = {
            "id_creator":str(open("token","r").read())
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
                    print("[!] Removing your app")
                    print("Error : Account not Found")
                    exit()
                elif json.loads(requete.text)["error"] == "Unverified_Account":
                    print("[!] Removing your app")
                    print("Error : Account not Verified")
                    exit()
                elif json.loads(requete.text)["error"] == "AppName_404":
                    print("[!] Removing your app")
                    print("Error : App Name not Found")
                    exit()
                elif json.loads(requete.text)["error"] == "AccountID_NotAllowed":
                    print("[!] Removing your app")
                    print("Error : You are not allowed to remove other creator apps")
                    exit()
            
            else:
                print("[OK] Removing your app")
        else:
            print("[!] Checking for connection saved")
            print(f"Error : Bad Request Code {requete.status_code}")
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
                print("[OK] Checking Updates")
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
                            print("[OK] Updating the CLI")
                            os.chdir(f"{os.getcwd()}/..") 
                            print(f"Note : Just delete the folder DJ-APPSTORE in the {os.getcwd()}")
                            exit()
                        else:
                            print("[!] Updating the CLI")
                            print("Error : ", result.stderr)

                    else:
                        print("[!] Updating the CLI")
                        print("Error : ", result.stderr)

                    ###################################################
                else:
                    print("[!] Updating the CLI")
                    print("Error : Bad Request / Internet Connexion")
                    exit()
            else:
                print("[OK] Checking Updates")
                exit()
        else:
            print("[!] Checking Updates")
            print("Error : Bad Request / Internet Connexion")
            exit()
    else:
        print("[!] Checking Updates")
        print("Error : Bad Request / Internet Connexion")
        exit()

def fix_cmd():
    print("Error : Comming Soon")

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
    #    print("[!] First check")
    #    print("Error : Use 'pip install .' then use 'djad help'")
    #    exit()
    #else:
    #    print("[OK] First Check")

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
                print("[OK] Checking Updates")
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
                            print("[OK] Updating the CLI")
                            os.chdir(f"{os.getcwd()}/..") 
                            print(f"Note : Just delete the folder DJ-APPSTORE in the {os.getcwd()}")
                            exit()
                        else:
                            print("[!] Updating the CLI")
                            print("Error : ", result.stderr)

                    else:
                        print("[!] Updating the CLI")
                        print("Error : ", result.stderr)

                    ###################################################
                else:
                    print("[!] Updating the CLI")
                    print("Error : Bad Request / Internet Connexion")
                    exit()
            else:
                print("[OK] Checking Updates")
                
        else:
            print("[!] Checking Updates")
            print("Error : Bad Request / Internet Connexion")
            exit()
    else:
        print("[!] Checking Updates")
        print("Error : Bad Request / Internet Connexion")
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
