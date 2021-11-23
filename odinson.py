#########################################################################################
# Odinson
# Scrape Guia dos Quadrinhos webpages to collect original Marvel editions
# from old magazines published in Brazil
# Author: Rodrigo Nobrega
# 20211114 / 20211123
#########################################################################################
__title__ = "Odinson"
__version__ = "0.10"


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
        self.editionurl = self.seteditionurl()
        self.pagesoup = self.getsoup()
        self.editionslist = self.seteditionslist()
        self.editionnumber = self.geteditionnumber()
        self.editioncontents = self.geteditioncontents()
        self.editionstorylist = self.getallstories()
        self.allstories = []
    
    def seteditionurl(self):
        """Take the edition part of the whole URL"""
        edu = self.initialurl.replace(URLROOT, "")
        print(" Obtained Edition URL")
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
        print(" -------------------------------------------")
        ed = self.pagesoup.find(id="nome_titulo_lb")
        edl = ed.contents
        edl = [f"{i}".strip() for i in edl]
        edl = [i.split(">")[1] if ">" in i else i for i in edl]
        edl = [i.split("<")[0] if "<" in i else i for i in edl]
        edl = [i.replace("n°", "").strip() for i in edl if i != '']
        singleed = [edl[0], edl[-1]]
        print(f"  {singleed[0]} #{singleed[1]}")
        print(" -------------------------------------------")
        return singleed
    
    def geteditioncontents(self):
        """Retrieve the text contents of the edition"""
        results = self.pagesoup.find(id="texto_pag_detalhe")
        results = results.text
        return results
    
    def getallstories(self):
        """Return a list of all stories of an edition"""
        # page section
        results = self.pagesoup.find(id="texto_pag_detalhe")
        # individual stories
        stories = results.find_all("div", class_="historia")
        stories = [i.text for i in stories]
        return stories


# Controller function
def odinsoncontrol(firsteditionurl):
    """Function to drive the workflow"""
    # 1. Take the first edition and set the edition custom URL
    od = Odinson(firsteditionurl)
    od.editionurl = od.seteditionurl()
    # 2. Get the edition's Soup
    od.pagesoup = od.getsoup()
    # 3. Set the list of ALL editions URLs to iterate
    alleditionslist = od.seteditionslist()
    alleditionslist.insert(0, od.editionurl)
    # 4. For each EDITION
    for edurl in alleditionslist:
        editionodinson = Odinson(f"{URLROOT}{edurl}")
        editionodinson.pagesoup = editionodinson.getsoup()
        #  4.1. Get the edition title & number
        editiontitlenumber = 
    #  4.2. Get the edition whole text contents
    #  4.3. Get the edition's stories list
    # 5. For each STORY
    #  5.1. Get the story details for each story
    #  5.2. Retrieve main character
    #  5.3. Retrieve original title
    #  5.4. Retrieve original number
    #  5.5. Retrieve original year
    # 6. Save record to CSV
    pass
    

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
#     print(f" DEBUG: Edition URL: {od.editionurl}")
    # Get page soup
#     od.pagesoup = od.getsoup()
#     print(od.pagesoup)
    # Define all Editions list
#     od.editionslist = od.seteditionslist()
#     [print(i) for i in od.editionslist]
    # Define Edition name and number
#     od.editionnumber = od.geteditionnumber()
    #
    # footer --------------------------------------------------------------
    print(f'\n{34 * "="}  OK  {35 * "="}\n')


# main, calling main loop
if __name__ == '__main__':
#     main()
    test()
