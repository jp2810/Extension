from __future__ import division
from flask import Flask, jsonify, render_template, request,redirect, url_for
import nltk,re,pprint
import urllib2
import sys
from bingapi import bingapi
from global_file import getbingid
import json
#from cate_mongo import categorization as CT
import datetime

app = Flask(__name__)
STOPWORDS = ["The", "the", "or"]

@app.route('/')
def index():
    return render_template('popup.html')

@app.route('/tokenize',methods=['GET','POST'])
def scraping():
    print "starting time:",
    now = datetime.datetime.now()
    print datetime.time(now.hour, now.minute, now.second)
#	url = request.args.get('url', 0, type=str)
    url = request.args.get('url', 0, type=str)
    webpage = urllib2.urlopen(url).read()
    para= re.compile('<p>(.*)</p>') #collect data in p tags and store in para object
    raw = re.findall(para , webpage)
    rawstr = ' '.join(raw)
    return_string = tokenize(rawstr)
    print "finish time:",  
    now = datetime.datetime.now()
    print datetime.time(now.hour, now.minute, now.second)
    return return_string
	
	

def tokenize(rawstr):
    clean_raw = nltk.clean_html(rawstr)  						#remove html tag
    token_raw = nltk.word_tokenize(clean_raw)
       
    for word in token_raw: # iterate over word_list
       	if word in nltk.corpus.stopwords.words('english') or not word.isalnum() or word in STOPWORDS: 
           	token_raw.remove(word)
	return NP_chunks(token_raw)                #token raw is list of word from web page excluding stopword 
	
def NP_chunks(token_raw):	    
	npchunks = []	#it will store noun,adjacent noun,proper noun
	pos_tag_raw = nltk.pos_tag(token_raw)  #pos_tag_raw is 2d array of word and pos tag
	grammar = """
      		 NP: {<JJ>*<NN>}
                  }<[\.VI].*>+{
                  {<NNP>+}
                  {<NN>+}  
                """
	chunks = nltk.RegexpParser(grammar)
	chunkset = chunks.parse(pos_tag_raw)
	traverse(chunkset,npchunks)
	return get_keywords(npchunks)

def get_keywords(npchunks):
	keywords = []
	fd1 = nltk.FreqDist(npchunks)
	fd1keys = fd1.keys() 
	most_freq = fd1.max()
	len_text = len(npchunks)#finding the length of npchunks array
	for ch in npchunks: 
	    chunk_position = npchunks.index(ch)  
	    position = 0 
	    if((chunk_position < (len_text/1.5)) and (fd1[ch] >= (fd1[most_freq]/3))):
	    	for (index,kw) in enumerate(keywords):
	           	if fd1[kw] <= fd1[ch]:
	        		position = index
		    		break
	       	keywords.insert(position,ch)
        
	keywords = [ keywords[i] for i,x in enumerate(keywords) if x not in keywords[i+1:]] 
	print "freaquency distribution in web page :"
	for kw in keywords: 
		print "%s:%d" %(kw,fd1[kw])
	return search_web(keywords)    
	 
def search_web(keywords):    
    print "\n\nKEYWORDS:"
    print keywords
   
    return_string ='{"final_results":['
    i=0
    #bing = bingapi.Bing(app_ID)
    bing = getbingid()
    #Getting Search results for each keywords and this loop builds json object. structure final_results:[array whr each element is {keyword:value, search_res:[arr of search res]}]
   # obj = CT()
    for kw in keywords:
    #    category = obj.get_category(kw)
	category= "cat"
        res = bing.do_web_search(kw)
        dump_res = json.dumps({"keyword":kw,"category":category,"search_res":res["SearchResponse"]["Web"]["Results"]}) 
        return_string += dump_res + ","
    return_string +='{"test":"dummy_res"}' #Add dummy result for comma after last result
    return_string += "]}"

    #print return_string
    return return_string
 

def traverse(t,npchunks):
    try:
        t.node 
    except AttributeError:
        return
    if t.node == 'NP':
        split_chunk = ' '.join(word for (word,tag) in t.leaves())
        npchunks.append(split_chunk) 
    else:
        for child in t:
            traverse(child,npchunks)

    
if __name__=="__main__":
    app.run(debug=True);
