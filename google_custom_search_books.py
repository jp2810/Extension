#API_key='AIzaSyBdGY-23XisY8ZwOuvdnseGBbFIndd3oYs'
#engine_id='008016317575559464792:m0_rq_ajn8g'
import urllib2
import json
import pprint


class search:
	def search_books(self,search_query):
		search_query=search_query.replace(' ','+')
		#search_query="harry+potter"
		#search_query = ' '.join(kw)
		try:
			data = urllib2.urlopen('https://www.googleapis.com/customsearch/v1?key=AIzaSyDPc6ocjFyiddxMc_pQNxGtnDM-P8634NU&cx=016488514495467573913:wbaw7mxdja8&q='+search_query+'&highrange=1&start=1')
			data = json.load(data)
#pprint.PrettyPrinter(indent=4).pprint(data['items'][0])
                
                        for item in data['items']:
				pass
                                #print "\n\n"
                                #print item['title']
                                #print item['snippet']
                                #print item['link']
                except Exception:
                        pass
		return data	
		

