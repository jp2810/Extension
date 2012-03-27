#DOCUMENT FREQUENCY
#Just import into other other file , call function get_no_of_occ to get DF
import freebase,re
no_of_occ = 0
from pymongo import Connection

connection = Connection()
db = connection.dataset_db


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
          no_of_occ += db.film_data.find({"$and":[{"article": {"$regex":word1,"$options":"i"}},{"article":{"$regex":word2,"$options":"i"}}]}).count()
          print "\nNO.OF OCC in film:%d"%(no_of_occ)
          no_of_occ += db.book_data.find({"$and":[{"article": {"$regex":word1,"$options":"i"}},{"article":{"$regex":word2,"$options":"i"}}]}).count()
          print "\nNO.OF OCC after books:%d"%(no_of_occ)
          no_of_occ += db.people_data.find({"$and":[{"article": {"$regex":word1,"$options":"i"}},{"article":{"$regex":word2,"$options":"i"}}]}).count()
          print "\nNO.OF OCC after people:%d"%(no_of_occ)
          no_of_occ += db.location_data.find({"$and":[{"article": {"$regex":word1,"$options":"i"}},{"article":{"$regex":word2,"$options":"i"}}]}).count()
          print "\nNO.OF OCC after location:%d"%(no_of_occ)
          #print no_of_occ
          return no_of_occ

#def main():
 #    obj = context()
  #   count = obj.get_together_DF(["Neal","Stephenson"],"confusion")
  #   print "No. of Occ = %d"%(count)


#if __name__ =="__main__":
 #    main()






