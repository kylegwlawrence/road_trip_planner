from OSMPythonTools.overpass import Overpass, overpassQueryBuilder
from OSMPythonTools.nominatim import Nominatim
from tags import list_tags
#overpass = Overpass()
#result = overpass.query('way["name"="Vienna"]; out body;')

#r = result.elements()[0]

#for tag in list_tags():
 #   if r.tag(tag)!=None:
  #      print(f"{tag}: {r.tag(tag)}")

user_agent = "hikylelawrence@protonmail.com // OSMPythonTools/0.3.5 (https://github.com/mocnik-science/osm-python-tools)"

nominatim = Nominatim(userAgent='road_trip_planner')
areaId = nominatim.query('Vienna, Austria').areaId()
overpass = Overpass()
query = overpassQueryBuilder(area=areaId, elementType='node', selector='"natural"="tree"', out='count')
result = overpass.query(query)
print(result.countElements())