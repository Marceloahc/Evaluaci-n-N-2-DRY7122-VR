import urllib.parse
import requests
import datetime

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "8EIKnFNK15ncVheFmhYzKJFotGnkgqDn"

while True:
   hora_actual=datetime.datetime.now()
   print("Hola, a las ", hora_actual,  " vas a realizar una consulta en nuestra api!!")
   print("")
   orig = input("Porfavor ingrese la ciudad de origen: ")
   if orig == "exit":
       break
   dest = input("Porfavor ingrese la ciudad de destino: ")
   if orig == "exit":
       break
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("Viaje desde " + (orig) + " hasta " + (dest))
        print("Duración del viaje:   " + str(json_data["route"]["formattedTime"]))
        print("Distancia recorrida en KM:           " + str("{:.2f}".format(json_data["route"]["distance"]*1.61)))
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str ("{:.4f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")

        print("")
        #print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        # La información sobre la gasolina no se puede solicitar o dara error

