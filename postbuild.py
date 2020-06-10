import pathlib
import json

from pathlib import Path

dest   = Path.home() / "/Documents/CnCRemastered/Mods/"
source = Path.home() / "<POINT TO CnC_Remastered_Collection git repo (relative from user directory)>"

#Red Alert Mod Handling
ccmod_path= source / "REDALERT" / "ccmod.json"

if Path(ccmod_path).is_file():
    print("Found Red Alert ccmod, creating Red Alert mod.")
    with ccmod_path.open() as file:
        modname = (json.load(file))['name']


    print ("Creating Mod folder: " + modname)
    modfolder = dest / "Red_Alert" / modname
    try:
        modfolder.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print("Mod folder already exists, overwriting.")
    else:
        print("Mod folder created")
        
   
    Path.joinpath(modfolder, "ccmod.json").write_bytes(ccmod_path.read_bytes())
    print("ccmod.json written")

    
    print("Checking if a .dll has been built.")
    dll_path = source / "bin" / "Win32" / "RedAlert.dll"
    
    if Path(dll_path).is_file():
        print ("Compiled dll found, creating Data folder");
        data_folder = modfolder / "Data";
        try:
            data_folder.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print("Data folder already exists, overwriting.")
        else:
            print("Data folder created")
        
        Path.joinpath(data_folder, "RedAlert.dll").write_bytes(dll_path.read_bytes())
        print("dll copied.")
    else:
        print("No compiled dll found")


    print("Checking for .ini files")
    inis = list(Path(source / "REDALERT").glob("*.ini"))
    
    if inis:
        print (".ini files found, creating CCDATA folder and copying them");
        ccdata_folder = modfolder / "CCDATA";
        try:
            ccdata_folder.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print("CCDATA folder already exists, overwriting.")
        else:
            print("CCDATA folder created")

        for ini in inis:
            Path.joinpath(ccdata_folder, ini.name).write_bytes(ini.read_bytes())
        print(".inis copied.")
    else:
        print("No .inis found")
    
      
else: 
    print("no ccmod.json found at <" + str(ccmod_path) + ">. Not creating a Red Alert Mod.")
