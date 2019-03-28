#!/usr/bin/python
import json
import urllib
import time
import random
import re
from pypexels import PyPexels
import subprocess
from pixabay import Image
listsource=["pexels.com","pixabay.com"]

def pingGetTime(host):
    ping_response = subprocess.Popen(["/bin/ping", "-c1", "-w100", host], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    m=re.search(r"time=(\S+)",ping_response.splitlines()[1])
    return m[1]

def getFromPexels():
    api_key = 'useyourownapi'

    py_pexels = PyPexels(api_key=api_key)
    listback=[]
    popular_photos = py_pexels.popular(page=random.randrange(0,202,2))
    for photo in popular_photos.entries:
        landsc=photo.src["landscape"]
        if landsc is not "":
           listback.append(photo.src["landscape"])
           #print(listback)
        #else:
        #   popular_photos=popular_photos.get_next_page()
    for i in range(len(listback)):
        try:
            print(listback[i])
            opener = urllib.request.Request(listback[i])
            opener.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')
            fx = open('/home/devnull/Pictures/background/background.jpg','wb')
            fx.write(urllib.request.urlopen(opener).read())
            fx.close()
            #listback.remove(listback[i])
            time.sleep(660)
        except IndexError:
            print("List Index Out of Range")
            break
def getFromPixabay():
    api_key="useyourownapi"
    image=Image(api_key)
    listurl=[]
    ims=image.search(q='',category="nature",min_width="1366", min_height="768",page=random.randrange(1,25),safesearch="yes")
    #print(ims["hits"])
    for i in ims["hits"]:
        listurl.append(i["fullHDURL"])
    print(len(listurl))
    for i in range(len(listurl)):
        try:
            print(listurl[i])
            opener=urllib.request.Request(listurl[i])
            opener.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')
            fx = open('/home/devnull/Pictures/background/background.jpg','wb')
            fx.write(urllib.request.urlopen(opener).read())
            fx.close()
            #listurl.remove(listurl[i])
            time.sleep(660)
        except IndexError:
            print("List Index Out of Range")
            break
def main():
    if float(pingGetTime("pexels.com")) > float(pingGetTime("pixabay.com")):
       getFromPixabay()
    elif float(pingGetTime("pexels.com")) < float(pingGetTime("pixabay.com")):
       getFromPexels()
    elif float(pingGetTime("pexels.com")) == float(pingGetTime("pixabay.com")):
        getFromPixabay()
    else:
        print("All source is not resolved")
if __name__=='__main__':
    main()


