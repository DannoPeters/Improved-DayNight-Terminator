# Copyright (C) SuperDARN Canada, University of Saskatchewan
# Authors: Marina Schmidt and Danno Peters

#Sources
	# From the Ground Up 29th Ed
	# Aviation Formulary V1.49
	

'''Cordinate Transformation'''
import math
import numpy

class Coord:
	def __init__(self, lat, lon, **kwargs):
		if type(lat) is type(lon):
			self.type = type(lat)
		else:
			pass #error

		if self.type is 'float' or self.type is 'int':
			if "zone" in kwargs:
				self.format = 'UTM'
			else:
				self.format = 'decDeg'

		if type(lat) is 'list':
			self.format = 'DMSlist'
		if type(lat) is 'set':
			self.format = 'DMSset'

		elevList = ['ele','elev','elevation', 'alt', 'altitude', 'height']
		measutmentList = ['unit', 'quantity', 'quant', 'measure', 'measurement', 'denomination', 'denom', 'value', 'val']
		
		for name in elevList:
			if name in kwargs:
				for label in measutmentList:
					if label in kwargs:
						self.elev = distConv(distkwargs[name], label)



'''radarGateCalc
		Finds the GPS centre of all of the gates for a specific radar

	Inputs:	lat1 - iniital lattitude, decimal degrees
			lon1 - initial longitude, decimal degrees
			boresight - radial direction of radar relitive to true noth, decimal degrees
			gates - number of range gates
			gatewidth - physical distance of gates (km)
			beams - number of beams
			beamwidth - radial width of beams

	Output:	lat2 - final lattitude, decinal degrees
			lon2 - final longitude, decimal degrees
'''

def radarGateCalc(lat1, lon1, boresight, gates, gatewidth, beams, beamwidth):
	#coords = [[[0]*2 ] * (beams+1)] * (gates+1) #array of beam and gate locations
	latitudes = numpy.empty([17,76])
	longitudes = numpy.empty([17,76])
	beamCount = 0
	while beamCount <= beams:
		gateCount = 0
		while gateCount <= gates:
			latitudes[beamCount][gateCount], longitudes[beamCount][gateCount] = radialDistance(lat1, lon1, (boresight-((beams/2)*beamwidth)+((beamCount*beamwidth))), (gateCount)*gatewidth, 'km')
			gateCount += 1
		beamCount += 1
	numpy.savetxt("SuperDARN-SAS-BeamGateCorners-Lattitude.csv", latitudes, delimiter=",")
	numpy.savetxt("SuperDARN-SAS-BeamGateCorners-Longitude.csv", longitudes, delimiter=",")
	






