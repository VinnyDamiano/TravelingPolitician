import pandas as pd 
import mpu
import sys
import copy
import itertools

data = pd.read_csv("zip_codes.csv") 
data = data.drop(["City", "State", "Classification", "Population"], axis = 1)


def distance(zip1,zip2):
    x = data.loc[data['ZipCode'] == zip1].index
    y = data.loc[data['ZipCode'] == zip2].index
    lat1 = data.iloc[x[0]]['Latitude']
    lon1 = data.iloc[x[0]]['Longitude']
    lat2 = data.iloc[y[0]]['Latitude']
    lon2 = data.iloc[y[0]]['Longitude']
    kmconstant = .621371
    dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
    return dist*kmconstant
    
def V1_0():
    dict = {"IA:DC": distance(50301, 20500)}
    return ("IA:DC",dict["IA:DC"])
    
    
def V1_1():
    iowaCal = distance(50301,94203)
    calDC = distance(94203, 20500)
    return iowaCal + calDC
    
def V1_2():
    calNY = distance(94203,12201)
    iowaCal  = distance(50301,94203)
    nyDC = distance(12201, 20500)
    option1 = calNY + iowaCal + nyDC
    iowaNY = distance(50301, 94203)
    calDC = distance(94203,20500)
    option2 = iowaNY + iowaCal + calDC
    return min(option1,option2) 

def v1_3():
    dict = {}
    iowaWash = distance(50301, 98501)
    washNY = distance(12201,98501)
    nyCal =  distance(12201, 94203)
    calDC = distance(94203, 20500)
    dict["IA:WA:NY:CA:DC"] = iowaWash + washNY + nyCal + calDC
    washCal = distance(98501,94203)
    nyDC = distance(12201,20500)
    dict["IA:WA:CA:NY:DC"] = iowaWash + washCal + nyCal + nyDC
    iowaCal  = distance(50301,94203)
    dict["IA:CA:WA:NY:DC"] = iowaCal + washCal + washNY + nyDC
    washDC = distance(20500, 98501)
    dict["IA:CA:NY:WA:DC"] = iowaCal + nyCal + washNY + washDC
    iowaNY = distance(12201, 94203)
    dict["IA:NY:CA:WA:DC"] = iowaNY + nyCal + washCal + washDC
    dict["IA:NY:WA:CA:DC"] = iowaNY + washNY + washCal + calDC
    key_min = min(dict.keys(), key=(lambda k: dict[k]))
    return (key_min, dict[key_min])
     
zipcodes = {
"AL": 36101,  #Alabama
"AK": 99801,  #Alaska
"AZ": 85001,  #Arizona
"AS": 72201,  #Arkansas
"CA": 94203,  #California
"CO": 80201,  #Colorado
"CT": 6101,   #Conneticut
"DE": 19901,  #Delaware
"FL": 32301,  #Florida
"GA": 30301,  #Georgia
"HI": 96801,  #Hawaii
"ID": 83701,  #Idaho
"IL": 62701,  #Illinois
"IN": 46201,  #Indiana
"IA": 50301,  #Iowa
"KS": 66601,  #Kansas
"KY": 40601,  #Kentucky
"LA": 70801,  #Louisiana
"ME": 4330,   #Maine
"MD": 21401,  #Maryland
"MA": 2108,   #Massachusets
"MI": 48901,  #Michigan
"MN": 55101,  #Minnesota
"MS": 39201,  #Missisipi
"MO": 65101,  #Missouri
"MT": 59601,  #Montanta
"NE": 68501,  #Nebraska
"NV": 89701,  #Nevada
"NH": 3301,   #New Hampshire
"NJ": 8601,   #New jersey
"NM": 87501,  #New mexico
"NY": 12201,  #New york
"NC": 27601,  #North carolina
"ND": 58501,  #North dakota
"OH": 43201,  #ohio
"OK": 73101,  #oklahoma
"OR": 97301,  #oregon
"PA": 17101,  #pennslyvania
"RI": 2901,   #rhode island
"SC": 29201,  #south carolina
"SD": 57501,  #south dakota
"TN": 37201,  #tennesee
"TX": 73301,  #texas
"UT": 84101,  #utah
"VT": 5601,   #vermont
"VA": 23218,  #virgina
"WA": 98501,  #washington
"WV": 25301,  #west virgina
"WI": 53701,  #wisconsin
"WY": 82001,  #wyoming
"DC": 20500}  #DC

                
                            
def perms(start, middle, end):
    perms = itertools.permutations(middle)
    perms = list(perms)
    finalPerms = []
    for i in range(len(perms)):
        cur = list(perms[i])
        cur.append(end)
        cur.insert(0,start)
        finalPerms.append(cur)
    return finalPerms
      
def pathDistance(lst, minDistance):
    dist = 0
    for i in range(len(lst)-1):
        dist += distance(zipcodes[lst[i]], zipcodes[lst[i+1]])
        if dist > minDistance:
            return -1
    return dist
        

def politician(start, middle,end):
    allPermutations = perms(start, middle, end)
    minDistance = sys.maxsize
    minIndex = 0
    for i in range(len(allPermutations)):
        tmpDistance = pathDistance(allPermutations[i],minDistance)
        if tmpDistance != -1:
            minIndex = i
            minDistance = tmpDistance
    return(minDistance, ':'.join(allPermutations[minIndex]))
        
    
if __name__ == "__main__":
    start = input("Start: ")
    middle = input("Middle: ")
    end = input("End: ")
    newMid = []
    for i in range(0,len(middle),2):
        newMid.append(middle[i:i+2])
    print(politician(start, newMid, end))
    