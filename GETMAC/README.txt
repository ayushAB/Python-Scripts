# Get MAC Details

## Prerequisite to run this pyhton program pyhton should be installed
Check if pyhton is installed  run the follwing command in your terminal
```
python -V
```
[Check for installation here](https://docs.python.org/3/using/unix.html#on-linux)

## Running the script
- Clone this repository
- Go to the folder where the getmac.py file is present and open terminal
- Then run the follwing command
```
python getmac.py <your MAC Addresss>
```
# Script explanation
### Algorithm
- Collect user input using sys module
- Construct endpoint to get the mac address detials from https://macaddress.io/ MAC address lookup API(using the apikey provided).
- Use request to make a get request to the above API with the user entered MAC address
- Parese the response to give meaningful information
> Note: `API KEY` can be loaded from enviroment variable as it can cause a security issue.