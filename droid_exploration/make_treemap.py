from tiers import tier_1_list, tier_2_list, tier_3_list

import csv
import plotly.plotly as py
import plotly.graph_objs as go
from collections import Counter
import squarify

tier_3_formats = []

with open("droid_sho-with_normalized_files.csv", mode="rb") as droid_sho:
    reader = csv.DictReader(droid_sho)
    for row in reader:
        
        if "." + row.get("EXT", "").lower() in tier_1_list:
            continue
            
        elif "." + row.get("EXT", "").lower() in tier_2_list:
            continue 
            
        else:
            tier_3_formats.append(row.get("FORMAT_NAME"))
            
x = 0.
y = 0.
width = 100.
height = 100.

values = []
values_text = []

for tier_3_format, count in Counter(tier_3_formats).most_common():
    # otherwise this gets a little unwieldy...
    if tier_3_format != "" and count > 100:
        values.append(count)
        values_text.append(tier_3_format)
    
normed = squarify.normalize_sizes(values, width, height)
rects = squarify.squarify(normed, x, y, width, height)

# Choose colors from http://colorbrewer2.org/ under "Export"
color_brewer = ['rgb(166,206,227)','rgb(31,120,180)','rgb(178,223,138)',
                'rgb(51,160,44)','rgb(251,154,153)','rgb(227,26,28)',
                'rgb(253,191,111)','rgb(255,127,0)','rgb(202,178,214)',
                'rgb(106,61,154)','rgb(255,255,153)','rgb(177,89,40)']

shapes = []
annotations = []
color_counter = 0
name_counter = 0

for r in rects:
    shapes.append( 
        dict(
            type = 'rect', 
            x0 = r['x'], 
            y0 = r['y'], 
            x1 = r['x']+r['dx'], 
            y1 = r['y']+r['dy'],
            line = dict( width = 2 ),
            fillcolor = color_brewer[color_counter]
        ) 
    )
    annotations.append(
        dict(
            x = r['x']+(r['dx']/2),
            y = r['y']+(r['dy']/2),
            text = values_text[name_counter],
            showarrow = False
        )
    )
    name_counter = name_counter + 1
    color_counter = color_counter + 1
    if color_counter >= len(color_brewer):
        color_counter = 0

# For hover text
trace = go.Scatter(
    x = [ r['x']+(r['dx']/2) for r in rects ], 
    y = [ r['y']+(r['dy']/2) for r in rects ],
    text = [ str(v) for v in values ], 
    mode = 'text',
)
        
layout = dict(
    height=700, 
    title='Tier 3 Formats if Count is Over 100 in the Dark Archive (<i>n</i>=261,669)<br>See <a href="http://bentley.umich.edu/about/what-we-do/digital-curation-strategies-and-procedures/680-2/">Format Conversion Strategies for Long-Term Preservation</a> for More Information',
    width=700,
    xaxis=dict(showgrid=False,zeroline=False),
    yaxis=dict(showgrid=False,zeroline=False),
    shapes=shapes,
    annotations=annotations,
    hovermode='closest'
)

treemap = dict(data=[trace], layout=layout)

py.plot(treemap)
