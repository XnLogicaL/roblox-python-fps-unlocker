# Made by CE0_OfTrolling/XnLogicaL
# MIT License

import os
import warnings

# configuration
target_fps = 144
roblox_path = r"C:\"
# path to roblox, should look something like "C:\Users\...\AppData\Local\Roblox\Versions\version-f2b5c592c03b4183"

# do not edit past this line
folder_path = roblox_path + "\ClientSettings"
json_path = folder_path + "\ClientAppSettings.json"

def main():
    if os.path.exists(json_path):
        warnings.warn("already running!")
        return

    if (os.path.exists(folder_path)) == False:
        os.mkdir(folder_path)
    
    with open(json_path, "w") as file:
        file.write('{"DFIntTaskSchedulerTargetFps": %s}' %str(target_fps))
        file.close()
        
    warnings.warn("success!")
        
if __name__ == "__main__":
    main()