'''radialDistance
		Finds the GPS cordinate of a new point, given an initial location, radial, and distance
		Uses the great circle method found in From the Ground Up 29th Ed

	Inputs:	lat1 - iniital lattitude, decimal degrees
			lon1 - initial longitude, decimal degrees
			radial - radial direction of new point relitive to true noth, decimal degrees
			dist - distance to new point in nautical miles
			unit - unit of measure to be converted from to nautical miles

	Output:	lat2 - final lattitude, decinal degrees
			lon2 - final longitude, decimal degrees
'''
def radialDistance(lat1, lon1, radial, dist, unit):
	dist = distConv(dist, unit)
	earthRadius = 6378137 #Radius of the Earth
	earthRadius = elipRadius(lat1, lon1)
	radial = math.radians(radial)
	latCheck = lat1
	lonCheck = lon1
	lat1 = math.radians(lat1) #Current lat point converted to radians
	lon1 = math.radians(lon1) #Current long point converted to radians
	'''error = 1
				
				lat2 = math.asin( math.sin(lat1)*math.cos(dist/earthRadius) + math.cos(lat1)*math.sin(dist/earthRadius)*math.cos(radial))
				lon2 = lon1 + math.atan2(math.sin(radial)*math.sin(dist/earthRadius)*math.cos(lat1), math.cos(dist/earthRadius)-math.sin(lat1)*math.sin(lat2))
			
				lat2 = math.degrees(lat2)
				lon2 = math.degrees(lon2)
			
				print(lat2, lon2)
			
			
				while error > 0.00000000001:
					lat2 = math.asin( math.sin(lat1)*math.cos(dist/earthRadius) + math.cos(lat1)*math.sin(dist/earthRadius)*math.cos(radial))
					lon2 = lon1 + math.atan2(math.sin(radial)*math.sin(dist/earthRadius)*math.cos(lat1), math.cos(dist/earthRadius)-math.sin(lat1)*math.sin(lat2))
			
					lat2 = math.degrees(lat2)
					lon2 = math.degrees(lon2)
					error = abs(lat2-latCheck)+abs(lon2-lonCheck)
					#print(error)
					earthRadius = elipRadius(lat2, lon2)
					latCheck = lat2
					lonCheck = lon2
					lat2 = math.radians(lat2)
					lon2 = math.radians(lon2)
				print("{lat}, {lon}".format(lat=math.degrees(lat2), lon=math.degrees(lon2)))
			'''
	sectionLength = 45000
	sections = int(dist/sectionLength)
	lastSection = dist%sectionLength

	lat3 = lat1
	lon3 = lon1

	#print(math.degrees(radial))
	for test in range(sections):
		earthRadius = elipRadius(lat3, lon3)
		lat2 = math.asin( math.sin(lat3)*math.cos(sectionLength/earthRadius) + math.cos(lat3)*math.sin(sectionLength/earthRadius)*math.cos(radial))
		lon2 = lon3 + math.atan2(math.sin(radial)*math.sin(sectionLength/earthRadius)*math.cos(lat3), math.cos(sectionLength/earthRadius)-math.sin(lat3)*math.sin(lat2))
		lat3 = lat2
		lon3 = lon2
		#print("{lat}, {lon}".format(lat=math.degrees(lat3), lon=math.degrees(lon3)))
	earthRadius = elipRadius(lat3, lon3)
	lat2 = math.asin( math.sin(lat3)*math.cos(lastSection/earthRadius) + math.cos(lat3)*math.sin(lastSection/earthRadius)*math.cos(radial))
	lon2 = lon3 + math.atan2(math.sin(radial)*math.sin(lastSection/earthRadius)*math.cos(lat3), math.cos(lastSection/earthRadius)-math.sin(lat3)*math.sin(lat2))
	lat2 = math.degrees(lat2)
	lon2 = math.degrees(lon2)
	#print(lat2, lon2)

	

	return lat2, lon2

def elipRadius(lattitude, longitude):
	semiMajor = 6378137.0
	flatteningCoef = 0.00335281068
	eplipsoid = {   'semiMajor' : semiMajor, 
					'flatteningRecip' : 1/flatteningCoef, 
					'semiMinor' : semiMajor*(1-flatteningCoef), 
					'firstEccentricity' : numpy.sqrt(abs(1-(pow((semiMajor*(1-flatteningCoef)),2))/(pow(semiMajor,2)))),
					'secondEccentricity' : numpy.sqrt(abs((pow((semiMajor*(1-flatteningCoef)),2))/(pow(semiMajor,2))-1))}
	elipsoidRadius = numpy.sqrt((pow((pow(eplipsoid['semiMajor'],2)*numpy.cos(lattitude)),2) +pow((pow(eplipsoid['semiMinor'],2)*numpy.sin(lattitude)),2))/(pow((eplipsoid['semiMajor']*numpy.cos(lattitude)),2) +pow((eplipsoid['semiMinor']*numpy.sin(lattitude)),2)))
	return elipsoidRadius

