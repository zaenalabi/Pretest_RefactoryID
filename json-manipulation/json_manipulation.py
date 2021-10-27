# gunakan modul json
import json

# buka file JSON
file_json = open("data.json")

# prsing data JSON
data = json.loads(file_json.read())

# cetak isi data JSON
#print(data)

#meeting room
for s in range(len(data)):
	if data[s]["placement"]["name"] == "Meeting Room":
		print("Find items in the Meeting Room is {} ".format(data[s]["name"]))
	

print()
#device electronic
for s in range(len(data)):
	if data[s]["type"] == "electronic":
		print("Find all electronic devices is {} ".format(data[s]["name"]))
		
			
print()
#furniture
for s in range(len(data)):
	if data[s]["type"] == "furniture":
		print("Find all furniture is {} ".format(data[s]["name"]))

			
print()
#Find all items were purchased on 16 Januari 2020
for s in range(len(data)):
	if data[s]["purchased_at"] == 16012020:
		print("Find all items were purchased 16012020 is {} ".format(data[s]["name"]))
		
		
print()
#Find all items with brown color (belum ketemu)
for s in range(len(data)):
	if data[s]["tags"][2] == "brown":
		print("Find all items with brown color is {} ".format(data[s]["name"]))

