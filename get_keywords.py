#TODO
#stemming
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup

import sys,re
import itertools
import urllib2,nltk
import AlchemyAPI

import itertools
import doc_freq_class



alchemyObj = AlchemyAPI.AlchemyAPI()    # Create an AlchemyAPI object.
alchemyObj.loadAPIKey("api_key.txt")    # Load the API key from disk.


class proper_noun:


    def __init__(self):
        pass

    def get_nnp_ngrams(self,original_text, highlight=5, minsize=0):
       

        keywords_by_postion = []
        minsize = minsize-1
        if minsize<0:
            minsize = 0 
        tokens = nltk.wordpunct_tokenize(original_text)
        tagged = nltk.word_tokenize(original_text)
        
        i = 0
        for t in tagged:
        	tagged[i]=str(t)
        	i = i + 1
        	
        tagged =  nltk.pos_tag(tokens)
        doc_length = len(tokens)
        counter = 0
        counter2 = 0
        if highlight==0:
            concated_test = doc_length # This is set to doc_length but could be anything recommend 3.
        else:
            concated_test = highlight
        list_of_NNPs = []
       
        while counter < (doc_length-1):
            while counter2 < concated_test:
                counter2 = counter2+1
                counter3 = 0
        
                temp_array = []
                all_nnp = True
                while counter3 < counter2:
                    if counter < (doc_length-counter3):
                        temp_array.append(tokens[counter+counter3])
                        if tagged[counter+counter3][1] != 'NNP':
                            all_nnp = False
                    counter3 = counter3+1
              
                counter3 = 0
                if all_nnp == True:
                    if(len(temp_array)>minsize):
                        list_of_NNPs.append(temp_array)
               
            counter2 = 0
            counter = counter+1
      
        for l in list_of_NNPs:
            str1 = ' '.join(l)
            if len(str1)< 3 or (not str1.isalnum()):
                list_of_NNPs.remove(l)

        unique_NNPs = list(list_of_NNPs for list_of_NNPs,_ in itertools.groupby(list_of_NNPs))
   
        #discard punctuations
        unique_NNPs = self.discard_words_after_punct(unique_NNPs)
        
        unique_NNPs.sort()
        unique_NNPs_final = list(unique_NNPs for unique_NNPs,_ in itertools.groupby(unique_NNPs))
        unique_NNPs_final.sort()
        
   
        #filter list to get max lenght n grams
        unique_NNPs_final = self.get_maxlength_ngram(unique_NNPs_final)
        unique_NNPs_final = self.remove_stopwords(unique_NNPs_final)
        unique_NNPs_final.sort()         ##for removing empty ngrams
        unique_NNPs_final = list(unique_NNPs_final for unique_NNPs_final,_ in itertools.groupby(unique_NNPs_final))
        if not unique_NNPs_final[0]:
            del unique_NNPs_final[0:1]
            #print unique_NNPs_final
        print "Keywords:"
        print unique_NNPs_final
        
        if len(tokens)> 200:
            for kw in unique_NNPs_final:
                print "kw[0]::" + kw[0]
                indx_NNP = tokens.index(kw[0])
                #indx_NNP = indx[0]
                i=1
                flag = 0
                for i in range(len(kw)):
                    if tokens[indx_NNP+i]<> kw[i]:
                        flag = 1
                        break
                    i = i + 1
                if flag == 0:
                    if indx_NNP>0 and indx_NNP<200 :
                        keywords_by_postion.append(kw)
            print "filtered Keywords:"
            print keywords_by_postion 
            unique_NNPs_final = keywords_by_postion
            for ngram in unique_NNPs_final:
		
                for i in ngram:
                    if len(i)==1:
                        ngram.remove(i)
                if len(ngram)== 0:
                    unique_NNPs_final.remove(ngram)
		
        
        return unique_NNPs_final

    def remove_stopwords(self,unique_NNPs_final):
        
        print "\nIN STOP WORDS"
        for ngram in unique_NNPs_final:
            for i in ngram:
                if i.lower() in nltk.corpus.stopwords.words('english'):
                   # print "DETECTED"
                    ngram.remove(i)

					
        return unique_NNPs_final


    def discard_words_after_punct(self,list_of_NNPs):
        
        for ngram in list_of_NNPs:
            for i in ngram:
                if i.isalnum() == False:
                    #print "ngrams:::"
                    #print ngram
                    #print i 
                    index = ngram.index(i)
                    length = len(ngram) 
                    del ngram[index:length]
                    #print ngram
        return list_of_NNPs

    def issubstring(self,thelist,tomatch): #check whether tomatch is part of thelist        
     
        #for sublist in thelist:
            
        if all(item in thelist for item in tomatch):
            return 1
        elif all(item in tomatch for item in thelist):
            return 2
        else:
            return -1
    


    def get_maxlength_ngram(self,list_of_NNPs):

        i = k = 0
        final_list_NNPs = []
        length = len(list_of_NNPs)
