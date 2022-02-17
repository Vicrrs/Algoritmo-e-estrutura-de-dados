import urllib
import urllib.request


try:
    site = urllib.request.urlopen(#Link)
except urllib.error.URLError:
    print("Deu erro!")
else:
    print("Tudo OK!")
    print(site.read())