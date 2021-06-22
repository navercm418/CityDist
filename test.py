import urllib.request

InFile = "cities.txt"
OutFile = "out.txt"

# ---------------------------------------------------------------------------------------------------
           # Holbrook,+MA
def DistCalc(city):
    _city = city
                 # https://www.travelmath.com/driving-time/from/Lowell,+MA/to/Middleborough,+MA
                 # <h3 class="space" id="drivetime">51 minutes</h3>
    zvHttpTrip = r'https://www.travelmath.com/driving-time/from/Lowell,+MA/to/'+ _city
            
    zvTripOut = urllib.request.urlopen(zvHttpTrip).read()
    zvTripOutFmt = zvTripOut.decode()
    zvTxt = str(zvTripOutFmt)
    zvTxt = zvTxt.split('<h3 class="space" id="drivetime">')[1]
    zvTxt = zvTxt.split(' minutes</h3>')[0]
    zvOut = zvTxt

    return zvOut
# ---------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------


# Using readlines()
file1 = open(InFile, 'r')
Lines = file1.readlines()
 
for line in Lines:
    _ln = line.strip()

    if _ln == 'Middleborough+Center,+MA':
        print(_ln + '|1hr')

    elif _ln == 'Lowell,+MA':
        print(_ln + '|0')

    elif _ln == 'Millis-Clicquot,+MA':
        _ln = 'Millis,+MA'
        print(_ln + '|' + DistCalc(_ln))

    elif _ln == 'Mansfield+Center,+MA':
        _ln = 'Mansfield,+MA'
        print(_ln + '|' + DistCalc(_ln))

    elif _ln == 'Norton+Center,+MA':
        _ln = 'Norton,+MA'
        print(_ln + '|' + DistCalc(_ln))

    else:
        print(_ln)
        print(_ln + '|' + DistCalc(_ln))


# print(DistCalc('Holbrook,+MA'))
