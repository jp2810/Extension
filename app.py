from __future__ import division
from flask import Flask, jsonify, render_template, request,redirect, url_for
import nltk,re,pprint
import urllib2
import sys
from bingapi import bingapi
from global_file import getbingid
import json
import search
import datetime
import get_keywords
import keywords_file
import getnearbywords_intokens
import AlchemyAPI
import scrape

app = Flask(__name__)
keywords = []
results = ""
pre_append = ""
doc_freq = []
url=""

@app.route('/tokenize',methods=['GET','POST'])
def rifu():
    global pre_append
    global keywords
    global doc_freq
    global url
    print "starting time:",
    now = datetime.datetime.now()
    print datetime.time(now.hour, now.minute, now.second)
   
    url = request.args.get('url', 0, type=str)
    
    #webpage = urllib2.urlopen(url).read()
    #para= re.compile('<p>(.*)</p>') #collect data in p tags and store in para object
   # raw = re.findall(para , webpage)
   # rawstr = ' '.join(raw)
   # text = tokenize(rawstr)
    #SCRAPE
    print "URL:"+url
    text = scrape.scrapePage(url)
    print "\nScraping Done"
    print text

    #GET KEYWORDS
   
    keywords = keywords_file.get_keywords(url,text)
    print "my keywords:::"
    print keywords
    #GET CONTEXT
    nearbywordsObj = getnearbywords_intokens.getnearbywords()
    doc_freq = nearbywordsObj.get_words_from_proximity(keywords,text) 
#    import pdb;pdb.set_trace();
    print "doc freq::::"+ str(doc_freq)
    
    #GET SEARCH RESULTS
    results =""
    results = search.search_web(doc_freq,results,0,4,url)
    pre_append = results
   
    tab_id = request.args.get('tab_id',0,type=int)
    results +='{"tab_id":'+str(tab_id)+'}' #Add dummy result for comma after last result
    results += "]}"

    #print results
    return results



@app.route('/get_remaining',methods=['GET','POST'])
def get_rem_results():
    global pre_append
    global keywords
    global doc_freq
    global url
    print "\n\nGETTING NEXT RESULTS SOON....."
    print "\nPREVIOUS RES:"
    #print pre_append 
    results = pre_append
    
    results = search.search_web(doc_freq,results,4,len(doc_freq),url) ############################
    #import pdb;pdb.set_trace();

    tab_id = request.args.get('tab_id',0,type=int)
    results +='{"tab_id":'+str(tab_id)+'}' #Add dummy result for comma after last result
    results += "]}"


    #print results
    print "\n\nDONE HERE..PLEASE SEE THE BROWSER"
    print "\nkeywords::"+str(len(keywords))
    print keywords

    return results


    

    


if __name__=="__main__":
    #app.run(debug=True);
    app.run(host='0.0.0.0')
