import urllib.request


zvHttpTrip = r'https://www.travelmath.com/driving-time/from/Lowell,+MA/to/Holbrook,+MA'
        
zvTripOut = urllib.request.urlopen(zvHttpTrip).read()
zvTripOutFmt = zvTripOut.decode()

print(zvTripOutFmt)
