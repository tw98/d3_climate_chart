import csv

CO2_data = []
GDP_data = []
continent_data = []
countries = []
final = []

with open('co-emissions-per-capita.csv', newline='') as csvfile1:
	CO2reader = csv.reader(csvfile1, delimiter=',')
	for row in CO2reader:
		ob = {}
		if row[0] != "Entity":
			ob["country"] = row[0]
			ob["abbr"] = row[1]
			ob["year"] = int(row[2])
			ob["CO2"] = float(row[3])
			CO2_data.append(ob)

			if ob["country"] not in countries:
				countries.append(ob["country"])

# print(CO2_data)
# print(countries)

with open('maddison-data-gdp-per-capita-in-2011us.csv', newline='') as csvfile2:
	GDPreader = csv.reader(csvfile2, delimiter=',')
	for row in GDPreader:
		ob = {}
		if row[0] != "Entity":
			ob["country"] = row[0]
			ob["abbr"] = row[1]
			ob["year"] = int(row[2])
			ob["GDP"] = float(row[3])
			GDP_data.append(ob)

# print(GDP_data)

with open('./data/countriesContinent.csv', newline='') as csvfile3:
	Continentreader = csv.reader(csvfile3, delimiter=',')
	for row in Continentreader:
		ob = {}
		if row[0] != "Continent":
			ob["continent"] = row[0]
			ob["country"] = row[1]
			continent_data.append(ob)

# print(continent_data)

output = []
for country in countries:
	for year in range(1910, 2017, 1):
		final_row = []
		for co2 in CO2_data: 
			if co2["year"] == year and co2["country"] == country:
				final_row.append(co2["country"])
				final_row.append(co2["abbr"])
				final_row.append(co2["year"])
				final_row.append(co2["CO2"])
				break
		
		GDP_count = 0
		for gdp in GDP_data:
			if gdp["year"] == year and gdp["country"] == country:
				final_row.append(gdp["GDP"])
				GDP_count = 0
				break
			else:
				GDP_count += 1
			
			if GDP_count == len(GDP_data):
				final_row.append(-1)
		
	
		for ele in continent_data:
			if ele["country"] == country:
				final_row.append(ele["continent"])
				break
		

		if len(final_row) < 6:
			print(final_row)
		else:
			output.append(final_row)

print("++++++++++++++++")
# for row in output:
# 	print(row)

# field names 
fields = ['Country', 'Abbr', 'Year', 'CO2 per capita', 'GDP per capita', 'Continent'] 

# name of csv file 
filename = "climate_GDP_data.csv"
  
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
      
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(output)








