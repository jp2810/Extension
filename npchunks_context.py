from __future__ import division
from flask import  Flask, redirect, url_for, request
import nltk, re , pprint
import urllib2
import urllib
import json
import sys
from pymongo import Connection
import re

connection = Connection()
db = connection.dataset_db
#url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyA9cFda8VLD_Nf83iK1mR4Rr8Vr81UhSLw&cx=003343581792201845772:b08qtr04hdk&#q=%s&gl=ca&num=1'
app = Flask(__name__)

chunk_count = 0
npchunks = []

#getting context of the keywords
#class of neighbouring element of a keyword
class neighbour:
    def __init__(self,word):  
        self.word = word  
        self.freq_word = 0#freq of the words in document
        self.window_freq = 0# frq of that word occuring with that keyword
        self.weight = 0
    def find_weight(self):
        if self.freq_word <> 0:
            self.weight = (self.window_freq)/self.freq_word 
        else:
	    self.weight = 0 

#class of context vector 
#initialisation 
class CV:
   def __init__(self,keyword):
       self.keyword = keyword
       self.neighbours = []
       self.cnt = 0 #number of neighbours for that keyword

   def addneighbour(self,word):
       self.neighbours.append(neighbour(word))  #append the neighbour of that keyword
       self.cnt += 1  


@app.route('/')
def view():
       
    str2 = """</br></br>My URL:<form action=tokenize method=\"post\"><p><input type=\"text\" name=\"url\"/></p><input type=\"submit\" value=\"Adress\"/></form>"""
    return str2

    

@app.route('/tokenize',methods=['GET','POST'])
def tokenize():
	#stopwords = ["The", "the", "or", "and"]
	keywords = []
	count = 0	 
	adr = request.form["url"]
	webpage = urllib2.urlopen(adr).read()
    
	para= re.compile('<p>(.*)</p>') #collect data in p tags and store in para object
	raw = re.findall(para , webpage)
	rawstr = ' '.join(raw) 
	clean_raw = nltk.clean_html(rawstr)
	token_raw = nltk.word_tokenize(clean_raw)
    
    
    ### removing stopwords
	filtered_word_list = token_raw[:] #make a copy of the word_list
	for word in token_raw: # iterate over word_list
	    if word in nltk.corpus.stopwords.words('english') or not word.isalnum(): 
	        filtered_word_list.remove(word)
	token_raw = []
	token_raw.extend(filtered_word_list)
	txt=' '
	txt = txt + 'Frequency Distribution: </br>' 
	pos_tag_raw = nltk.pos_tag(token_raw)
	grammar = """
	          NP: {<JJ>*<NN>}
	              }<[\.VI].*>+{
	              {<NNP>+}
	              {<NN>+}  
	            """
	chunks = nltk.RegexpParser(grammar)
	chunkset = chunks.parse(pos_tag_raw)
    
    
	del npchunks[0:]
	traverse(chunkset)
   
	fd1 = nltk.FreqDist(npchunks)
	fd1keys = fd1.keys() 
	most_freq = fd1.max()

	len_text = len(npchunks)
	for ch in npchunks: 
	    chunk_index = [index for (index, chnk) in enumerate(npchunks) if chnk == ch]
	    chunk_position = chunk_index[0]
	    if((chunk_position < (len_text/1.5)) and (fd1[ch] >= (fd1[most_freq]/3))) : 
	        keywords.append(ch)
	        count += 1
 
        keywords = set(keywords)
  
	raw_text = nltk.Text(token_raw)

	context_vectors = []
	CV_cnt = 0

	print "found keywords"
	
	
	
	for kw in keywords :
	    print "kyword:" + kw
	    txt = txt + kw + ':' + str(fd1[kw]) + '</br>'
	    context_vectors.append(CV(kw)) 
	    c = nltk.ConcordanceIndex(token_raw, key = lambda s: s.lower())
        #print raw_text.concordance(kw,40)
	    i = 5

	    for offset in c.offsets(kw):
	        while i > 0 :
	            if (offset-i) < 0:
	                break

	            flag = 0
	            j = 0  
	            while j < context_vectors[CV_cnt].cnt:
	                if token_raw[offset-i] == context_vectors[CV_cnt].neighbours[j].word:
	                    flag = 1
                            context_vectors[CV_cnt].neighbours[j].window_freq += 1 #if the neighbour keyword occurs in the window more than once
                            break
		        j = j + 1
			
                #completelty new neighbour
	            if flag == 0:
	                context_vectors[CV_cnt].addneighbour(token_raw[offset-i])
                #print(token_raw[offset-i]),
	        i = i - 1
                flag = 0	
	    #print kw,
	    i = 0
            while i < 5 :
                if (offset+i) >= len(token_raw):
                    break
    	
		flag = 0
                j = 0  
                while j < context_vectors[CV_cnt].cnt:
                    if token_raw[offset+i] == context_vectors[CV_cnt].neighbours[j].word:
                        flag = 1
     			context_vectors[CV_cnt].neighbours[j].window_freq += 1
			break
                    j = j + 1
			

                if flag == 0:
                    context_vectors[CV_cnt].addneighbour(token_raw[offset+i])
                #print(token_raw[offset-i]),
	        flag = 0   
                i = i + 1
            #print "------------------"
        k = 0
        print "Keyword: " + context_vectors[CV_cnt].keyword
        print "Neighbours:" 
        
        while k < context_vectors[CV_cnt].cnt:
        	context_vectors[CV_cnt].neighbours[k].freq_word = fd1[context_vectors[CV_cnt].keyword]
 	    	context_vectors[CV_cnt].neighbours[k].find_weight()
	    	k = k + 1

        context_vectors[CV_cnt].neighbours.sort(key=lambda x: x.weight, reverse=True)
	if context_vectors[CV_cnt].cnt > 10:
            context_vectors[CV_cnt].neighbours = context_vectors[CV_cnt].neighbours[:10]        #take 10 neighbours with highest weight
	    context_vectors[CV_cnt].cnt = 10
	k = 0
	while k < context_vectors[CV_cnt].cnt:
            print  context_vectors[CV_cnt].neighbours[k].word + "       " + str(context_vectors[CV_cnt].neighbours[k].weight)
	    k += 1
        
        CV_cnt = CV_cnt + 1
        



    #for kw in keywords:
        
     #   url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyA9cFda8VLD_Nf83iK1mR4Rr8Vr81UhSLw&cx=003343581792201845772:b08qtr04hdk&q=%s&gl=ca&num=1' %(kw)

#        sr = urllib.urlopen(url)

 #       json_data = json.load(sr)  #It returns data in json format
  #      results = json_data['items']

   #     for i in results:
    #        print '---'
     #       print 'title:',i['title']
      #      print 'text:',i['snippet']
       #     print 'url:', i['link'], '\n'  
        return txt

    # a tree traversal function for extracting NP chunks in the parsed tree
def traverse(t):
    global chunk_count
    try:
        t.node
    except AttributeError:
        return
    if t.node == 'NP':
        split_chunk = ' '.join(word for (word,tag) in t.leaves())
        npchunks.append(split_chunk) 
    else:
        for child in t:
            traverse(child)



if __name__== '__main__':
    app.debug= True
    app.run()
