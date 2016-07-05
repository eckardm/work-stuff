from tiers import tier_1_list, tier_2_list, tier_3_list

import csv
import plotly.plotly as py

tier_1_count = 0
tier_2_count = 0
tier_3_count = 0

with open("droid_sho.csv", mode="rb") as droid_sho:
    reader = csv.DictReader(droid_sho)
    for row in reader:
        
        if "." + row.get("EXT", "").lower() in tier_1_list:
            tier_1_count += 1
        elif "." + row.get("EXT", "").lower() in tier_2_list:
            tier_2_count += 1
        else:
            tier_3_count += 1

basic_pie_chart = {
    "data": [{
        "labels": ["Tier 1 (Sustainable Formats)", 'Tier 2 (Common "At-Risk" Formats)', "Tier 3 (Weird Stuff)"],
        "values": [tier_1_count, tier_2_count, tier_3_count],
        "type": "pie"}],
    "layout": {
        "title": '<b>Tiers of Original Files in Dark Archive</b> (<i>n</i>=731,942)<br>See <a href="http://bentley.umich.edu/about/what-we-do/digital-curation-strategies-and-procedures/680-2/">Format Conversion Strategies for Long-Term Preservation</a> for More Information'}
}

py.plot(basic_pie_chart)
     