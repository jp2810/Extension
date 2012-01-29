from __future__ import division
from flask import Flask, jsonify, render_template, request
from flask import redirect, url_for
import nltk,re , pprint
import urllib2
import urllib
import json
import sys
from bingapi import bingapi
#from cate_mongo import categorization as CT


app = Flask(__name__)
STOPWORDS = ["The", "the", "or"]
app_ID="F0EB80C0CD181F47B512016FD3A74CDB58D302B4"
chunk_count = 0
keywords = []

@app.route('/')
def index():
    return render_template('popup.html')

@app.route('/tokenize',methods=['GET','POST'])
def tokenize():
    global keywords    
    npchunks = []	
    count = 0	 
    url = request.args.get('url', 0, type=str)
    webpage = urllib2.urlopen(url).read()
    para= re.compile('<p>(.*)</p>') #collect data in p tags and store in para object
    raw = re.findall(para , webpage)
    rawstr = ' '.join(raw) 
    clean_raw = nltk.clean_html(rawstr)
    token_raw = nltk.word_tokenize(clean_raw)
    
    
    ### removing stopwords
    #filtered_word_list = token_raw[:] #make a copy of the word_list
    for word in token_raw: # iterate over word_list
        if word in nltk.corpus.stopwords.words('english') or not word.isalnum(): 
            token_raw.remove(word)
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
    traverse(chunkset,npchunks)
    
    fd1 = nltk.FreqDist(npchunks)
    fd1keys = fd1.keys() 

    most_freq = fd1.max()

    len_text = len(npchunks)
    for kw in keywords:
        print "keywords:%s:%d" %(kw,fd1[kw])
 
    for ch in npchunks: 
        chunk_position = npchunks.index(ch)  
        position = 0 
        if((chunk_position < (len_text/1.5)) and (fd1[ch] >= (fd1[most_freq]/3))) :
	    for (index,kw) in enumerate(keywords):
                if fd1[kw] <= fd1[ch]:
	            position = index
		    break

            keywords.insert(position,ch)
            count += 1
    
    keywords = [ keywords[i] for i,x in enumerate(keywords) if x not in keywords[i+1:]] 
    for kw in keywords:
        print "%s:%d" %(kw,fd1[kw])
        
    txt= '{"result":'
    txt += json.dumps(keywords)
    txt += "}"
    print "\n\n\n"
    print txt
    print "\n\nKEYWORDS:"
    print keywords
   
    return_string ='{"final_results":['
    i=0
    bing = bingapi.Bing(app_ID)

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

    print return_string
    return return_string
 


    


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

    
if __name__=="__main__":
    app.run(debug=True);
