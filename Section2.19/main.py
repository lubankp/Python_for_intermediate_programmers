import os
import urllib.request

data_dir = 'C:/Users/Dell/Desktop/Python/Python_dla_sredniozaawansowanych/Section2.19'

pages = [{'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
         {'name': 'nonexistent', 'url': 'http://google.com/'},
         {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}]

for page in pages:
    try:
        local_filename, header = urllib.request.urlretrieve(page["url"], filename=f"{data_dir}/{page['name']}.html")
    except:
        print("Can not find page")
        break
else:
    print("Operation successful")


