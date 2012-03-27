from pymongo import Connection
import freebase

lim = 2000

connection = Connection()
db = connection.dataset_db_spec  ### database name
cursor1 = None


query_film = [{
         "type":"/film/film",
         "name":[],
         "starring":[],
          "directed_by":[],
          "music":[],
          "story_by":[],
          "produced_by":[],
          "written_by":[],
        #"/common/topic/article" : {"id" : None, "optional" : True, "limit" : 1},
         "film_series":[], 
         "limit":lim
    }]
results_film = freebase.mqlread(query_film)

query_book = [{
         "type":"/book/book",
        #"/common/topic/article" : {"id" : None, "optional" : True, "limit" : 1},
         "characters":[], 
         "name":[],
         #"short_story":[],
         "limit":lim
    }]
results_book = freebase.mqlread(query_book)

query_people = [{
         "type":"/people/person",
        #"/common/topic/article" : {"id" : None, "optional" : True, "limit" : 1},
         "name":[], 
         "limit":lim
    }]
results_people = freebase.mqlread(query_people)

query_location = [{
         "type":"/location/location",
        #"/common/topic/article" : {"id" : None, "optional" : True, "limit" : 1},
         "coterminous_with":[],
         "name":[],
         "containedby":[],
         "contains":[],
         #"region":[],
         #"us_state":[],
         #"in_city":[],
         #"in_state":[], 
         #"limit":lim
    }]
results_location = freebase.mqlread(query_location)


###### removing previous contents to eliminate repetition
db.film_data.remove()
db.book_data.remove()
db.people_data.remove()
db.location_data.remove()


for r in results_film:
    j = {"name":r["name"],"starring":r["starring"],"directed_by":r["directed_by"],"produced_by":r["produced_by"],"story_by":r["story_by"],"written_by":r["written_by"],"music":r["music"],"film_series":r["film_series"]}
    #print j
    db.film_data.save(j)

print "\n\nfilm database contents:"
#for cursor1 in db.film_data.find():
 #   print cursor1.get("name","not existing") 
  #  print cursor1.get("characters","not existing") 

for r in results_book:
    j = {"name":r["name"],"characters":r["characters"]}
    #print j
    db.book_data.save(j)

print "\n\nbook database contents:"
#for cursor1 in db.book_data.find():
 #   print cursor1.get("name","not existing") 
 #   print cursor1.get("article","not existing") 

for r in results_people:
    j = {"name":r["name"]}
    #print j
    db.people_data.save(j)

print "\n\npeople database contents:"
#for cursor1 in db.people_data.find():
 #   print cursor1.get("name","not existing") 
 #   print cursor1.get("article","not existing") 


for r in results_location:
    j = {"name":r["name"],"coterminous_with":r["coterminous_with"],"containedby":r["containedby"],"contains":r["contains"]}
    #print j
    db.location_data.save(j)

print "\n\n location database contents:"
#for cursor1 in db.location_data.find():
    #print cursor1.get("name","not existing") 
   # print cursor1.get("article","not existing") 






