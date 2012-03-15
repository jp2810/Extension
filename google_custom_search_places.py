#API_key='AIzaSyBdGY-23XisY8ZwOuvdnseGBbFIndd3oYs'
#engine_id='008016317575559464792:m0_rq_ajn8g'
import urllib2
import json
import pprint


class search:
	def search_places(self,search_query):
		#search_query = ' '.join(kw)
		print "search query:" + search_query
		search_query=search_query.replace(" ","+")
		print "search query:" + search_query
		#search_query="pune"
		#data = urllib2.urlopen('https://www.googleapis.com/customsearch/v1?key=AIzaSyBdGY-23XisY8ZwOuvdnseGBbFIndd3oYs&cx=008016317575559464792:luzdbvjplgm&q='+search_query+'&highrange=1&start=1')
		data = urllib2.urlopen('https://www.googleapis.com/customsearch/v1?key=AIzaSyBdGY-23XisY8ZwOuvdnseGBbFIndd3oYs&cx=008016317575559464792:luzdbvjplgm&q='+search_query+'&highrange=1&start=1')
		data = json.load(data)
#pprint.PrettyPrinter(indent=4).pprint(data['items'][0])
		try:
			for item in data['items']:
				print "\n\n"
				print item['title']
				print item['snippet']
				print item['link']
		except Exception:
			pass
		return data


#obj = search()
#obj.search_places("pune")
