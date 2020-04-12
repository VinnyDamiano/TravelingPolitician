
###############################################################################
#
#FILE:  politician.py
#
#USAGE: politician.py INPUTJSONFILE OUTPUTJSONFILE
#
#DESCRIPTION: This file constains a solution to the traveling politician problem.
#             See https://github.com/VinnyDamiano/TravelingPolitician to learn 
#             more about the problem.
#
#DEVELOPER: Vincent Damiano   
#DEVELOPER PHONE: +1 (631)-786-7688
#DEVELOPER EMAIL: vinnyd783@yahoo.com
#
#   
#VERSION 1.0
#CREATED DATE-TIME: 03/22/2020-18:00 Eastern Standard Time  USA
#
#   
#VERSION 1.1
#REVISION DATE-TIME: 04/05/2020-18:00
#DEVELOPER MAKING CHANGE: Vincent Damiano					
#DEVELOPER MAKING CHANGE: PHONE: +1 (631)-786-7688			
#DEVELOPER MAKING CHANGE: EMAIL: vinnyd783@yahoo.com	
#   
###############################################################################
import pandas as pd 
import mpu
import sys
import copy
import itertools
import json

#reading in our zip code date
data = pd.read_csv("zip_codes.csv") 
data = data.drop(["City", "State", "Classification", "Population"], axis = 1)

#calculates the distance between two zip codes
def distance(zip1,zip2):
    x = data.loc[data['ZipCode'] == zip1].index
    y = data.loc[data['ZipCode'] == zip2].index
    #reads the lat and long data from our zipcode data
    lat1 = data.iloc[x[0]]['Latitude']
    lon1 = data.iloc[x[0]]['Longitude']
    lat2 = data.iloc[y[0]]['Latitude']
    lon2 = data.iloc[y[0]]['Longitude']
    kmconstant = .621371
    dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
    #returns distance in miles
    return dist*kmconstant
    
#a dictionary containing the zipcodes of all 50 states capitals and D.C.
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



#creates a permuation of all combinations of states
#middle must be a list of states, start and end are a string
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
      
#given a list of states, calculates distance of that path in order
def pathDistance(lst, minDistance):
    dist = 0
    for i in range(len(lst)-1):
        dist += distance(zipcodes[lst[i]], zipcodes[lst[i+1]])
        if dist > minDistance:
            #return -1 if our distance exceeds our min distance thus far
            return -1
    return dist
        
#solves tarveling politician problem
def politician(start, middle,end):
    allPermutations = perms(start, middle, end)
    #start with our min distance at 2 ^ 31
    minDistance = sys.maxsize
    minIndex = 0
    for i in range(len(allPermutations)):
        tmpDistance = pathDistance(allPermutations[i],minDistance)
        if tmpDistance != -1:
            minIndex = i
            minDistance = tmpDistance
    return(minDistance, ':'.join(allPermutations[minIndex]))
        
import os

if __name__ == "__main__":
    this_dir = os.path.dirname(os.path.realpath(__file__))
    log_path = os.path.join(this_dir, 'log.txt')
    log = open(log_path, 'a+')
    log.write('\n')
    log.write('Args: ' + str(sys.argv) + ' ')
    try:
        with open(sys.argv[1]) as json_data:
            input = json.load(json_data)
            if input is None:
                print("Error: Could not read JSON")
        start = input["start"]
        middle = str.split(input["middle"], sep = ",")
        
        end = input["end"]
        solution = politician(start, middle, end)
        jsonDict = {}
        jsonDict["Input"] = {"Start":start, "Middle":middle, "End": end}
        jsonDict["Distance"] = str(round(solution[0],1)) + " miles"
        jsonDict["Path"] = solution[1]
        
        jsonFile = json.dumps(jsonDict)
        path = sys.argv[2]
        f = open(path, 'w+')
        json.dump(jsonDict, f, indent=4)
        f.close()
    except ValueError as err:
        log.write(str(err))
    except KeyError as err:
        log.write(str(err))
    except OSError as err:
        log.write(str(err))
    except NameError as err:
        log.write(str(err))
    except TimeoutError as err:
        log.write(str(err))
    except:
        log.write("Unknown Error")
        raise
    