#Uses WGS84 sea level correction using bilinear interpolation of point table
def altitudeCorrection(latitude, longitude, elevation):
    if elevation < 100:
        #use geoid model if near ground
        for line in open('WGS84-elev-grid.txt'): #finds 4 points surrounding GPS location
            splitLine = line.split('\\s')
            if numpy.floor(lattitude*2)/2 is float(splitLine[0]) and numpy.floor(longitude*2)/2 is float(splitLine[1]):
                elevationCorr[0][0] = float(splitLine[2])
            if numpy.ceil(lattitude*2)/2 is float(splitLine[0]) and numpy.ceil(longitude*2)/2 is float(splitLine[1]):
                elevationCorr[1][1] = float(splitLine[2])
            if numpy.floor(lattitude*2)/2 is float(splitLine[0]) and numpy.ceil(longitude*2)/2 is float(splitLine[1]):
                elevationCorr[0][1] = float(splitLine[2])
            if numpy.ceil(lattitude*2)/2 is float(splitLine[0]) and numpy.floor(longitude*2)/2 is float(splitLine[1]):
                elevationCorr[1][0] = float(splitLine[2])
    else:
        #use elipsoid for atmospheric calculations
        #configured for WGS84 elipsoid
        semiMajor = 6378137.0
        flatteningCoef = 0.00335281068
        eplipsoid = {   'semiMajor' : semiMajor, 
                        'flatteningRecip' : 1/flatteningCoef, 
                        'semiMinor' : semiMajor*(1-flatteningCoef), 
                        'firstEccentricity' : numpy.sqrt(abs(1-(pow((semiMajor*(1-flatteningCoef)),2))/(pow(semiMajor,2)))),
                        'secondEccentricity' : numpy.sqrt(abs((pow((semiMajor*(1-flatteningCoef)),2))/(pow(semiMajor,2))-1))}
        elipsoidRadius = numpy.sqrt((pow((pow(eplipsoid['semiMajor'],2)*numpy.cos(lattitude)),2) +pow((pow(eplipsoid['semiMinor'],2)*numpy.sin(lattitude)),2))/(pow((eplipsoid['semiMajor']*numpy.cos(lattitude)),2) +pow((eplipsoid['semiMinor']*numpy.sin(lattitude)),2)))
        
    
    #Bilinear interpolation of geoid model

    altitudeCorr = -2.076*numpy.sqrt(altitude)/60

'''distConv
		Finds the GPS cordinate of a new point, given an initial location, radial, and distance
		Uses the great circle method found in From the Ground Up 29th Ed

	Inputs:	dist - distance to convert
			label - unit of measure to be converted from to nautical miles

	Output:	distNM - distance in nautical miles
'''
def distConv(dist, unit):

	unitDict = {'ft': ['foot', 'ft', 'feet', ''], 
					'in': ['in', 'inch', "'"],
					'm':['m', 'meter', 'meters'], 
					'km': ['km', 'kilometer', 'kilo'],
					'cm': ['centimeter', 'cent', 'cm'],
					'mi':['mi', 'mile', 'miles'],
					'yd': ['yd', 'yard', 'yards'],
					'nm': ['nm', 'natical mile', 'nautical miles']}

	unitConv = {"km": 1000, "m": 0, "cm": 1/100, "mi": 1609.34, "yd": 0.9144, "ft": 0.3048, "in": 0.0254, 'nm': 1852}

	for label in unitDict:
		for variation in unitDict[label]:
			if variation == unit.lower():
				distKm = unitConv[label]*dist
				return distKm
			else:
				pass #error
	print("Unknown Unit")
	return dist

'''deg2DMS
		Finds the GPS cordinate of a new point, given an initial location, radial, and distance
		Uses the great circle method found in From the Ground Up 29th Ed

	Inputs:	dist - distance to convert
			unit - unit of measure to be converted from to nautical miles

	Output:	distNM - distance in nautical miles
'''
def deg2DMS(lat, lon):
	lat2 = {'degree': 0, 'minuite': 0, 'second': 0}
	lon2 = {'degree': 0, 'minuite': 0, 'second': 0}

	return lat2, lon2

#for deg in range (0,360, 5):
#	print(radialDistance(52.142556, -106.616329,deg, 3000, 'km'))

#print(radialDistance(52.142556, -106.616329, 88, 3233, 'km'))
radarGateCalc(52.160, -106.530, 23.1, 75, 45, 16, 3.24)




