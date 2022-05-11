from mpl_toolkits.basemap import Basemap
import numpy as np
import csv
import urllib2
import re
import matplotlib.pyplot as plt
"""Requires matplotlib version < 2.0.0 to run"""
#stop the interactive plotting window from popping up
plt.ioff()
#get URL of csv data so that the results of this program update as the csv does
url = "http://chargepoints.dft.gov.uk/api/retrieve/registry/format/csv"
#open the csv file from this URL
response = urllib2.urlopen(url, 'rU')
#read the csv
cr = csv.reader(response, delimiter = ',')
#extract the data
csvdata = [row for i, row in enumerate(cr) if i > 10]
#problem with pulling it off the internet is it's full of crap
#do this to get only the good stuff and ignore the crap
longitudes = []
latitudes = []
for i in csvdata:
#search for the latitude and longitude fields
	lontemp = re.search("<Longitude>(.*)</Longitude>", i[0])
	if str(type(lontemp)) != "<type 'NoneType'>":
		longitudes.append(lontemp.group(1))
	lattemp = re.search("<Latitude>(.*)</Latitude>", i[0])
	if str(type(lattemp)) != "<type 'NoneType'>":
		latitudes.append(lattemp.group(1))
#convert strings to floats
longitudes = [float(i) for i in longitudes]
latitudes = [float(i) for i in latitudes]

#fig = plt.figure()
#plot it up on a map focussed in on the UK
#map = Basemap(projection='ortho', lat_0=50, lon_0=0, resolution='l')
map = Basemap(llcrnrlon = -12.0, llcrnrlat = 48.0, urcrnrlon = 5.0, urcrnrlat = 62.0, resolution = 'h')
map.drawcoastlines()
map.drawcountries()
#map.drawlsmask(land_color = 'green', ocean_color = 'aqua')

map.scatter(longitudes, latitudes, latlon = True, marker = '.')
#save that shit!
plt.savefig("C:\\Users\\User\\Documents\\Python\\EV Charging Stations\\ChargingStations.png", dpi = 600)
plt.close('all')