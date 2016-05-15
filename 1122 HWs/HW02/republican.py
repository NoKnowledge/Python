'''
Jimmy Lauchoy
CS1122
'''
import json
import urllib2

data = json.load(urllib2.urlopen('http://elections.huffingtonpost.com/pollster/api/charts/2016-national-gop-primary'))

with open("http://elections.huffingtonpost.com/pollster/api/charts/2016-national-gop-primary") as data:
	information = json.load((urllib2.urlopen(data)))

for element in information:
	if element == "estimates":
		for i in range(len(information[element])):
			if information[element][i]["choice"] == "Trump":
				trump = information[element][i]["value"]
			if information[element][i]["choice"] == "Cruz":
				cruz = information[element][i]["value"]
			if information[element][i]["choice"] == "Rubio":
				rubio = information[element][i]["value"]
			if information[element][i]["choice"] == "Carson":
				carson = information[element][i]["value"]
			if information[element][i]["choice"] == "Bush":
				bush = information[element][i]["value"]
			if information[element][i]["choice"] == "Christie":
				christie = information[element][i]["value"]
			if information[element][i]["choice"] == "Rand Paul":
				paul = information[element][i]["value"]
			if information[element][i]["choice"] == "Kasich":
				kasich = information[element][i]["value"]
			if information[element][i]["choice"] == "Fiorina":
				fiorina = information[element][i]["value"]
			if information[element][i]["choice"] == "Huckabee":
				huckabee = information[element][i]["value"]
			if information[element][i]["choice"] == "Santorum":
				santorum = information[element][i]["value"]
			if information[element][i]["choice"] == "Undecided":
				undecided = information[element][i]["value"] 
			if information[element][i]["choice"] == "Other":
				other = information[element][i]["value"]

print("Republican Candidates:")
print("Donald Trump:", trump)
print("Ted Cruz:", cruz)
print("Marco Rubio:", rubio)
print("Ben Carson:", carson)
print("Jeb Bush:", bush)
print("Chris Christie:", christie)
print("Rand Paul:", paul)
print("John Kasich:", kasich)
print("Carly Fiorina:", fiorina)
print("Mike Huckabee:", huckabee)
print("Rick Santorum:", santorum)
print("Undecided:", undecided)
print("Other:", other)
