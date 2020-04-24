# TravelingPolitician
A politician hopes to become the president of the United States. Their campaign starts with the presidential primaries in the capital of Iowa. The politician then wants to visit the capital of every U.S. state to campaign before ending in the White House in the nation's capital of Washington, D.C. The politician does not want to visit any capital more than once. They would like to campaign in every capital one and only once. To be efficient and save on time and money, they would like to do this in as short a path as possible. The Traveling Politician Problem aims to find this shortest path. The map can be thought of as a graph with 51 points (the capitals of all 50 U.S. states, plus Washington, D.C.) and a set of distances between each of them. The starting point and ending point are already set (the capital of Iowa and Washington, D.C., respectively). This leaves 49 points to be visited in between the starting and ending points, this does not include the start and end points.

This problem is much harder than it may sound. The main solution to the problem is factorial time-that is, the time it takes to solve will be proportional to 49!. It is not 51! because the starting and ending cities are already set. After starting in Iowa, one of the 49 remaining capitals can be chosen as the first one to travel to. Now that one of the 49 has been chosen as the first, one of the remaining 48 capitals can be chosen as the second to travel to. Now there are 47 remaining capitals to choose as the third, and so on. The total number of paths to be compared will be 49x48x47x ... 3x2x1, which is 49! (49 factorial). This evaluates to around 6*10^62 different total paths to be compared. That's around a trillion trillion trillion trillion trillion. 

One particular mistake is very easy to make here: why not just find the shortest path from the capital of Iowa to any other one state capital, then take the shortest path from there to any other one state capital, and then keep going until you wind up in D.C.? This could possibly give you a better solution than trillions of trillions of other solutions, but it's unlikely to give you the very best overall path to D.C. For example, let's say we only visit Texas and California in the middle: the distance from Iowa to Texas is shorter than the distance from Iowa to California, so you go to Texas first and then to California and then to D.C. This is around 5,300 miles. It's longer to go to California first than to Texas, but if you visit California first, then Texas, then D.C., you get around 4,900 miles, which is the shorter path. As you can see, finding the shortest distance from one capital to another at any given point is not necessarily going to give you the shortest overall path to visit each capital only once. 

This problem is based on the "Traveling Salesman Problem", which is a well-known graph theory problem that has been heavily studied by mathematicians. Many resources are available to study this problem under the title "Traveling Salesman Problem".

https://en.wikipedia.org/wiki/Travelling_salesman_problem

## Getting Started 

### Prerequisites

In order for this file to run, you must install the pandas and mpu this can be done with the following:

```
pip install mpu
pip install pandas
```
It is also neccesary to have the zip_codes.csv file, from this repository, in the same folder as the politician.py file. You should have have your JSON files, in the same directory as well.

### Running on Windows
To run this, type in the following command:

```
python politician.py JSONINPUTFILE JSONOUTPUTFILE
```

### Running on Linux and Mac
To run this, type in the following command:

```
python3 politician.py JSONINPUTFILE JSONOUTPUTFILE
```

### JSON Input File

Your json input file has three fields start middle and end. Both start and end should be a single state in which you chose to begin and end your path. Middle should be a list of states seperated by a comma.

States should be the 2 letter nationally recognized abreviation of each state. For example, Iowa is IA and New York is NY.

Washington D.C. should be abreviated as DC

An example of a json file is provied named test.json. You json file should be similiar to the one below:

```
{
    "start": "IA",
    "middle": "NY,WA,CA",
    "end": "DC"
}
```

### JSON Output File

Your Json output file should have both a distance and a path field. Each time we run the program, this file will be written with the solution. I provided the template above named solution.json. An example of what the output file would look like after running our above input file is the following:

```
{
    "Input": {
      "Start": "IA",
      "Middle": "CA,WA,NY",
      "End": "DC"
    },
    "Distance": "4762.3 miles",
    "Path": "IA:CA:WA:NY:DC"
}
```

### Adding More Locations

To add or change location you will want to open the politician.py file. In that file on line 35-86 is a dictionary called zipcodes. To add a new location simply add the following code on line 87:

```
zipcodes["ABREVIATION"] = ZIPCODE
```
### Runtime Aanalysis

The current system specs that I am running this program on are:
```
OS: Windows 10
Processor: Intel(R) Core(TM) i7-7500u CPU @ 2.7 GHz
System Type: 64 Bit OS x-64 based processor
```
I was able to collect the following data:

![Runtime Data](C:/Users/vnjda/Desktop/ERT JOB/runtime.PNG)

From this data we see that we have a factorial curve. To predict the time needed for more states, we can use the equation:

```
Seconds = (Number of Middle States)! / 100
```

### Authors 
* **Vincent Damiano** 
* **Verbus Counts** 
* **Trent Rogers**
