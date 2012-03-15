#DOCUMENT FREQUENCY
#Just import into other other file , call function get_no_of_occ to get DF
import freebase,re
no_of_occ = 0


class context:

     def __init__(self):
         self. keyword="Beautiful Mind"
         self.keyword=self.keyword.lower()

     def get_individual_DF(self,word1):
          pass
          
          
     def get_together_DF(self,ngram,word2):
     	  print "in doc_freq"
     	  word1 = ' '.join(ngram)
     	  word1 = word1.lower()
          no_of_occ = 0
          query = {
                  "name~=":"*"+ word1 + "*",
               "id":[],
               "limit":7
                 }
		
          try:

               result = freebase.mqlreaditer(query)
               		 
               top_ten = []
               count = 0
         # print "\nIDs Retrieved"
               for i in result:
                    if count > 10:
                         break
                    for str1 in i["id"]:
                    #print str
                         top_ten.append(str1)
      
                         count += 1
   
          #print "\nPrinting top ten"
                    #for i in top_ten:
                     #    print i


                    for id_name in top_ten:

                         query = {
                              "id":id_name,
                              "/common/topic/article" : {"id" : None, "optional" : True, "limit" : 1}
                              }
                    try:

                         r = freebase.mqlread(query)
                    #print "currnt ID:"
                    #print id_name
       
                         article_id = r["/common/topic/article"]["id"]
                         text = freebase.blurb(article_id, maxlength=20000).lower()

                    #print text
                    #print "\nFind word now:"

                         pattern = re.compile(word2.lower())
                    
                         no_of_occ += len(pattern.findall(text))
                    #print "\nNO.OF OCC%d"%(no_of_occ)
                    except Exception:
                         pass
         #print "\nNone type error"
          except Exception:
               pass     
          print no_of_occ
          return no_of_occ

def main():
     obj = context()
     count = obj.get_together_DF(obj.keyword,"john nash")
     print "No. of Occ = %d"%(count)


if __name__ =="__main__":
     main()






