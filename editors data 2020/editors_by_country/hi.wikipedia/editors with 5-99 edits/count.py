import json 
import csv
  
# Opening JSON file 
de = 0
others = 0
de_list =["India"]
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
                        if(countries['country']=="IN"):
                              de_list.append(countries['editors-ceil'])
                              de = de + countries['editors-ceil']
                        else:
                              temp = temp + countries['editors-ceil']
                              others = others + countries['editors-ceil']
            
            others_list.append(temp)

            # print(de)
            # print(others)
            # Closing file 

            f.close() 

      de_list.append(de)
      others_list.append(others)
      
      writer.writerow(["Country","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","TOTAL"])

      writer.writerow(de_list)
      writer.writerow(others_list)
      file_.close
