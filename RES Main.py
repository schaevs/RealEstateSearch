__author__ = 'alexanderschaevitz'

import urllib
import urllib.request
import re

def main():

    url = ("http://norcalmls.rapmls.com/scripts/mgrqispi.dll?APPNAME=Bareis&PRGNAME=MLSLogin&ARGUMENT=m2yr6j10eFDGrzaxFb%2FJ2fsiiWLhDAVxfZsscUqnRY0%3D&KeyRid=1&Include_Search_Criteria=&CurrentSID=143949614&MLS_Origin=BARI")
    htmlfile = urllib.request.urlopen(url)
    htmltext = htmlfile.read().decode('utf-8')


    print(url)
    print (htmltext)

    regex = '<td nowrap width="11%"  class="LargerLabel"  >(.+?)</td>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)

    print(price)

if __name__ == "__main__":
    main()