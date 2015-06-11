# import what we need
import xmltodict
import json

xml = 'S:/MLibrary/archivematica/backlog/originals/max-0713_0001-251d3e4d-88c5-45b2-ab17-5d058247cffc/metadata/submissionDocumentation/METS.xml'

o = xmltodict.parse(xml)
json.dumps(o)