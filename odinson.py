#########################################################################################
# Odinson
# Scrape Guia dos Quadrinhos webpages to collect original Marvel editions
# from old magazines published in Brazil
# Author: Rodrigo Nobrega
# 20211114 20211121
#########################################################################################
__title__ = "Odinson"
__version__ = 0.08


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
        self.editionurl = ""
        self.pagesoup = None
        self.editionslist = []
        self.editionnumber = []
    
    def seteditionurl(self):
        """Take the edition part of the whole URL"""
        print(" Defining Edition URL")
        edu = self.initialurl.replace(URLROOT, "")
        return edu
    
    def getsoup(self):
        """Retrieve the Beautiful Soup version of a page"""
        URL = URLROOT + self.editionurl
        print(" Retrieving page contents")
        page = requests.get(URL)
        thesoup = BeautifulSoup(page.content, "html.parser")
        return thesoup
           
    def seteditionslist(self):
        """Create a list of all editions URLs"""
        outlist = []
        print(" Retrieving all Editions URL list")
        nav = self.pagesoup.find(id="d0")
        for link in nav.find_all("a"):
            outlist.append(f'{link["href"].replace("../", "")}')
        return outlist
    
    def geteditionnumber(self):
        """Takes the edition title and number"""
        ed = self.pagesoup.find(id="nome_titulo_lb")
        edl = ed.contents
        edl = [f"{i}".strip() for i in edl]
        edl = [i.split(">")[1] if ">" in i else i for i in edl]
        edl = [i.split("<")[0] if "<" in i else i for i in edl]
        edl = [i.replace("n°", "").strip() for i in edl if i != '']
        singleed = [edl[0], edl[-1]]
        return singleed      
    
    
        

# main loop
def main():
    # header --------------------------------------------------------------
    print(f'\n{75 * "="}')
    print(f'{f"{__title__} v.{__version__}":^75}')
    print(f'{75 * "="}\n')
    # ---------------------------------------------------------------------
    # main code goes here
    #
    # footer --------------------------------------------------------------
    print(f'\n{34 * "="}  OK  {35 * "="}\n')


# test loop
def test():
    # header --------------------------------------------------------------
    print(f'\n{75 * "="}')
    print(f'{"TEST":^75}')
    print(f'{f"{__title__} v.{__version__}":^75}')
    print(f'{75 * "="}\n')
    # ---------------------------------------------------------------------
    od = Odinson("http://www.guiadosquadrinhos.com/edicao/herois-da-tv-2-serie-n-1/htv0302/6274")
    # Set Edition URL
    od.editionurl = od.seteditionurl()
#     print(f" Edition URL: {od.editionurl}")
    # Get page soup
    od.pagesoup = od.getsoup()
#     print(od.pagesoup)
    # Define all Editions list
    od.editionslist = od.seteditionslist()
#     [print(i) for i in od.editionslist]
    # Define Edition name and number
    od.editionnumber = od.geteditionnumber()
    print(f" Edition Number: {od.editionnumber}")
    #
    # footer --------------------------------------------------------------
    print(f'\n{34 * "="}  OK  {35 * "="}\n')


# main, calling main loop
if __name__ == '__main__':
#     main()
    test()
