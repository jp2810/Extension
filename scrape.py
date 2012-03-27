from BeautifulSoup import BeautifulSoup
import AlchemyAPI
import sys
import re,urllib2,nltk
alchemyObj = AlchemyAPI.AlchemyAPI()    # Create an AlchemyAPI object.
alchemyObj.loadAPIKey("api_key.txt")    # Load the API key from disk.



def scrapePage(url):
    # Extract page text from a web URL (ignoring navigation links, ads, etc.).
    try:
        print "URL: "+ url
        #url=url.replace('(','%28')
        #url=url.replace(')','%29')
        #print "New URL:"+url
        result = alchemyObj.URLGetText(url)
        
        soup = BeautifulSoup(result)
        raw = soup('text')
        raw = [text.text for text in raw]
        
        rawstr = ' '.join(raw)
        
    except Exception:
        try:
            print "\n\nscraping using regex"
            webpage = urllib2.urlopen(url).read()
    #webpage = str(webpage)
            para= re.compile('<p>(.*)</p>') #collect data in p tags and store in para object
            raw = re.findall(para , webpage)
            rawstr = ' '.join(raw) 
            clean_raw = nltk.clean_html(rawstr)
            rawstr=clean_raw
        except Exception:
            rawstr = "Web page could not be scraped..."


    print rawstr
    return rawstr



  
#url = sys.argv[1]
    
#SCRAPE
#print "URL:"+url
#scrapePage(url)
