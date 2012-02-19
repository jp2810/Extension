#CATEGORIZATION PROGRAM: searches occurrences for keywords in four domains. Articles from freebase are saved in database.
#Mongodb regular expressions are used which eliminates need searching using NLTK. It reduces need for parsing every article repeately
#DEPENDACY : mongodb
#
#


from pymongo import Connection
import re
from imdb import IMDb

i = 0
#connecting with mongodb
connection = Connection()
db = connection.dataset_db
	       	

class categorization:
	
        #class cha constructor
	def __init__(self):
		print "hello"
	

	def init(self):
		ismovie = 0#function to initialise the variables

	def get_category(self,kw):
		category = []		
		count_film = 0
		count_books = 0
		count_location = 0
		count_people = 0
		threshold = 0
		ismovie = 0
		self.init()
		count_film += db.film_data.find({"name": {"$regex":kw, "$options":"i"}}).count()
		print "\nname count = %d"%count_film
		if(db.film_data.find({"name": {"$regex":kw, "$options":"i"}}).count()):
			ismovie = 1#if count is more than 1
			self.search_film(kw)
		count_film += db.film_data.find({"article": {"$regex":kw,"$options":"i"}}).count()
	
		count_books += db.book_data.find({"name": {"$regex":kw, "$options":"i"}}).count()
		count_books += db.book_data.find({"article": {"$regex":kw,"$options":"i"}}).count()
	
		count_location += db.location_data.find({"name": {"$regex":kw, "$options":"i"}}).count()
		count_location += db.location_data.find({"article": {"$regex":kw,"$options":"i"}}).count()

		count_people += db.people_data.find({"name": {"$regex":kw, "$options":"i"}}).count()
		count_people += db.people_data.find({"article": {"$regex":kw,"$options":"i"}}).count()
	
		threshold = (count_film+count_books+count_location+count_people)/4
	
		
		print "\n\n" + kw + "\nfilm:"+ str(count_film)+"\nbook:"+str(count_books)+"\npeople:"+str(count_people)+"\nlocation:"+str(count_location)

		print "CATEGORY:" 
		if (threshold< count_film):
			print " film "
			category.append("film")
			#search_film()
		if (threshold< count_books):
			category.append("books")
			print " books "
	       	if (threshold< count_people):
			category.append("people")
			print " people "
		if (threshold< count_location):
			category.append("location")
			print " location "
			

		return category	
	
	def search_film(self, kw):
		
		#make connection
		ia = IMDb()
		movie_list = ia.search_movie(kw)
		movie = movie_list[0]
		movie_id = ia.get_movie(movie.movieID)
		plot = movie_id.get("plot",[''])[0] 
		plot = plot.split('::')[0]
		print plot




		






