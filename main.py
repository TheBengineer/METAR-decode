from xml.dom import minidom
import urllib2


def get_METAR(station):
    if station == "atl":
        url = "https://www.aviationweather.gov/adds/dataserver_current/httpparam?datasource=metars&requestType=retrieve&format=xml&mostRecentForEachStation=constraint&hoursBeforeNow=1.25&stationString=Katl"
        response = urllib2.urlopen(url)
        xml_data = response.read()
        xmldoc = minidom.parseString(xml_data)
        return xmldoc.getElementsByTagName('raw_text')[0].childNodes[0]._get_wholeText()
    else:
        return "KATL 211352Z 35003KT 1/8SM R09R/2800VP6000FT FG OVC002 09/08 A3014 RMK AO2 SFC VIS 1/2 RAB22E34 SLP208 P0000 T00890078"


m = get_METAR("atl").split(" ")

station_name = m[0][1:]
print "Station name:", station_name

station_name = m[1][1:]
print "Station name", station_name
