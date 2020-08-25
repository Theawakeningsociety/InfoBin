#!/usr/bin/python
#coding: utf-8
# BIN que da telefono y pagina web 454323
embl =  """
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 ? _____________________      ?
 ?| Hello member,       |     ?
 ?| welcome to          |     ?
 ?| RESET INFO BIN      |     ?
 ? ---------------------      ?
 ?                    \       ?
 ?                     (oo)   ?
 ?                     (__)   ?
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 |Created by: Durd3n & Guarc0n|
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 """
from colorama import init
from termcolor import colored
init()
print(colored(embl, 'red'))
b = raw_input(colored(' Escribe el BIN: ', 'yellow'))
def check(Bin):
	Bin = Bin.replace(" ", "")
	if Bin.isdigit():
		getInfo(Bin)
	else:
		print " Escribe un bin valido"

def getInfo(Bin):
	print(colored(' SEARCHING BIN DATA ...', 'green'))

	url = 'https://lookup.binlist.net/'
	http = requests.get(url+Bin)
	content = http.content
	json_data = json.loads(content)
	file = open("TempInfo.txt", 'w')
	file.write(str(json_data))
	file.close()
	for i in json_data.keys():
		print ("\n" + " " + colored(i, 'red') + " : "+str(json_data[i]))
		
while len(b) != 6:
	b = raw_input("Insert your BIN: ")
else:
	try:
		import json
		import requests
		import colorama
		import termcolor
		check(b)
	except ValueError as e:
		print "No se ha obtenido informacion alguna de dicho BIN, vuelva a intentar con un BIN distinto"
	except ImportError as a:
		print("\t\nParece ser que no haz instalado los requisitos necesarios para poder usar la herramienta")#
		print("\nSolo es necesario escribir este sencillo comando: pip install -r req.txt")