#working with CSV file format:
import pandas as pd
import numpy as np
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df = df.transform(func = lambda x : x + 10)
result = df.transform(func = ['sqrt'])


#working with JSON file Format:
import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}
  #Serializing json:
with open('person.json', 'w') as f: 
    json.dump(person, f)
json_object = json.dumps(person, indent = 4) 
  #deserializing json:
with open('sample.json', 'r') as openfile: 
    json_object = json.load(openfile) 

    
#working with XLSX file format:
import pandas as pd
import urllib.request
urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")
df = pd.read_excel("sample.xlsx")


#working with XML file format:
import xml.etree.ElementTree as ET
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'
mydata1 = ET.ElementTree(employee)

with open("new_sample.xml", "wb") as files:
    mydata1.write(files)
import pandas as pd 
import xml.etree.ElementTree as etree
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml
  #parse XML and put information in a dataframe: 
tree = etree.parse("Sample-employee-XML-file.xml")
root = tree.getroot()
columns = ["firstname", "lastname", "title", "division", "building","room"]
datatframe = pd.DataFrame(columns = columns)
for node in root: 
    firstname = node.find("firstname").text
    lastname = node.find("lastname").text 
    title = node.find("title").text     
    division = node.find("division").text    
    building = node.find("building").text    
    room = node.find("room").text
    datatframe = datatframe.append(pd.Series([firstname, lastname, title, division, building, room], index = columns), ignore_index = True)

df=pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details") 
datatframe.to_csv("employee.csv", index=False)


#read the image file:
from PIL import Image 
import urllib.request
urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")

img = Image.open('dog.jpg') 
display(img)
