#########################################################################################
# Odinson
# Scrape Guia dos Quadrinhos webpages to collect original Marvel editions
# from old magazines published in Brazil
# Author: Rodrigo Nobrega
# 20211114 20211116
#########################################################################################
__version__ = 0.07


# import libraries
import requests
from bs4 import BeautifulSoup


# global variables
URLROOT = "http://www.guiadosquadrinhos.com/"


# Odinson Class
class Odinson(object):
    """
    Class to find original Marvel editions from old magazines published in Brazil
    """
    def __init__(self, initialurl):
        self.initialurl = initialurl
        self.editionurl = self.geteditionurl()
    
    def geteditionurl(self):
        edu = self.initialurl.replace(URLROOT, "")
        return edu
        

# main loop
def main():
    print('\n===========================================================================')
    print('                                  Odinson')
    print('===========================================================================\n')
    od = Odinson("http://www.guiadosquadrinhos.com/edicao/herois-da-tv-2-serie-n-1/htv0302/6274")
    print(od.editionurl)
    print('\n================================= THE END =================================\n')


# main, calling main loop
if __name__ == '__main__':
    main()
