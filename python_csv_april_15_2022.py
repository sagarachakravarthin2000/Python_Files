import csv

##with open("python.csv","w")as file_obj:
##    
##    file_obj_csv = csv.writer(file_obj)
##    file_obj_csv.writerow(["name","age","runs"])
##    file_obj_csv.writerows([["dhoni","33","99"],["a","44","55"]])
                          
##with open("python1.csv", "w",newline = "") as file_obj:
##    file_obj_csv = csv.DictWriter(file_obj,["name","age","runs"])
##    file_obj_csv.writeheader()
##    file_obj_csv.writerows([{"name":"a","age":44,"runs":55},{"name":"b","age":22,"runs":55}])

import pandas

my_input = [["name","age","runs"],["sagi",22,100],["sagar",23,96]]
my_final_input = pandas.DataFrame(my_input)
print(my_final_input)

my_final_input.to_csv("mydata.csv",index = None)
