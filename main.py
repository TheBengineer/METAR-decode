from xml.dom import minidom
import urllib2
import itertools


def get_METAR(station):
    if station == "atl":
        url = "https://www.aviationweather.gov/adds/dataserver_current/httpparam?datasource=metars&requestType=retrieve&format=xml&mostRecentForEachStation=constraint&hoursBeforeNow=1.25&stationString=Katl"
        response = urllib2.urlopen(url)
        xml_data = response.read()
        xmldoc = minidom.parseString(xml_data)
        return xmldoc.getElementsByTagName('raw_text')[0].childNodes[0]._get_wholeText()
    else:
        return "KATL 211352Z 35003KT 1/8SM R09R/2800VP6000FT FG OVC002 09/08 A3014 RMK AO2 SFC VIS 1/2 RAB22E34 SLP208 P0000 T00890078"


m = [str(u) for u in get_METAR("atl").split(" ")]
print m

station_name = m[0][1:]
print "Station name:", station_name

report_time = m[1]
print "Data recorded on {} at {}:{} zulu time".format(int(report_time[:2]), int(report_time[2:4]), report_time[4:6])

wind_dir = m[2]
wind_dir_num = "".join(itertools.takewhile(str.isdigit, wind_dir))
wind_speeds = {"KT": "Knots", "MPS": "Meters per Second"}

print "Wind is at a speed of {} {} from direction {}".format(int(wind_dir_num[3:]), wind_speeds[wind_dir[len(wind_dir_num):]], wind_dir_num[:3])

# print "Wind direction is varying from {} to {}".format(int(wind_var[:wind_var.find("V")]), int(wind_var[wind_var.find("V"):]))

visibility = m[3]
print "Visibility is {} statute miles".format(visibility[:-2])

runway = m[4]
print "Runway  is {} statute miles".format(visibility[:-2])
