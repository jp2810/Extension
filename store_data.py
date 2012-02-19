#fetch data from freebase and store in mongodb
#dependancy: Mongodb, freebase
from pymongo import Connection
import freebase

lim = 200

connection = Connection()
db = connection.dataset_db
cursor1 = None


query_film = [{
         "type":"/film/film",
         #"film/actor":[],
          #"director":[],
        "/common/topic/article" : {"id" : None, "optional" : True, "limit" : 1},
         "name":[], 
         "limit":lim
    }]
results_film = freebase.mqlread(query_film)

query_book = [{
         "type":"/book/book",
        "/common/topic/article" : {"id" : None, "optional" : True, "limit" : 1},
         "name":[], 
         "limit":lim
    }]
results_book = freebase.mqlread(query_book)

query_people = [{
         "type":"/people/person",
        "/common/topic/article" : {"id" : None, "optional" : True, "limit" : 1},
         "name":[],  
         "limit":lim
    }]

#this query returns the results 
results_people = freebase.mqlread(query_people)

query_location = [{
         "type":"/location/location",
        "/common/topic/article" : {"id" : None, "optional" : True, "limit" : 1},
         "name":[], 
         "limit":lim
    }]
results_location = freebase.mqlread(query_location)


###### removing previous contents to eliminate repetition
db.film_data.remove()
db.book_data.remove()
db.people_data.remove()
db.location_data.remove()


for r in results_film:
    if r["/common/topic/article"]:
        article_id = r["/common/topic/article"]["id"]
        article = freebase.blurb(article_id,5000)
    #article = freebase.raw(article_id)
        
    else:
        article = ""
    j = {"name":r["name"],"article":article}
    #print j
    db.film_data.save(j)

print "\n\nfilm database contents:"
for cursor1 in db.film_data.find():
    print cursor1.get("name","not existing") 
    print cursor1.get("article","not existing") 

for r in results_book:
    if r["/common/topic/article"]:
        article_id = r["/common/topic/article"]["id"]
        article = freebase.blurb(article_id,5000)
    #article = freebase.raw(article_id)
        
    else:
        article = ""
    j = {"name":r["name"],"article":article}
    #print j
    db.book_data.save(j)

print "\n\nbook database contents:"
for cursor1 in db.book_data.find():
    print cursor1.get("name","not existing") 
    print cursor1.get("article","not existing") 

for r in results_people:
    if r["/common/topic/article"]:
        article_id = r["/common/topic/article"]["id"]
        article = freebase.blurb(article_id,5000)
    #article = freebase.raw(article_id)
        
    else:
        article = ""
    j = {"name":r["name"],"article":article}
    #print j
    db.people_data.save(j)

print "\n\npeople database contents:"
for cursor1 in db.people_data.find():
    print cursor1.get("name","not existing") 
    print cursor1.get("article","not existing") 


for r in results_location:
    if r["/common/topic/article"]:
        article_id = r["/common/topic/article"]["id"]
        article = freebase.blurb(article_id,5000)
    #article = freebase.raw(article_id)
        
    else:
        article = ""
    j = {"name":r["name"],"article":article}
    #print j
    db.location_data.save(j)

print "\n\n location database contents:"
for cursor1 in db.location_data.find():
    print cursor1.get("name","not existing") 
    print cursor1.get("article","not existing") 






