from bingapi import bingapi
from global_file import getbingid
import cate_mongo_specific1
import json

global_ct = 0
return_string = ""
#doc_freq = []   ##########

def search_web(keywords,prev_results,start,end,url):    
   
    doc_freq = keywords[start:end]
        
    print "\n next keywords:::"
    for i in doc_freq:
    	print i.keyword
    
    
    if start == 0 :
         return_string ='{"final_results":['
    else:
        return_string = prev_results 
    
    i=0
    cate_obj = cate_mongo_specific1.categorization()
    #bing = bingapi.Bing(app_ID)
    bing = getbingid()
    print "\n\nMY KEYWORDS:"
    for l in doc_freq:
   
        film =" "
        books=" "
        people = " "
        location =" "

        #str1 = l.keyword
        str1 = ' '.join(l.keyword)
        print "keyword:" + str1
        keyword = str1

    	category = cate_obj.get_category(str1) #get category of keyword

    	#print category
	
        for n in l.neighbours:
            str1 = str1 + " " + n.word
        #category = "cat"
        search_query = str1
	#search_query = str1
        print "search_query::::::::" + str1
		
        #for neighbour in df.neighbours:
        #    print neighbour.word
        #    search_query = search_query + neighbour.word + " "

	
	if "film" in category:
		
		#if c is "film":
            print "\n\n in film:"
            film = cate_obj.search_film(search_query)
            print film
	elif "books" in category:
            books = cate_obj.search_books(search_query)
        elif "people" in category:
            people = cate_obj.search_people(search_query)
        elif "location" in category:
            location = cate_obj.search_location(search_query)
	
		
        else:
            pass
        
#        search_query = "sachin"
	print "do web search"
        try:
           
            res = bing.do_web_search(search_query)
            for i in res["SearchResponse"]["Web"]["Results"]: #Removing current URL
                if i["Url"]==url:
                    res["SearchResponse"]["Web"]["Results"].remove(i)
    
            dump_res = json.dumps({"keyword":keyword,"category":category,"search_res":res["SearchResponse"]["Web"]["Results"][0:5],"film":film,"books":books,"people":people,"location":location}) 
            return_string += dump_res+","
            print "web search done"
        except Exception:
            print "search not done"
            pass
        


    #print return_string
 #   import pdb;pdb.set_trace();    
    return return_string     
        
