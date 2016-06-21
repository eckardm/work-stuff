from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader

URL = 'http://uni.edu/ir/oaipmh'

registry = MetadataRegistry()
registry.registerReader('oai_dc', oai_dc_reader)
client = Client(URL, registry)

for record in client.listRecords(metadataPrefix='oai_dc'):
   print record
