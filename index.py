from rblxopencloud import *
import dotenv
import time
import os

file_path = input("File path: ")

if dotenv.get_variable(".env","RBLX_USER_ID") != 1234 and dotenv.get_variable(".env","RBLX_API_KEY") != "replaceable":
    creator = User(
       dotenv.get_variable(".env","RBLX_USER_ID"),dotenv.get_variable(".env","RBLX_API_KEY")
    )

    with open(file_path, 'rb') as file:
        creator.upload_asset(file, AssetType.Decal, "Asset Name", "This is the description")
        print("You can check your inventory or creator dashboard at your decals, you can rename them however you want. =)")
else:
    api_key = input("Your Api key: ")
    user_id = input("Your User Id: ")
    dotenv.set_variable(".env","RBLX_USER_ID",user_id)
    dotenv.set_variable(".env","RBLX_API_KEY",api_key)
    print("The program needs to restart, restarting in 5 secs")
    time.sleep(5)
    os.system("python index.py")
    exit(0)
    










