import json 
import csv
  
# Opening JSON file 
de = 0
fr = 0
hi = 0
others = 0

de_list =["Germany"]
fr_list = ["France"]
hi_list = ["India"]
others_list = ["Others"]

file_= open('data.csv', 'w')

with file_:
      writer = csv.writer(file_)

      for i in range(1,13):
            filename = str(i) + ".json"
            print(filename)
            f = open(filename,) 

            # returns JSON object as  
            # a dictionary 
            data = json.load(f) 
            
            # Iterating through the json 
            # list 
            temp = 0
            for item in data['items']: 
                  for countries in item['countries']:
                        if(countries['country']=="DE"):
                              de_list.append(countries['editors-ceil'])
                              de = de + countries['editors-ceil']

                        elif(countries['country']=="IN"):
                              hi_list.append(countries['editors-ceil'])
                              hi = hi + countries['editors-ceil']   

                        elif(countries['country']=="FR"):
                              fr_list.append(countries['editors-ceil'])
                              fr = fr + countries['editors-ceil']                                                         
                        else:
                              temp = temp + countries['editors-ceil']
                              others = others + countries['editors-ceil']
            
            others_list.append(temp)

            # print(de)
            # print(others)
            # Closing file 

            f.close() 

      de_list.append(de)
      hi_list.append(hi)
      fr_list.append(fr)
      others_list.append(others)
      
      writer.writerow(["Country","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","TOTAL"])

      writer.writerow(de_list)
      writer.writerow(hi_list)
      writer.writerow(fr_list)
      writer.writerow(others_list)
      file_.close