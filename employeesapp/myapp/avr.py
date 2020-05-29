import requests
import json
from datetime import datetime, date



url = "http://127.0.0.1:8000/employee/"

payload = "{\"name\": \"guy\",\"age\": 20, \"member\": false, \"grade\": 39}"
headers = {
  'Authorization': 'Basic RWxsYUE6RWxsYWFjY29zMQ==',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data = payload)
data = json.loads(response.text.encode('utf8'))

with open('api_result.json') as file:
  data = json.load(file)
print(data)
sum = 0
sumL = []
for employee1 in data['employee']:
  sum = sum + employee1['SALARY']
  sumL.append(employee1['SALARY'])
avr = sum / len(sumL)
print(sum)
print(sumL)
print(avr)
#
emplist = []
x= date.today()
for emp in data['employee']:
  z = datetime.strptime(emp['HIRE_DATE'],'%Y-%m-%d').date()
  if x.year - z.year - ((x.month, x.day) < (z.month, z.day)) > 1 and emp['SALARY']< avr:
    emplist.append(emp)
print(emplist)

with open("resoult.json","w") as file1:
  json.dump(emplist,file1,indent=2)