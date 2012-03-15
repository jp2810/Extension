import youtube 
import google_custom_search_books
import google_custom_search_people
import google_custom_search_places
import freebase,re

from pymongo import Connection
import re
#from imdb import IMDb

#connecting with mongodb
connection = Connection()
db = connection.dataset_db_spec


film_count = 0
books_count = 0
location_count = 0
people_count = 0
#category = []


class categorization: 


    def __init__(self):
        print "hello"

    def get_category(self,kw):
        category = []		
	count_film = 0
	count_books = 0
	count_location = 0
	count_people = 0
	threshold = 0
	ismovie = 0
	self.__init__()
	#kw = ' '.join(kwd)
	count_film += db.film_data.find({"name": {"$regex":kw, "$options":"i"}}).count()
        count_film += db.film_data.find({"starring": {"$regex":kw, "$options":"i"}}).count()
        count_film += db.film_data.find({"directed_by": {"$regex":kw, "$options":"i"}}).count()
        count_film += db.film_data.find({"produced_by": {"$regex":kw, "$options":"i"}}).count()
        count_film += db.film_data.find({"story_by": {"$regex":kw, "$options":"i"}}).count()
        count_film += db.film_data.find({"written_by": {"$regex":kw, "$options":"i"}}).count()
        count_film += db.film_data.find({"music": {"$regex":kw, "$options":"i"}}).count()
        count_film += db.film_data.find({"film_series": {"$regex":kw, "$options":"i"}}).count()


	#print "\nname count = %d"%count_film
	#if(db.film_data.find({"name": {"$regex":kw, "$options":"i"}}).count()):
	#	ismovie = 1#if count is more than 1
	#	self.search_film(kw)
	#count_film += db.film_data.find({"article": {"$regex":kw,"$options":"i"}}).count()
	
	count_books += db.book_data.find({"name": {"$regex":kw, "$options":"i"}}).count()
	count_books += db.book_data.find({"characters": {"$regex":kw,"$options":"i"}}).count()
	
	count_location += db.location_data.find({"name": {"$regex":kw, "$options":"i"}}).count()
	count_location += db.location_data.find({"coterminous_with": {"$regex":kw,"$options":"i"}}).count()
        count_location += db.location_data.find({"containedby": {"$regex":kw,"$options":"i"}}).count()
        count_location += db.location_data.find({"contains": {"$regex":kw,"$options":"i"}}).count()

	count_people += db.people_data.find({"name": {"$regex":kw, "$options":"i"}}).count()
	#count_people += db.people_data.find({"article": {"$regex":kw,"$options":"i"}}).count()
	
	#threshold = (count_film+count_books+count_location+count_people)/4
	
		
	print "\n\n" + kw + "\nfilm:"+ str(count_film)+"\nbook:"+str(count_books)+"\npeople:"+str(count_people)+"\nlocation:"+str(count_location)

	print "CATEGORY:" 
	if (count_film>=1):
		print " film "
		category.append("film")
			#search_film()
	if (count_books>=1):
		category.append("books")
		print " books "
        if (count_people>=1):
		category.append("people")
		print " people "
	if (count_location>=1):
		category.append("location")
		print " location "
			

	return category	




    def search_film(self,kwd):
            
        youtube_obj = youtube.youtube()
        result = youtube_obj.SearchAndPrint(kwd) 
	#print "\nRESULT for video \n:"
	#print result
        return result
	

    def search_books(self,search_query):
        print "\n\nsearch books"
        bookobj = google_custom_search_books.search()
        result = bookobj.search_books(search_query)		
        return result

		
    def search_people(self,search_query):
        print "\n\nsearch people"
        peopleobj = google_custom_search_people.search()
        result = peopleobj.search_people(search_query)		
        return result

    def search_location(self,search_query):
        print "\n\nsearch location"
        placesobj = google_custom_search_places.search()
        result = placesobj.search_places(search_query)		
        return result
	

#obj = categorization()
#obj.get_category(["steven","spielberg"])
