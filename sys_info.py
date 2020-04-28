#_autor_ @leoDev
#_verison_ 0.0.1
#2020
import platform, sys, os, socket, json, re, uuid
# ARCHITECTURE

def pc_info():
    _pc = {
        'architecture' : platform.machine(),
        'processor' : platform.processor(),
        'hostname' : socket.gethostname(),
        'platform' : platform.platform(),
        'sys_vers' : platform.version(),
        'release' : platform.release(),
        'os' : platform.system()
    }
    
    return json.dumps(_pc)