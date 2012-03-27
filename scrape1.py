from BeautifulSoup import BeautifulSoup
import AlchemyAPI


def scrapePage(url):
    # Extract page text from a web URL (ignoring navigation links, ads, etc.).
    try:

        alchemyObj = AlchemyAPI.AlchemyAPI()    # Create an AlchemyAPI object.
        alchemyObj.loadAPIKey("api_key.txt")    # Load the API key from disk.

        result = alchemyObj.URLGetText(url)
        
        soup = BeautifulSoup(result)
        raw = soup('text')
        raw = [text.text for text in raw]
        
        rawstr = ' '.join(raw)

    except Exception,err:
        webpage = urllib2.urlopen(url).read()
        para= re.compile('<p>(.*)</p>') #collect data in p tags and store in para object
        raw = re.findall(para , webpage)
        raw = ' '.join(raw) 
        rawstr = nltk.clean_html(raw)
        print "ERROR IS %s"%(str(err))
    
    return rawstr
