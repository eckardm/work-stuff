from tiers import tier_1_list, tier_2_list, tier_3_list

import csv
import plotly.plotly as py
from collections import Counter

tier_1_formats = []
tier_2_formats = []
tier_3_formats = []

with open("droid_sho-with_normalized_files.csv", mode="rb") as droid_sho:
    reader = csv.DictReader(droid_sho)
    for row in reader:
        
        # skip normalized files
        if "_bhl-" in row.get("NAME", ""):
            continue
        
        if "." + row.get("EXT", "").lower() in tier_1_list:
            tier_1_formats.append(row.get("FORMAT_NAME"))
            
        elif "." + row.get("EXT", "").lower() in tier_2_list:
            tier_2_formats.append(row.get("FORMAT_NAME"))
                
        else:
            tier_3_formats.append(row.get("FORMAT_NAME"))
                
donut_chart = {
  "data": [
    {
      "values": [
        Counter(tier_1_formats).most_common(5)[0][1], 
        Counter(tier_1_formats).most_common(5)[1][1], 
        Counter(tier_1_formats).most_common(5)[2][1], 
        Counter(tier_1_formats).most_common(5)[3][1], 
        Counter(tier_1_formats).most_common(5)[4][1], 
      ],
      "labels": [
        Counter(tier_1_formats).most_common(5)[0][0], 
        Counter(tier_1_formats).most_common(5)[1][0], 
        Counter(tier_1_formats).most_common(5)[2][0], 
        Counter(tier_1_formats).most_common(5)[3][0], 
        Counter(tier_1_formats).most_common(5)[4][0], 
      ],
      "domain": {"x": [0, .48],
                 "y": [.52, 1]},
      "name": "Tier 1",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },     
    {
      "values": [
        Counter(tier_2_formats).most_common(5)[0][1], 
        Counter(tier_2_formats).most_common(5)[1][1], 
        Counter(tier_2_formats).most_common(5)[2][1], 
        Counter(tier_2_formats).most_common(5)[3][1], 
        Counter(tier_2_formats).most_common(5)[4][1], 
      ],
      "labels": [
        Counter(tier_2_formats).most_common(5)[0][0], 
        Counter(tier_2_formats).most_common(5)[1][0], 
        Counter(tier_2_formats).most_common(5)[2][0], 
        Counter(tier_2_formats).most_common(5)[3][0], 
        Counter(tier_2_formats).most_common(5)[4][0], 
      ],
      "domain": {"x": [.52, 1],
                 "y": [.52, 1]},
      "name": "Tier 2",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },
    {
      "values": [
        Counter(tier_3_formats).most_common(5)[0][1], 
        Counter(tier_3_formats).most_common(5)[1][1], 
        Counter(tier_3_formats).most_common(5)[2][1], 
        Counter(tier_3_formats).most_common(5)[3][1], 
        Counter(tier_3_formats).most_common(5)[4][1], 
      ],
      "labels": [
        Counter(tier_3_formats).most_common(5)[0][0], 
        Counter(tier_3_formats).most_common(5)[1][0], 
        Counter(tier_3_formats).most_common(5)[2][0], 
        Counter(tier_3_formats).most_common(5)[3][0], 
        Counter(tier_3_formats).most_common(5)[4][0], 
      ],
      "domain": {"x": [.26, .74],
                 "y": [0, .48]},      
      "name": "Tier 3",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    }],
  "layout": {
        "title":'<b>Top Five Original File Formats per Tier in Dark Archive</b> (<i>n</i>=761,942)<br>See <a href="http://bentley.umich.edu/about/what-we-do/digital-curation-strategies-and-procedures/680-2/">Format Conversion Strategies for Long-Term Preservation</a> for More Information',
        "showlegend": False,
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Tier 1",
                "x": 0.22,
                "y": 0.78
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": 'Tier 2',
                "x": 0.78,
                "y": 0.78
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Tier 3",
                "x": 0.5,
                "y": 0.22
            }
        ]
    }
}

py.plot(donut_chart)
