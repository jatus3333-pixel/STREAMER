from flask_cors import CORS
from flask import *
from keyauth import *
import pymem
import sys

def send_command_to_esp(command: str):
    pipe_path = r'\\.\pipe\esp_pipe'
    try:
        with open(pipe_path, 'w') as pipe:
            pipe.write(command + '\n')
    except FileNotFoundError:
        print("Pipe not found. Make sure the C# ESP app is running.")
    except Exception as e:
        print(f"Pipe error: {e}")

def aimbotvisible():
    send_command_to_esp("aimbotvisible")
    return "Aimbot Initialized Successfully."

def aimbotvisibleoff():
    send_command_to_esp("aimbotvisibleoff")
    return "Aimbot Turned off."
    
def silentaim():
    send_command_to_esp("silentaim")

def silentaimoff():
    send_command_to_esp("silentaimoff")

def upplayer():
    send_command_to_esp("upplayer")
    return "Up Player enabled."
    
def upplayeroff():
    send_command_to_esp("upplayeroff")
    return "Up Player disabled."

def enablefunction():
    send_command_to_esp("enablefunction")

def enablefunctionoff():
    send_command_to_esp("enablefunctionoff")

def aimbotrage():
    send_command_to_esp("aimbotrage")
    
def aimbotrageoff():
    send_command_to_esp("aimbotrageoff")

def aimbothex():
    send_command_to_esp("aimbothex")

def aimbothexoff():
    send_command_to_esp("aimbothexoff")

def noreload():
    send_command_to_esp("noreload")

def noreloadoff():
    send_command_to_esp("noreloadoff")

def streamermode():
    send_command_to_esp("streammode")
    return "Streamer mode enabled."

def streamermodeoff():
    send_command_to_esp("streammodeoff")
    return "Streamer mode disabled."

def drawfov():
    send_command_to_esp("drawfov")
    return "Fov Drawn on Screen."

def drawfovoff():
    send_command_to_esp("drawfovoff")
    return "Fov Drawn off from Screen."

def on_fov_change(value):
    send_command_to_esp(f"aimfov:{value:.1f}")

def set_silentaim_mode(mode_index):
    send_command_to_esp(f"silentaim_mode:{mode_index}")
    return f"Silent Aim mode set to: {mode_index}"

def espline():
    send_command_to_esp("espline")
    return "Esp line On."

def esplineoff():
    send_command_to_esp("esplineoff")
    return "Esp line Off."

def espboxon():
    send_command_to_esp("espboxon")
    return "Esp Box On."

def espboxoff():
    send_command_to_esp("espboxoff")
    return "Esp Box Off."

def espname():
    send_command_to_esp("espname")
    return "Esp Name On."

def espnameoff():
    send_command_to_esp("espnameoff")
    return "Esp Name Off."

def esphealth():
    send_command_to_esp("esphealth")
    return "Esp Health On."

def esphealthoff():
    send_command_to_esp("esphealthoff")
    return "Esp Health Off."

def espskeleton():
    send_command_to_esp("espskeleton")
    return "Esp Skeleton On."

def espskeletonoff():
    send_command_to_esp("espskeletonoff")
    return "Esp Skeleton Off."

def espaimtrack():
    send_command_to_esp("espaimtrack")
    return "Esp Aim Track On."

def espaimtrackoff():
    send_command_to_esp("espaimtrackoff")
    return "Esp Aim Track Off."

def norecoil():
    send_command_to_esp("norecoil")
    return "Recoil mode set to 0."

def norecoiloff():
    send_command_to_esp("norecoiloff")
    return "Recoil mode set to normal."

def telekil():
    send_command_to_esp("telekil")
    return "Tele Kill enabled."

def telekiloff():
    send_command_to_esp("telekiloff")
    return "Tele Kill disabled."

def ignoreknocked():
    send_command_to_esp("ignoreknocked")
    return "ignoreknocked enabled."

def ignoreknockedoff():
    send_command_to_esp("ignoreknockedoff")
    return "ignoreknocked disabled"

def speed():
    send_command_to_esp("speed")
    return "SPEED ENABLED"

def speedoff():
    send_command_to_esp("speedoff")
    return "SPEED DISABLED"
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def find_dll(name):
    locations = [
        resource_path(name),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), name),
        os.path.join(os.getcwd(), name),
        os.path.join(os.getcwd(), 'dlls', name),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dlls', name),
    ]
    for loc in locations:
        if os.path.exists(loc):
            return loc
    return None
def inject_dll_from_path(process, dll_path):
    try:
        if not os.path.exists(dll_path):
            raise FileNotFoundError(f"DLL file not found: {dll_path}")
        dll_path_bytes = bytes(dll_path.encode('UTF-8'))
        pymem.process.inject_dll(process.process_handle, dll_path_bytes)
        print(f"{dll_path} Injected Successfully!")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"Injection error: {e}")
def chams():        
    try:
                process_name = "HD-Player.exe"
                process = pymem.Pymem(process_name)
                jatin_path  = find_dll('jatin dll.dll')
                print(f"[DEBUG] jatin dll.dll -> {jatin_path}")
    except:
               if not jatin_path:
                print("Error: jatin dll.dll not found in any location")
                return    
    inject_dll_from_path(process, jatin_path)
    print("Injection completed successfully.")
    send_command_to_esp("chams")
    return "CHAMS ENABLED"

