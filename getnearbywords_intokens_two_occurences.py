import re,sys
import json
from pprint import pprint
import nltk,urllib2
import doc_freq_class
from pprint import pprint
import doc_freq_class
from bingapi import bingapi
from global_file import getbingid
import search
import cate_mongo_specific1


#getting context of the keywords
#class of neighbouring element of a keyword
class neighbour:
    def __init__(self,word):  
        self.word = word  
        self.freq_word = 0#freq of the words in document
        self.freq_together = 0# frq of that word occuring with that keyword
        self.doc_freq_obj = doc_freq_class.context()
    def find_doc_freq(self,keyword):
    	self.freq_together = self.doc_freq_obj.get_together_DF(keyword,self.word)
        print keyword,
        print self.word
        print "doc freq:" + str(self.freq_together)
        #print keyword,
        #print "    " + self.word 

#class of context vector 
#initialisation 
class document_frequency:
   def __init__(self,keyword):
       self.keyword = keyword
       self.neighbours = []
       self.cnt = 0 #number of neighbours for that keyword

   def addneighbour(self,word):
       self.neighbours.append(neighbour(word))  #append the neighbour of that keyword
       self.cnt += 1  


class getnearbywords:
    
    def __init__(self):
        print "\nHELLO"

    def scrape(self,url):
        webpage = urllib2.urlopen(sys.argv[1]).read()
    #webpage = str(webpage)
        para = re.compile('<p>(.*)</p>') #collect data in p tags and store in para object
        raw = re.findall(para , webpage)
        rawstr = ' '.join(raw)
        clean_raw = nltk.clean_html(rawstr)
        #print clean_raw
        return clean_raw
   
    def get_words_from_proximity(self,keywords,text):  #think of how to get nouns from sentence only... !!
        #create object of doc_frequency

        doc_freq_obj = doc_freq_class.context()
    	#see if processing can be reduced
        tokens = nltk.word_tokenize(text)
        #print "tokens:"
        #print tokens
        for i in tokens:
            if i.isalnum()== False:
                tokens.remove(i)
            
        c = nltk.ConcordanceIndex(tokens, key = lambda s: s.lower())
      
        tokens_pos = nltk.pos_tag(tokens)  
        i = 5
        doc_freq = []
        df_cnt = 0

        print "keywords going to loop",
        print keywords
        for kw in keywords:
            print "keyword::::::::",
            print kw
			#split keyword not required as kw is list of strings
            #k = nltk.word_tokenize(kw)
            #print k
            
            #print "keywords in for ", 
            #print kw
            first_word = kw[0]        #1st word in keyword
            #print "first word"
            #print first_word
            keyword_len = len(kw)
            #print "LEN="+str(keyword_len)
            i = 5
            nomatch = 0
            #print "IN KWD LOOP."
            print "offset",
            print c.offsets(first_word)
            
            no_of_times = 0
            for offset in c.offsets(first_word):
                print kw
                j = 1
                i = 5
                #print "Keyword=",
                #print kw,
                #print " OFFSET=" + str(offset) 
                nomatch = 0
                while j < keyword_len:
                    #print "in while"
                    #print tokens[offset+j]
                    #print kw[j]
                    
                    if tokens[offset+j].lower() <> kw[j].lower():
                        #print tokens[offset+j]
                        #print k[j]
                	nomatch = 1
                       	break 
                    j = j + 1
                if nomatch == 0:
                    doc_freq.append(document_frequency(kw))
                    #print "matched kwd",
                    #print tokens[offset:offset+j-1]
                    #print tokens[offset-5:offset+5]
                    i = 5
                    while i > 0 :
                	if (offset-i) < 0:
                    	    break
                        
                    	if (tokens_pos[offset-i][1] in ["NN","NNP"]) and (tokens_pos[offset-i][1].lower() not in  nltk.corpus.stopwords.words('english')):
                       		#doc_freq_obj.get_together_DF("")
                            #print "dfcnt:" + str(df_cnt) 
                            #print "i: " + str(i)
                            doc_freq[df_cnt].addneighbour(tokens_pos[offset-i][0])
                       		
                            print tokens_pos[offset-i][0],
                            
                            #pass
                    	i = i - 1
                
                
                    print "\m/ ",
                    print kw,
                    print "\m/ ",
                    i = 1
           
                    while i < 5 :
                        if (offset+i+(keyword_len-1)) >= len(tokens):
                            break
    	
                        if (tokens_pos[offset+i+(keyword_len-1)][1] in ["NN","NNP"]) and (tokens_pos[offset+i+(keyword_len-1)][1].lower() not in  nltk.corpus.stopwords.words('english')): 
                            #pass
                            doc_freq[df_cnt].addneighbour(tokens[offset+i+(keyword_len-1)])
                            print tokens_pos[offset+i+(keyword_len-1)][0],
                
	        
                        i = i + 1
                    k = 0
                    print "\n\n"    
                    while k < doc_freq[df_cnt].cnt:
                        #doc_freq[df_cnt].neighbours[k].freq_word = fd1[context_vectors[CV_cnt].keyword]
                        doc_freq[df_cnt].neighbours[k].find_doc_freq(doc_freq[df_cnt].keyword)
                        k = k + 1
                    #TODO = normalize
                    doc_freq[df_cnt].neighbours.sort(key=lambda x: x.freq_together, reverse=True)
                    if doc_freq[df_cnt].cnt > 5:
                        doc_freq[df_cnt].neighbours = doc_freq[df_cnt].neighbours[:5]        #take 10 neighbours with highest weight
                        doc_freq[df_cnt].cnt = 5
                    k = 0
                    #while k < doc_freq[df_cnt].cnt:
                    print "keyword: ",
                    for l in doc_freq[df_cnt].keyword: 
                        print  l,
                    print "\n"
                    print  "neighbours: ",
                    for m in doc_freq[df_cnt].neighbours:
                        print m.word,
                        print "\n"
                        #k += 1
                    
                    
                    df_cnt = df_cnt + 1
                no_of_times = no_of_times + 1
                if no_of_times>=2:
                    break
        #results = search_web(doc_freq)
        return doc_freq



            
        



#def main():
#    print "\nIN THE MAIN"
#    obj = getnearbywords()
#    #text = obj.scrape(sys.argv[1])
#    #print text
#    obj.do_web_search()



#if __name__ =="__main__":
#    main()




    
