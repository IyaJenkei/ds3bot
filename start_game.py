import subprocess
import time
import direct_inputs
import ctypes

path_to_game = 'C:\Program Files (x86)\Steam\steamapps\common\DARK SOULS III\Game\DarkSoulsIII.exe'

def open_civ(path_to_game):
    return subprocess.Popen([path_to_game], shell=True)

def close_civ(path_to_game):
    open_civ(path_to_game).terminate()

def press_key_once(key):
    direct_inputs.PressKey(key)
    time.sleep(2)
    direct_inputs.ReleaseKey(key)

# def start_game():
#     time.sleep(20)
#     print('ues')
#     press_key_once(direct_inputs.keys['INTR'])
#     press_key_once(direct_inputs.keys['INTR'])
#     press_key_once(direct_inputs.keys['INTR'])
#     time.sleep(15)
#     print('yes')
#     press_key_once(direct_inputs.keys['INTR'])
#     time.sleep(1)
#     press_key_once(direct_inputs.keys['INTR'])
#     time.sleep(1)
#     press_key_once(direct_inputs.keys['INTR'])
#
#
# open_civ(path_to_game)
# start_game()

time.sleep(10)
for element in direct_inputs.keys:
    press_key_once(direct_inputs.keys[element])