# Made by CE0_OfTrolling/XnLogicaL
# MIT License

import os
import json
from warnings import *


def make_client_settings_file_json(path, target_fps):
    with open(path, "w") as f:
        f.write('{"DFIntTaskSchedulerTargetFps": %s}' % target_fps)
        f.close()


def main():
    with open("./config.json") as f:
        cfg = json.loads(f.read())
        target_fps = cfg["target-fps"]
        roblox_path = r"%s" % cfg["roblox-path"]
        f.close()

    folder_path = roblox_path + "/ClientSettings"
    json_path = folder_path + "/ClientAppSettings.json"

    if os.path.exists(folder_path):
        if os.path.exists(json_path):
            return
        else:
            make_client_settings_file_json(json_path, target_fps)
    else:
        try:
            os.mkdir(folder_path)
            make_client_settings_file_json(json_path, target_fps)
        except Exception as e:
            warn("\n Exception while running os.mkdir: Invalid roblox path\n traceback:")


if __name__ == "__main__":
    main()
