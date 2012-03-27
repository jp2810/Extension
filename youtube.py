import gdata.youtube
import gdata.youtube.service
from pprint import pprint
yt_service = gdata.youtube.service.YouTubeService()

yt_service.developer_key = 'AI39si5p3RrpZZlbchBxo9vrn701RTZyaeYRwKJcRywG3ORiPo46dnumoWplhNKSgKE7FS3kGMUx1fuU7e33Xrx9UOjZephCFQ'


class youtube:
	
	video_links = []
	def __init__(self):
		print "\nHELOO"
		self.video_links = []


	def SearchAndPrint(self,kwd):
		
		try:
			yt_service = gdata.youtube.service.YouTubeService()
			query = gdata.youtube.service.YouTubeVideoQuery()
			query.vq = kwd    #search query
			query.orderby = 'relevance'
			query.racy = 'exclude'
			query.max_results = '2'
			query.start_index = '1'
		#prettyprint = True 
			feed = yt_service.YouTubeQuery(query)

			print 'got feed'

			for entry in feed.entry:
		#PrintEntryDetails(entry)
			#print "\n\n entry:"
			#print entry.title
		#pprint (vars(entry.link[0]))
				self.video_links.append(entry.link[0].href)
			#print entry.link[0].href
			#print 'in print function'
			return self.video_links
		except Exception:
			print "ERROR IN YOUTUBE"



#def main():
#	obj = youtube()
#	result = obj.SearchAndPrint("klaus demon")
#	print "\nRESULt:"
#	print result


#if __name__ =="__main__":
#	main()


