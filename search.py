from bingapi import bingapi
from global_file import getbingid
import cate_mongo_specific1
import json

global_ct = 0
return_string = ""

def search_web(keywords,prev_results,start,end):    
   
    doc_freq = keywords[start:end]
        
    print "\nkeywords:::"
    print doc_freq
    
    
    if start == 0 :
         return_string ='{"final_results":['
    else:
        return_string = prev_results 
    
    i=0
    cate_obj = cate_mongo_specific1.categorization()
    #bing = bingapi.Bing(app_ID)
    bing = getbingid()
    print "\n\nKEYWORDS:"
    for l in doc_freq:
   
        film =" "
        books=" "
        people = " "
        location =" "


        str1 = ' '.join(l)
        print "keyword:" + str1

    	#category = cate_obj.get_category(str1) #get category of keyword
    	#print category
	
        #for n in l.neighbours:
        #    str1 = str1 + " " + n.word
        category = "cat"
        search_query = str1
	#search_query = str1
        #print "search_query::::::::" + str1

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
        
            
        res = bing.do_web_search(search_query)
        dump_res = json.dumps({"keyword":search_query,"category":category,"search_res":res["SearchResponse"]["Web"]["Results"],"film":film,"books":books,"people":people,"location":location}) 
        return_string += dump_res+","


    #return_string += "]}"

        #return_string +='{"test":"dummy_res"}' #Add dummy result for comma after last result
    #return_string += "]}"

    #print return_string
    return return_string     
        
