from __future__ import division
from flask import Flask, jsonify, render_template, request
from flask import redirect, url_for
import nltk,re , pprint
from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import json
import sys
import AlchemyAPI

import scrape,re


alchemyObj = AlchemyAPI.AlchemyAPI()    # Create an AlchemyAPI object.
alchemyObj.loadAPIKey("api_key.txt")    # Load the API key from disk.

STOPWORDS = ["The", "the", "or","an","An"]

chunk_count = 0
#keywords = []


def get_keywords(url,text):
   # global keywords    
    keywords=[]
    global STOPWORDS
    npchunks = []	
    count = 0	 
	#scraping
    #keywords = add_title_keywords(url,keywords)
    #text = scrape.scrapePage()
    token_raw = nltk.wordpunct_tokenize(text)
    
    
    
    ### removing stopwords
    #filtered_word_list = token_raw[:] #make a copy of the word_list
    #for word in token_raw: # iterate over word_list
    #    if word.lower() in nltk.corpus.stopwords.words('english') or (not word.isalnum()) or (word.lower() in STOPWORDS):
    #        token_raw.remove(word)
    
    #convert tokens to lowercase
   
    pos_tag_raw = nltk.pos_tag(token_raw)
    grammar = """
              NP: {<NNP>+}
                    
                """
    chunks = nltk.RegexpParser(grammar)
    chunkset = chunks.parse(pos_tag_raw)
     
    #del npchunks[0:]# delete  
    traverse(chunkset,npchunks)
    #frquency distribution finds the number of times that chunk is present in the document
    fd1 = nltk.FreqDist(npchunks) #gets freq of each chunk
    most_freq = fd1.max() #returns the maximum frq chunk

    len_text = len(npchunks)

    for ch in npchunks:
         #find the postion of each npchunk wrt whole text 
        chunk_position = npchunks.index(ch)  
        position = 0 
        if((chunk_position < (len_text/1.5))):### and (fd1[ch] >= (fd1[most_freq]/3))) :
            
            #SORT BY FREQ
	    #for (index,kw) in enumerate(keywords): #index is the index of arreay and kw is the value at that index
            #    if fd1[kw] <= fd1[ch]:
	     #       position = index
		#    break

            keywords.append(ch)
           
    #remove duplicates
    keywords = [ keywords[i] for i,x in enumerate(keywords) if x not in keywords[i+1:]] 
    #for kw in keywords:
    #    print "%s:%d" %(kw,fd1[kw])
        
    #txt= '{"result":'
    #txt += json.dumps(keywords)
    #txt += "}"
    #print "\n\n\n"
    #print txt
#    import pdb;pdb.set_trace();

    
    for i in keywords:
        if len(i)<=2:
            keywords.remove(i)

    
  
    keywords = remove_stopwords_from_kwds(keywords)                                     #REMOVE STOPWORDS
   
    keywords = [x.lower() for x in keywords]                                            #CONVERTING TO LOWER

    
   
    keywords = [ keywords[i] for i,x in enumerate(keywords) if x not in keywords[i+1:]] #REMOVING DUPLICATES
    
    #REMOVE HEX VALUES
#    import pdb;    pdb.set_trace();
    #count = 0
    #print "LEN:"+str(len(keywords))
       
    
    keywords = remove_substr(keywords)
    keywords = sort_using_title(url,keywords)

   # print "Loop is running "+str(count)+" times"
    print "\n\nKEYWORDS:"
    print keywords
    print "\n\n"
    return keywords
    


def sort_using_title(url,keywords):
     
    title = alchemyObj.URLGetTitle(url)
    soup = BeautifulSoup(title)
    raw = soup('title')
    title_text = [str(title.text) for title in raw]

    print "title::",
    print title_text[0]
	    #text = original
	    ### Take nouns in title
    tokens_title = nltk.word_tokenize(title_text[0])
    tokens_title_pos = nltk.pos_tag(tokens_title) 
    print tokens_title_pos
#    import pdb;pdb.set_trace();
    tokens_title_NNP = []
    grammar = """
              NP: {<NNP>+}
                    
                """
    chunks = nltk.RegexpParser(grammar)
    chunkset = chunks.parse(tokens_title_pos)
    traverse(chunkset,tokens_title_NNP)
#    for t in tokens_title:
 #       index = tokens_title.index(t)
  #      if t.isalnum() and (tokens_title_pos[index][1] == "NNP"):
   #         tokens_title_NNP.append(t)

    print "\ntitle only NNP::",
    print tokens_title_NNP
    title_keywords = []
    keywords_copy=keywords
    for k in keywords_copy:
        for t in tokens_title_NNP:
            if (k.lower() in t.lower()) or (t.lower() in k.lower()) or (k.lower() == t.lower()):
                print "title keyword:::" + k
                keywords.remove(k)
                title_keywords.append(k)
    index = 0
    for t in title_keywords:
        keywords.insert(index,t)
        index = index + 1
    return keywords

def issubstring(thelist,tomatch): #check whether tomatch is part of thelist        
     
        #for sublist in thelist:
            
    if all(item in thelist for item in tomatch):
        return 1
    elif all(item in tomatch for item in thelist):
        return 2
    else:
        return -1



def remove_substr(kwds):
    tokenized_keywords = []
    #Preparing list of tokenized keywords
    for k in kwds:
        tokens = nltk.word_tokenize(k)
        tokenized_keywords.append(tokens)
        
    print tokenized_keywords
    
    for k in tokenized_keywords:
     #   count += 1
     	for ch in k:
            if re.match("[.]*x[0-9]+[a-z]*",ch):  ############
                tokenized_keywords.remove(k)
            	break
    
    tokenized_keywords_copy = tokenized_keywords
	    
    #loop for removal if match found
    for k in tokenized_keywords:
        
     #   match = 0
        for kw in tokenized_keywords_copy:
            #import pdb;pdb.set_trace();
            if issubstring(k,kw)==1 and k <> kw:
                tokenized_keywords.remove(kw)
            elif issubstring(k,kw)==2 and k <> kw:
                tokenized_keywords.remove(k)
                break
                
    
    #join tokenized_keywords list
    keywords_list = []
    for k in tokenized_keywords:
        
        word = ' '.join(k)
        keywords_list.append(word)
    print keywords_list
    return keywords_list
           

                
                
    
            

            
        
        

#    kwds1 = kwds
#    len1 =0
#    for i in kwds:
#        len = kwds.index(i)+1
#        print len
  #      for j in kwds1[len1:len(kwds)-1]
#            if j.find(i)==-1:
#                print "word:"+i
#                kwds.remove(i)
#                print "REMoVED"+i
#                break
 #       kwds1=kwds

#REMOVE STOPWPRDS WHICH ARE PART OF Keywords
def remove_stopwords_from_kwds(kwds):

    index=0
    for i in kwds:
        #print "hello"
        token = nltk.word_tokenize(i)
        for j in token:
             if j.lower() in nltk.corpus.stopwords.words('english') or not j.isalnum() or (j.lower() in STOPWORDS):
                token.remove(j)
        if len(token)!=0:
            kwds.remove(i) #first remove then insert
            str1=token[0]
            for k in token[1:]:
                str1 = str1+" "+k
            kwds.insert(index,str1)
        else:
            kwds.remove(i)
        index= index+1
    return kwds
        
#def remove_duplicates():
    

#traverse the npchunks that is got by parsing pos_tag data
def traverse(t,npchunks):
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
            traverse(child,npchunks)


