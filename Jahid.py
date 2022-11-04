import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')



import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from Jahidul import __xarGyc

        __xarGyc()



elif bit == "32bit":

        print("   your device is 32 bit ")

        print("   32 bit will update soon")

        exit()
