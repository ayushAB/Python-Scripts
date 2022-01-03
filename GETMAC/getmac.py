import sys
import requests

# api key that is generated from the website https://macaddress.io/ after signup
apiKey = "at_5ElKnjROfWFUmquGtugOGLyn9KSqY"
# endpoint to get the MAC Address details
# concatenating the string with the api key variable and the system argv
# get the system argument on index 1 as
# sys.argv[0] returns the file name
# sys.argv[1] returns the first argument i.e in this case our MAC Address entered by user

# decalaring a URL variable with the required endpoint url for the request
# this endpoint return json result
URL = "https://api.macaddress.io/v1?apiKey=" + \
    apiKey+"&output=json&search="+sys.argv[1]

# using requests to make aget request with the above created url
response = requests.get(url=URL)
# getting the json response from the above get request
# response.json() response.json() returns a JSON object of the result (if the result is written in JSON format, if not it raises an error)
data = response.json()
# printing the data recived
# Checking if error present
if 'error' in data.keys():
  print(data["error"])
else:
    #  extracting vendorDetails(companyName,companyAddress,countryCode),macAddressDetails(searchTerm,isValid)
  print("-------------------------------------------------------------")
  print("Vendor Details")
  print("-------------------------------------------------------------")
  print("Company Name :" + data['vendorDetails']['companyName'])
  print("Company Address :" + data['vendorDetails']['companyAddress'])
  print("Country Code :" + data['vendorDetails']['countryCode'])
  print("-------------------------------------------------------------")
  print("MAC Address Details")
  print("-------------------------------------------------------------")
  print("MAC Address : " + data['macAddressDetails']['searchTerm'])
  print("Is a Valid MAC address? :" + 'Yes' if data['macAddressDetails']['isValid']==True else 'No')
  print("-------------------------------------------------------------")