#        import pdb;pdb.set_trace();
        
       
        for i in range(length-3):#******************
         
           
            return_val = self.issubstring(list_of_NNPs[i+1],list_of_NNPs[i])
            #print "value %d"%(return_val)
            inloop = 0
            #k = i
            while(self.issubstring(list_of_NNPs[i+1],list_of_NNPs[i]) == 1):
                i += 1
            flag = 0
            for (index,nnp) in enumerate(final_list_NNPs):
            	if_sub = self.issubstring(nnp,list_of_NNPs[i])
            	if if_sub == 1:
                    flag = 1
                    break
            	if if_sub == 2:
            	    flag = 1
                    del final_list_NNPs[index]
                    final_list_NNPs.append(list_of_NNPs[i])
                else: 
                    continue       	
            	
            if(flag == 0):	
            	final_list_NNPs.append(list_of_NNPs[i])

            	
            	
            i = i + 1 
            print "\nADDED TO NEW LIST"
            print list_of_NNPs[i]
        print "\nAt the end of get_max_lenght function"
        for i in final_list_NNPs:
            print i
        
    
        return final_list_NNPs
                            

   
    def keywords(self,url,text):
        
#        import pdb;pdb.set_trace();
        title = alchemyObj.URLGetTitle(url)
        soup = BeautifulSoup(title)
        raw = soup('title')
        tokens_title_first = [str(title.text) for title in raw]
   
        print "title::",
        print tokens_title_first
    #text = original
    ### Take nouns in title
        tokens_title_first = str(tokens_title_first[0])
        print tokens_title_first
        tokens_title_temp = nltk.word_tokenize(tokens_title_first)
        tokens_title_pos = nltk.pos_tag(tokens_title_temp)
        print "tokens_title_temp::",
        print tokens_title_temp

        tokens_title = []      ##create duplicate list
        for t in tokens_title_temp:
            index = tokens_title_temp.index(t)
            print "t::" + t
            print "index::" + str(index) 
            print "tag::" + tokens_title_pos[index][1]
            print "len" + str(len(t))
            if (t.isalpha() and (tokens_title_pos[index][1] == "NNP") and (len(t) >= 3)):
           # tokens_title.remove(t)
                tokens_title.append(t)
        tokens_title.sort()
        tokens_title = list(tokens_title for tokens_title,_ in itertools.groupby(tokens_title))
        print "title::",
        print tokens_title 
        list_of_NNPs = self.get_nnp_ngrams(text,5,0)
    
   
        print "list of NNPs: ",
        print list_of_NNPs
        doc_freq_obj = doc_freq_class.context()
        print "getting doc freq"
        max_df = []
       # for n in list_of_NNPs:
            #print "got n"
        #    max_freq = 0
         #   for t in tokens_title:
             #   print "got t"
          #      df = doc_freq_obj.get_together_DF(n,t)
          #      if df > max_freq:
          #          max_freq = df
              #      print "ngram:",
              #      print n
              #      print "title word:",
              #      print t
              #      print "df:",
              #      print df
          #  max_df.append(max_freq)
        #i = 0
        #for df in max_df:
        #    for i in range(len(max_df)-1):
        #        if max_df[i]<max_df[i+1]:
         #           t = list_of_NNPs[i]
         #           list_of_NNPs[i]=list_of_NNPs[i+1]
         #           list_of_NNPs[i+1]= t
         #           t1 = max_df[i]
         #           max_df[i]=max_df[i+1]
         #           max_df[i+1] = t1
   
       # for i in range(len(list_of_NNPs)):
       #     print "keyword: ",
       #     print list_of_NNPs[i] 
       #     print "df:",
       #     print max_df[i]
       # print "\n\nfinal list:",
       # print list_of_NNPs
        return list_of_NNPs
       
      
    

#if __name__ == "__main__":
#    main()
