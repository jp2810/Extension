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
import getnearbywords_intokens
import AlchemyAPI
import scrape

app = Flask(__name__)
keywords = []
results = ""
pre_append = ""
@app.route('/tokenize',methods=['GET','POST'])
def rifu():
    global pre_append
    global keywords
    print "starting time:",
    now = datetime.datetime.now()
    print datetime.time(now.hour, now.minute, now.second)
   
    url = request.args.get('url', 0, type=str)
    
    #SCRAPE
    print "URL:"+url
    text = scrape.scrapePage(url)
    print text

    #GET KEYWORDS
    obj = get_keywords.proper_noun()
    keywords = obj.keywords(url,text)
   
    #GET CONTEXT
    #nearbywordsObj = getnearbywords_intokens.getnearbywords()
    #results = nearbywordsObj.get_words_from_proximity(keywords,text) 
    
    #GET SEARCH RESULTS
    results =""
    results = search.search_web(keywords,results,0,4)
    pre_append = results
   

    results +='{"test":"dummy_res"}' #Add dummy result for comma after last result
    results += "]}"

    print "\n\ntokenize :\n\n"+results
    return results



@app.route('/get_remaining',methods=['GET','POST'])
def get_rem_results():
    global pre_append
    global keywords
    print "\n\nGETTING NEXT RESULTS SOON....."
    print "\nPREVIOUS RES:"
    print pre_append 
    results = pre_append
    results = search.search_web(keywords,results,4,len(keywords))
   
    results +='{"test":"dummy_res"}' #Add dummy result for comma after last result
    results += "]}"

    print "\n\nget remaining result :\n\n"+results
    print "\n\nDONE HERE..PLEASE SEE THE BROWSER"
    return results


    

    


if __name__=="__main__":
    app.run(debug=True);
