from __future__ import division
from flask import Flask, jsonify, render_template, request
from flask import redirect, url_for
import nltk,re , pprint
import urllib2
import urllib
import json
import sys
from bingapi import bingapi
import pdb
app = Flask(__name__)
STOPWORDS = ["The", "the", "or"]
chunk_count = 0
npchunks = []
keywords = []

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    c = request.args.get('c', 0, type=str)
    
    print "hello";
    print c;
    return jsonify(result=a+b)

@app.route('/')
def index():
    return render_template('popup.html')

@app.route('/tokenize',methods=['GET','POST'])
def tokenize():
    count = 0	 
    adr = request.args.get('url', 0, type=str)
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
   # txt=' '
   # txt = txt + 'Frequency Distribution: </br>' 
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
   
    #for kw in keywords:
     #   print "%s" %(kw)
        
    txt= '{"result":'
    txt += json.dumps(keywords)
    txt += "}"
    #print "\n\n\n"
    #print txt
    #print "\n\nKEYWORDS:"
    #print keywords
    #search_bing(keywords) 
    return txt

@app.route('/search_results')
def search_bing():
    app_ID="F0EB80C0CD181F47B512016FD3A74CDB58D302B4"

    bing = bingapi.Bing(app_ID)
    #results has json format
    #for kw in keywords:
    kw="hunting"
    res = bing.do_web_search(kw)
    print "\n\nKEYWORD=%s" %(kw)
    print res["SearchResponse"]["Web"]["Results"]
    print "\n\n\nTitle  :"
    #print res["SearchResponse"]["Web"]["Results"]["Title"]
    #for i in  res["SearchResponse"]["Web"]["Results"]:
     #   print i["Title"]
      #  #print i["Description"]
       # print i["Url"]
        #print "\n---------------------------------"

    txt1 = json.dumps(res["SearchResponse"]["Web"]["Results"])
    #c=["jayesh","pawar"]
    #txt='{"result" : '
    #xt += json.dumps(c)
    #txt += "}"
    print txt1
    return txt1
    

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

    
if __name__=="__main__":
    app.run(debug=True);
