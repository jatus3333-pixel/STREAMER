import os
import sys
import shutil
import pymem
import time

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
        print(f"Failed to inject {dll_path}: {e}")

def streamesp():
    process_name = "HD-Player.exe"
    try:
        process = pymem.Pymem(process_name)

        cimgui_path = find_dll('cimgui.dll')
        aotbst_path = find_dll('AotBst.dll')
        client_path = find_dll('Client.dll')
       

        print(f"[DEBUG] cimgui.dll -> {cimgui_path}")
        print(f"[DEBUG] AotBst.dll -> {aotbst_path}")
        print(f"[DEBUG] Client.dll -> {client_path}")
        
        if not cimgui_path:
            print("Error: cimgui.dll not found in any location")
            return
        if not aotbst_path:
            print("Error: AotBst.dll not found in any location")
            return
        if not client_path:
            print("Error: Client.dll not found in any location")
            return
        
        
          

        win_temp = os.environ.get('SystemRoot', 'C:\\Windows') + '\\Temp'
        client_dll_temp_path = os.path.join(win_temp, "Client.dll")
        try:
            if os.path.exists(client_dll_temp_path):
                os.remove(client_dll_temp_path)
            shutil.copy2(client_path, client_dll_temp_path)
            print(f"Copied Client.dll to {client_dll_temp_path}")
        except Exception as e:
            print(f"Error copying Client.dll to temp: {e}")
            return

        inject_dll_from_path(process, cimgui_path)
        time.sleep(1)
        inject_dll_from_path(process, aotbst_path)
        time.sleep(0.5)
        inject_dll_from_path(process, client_dll_temp_path)
        
        print("Injection completed successfully.")

    except pymem.exception.ProcessNotFound:
        print("Emulator not found.")
    except Exception as e:
        print(f"Error: {e}")
