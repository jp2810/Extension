import youtube 
import google_custom_search_books
import google_custom_search_people
import google_custom_search_places
import freebase,re
#kwd = "beautiful mind"

film_count = 0
books_count = 0
location_count = 0
people_count = 0
#category = []

class categorization: 


    def __init__(self):
        print "hello"

    def get_category(self,kwd):

	category = ""
	#FILM

	query1 ={
	    "type" : "/film/film",
	    "name~=" : "*"+kwd+"*",
	     "return":"count"
	 }
	result1 = freebase.mqlread(query1)

	#FILM ACTOR
	query2 ={
	    "type" : "/film/actor",
	   "name~=" : "*"+kwd+"$",
	   "return":"count" 
	}
	result2 = freebase.mqlread(query2)

	#DIRECTOR
	query3 ={
	   "type" : "/film/director",
	   "name~=" : "*"+kwd+"$",
	   "return":"count" 
	}
	result3 = freebase.mqlread(query3)

	#CHARACTER
	query4 ={
	    "type" : "/film/character",
	   "name~=" : "*"+kwd+"$",
	   "return":"count" 
	}
	result4 = freebase.mqlread(query4)

	#SERIES
	query5 ={
	    "type" : "/film/series",
	   "name~=" : "*"+kwd+"$",
	   "return":"count"
	}
	result5 = freebase.mqlread(query5)

	#PRODUCER
	query6 ={

	   "type" : "/film/producer",
	   "name~=" : "*"+kwd+"$",
	   "return":"count"
	 }
	result6 = freebase.mqlread(query6)

	#WRITER
	query7 ={

	   "type" : "/film/writer",
	   "name~=" : "*"+kwd+"$",
	   "return":"count"
	}
	result7 = freebase.mqlread(query7)

	film_count = result1 + result2 + result3 + result4 + result5 + result6 + result7
	#import pdb;pdb.set_trace();
	#########################################################################################

	#BOOK
	query8 ={
	    "type" : "/book/book",
	  "name~=" : "*"+kwd+"*",
	  "return":"count"
	 }
	#result8 = freebase.mqlread(query8)

	query9 ={
	    "type" : "/book/short_story",
	  "name~=" : "*"+kwd+"*",
	  "return":"count"
	 }
	#result9 = freebase.mqlread(query9)

	query10 ={
	    "type" : "/book/book_character",
	  "name~=" : "*"+kwd+"*",
	  "return":"count"
	 }
	#result10 = freebase.mqlread(query10)

	#books_count = result8 +result9 + result10

	#######################PEOPLE#########################################

	query11 ={
	    "type" : "/people/person",
	  "name~=" : "*"+kwd+"*",
	  "return":"count"
	 }
	#result11 = freebase.mqlread(query11)

	#people_count = result11

	################################PLACES########################33
	query12 ={
	    "type" : "/location/country",
	  "name~=" : "*"+kwd+"*",
	  "return":"count"
	 }
	#result12 = freebase.mqlread(query12)

	query13 ={
	    "type" : "/location/location",
	  "name~=" : "*"+kwd+"*",
	  "return":"count"
	 }
	#result13 = freebase.mqlread(query13)

	query14 ={
	    "type" : "/location/region",
	  "name~=" : "*"+kwd+"*",
	  "return":"count"
	 }
	#result14 = freebase.mqlread(query14)

	query15 ={
	    "type" : "/location/us_state",
	  "name~=" : "*"+kwd+"*",
	  "return":"count"
	 }
	#result15 = freebase.mqlread(query15)

	query16 ={
	    "type" : "/location/in_city",
	  "name~=" : "*"+kwd+"*",
	  "return":"count"
	 }
#	result16 = freebase.mqlread(query16)

	query17 ={
	    "type" : "/location/in_state",
	  "name~=" : "*"+kwd+"*",
	  "return":"count"
	 }
#	result17 = freebase.mqlread(query17)

#	location_count = result12 + result13 + result14 + result15 + result16 +result17


	if film_count >= 1:
	    category="film"
	#if books_count >= 1 :
	#    category.append("books")
	#if people_count >= 1:
	 #   category.append("people")
	#if location_count >= 1 :
	 #   category.append("location")
	    

	print category
	return category


    def search_film(self,kwd):
            
        youtube_obj = youtube.youtube()
        result = youtube_obj.SearchAndPrint(kwd) 
	print "\nRESULT for video \n:"
	print result
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
        print "\n\nsearch books"
        placesobj = google_custom_search_places.search()
        result = placesobj.search_places(search_query)		
        return result
	

