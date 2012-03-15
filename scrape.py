from BeautifulSoup import BeautifulSoup
import AlchemyAPI

alchemyObj = AlchemyAPI.AlchemyAPI()    # Create an AlchemyAPI object.
alchemyObj.loadAPIKey("api_key.txt")    # Load the API key from disk.



def scrapePage(url):
    # Extract page text from a web URL (ignoring navigation links, ads, etc.).
    result = alchemyObj.URLGetText(url)
        
    soup = BeautifulSoup(result)
    raw = soup('text')
    raw = [text.text for text in raw]
        
    rawstr = ' '.join(raw)
    return rawstr
