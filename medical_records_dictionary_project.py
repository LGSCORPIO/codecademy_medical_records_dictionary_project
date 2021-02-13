#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 14:48:40 2021

@author: lilygoodyersait
"""

# Add your code here
medical_costs={}
## Adding to the dictionary
medical_costs.update({"Marina": 6607.0, "Vinay": 3225.0})
print(medical_costs)
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
print(medical_costs)

###correcting value 
medical_costs["Vinay"]=3325.0

## calculate average insurance
total_costs=0
for i in medical_costs.values():
  total_costs+=i
average_cost=total_costs/len(medical_costs)
print("Average Insurance Cost: {}".format(average_cost))

## create dictionary from zipped lists
names=["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages=[27, 24,43,35,52]
zipped_ages=zip(names, ages)
names_to_ages={key:value for key, value in zipped_ages}
print(names_to_ages)

##get value for a given key
marina_age=names_to_ages.get("Marina")
print(marina_age)

###update dictionary with key:value pairs with the value being dictionaries
medical_records={}
medical_records["Marina"]={"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records.update({"Vinay": {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0 }, "Connie": {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}, "Isaac":{"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0},"Valentina":{"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}})

print(medical_records)

###access specific information about Connie
print("Connie's insurance cost is {} dollars.".format(str(medical_records["Connie"] ["Insurance_cost"])))

medical_records.pop("Vinay")

##Access key:value when vlaue is a dictionary
for name, record in medical_records.items():
  print(name + " is a " + str(record["Age"]) + \
  " year old " + record["Sex"] + " " + record["Smoker"] \
  + " with a BMI of " + str(record["BMI"]) + \
  " and insurance cost of " + str(record["Insurance_cost"]))

### create function which adds a person's name and medical records to the dictionary

def update_medical_records(name,record):
  new_record_dic={}
  new_record_dic[name]=record
  medical_records.update(new_record_dic)
  print(medical_records)

update_medical_records("Tom",{"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0} )

###Create code that creates dictionary with just BMI data:
names=[]
bmis=[]
for name, record in medical_records.items():
  names.append(name)
  bmis.append(record["BMI"])
  bmi_dic_zip=zip(names,bmis)
  bmi_dic={key:value for key, value in bmi_dic_zip}
  print(bmi_dic)