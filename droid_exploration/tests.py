import csv

'''
materials produced in sustainable formats will be maintained in their original version'''
tier_1_list = [
    # office documents and text-based files
    # docx
    ".docx", 
    ".docm", 
    # xlsx
    ".xlsx", 
    ".xlsm", 
    # pptx
    ".pptx", 
    ".pptm", 
    # odt
    ".odt", 
    ".fodt", 
    # ods
    ".ods", 
    ".fods", 
    # odp
    ".odp", 
    ".fodp", 
    # pdf/a
    ".pdf", # <-- will this work?
    # txt
    ".txt", 
    # rtf
    ".rtf", 
    # xml
    ".xml", 
    # csv
    ".cxv", 
    # tsv
    ".tsv", 
    ".tab", 
    # audio files
    # wav
    ".wav", 
    ".wave", 
    # aiff
    ".aiff", 
    ".aif", 
    ".aifc", 
    # mp3
    ".mp3", 
    # flac
    ".flac", 
    # ogg
    ".ogg", 
    ".ogv", 
    ".oga", 
    ".ogx", 
    ".ogm", 
    ".spx", 
    ".opus", 
    # video files
    # mpeg-1/2
    ".mpg", 
    ".mpeg", 
    ".mp1", 
    ".mp2", 
    ".mp3", 
    ".m1v", 
    ".m1a", 
    ".m2a", 
    ".mpa", 
    ".mpv", 
    ".mpg", 
    ".mpeg", 
    ".m2v", 
    ".mp3", 
    # avi
    ".avi", 
    # mov
    ".mov", 
    ".qt", 
    # mp4
    ".mp4", 
    ".m4a", 
    ".m4p", 
    ".m4b", 
    ".m4r", 
    ".m4v", 
    # mj2
    ".mj2", 
    ".mjp2", 
    # dv
    ".dv", 
    ".dif", 
    # raster (or bitmap) image files
    # tiff
    ".tiff", 
    ".tif", 
    # jpeg/jfif
    ".jpg", 
    ".jpeg", 
    ".jpe", 
    ".jif", 
    ".jfif", 
    ".jfi", 
    # jpeg 2000
    ".jp2", 
    ".j2k", 
    ".jpf", 
    ".jpx",
    ".jpm",
    ".mj2", 
    # gif
    ".gif", 
    # png
    ".png", 
    # vector image files
    # svg
    ".svg", 
    ".svgz", 
    # email files
    # mbox
    ".mbox", 
    # database files
    # csv
    ".csv", 
    # siard
    ".siard", 
    # mysql sql
    ".sql"
]

'''
common "at-risk" formats will be converted to preservation-quality file types to retain important features and functionalities'''
tier_2_list = [
    # audio files
    # wma
    ".asf", 
    ".wma", 
    ".wmv", 
    # ra
    ".ra", 
    ".ram", 
    # snd
    ".snd", 
    # au
    ".au", 
    ".snd", 
    # office documents and text-based files
    # doc
    ".doc", 
    # ppt
    ".ppt", 
    # xls
    ".xls", 
    # email files
    # eml
    ".eml", 
    # pst
    ".pst", 
    # eudora
    ".csom", 
    ".euhl", 
    ".mbx", 
    ".pce", 
    ".rce", 
    ".sta", 
    ".toc", 
    # raster image files
    # bmp
    ".bmp", 
    ".dib", 
    # psd
    ".psd", 
    # fpx
    ".fpx", 
    # pcd
    ".pcd", 
    # pct
    ".pict", 
    ".pct", 
    ".pic", 
    # tga
    ".tga", 
    # vector image files
    # ai
    ".ai", 
    # wmf
    ".wfm", 
    ".emf", 
    ".wmz", 
    ".emz", 
    # ps
    ".ps", 
    # eps
    ".eps", 
    ".epsf", 
    ".epsi", 
    # video files
    # swf
    ".swf", 
    # flv
    ".flv", 
    ".f4v", 
    ".f4p", 
    ".f4a", 
    ".f4b", 
    # wmv
    ".asf", 
    ".wma", 
    ".wmv", 
    # rv
    ".rv"
]

'''
all other content will receive basic bit-level preservation'''
tier_3_list = []

normalized = 0
total = 0
tier_1_count = 0
tier_1_formats = []
tier_2_count = 0
tier_2_formats = []
tier_3_count = 0
tier_3_formats = []

tiers_dicts = {}
formats_dict = {}
mime_type_dict = {}

with open("droid_sho-with_normalized_files.csv", mode="rb") as droid_sho:
    reader = csv.DictReader(droid_sho)
    for row in reader:
        
        if "_bhl-" in row.get("NAME", ""):
            normalized += 1
            continue
        
        total += 1
        
        if row.get("FORMAT_NAME", "") not in formats_dict:
            formats_dict[row.get("FORMAT_NAME")] = 1
        else:
            formats_dict[row.get("FORMAT_NAME")] += 1
            
        if row.get("MIME_TYPE", "") not in formats_dict:
            formats_dict[row.get("MIME_TYPE")] = 1
        else:
            formats_dict[row.get("MIME_TYPE")] += 1
        
        if row.get("LAST_MODIFIED", "").split("-")[0] not in tiers_dicts:
            tiers_dicts[row.get("LAST_MODIFIED", "").split("-")[0]] = {}
        
        if "." + row.get("EXT", "").lower() in tier_1_list:
            tier_1_count += 1
            tier_1_formats.append(row.get("FORMAT_NAME"))
            if "tier_1" not in tiers_dicts[row.get("LAST_MODIFIED", "").split("-")[0]]:
                tiers_dicts[row.get("LAST_MODIFIED", "").split("-")[0]]["tier_1"] = 1
            else:
                tiers_dicts[row.get("LAST_MODIFIED", "").split("-")[0]]["tier_1"] += 1
            
        elif "." + row.get("EXT", "").lower() in tier_2_list:
            tier_2_count += 1
            tier_2_formats.append(row.get("FORMAT_NAME"))
            if "tier_2" not in tiers_dicts[row.get("LAST_MODIFIED", "").split("-")[0]]:
                tiers_dicts[row.get("LAST_MODIFIED", "").split("-")[0]]["tier_2"] = 1
            else:
                tiers_dicts[row.get("LAST_MODIFIED", "").split("-")[0]]["tier_2"] += 1
                
        else:
            tier_3_count += 1
            tier_3_formats.append(row.get("FORMAT_NAME"))
            if "tier_3" not in tiers_dicts[row.get("LAST_MODIFIED", "").split("-")[0]]:
                tiers_dicts[row.get("LAST_MODIFIED", "").split("-")[0]]["tier_3"] = 1
            else:
                tiers_dicts[row.get("LAST_MODIFIED", "").split("-")[0]]["tier_3"] += 1
            
print "Total number of original files: " + str(total)
print "Total number of original and normalized files: " + str(total + normalized)
print "Tier 1 files: " + str(tier_1_count) + " (" + str(float(tier_1_count) / total * 100) + "% of total original files)"
print "Tier 2 files: " + str(tier_2_count) + " (" + str(float(tier_2_count) / total * 100) + "% of total original files)"
print "Tier 3 files: " + str(tier_3_count) + " (" + str(float(tier_3_count) / total * 100) + "% of total original files)"
print "Total number of normalized files: " + str(normalized) + " (" + str(float(normalized) / (total) * 100) + "% of total original files)"
print "Number of files that should have been normalized but weren't: " + str(tier_2_count - normalized) + " (" + str(float(normalized) / (tier_2_count) * 100) + "% of Tier 2 files"

import plotly.plotly as py
import plotly.graph_objs as go

fig1 = {
    'data': [{'labels': ['Tier 1 (Sustainable Formats)', 'Tier 2 (Common "At-Risk" Formats)', 'Tier 3 (Wierd Stuff)'],
              'values': [tier_1_count, tier_2_count, tier_3_count],
              'type': 'pie'}],
    'layout': {'title': '<b>Tiers of Original Files in Dark Archive</b> (<i>n</i>=731,942)<br>See <a href="http://bentley.umich.edu/about/what-we-do/digital-curation-strategies-and-procedures/680-2/">Format Conversion Strategies for Long-Term Preservation</a> for More Information'}
     }

from collections import Counter

print "Top Ten Tier 1 Formats"
print Counter(tier_1_formats).most_common(10)
print "Top Ten Tier 2 Formats"
print Counter(tier_2_formats).most_common(10)
print "Top Ten Tier 2 Formats"
print Counter(tier_3_formats).most_common(10)

fig2 = {
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
      "name": 'Tier 2',
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
        # "showlegend": False,
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

from collections import OrderedDict

trace_tier_1 = go.Scatter(
    x = [
        1980, 
        1983, 
        1986, 
        1987, 
        1988, 
        1989, 
        1990, 
        1991, 
        1992, 
        1993, 
        1994, 
        1995, 
        1996, 
        1997, 
        1998, 
        1999, 
        2000, 
        2001, 
        2002, 
        2003, 
        2004, 
        2005, 
        2006, 
        2007, 
        2008, 
        2009, 
        2010, 
        2011, 
        2012, 
        2013, 
        2014, 
        2015, 
        2016
    ], 
    y=[
        tiers_dicts.get("1980", 0).get("tier_1", ""), 
        tiers_dicts.get("1983", 0).get("tier_1", ""), 
        tiers_dicts.get("1986", 0).get("tier_1", ""), 
        tiers_dicts.get("1987", 0).get("tier_1", ""), 
        tiers_dicts.get("1988", 0).get("tier_1", ""), 
        tiers_dicts.get("1989", 0).get("tier_1", ""), 
        tiers_dicts.get("1990", 0).get("tier_1", ""), 
        tiers_dicts.get("1991", 0).get("tier_1", ""), 
        tiers_dicts.get("1992", 0).get("tier_1", ""), 
        tiers_dicts.get("1993", 0).get("tier_1", ""), 
        tiers_dicts.get("1994", 0).get("tier_1", ""), 
        tiers_dicts.get("1995", 0).get("tier_1", ""), 
        tiers_dicts.get("1996", 0).get("tier_1", ""), 
        tiers_dicts.get("1997", 0).get("tier_1", ""), 
        tiers_dicts.get("1998", 0).get("tier_1", ""), 
        tiers_dicts.get("1999", 0).get("tier_1", ""), 
        tiers_dicts.get("2000", 0).get("tier_1", ""), 
        tiers_dicts.get("2001", 0).get("tier_1", ""), 
        tiers_dicts.get("2002", 0).get("tier_1", ""), 
        tiers_dicts.get("2003", 0).get("tier_1", ""), 
        tiers_dicts.get("2004", 0).get("tier_1", ""), 
        tiers_dicts.get("2005", 0).get("tier_1", ""), 
        tiers_dicts.get("2006", 0).get("tier_1", ""), 
        tiers_dicts.get("2007", 0).get("tier_1", ""), 
        tiers_dicts.get("2008", 0).get("tier_1", ""), 
        tiers_dicts.get("2009", 0).get("tier_1", ""), 
        tiers_dicts.get("2010", 0).get("tier_1", ""), 
        tiers_dicts.get("2011", 0).get("tier_1", ""), 
        tiers_dicts.get("2012", 0).get("tier_1", ""), 
        tiers_dicts.get("2013", 0).get("tier_1", ""), 
        tiers_dicts.get("2014", 0).get("tier_1", ""), 
        tiers_dicts.get("2015", 0).get("tier_1", ""), 
        tiers_dicts.get("2016", 0).get("tier_1", ""), 
    ], 
    name='Tier 1 (Sustainable Formats)',
    fill="tozeroy"
)

trace_tier_2 = go.Scatter(
    x = [
        1980, 
        1983, 
        1986, 
        1987, 
        1988, 
        1989, 
        1990, 
        1991, 
        1992, 
        1993, 
        1994, 
        1995, 
        1996, 
        1997, 
        1998, 
        1999, 
        2000, 
        2001, 
        2002, 
        2003, 
        2004, 
        2005, 
        2006, 
        2007, 
        2008, 
        2009, 
        2010, 
        2011, 
        2012, 
        2013, 
        2014, 
        2015, 
        2016
    ], 
    y=[
        tiers_dicts.get("1980", "").get("tier_2", 0) + tiers_dicts.get("1980", "").get("tier_1", 0), 
        tiers_dicts.get("1983", "").get("tier_2", 0) + tiers_dicts.get("1983", "").get("tier_1", 0), 
        tiers_dicts.get("1986", "").get("tier_2", 0) + tiers_dicts.get("1986", "").get("tier_1", 0), 
        tiers_dicts.get("1987", "").get("tier_2", 0) + tiers_dicts.get("1987", "").get("tier_1", 0), 
        tiers_dicts.get("1988", "").get("tier_2", 0) + tiers_dicts.get("1988", "").get("tier_1", 0), 
        tiers_dicts.get("1989", "").get("tier_2", 0) + tiers_dicts.get("1989", "").get("tier_1", 0), 
        tiers_dicts.get("1990", "").get("tier_2", 0) + tiers_dicts.get("1990", "").get("tier_1", 0), 
        tiers_dicts.get("1991", "").get("tier_2", 0) + tiers_dicts.get("1991", "").get("tier_1", 0), 
        tiers_dicts.get("1992", "").get("tier_2", 0) + tiers_dicts.get("1992", "").get("tier_1", 0), 
        tiers_dicts.get("1993", "").get("tier_2", 0) + tiers_dicts.get("1993", "").get("tier_1", 0), 
        tiers_dicts.get("1994", "").get("tier_2", 0) + tiers_dicts.get("1994", "").get("tier_1", 0), 
        tiers_dicts.get("1995", "").get("tier_2", 0) + tiers_dicts.get("1995", "").get("tier_1", 0), 
        tiers_dicts.get("1996", "").get("tier_2", 0) + tiers_dicts.get("1996", "").get("tier_1", 0), 
        tiers_dicts.get("1997", "").get("tier_2", 0) + tiers_dicts.get("1997", "").get("tier_1", 0), 
        tiers_dicts.get("1998", "").get("tier_2", 0) + tiers_dicts.get("1998", "").get("tier_1", 0), 
        tiers_dicts.get("1999", "").get("tier_2", 0) + tiers_dicts.get("1999", "").get("tier_1", 0), 
        tiers_dicts.get("2000", "").get("tier_2", 0) + tiers_dicts.get("2000", "").get("tier_1", 0), 
        tiers_dicts.get("2001", "").get("tier_2", 0) + tiers_dicts.get("2001", "").get("tier_1", 0), 
        tiers_dicts.get("2002", "").get("tier_2", 0) + tiers_dicts.get("2002", "").get("tier_1", 0), 
        tiers_dicts.get("2003", "").get("tier_2", 0) + tiers_dicts.get("2003", "").get("tier_1", 0), 
        tiers_dicts.get("2004", "").get("tier_2", 0) + tiers_dicts.get("2004", "").get("tier_1", 0), 
        tiers_dicts.get("2005", "").get("tier_2", 0) + tiers_dicts.get("2005", "").get("tier_1", 0), 
        tiers_dicts.get("2006", "").get("tier_2", 0) + tiers_dicts.get("2006", "").get("tier_1", 0), 
        tiers_dicts.get("2007", "").get("tier_2", 0) + tiers_dicts.get("2007", "").get("tier_1", 0), 
        tiers_dicts.get("2008", "").get("tier_2", 0) + tiers_dicts.get("2008", "").get("tier_1", 0), 
        tiers_dicts.get("2009", "").get("tier_2", 0) + tiers_dicts.get("2009", "").get("tier_1", 0), 
        tiers_dicts.get("2010", "").get("tier_2", 0) + tiers_dicts.get("2010", "").get("tier_1", 0), 
        tiers_dicts.get("2011", "").get("tier_2", 0) + tiers_dicts.get("2011", "").get("tier_1", 0), 
        tiers_dicts.get("2012", "").get("tier_2", 0) + tiers_dicts.get("2012", "").get("tier_1", 0), 
        tiers_dicts.get("2013", "").get("tier_2", 0) + tiers_dicts.get("2013", "").get("tier_1", 0), 
        tiers_dicts.get("2014", "").get("tier_2", 0) + tiers_dicts.get("2014", "").get("tier_1", 0), 
        tiers_dicts.get("2015", "").get("tier_2", 0) + tiers_dicts.get("2015", "").get("tier_1", 0), 
        tiers_dicts.get("2016", "").get("tier_2", 0) + tiers_dicts.get("2016", "").get("tier_1", 0), 
    ], 
    name='Tier 2 (Common "At-Risk" Formats)',
    fill="tonexty"
)

trace_tier_3 = go.Scatter(
    x = [
        1980, 
        1983, 
        1986, 
        1987, 
        1988, 
        1989, 
        1990, 
        1991, 
        1992, 
        1993, 
        1994, 
        1995, 
        1996, 
        1997, 
        1998, 
        1999, 
        2000, 
        2001, 
        2002, 
        2003, 
        2004, 
        2005, 
        2006, 
        2007, 
        2008, 
        2009, 
        2010, 
        2011, 
        2012, 
        2013, 
        2014, 
        2015, 
        2016
    ], 
    y=[
        tiers_dicts.get("1980", "").get("tier_3", 0) + tiers_dicts.get("1980", "").get("tier_2", 0) + tiers_dicts.get("1980", "").get("tier_1", 0), 
        tiers_dicts.get("1983", "").get("tier_3", 0) + tiers_dicts.get("1983", "").get("tier_2", 0) + tiers_dicts.get("1983", "").get("tier_1", 0), 
        tiers_dicts.get("1986", "").get("tier_3", 0) + tiers_dicts.get("1986", "").get("tier_2", 0) + tiers_dicts.get("1986", "").get("tier_1", 0), 
        tiers_dicts.get("1987", "").get("tier_3", 0) + tiers_dicts.get("1987", "").get("tier_2", 0) + tiers_dicts.get("1987", "").get("tier_1", 0), 
        tiers_dicts.get("1988", "").get("tier_3", 0) + tiers_dicts.get("1988", "").get("tier_2", 0) + tiers_dicts.get("1988", "").get("tier_1", 0), 
        tiers_dicts.get("1989", "").get("tier_3", 0) + tiers_dicts.get("1989", "").get("tier_2", 0) + tiers_dicts.get("1989", "").get("tier_1", 0), 
        tiers_dicts.get("1990", "").get("tier_3", 0) + tiers_dicts.get("1990", "").get("tier_2", 0) + tiers_dicts.get("1990", "").get("tier_1", 0), 
        tiers_dicts.get("1991", "").get("tier_3", 0) + tiers_dicts.get("1991", "").get("tier_2", 0) + tiers_dicts.get("1991", "").get("tier_1", 0), 
        tiers_dicts.get("1992", "").get("tier_3", 0) + tiers_dicts.get("1992", "").get("tier_2", 0) + tiers_dicts.get("1992", "").get("tier_1", 0), 
        tiers_dicts.get("1993", "").get("tier_3", 0) + tiers_dicts.get("1993", "").get("tier_2", 0) + tiers_dicts.get("1993", "").get("tier_1", 0), 
        tiers_dicts.get("1994", "").get("tier_3", 0) + tiers_dicts.get("1994", "").get("tier_2", 0) + tiers_dicts.get("1994", "").get("tier_1", 0), 
        tiers_dicts.get("1995", "").get("tier_3", 0) + tiers_dicts.get("1995", "").get("tier_2", 0) + tiers_dicts.get("1995", "").get("tier_1", 0), 
        tiers_dicts.get("1996", "").get("tier_3", 0) + tiers_dicts.get("1996", "").get("tier_2", 0) + tiers_dicts.get("1996", "").get("tier_1", 0), 
        tiers_dicts.get("1997", "").get("tier_3", 0) + tiers_dicts.get("1997", "").get("tier_2", 0) + tiers_dicts.get("1997", "").get("tier_1", 0), 
        tiers_dicts.get("1998", "").get("tier_3", 0) + tiers_dicts.get("1998", "").get("tier_2", 0) + tiers_dicts.get("1998", "").get("tier_1", 0), 
        tiers_dicts.get("1999", "").get("tier_3", 0) + tiers_dicts.get("1999", "").get("tier_2", 0) + tiers_dicts.get("1999", "").get("tier_1", 0), 
        tiers_dicts.get("2000", "").get("tier_3", 0) + tiers_dicts.get("2000", "").get("tier_2", 0) + tiers_dicts.get("2000", "").get("tier_1", 0), 
        tiers_dicts.get("2001", "").get("tier_3", 0) + tiers_dicts.get("2001", "").get("tier_2", 0) + tiers_dicts.get("2001", "").get("tier_1", 0), 
        tiers_dicts.get("2002", "").get("tier_3", 0) + tiers_dicts.get("2002", "").get("tier_2", 0) + tiers_dicts.get("2002", "").get("tier_1", 0), 
        tiers_dicts.get("2003", "").get("tier_3", 0) + tiers_dicts.get("2003", "").get("tier_2", 0) + tiers_dicts.get("2003", "").get("tier_1", 0), 
        tiers_dicts.get("2004", "").get("tier_3", 0) + tiers_dicts.get("2004", "").get("tier_2", 0) + tiers_dicts.get("2004", "").get("tier_1", 0), 
        tiers_dicts.get("2005", "").get("tier_3", 0) + tiers_dicts.get("2005", "").get("tier_2", 0) + tiers_dicts.get("2005", "").get("tier_1", 0), 
        tiers_dicts.get("2006", "").get("tier_3", 0) + tiers_dicts.get("2006", "").get("tier_2", 0) + tiers_dicts.get("2006", "").get("tier_1", 0), 
        tiers_dicts.get("2007", "").get("tier_3", 0) + tiers_dicts.get("2007", "").get("tier_2", 0) + tiers_dicts.get("2007", "").get("tier_1", 0), 
        tiers_dicts.get("2008", "").get("tier_3", 0) + tiers_dicts.get("2008", "").get("tier_2", 0) + tiers_dicts.get("2008", "").get("tier_1", 0), 
        tiers_dicts.get("2009", "").get("tier_3", 0) + tiers_dicts.get("2009", "").get("tier_2", 0) + tiers_dicts.get("2009", "").get("tier_1", 0), 
        tiers_dicts.get("2010", "").get("tier_3", 0) + tiers_dicts.get("2010", "").get("tier_2", 0) + tiers_dicts.get("2010", "").get("tier_1", 0), 
        tiers_dicts.get("2011", "").get("tier_3", 0) + tiers_dicts.get("2011", "").get("tier_2", 0) + tiers_dicts.get("2011", "").get("tier_1", 0), 
        tiers_dicts.get("2012", "").get("tier_3", 0) + tiers_dicts.get("2012", "").get("tier_2", 0) + tiers_dicts.get("2012", "").get("tier_1", 0), 
        tiers_dicts.get("2013", "").get("tier_3", 0) + tiers_dicts.get("2013", "").get("tier_2", 0) + tiers_dicts.get("2013", "").get("tier_1", 0), 
        tiers_dicts.get("2014", "").get("tier_3", 0) + tiers_dicts.get("2014", "").get("tier_2", 0) + tiers_dicts.get("2014", "").get("tier_1", 0), 
        tiers_dicts.get("2015", "").get("tier_3", 0) + tiers_dicts.get("2015", "").get("tier_2", 0) + tiers_dicts.get("2015", "").get("tier_1", 0), 
        tiers_dicts.get("2016", "").get("tier_3", 0) + tiers_dicts.get("2016", "").get("tier_2", 0) + tiers_dicts.get("2016", "").get("tier_1", 0), 
    ], 
    name='Tier 3 (Wierd Stuff)',
    fill="tonexty"
)

data = [trace_tier_1, trace_tier_2, trace_tier_3]
layout = go.Layout(
    title='<b>Number of Original Files per Tier by Last Modified Date in Dark Archive</b> (<i>n</i>=761,942)<br>See <a href="http://bentley.umich.edu/about/what-we-do/digital-curation-strategies-and-procedures/680-2/">Format Conversion Strategies for Long-Term Preservation</a> for More Information',
    barmode='stack',
)

fig3 = go.Figure(data=data, layout=layout)

percentage_trace_tier_1 = go.Bar(
    x = [
        1980, 
        1983, 
        1986, 
        1987, 
        1988, 
        1989, 
        1990, 
        1991, 
        1992, 
        1993, 
        1994, 
        1995, 
        1996, 
        1997, 
        1998, 
        1999, 
        2000, 
        2001, 
        2002, 
        2003, 
        2004, 
        2005, 
        2006, 
        2007, 
        2008, 
        2009, 
        2010, 
        2011, 
        2012, 
        2013, 
        2014, 
        2015, 
        2016
    ], 
    y=[
        float(tiers_dicts.get("1980", "").get("tier_1", 0)) / (tiers_dicts.get("1980", "").get("tier_1", 0) + tiers_dicts.get("1980", "").get("tier_2", 0) + tiers_dicts.get("1980", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1983", "").get("tier_1", 0)) / (tiers_dicts.get("1983", "").get("tier_1", 0) + tiers_dicts.get("1983", "").get("tier_2", 0) + tiers_dicts.get("1983", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1986", "").get("tier_1", 0)) / (tiers_dicts.get("1986", "").get("tier_1", 0) + tiers_dicts.get("1986", "").get("tier_2", 0) + tiers_dicts.get("1986", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1987", "").get("tier_1", 0)) / (tiers_dicts.get("1987", "").get("tier_1", 0) + tiers_dicts.get("1987", "").get("tier_2", 0) + tiers_dicts.get("1987", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1988", "").get("tier_1", 0)) / (tiers_dicts.get("1988", "").get("tier_1", 0) + tiers_dicts.get("1988", "").get("tier_2", 0) + tiers_dicts.get("1988", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1989", "").get("tier_1", 0)) / (tiers_dicts.get("1989", "").get("tier_1", 0) + tiers_dicts.get("1989", "").get("tier_2", 0) + tiers_dicts.get("1989", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1990", "").get("tier_1", 0)) / (tiers_dicts.get("1990", "").get("tier_1", 0) + tiers_dicts.get("1990", "").get("tier_2", 0) + tiers_dicts.get("1990", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1991", "").get("tier_1", 0)) / (tiers_dicts.get("1991", "").get("tier_1", 0) + tiers_dicts.get("1991", "").get("tier_2", 0) + tiers_dicts.get("1991", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1992", "").get("tier_1", 0)) / (tiers_dicts.get("1992", "").get("tier_1", 0) + tiers_dicts.get("1992", "").get("tier_2", 0) + tiers_dicts.get("1992", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1993", "").get("tier_1", 0)) / (tiers_dicts.get("1993", "").get("tier_1", 0) + tiers_dicts.get("1993", "").get("tier_2", 0) + tiers_dicts.get("1993", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1994", "").get("tier_1", 0)) / (tiers_dicts.get("1994", "").get("tier_1", 0) + tiers_dicts.get("1994", "").get("tier_2", 0) + tiers_dicts.get("1994", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1995", "").get("tier_1", 0)) / (tiers_dicts.get("1995", "").get("tier_1", 0) + tiers_dicts.get("1995", "").get("tier_2", 0) + tiers_dicts.get("1995", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1996", "").get("tier_1", 0)) / (tiers_dicts.get("1996", "").get("tier_1", 0) + tiers_dicts.get("1996", "").get("tier_2", 0) + tiers_dicts.get("1996", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1997", "").get("tier_1", 0)) / (tiers_dicts.get("1997", "").get("tier_1", 0) + tiers_dicts.get("1997", "").get("tier_2", 0) + tiers_dicts.get("1997", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1998", "").get("tier_1", 0)) / (tiers_dicts.get("1998", "").get("tier_1", 0) + tiers_dicts.get("1998", "").get("tier_2", 0) + tiers_dicts.get("1998", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1999", "").get("tier_1", 0)) / (tiers_dicts.get("1999", "").get("tier_1", 0) + tiers_dicts.get("1999", "").get("tier_2", 0) + tiers_dicts.get("1999", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2000", "").get("tier_1", 0)) / (tiers_dicts.get("2000", "").get("tier_1", 0) + tiers_dicts.get("2000", "").get("tier_2", 0) + tiers_dicts.get("2000", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2001", "").get("tier_1", 0)) / (tiers_dicts.get("2001", "").get("tier_1", 0) + tiers_dicts.get("2001", "").get("tier_2", 0) + tiers_dicts.get("2001", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2002", "").get("tier_1", 0)) / (tiers_dicts.get("2002", "").get("tier_1", 0) + tiers_dicts.get("2002", "").get("tier_2", 0) + tiers_dicts.get("2002", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2003", "").get("tier_1", 0)) / (tiers_dicts.get("2003", "").get("tier_1", 0) + tiers_dicts.get("2003", "").get("tier_2", 0) + tiers_dicts.get("2003", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2004", "").get("tier_1", 0)) / (tiers_dicts.get("2004", "").get("tier_1", 0) + tiers_dicts.get("2004", "").get("tier_2", 0) + tiers_dicts.get("2004", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2005", "").get("tier_1", 0)) / (tiers_dicts.get("2005", "").get("tier_1", 0) + tiers_dicts.get("2005", "").get("tier_2", 0) + tiers_dicts.get("2005", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2006", "").get("tier_1", 0)) / (tiers_dicts.get("2006", "").get("tier_1", 0) + tiers_dicts.get("2006", "").get("tier_2", 0) + tiers_dicts.get("2006", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2007", "").get("tier_1", 0)) / (tiers_dicts.get("2007", "").get("tier_1", 0) + tiers_dicts.get("2007", "").get("tier_2", 0) + tiers_dicts.get("2007", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2008", "").get("tier_1", 0)) / (tiers_dicts.get("2008", "").get("tier_1", 0) + tiers_dicts.get("2008", "").get("tier_2", 0) + tiers_dicts.get("2008", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2009", "").get("tier_1", 0)) / (tiers_dicts.get("2009", "").get("tier_1", 0) + tiers_dicts.get("2009", "").get("tier_2", 0) + tiers_dicts.get("2009", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2010", "").get("tier_1", 0)) / (tiers_dicts.get("2010", "").get("tier_1", 0) + tiers_dicts.get("2010", "").get("tier_2", 0) + tiers_dicts.get("2010", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2011", "").get("tier_1", 0)) / (tiers_dicts.get("2011", "").get("tier_1", 0) + tiers_dicts.get("2011", "").get("tier_2", 0) + tiers_dicts.get("2011", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2012", "").get("tier_1", 0)) / (tiers_dicts.get("2012", "").get("tier_1", 0) + tiers_dicts.get("2012", "").get("tier_2", 0) + tiers_dicts.get("2012", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2013", "").get("tier_1", 0)) / (tiers_dicts.get("2013", "").get("tier_1", 0) + tiers_dicts.get("2013", "").get("tier_2", 0) + tiers_dicts.get("2013", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2014", "").get("tier_1", 0)) / (tiers_dicts.get("2014", "").get("tier_1", 0) + tiers_dicts.get("2014", "").get("tier_2", 0) + tiers_dicts.get("2014", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2015", "").get("tier_1", 0)) / (tiers_dicts.get("2015", "").get("tier_1", 0) + tiers_dicts.get("2015", "").get("tier_2", 0) + tiers_dicts.get("2015", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2016", "").get("tier_1", 0)) / (tiers_dicts.get("2016", "").get("tier_1", 0) + tiers_dicts.get("2016", "").get("tier_2", 0) + tiers_dicts.get("2016", "").get("tier_3", 0)) * 100, 
    ], 
    name='Tier 1 (Sustainable Formats)'
)

percentage_trace_tier_2 = go.Bar(
    x = [
        1980, 
        1983, 
        1986, 
        1987, 
        1988, 
        1989, 
        1990, 
        1991, 
        1992, 
        1993, 
        1994, 
        1995, 
        1996, 
        1997, 
        1998, 
        1999, 
        2000, 
        2001, 
        2002, 
        2003, 
        2004, 
        2005, 
        2006, 
        2007, 
        2008, 
        2009, 
        2010, 
        2011, 
        2012, 
        2013, 
        2014, 
        2015, 
        2016
    ], 
    y=[
        float(tiers_dicts.get("1980", "").get("tier_2", 0)) / (tiers_dicts.get("1980", "").get("tier_1", 0) + tiers_dicts.get("1980", "").get("tier_2", 0) + tiers_dicts.get("1980", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1983", "").get("tier_2", 0)) / (tiers_dicts.get("1983", "").get("tier_1", 0) + tiers_dicts.get("1983", "").get("tier_2", 0) + tiers_dicts.get("1983", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1986", "").get("tier_2", 0)) / (tiers_dicts.get("1986", "").get("tier_1", 0) + tiers_dicts.get("1986", "").get("tier_2", 0) + tiers_dicts.get("1986", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1987", "").get("tier_2", 0)) / (tiers_dicts.get("1987", "").get("tier_1", 0) + tiers_dicts.get("1987", "").get("tier_2", 0) + tiers_dicts.get("1987", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1988", "").get("tier_2", 0)) / (tiers_dicts.get("1988", "").get("tier_1", 0) + tiers_dicts.get("1988", "").get("tier_2", 0) + tiers_dicts.get("1988", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1989", "").get("tier_2", 0)) / (tiers_dicts.get("1989", "").get("tier_1", 0) + tiers_dicts.get("1989", "").get("tier_2", 0) + tiers_dicts.get("1989", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1990", "").get("tier_2", 0)) / (tiers_dicts.get("1990", "").get("tier_1", 0) + tiers_dicts.get("1990", "").get("tier_2", 0) + tiers_dicts.get("1990", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1991", "").get("tier_2", 0)) / (tiers_dicts.get("1991", "").get("tier_1", 0) + tiers_dicts.get("1991", "").get("tier_2", 0) + tiers_dicts.get("1991", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1992", "").get("tier_2", 0)) / (tiers_dicts.get("1992", "").get("tier_1", 0) + tiers_dicts.get("1992", "").get("tier_2", 0) + tiers_dicts.get("1992", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1993", "").get("tier_2", 0)) / (tiers_dicts.get("1993", "").get("tier_1", 0) + tiers_dicts.get("1993", "").get("tier_2", 0) + tiers_dicts.get("1993", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1994", "").get("tier_2", 0)) / (tiers_dicts.get("1994", "").get("tier_1", 0) + tiers_dicts.get("1994", "").get("tier_2", 0) + tiers_dicts.get("1994", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1995", "").get("tier_2", 0)) / (tiers_dicts.get("1995", "").get("tier_1", 0) + tiers_dicts.get("1995", "").get("tier_2", 0) + tiers_dicts.get("1995", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1996", "").get("tier_2", 0)) / (tiers_dicts.get("1996", "").get("tier_1", 0) + tiers_dicts.get("1996", "").get("tier_2", 0) + tiers_dicts.get("1996", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1997", "").get("tier_2", 0)) / (tiers_dicts.get("1997", "").get("tier_1", 0) + tiers_dicts.get("1997", "").get("tier_2", 0) + tiers_dicts.get("1997", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1998", "").get("tier_2", 0)) / (tiers_dicts.get("1998", "").get("tier_1", 0) + tiers_dicts.get("1998", "").get("tier_2", 0) + tiers_dicts.get("1998", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1999", "").get("tier_2", 0)) / (tiers_dicts.get("1999", "").get("tier_1", 0) + tiers_dicts.get("1999", "").get("tier_2", 0) + tiers_dicts.get("1999", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2000", "").get("tier_2", 0)) / (tiers_dicts.get("2000", "").get("tier_1", 0) + tiers_dicts.get("2000", "").get("tier_2", 0) + tiers_dicts.get("2000", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2001", "").get("tier_2", 0)) / (tiers_dicts.get("2001", "").get("tier_1", 0) + tiers_dicts.get("2001", "").get("tier_2", 0) + tiers_dicts.get("2001", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2002", "").get("tier_2", 0)) / (tiers_dicts.get("2002", "").get("tier_1", 0) + tiers_dicts.get("2002", "").get("tier_2", 0) + tiers_dicts.get("2002", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2003", "").get("tier_2", 0)) / (tiers_dicts.get("2003", "").get("tier_1", 0) + tiers_dicts.get("2003", "").get("tier_2", 0) + tiers_dicts.get("2003", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2004", "").get("tier_2", 0)) / (tiers_dicts.get("2004", "").get("tier_1", 0) + tiers_dicts.get("2004", "").get("tier_2", 0) + tiers_dicts.get("2004", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2005", "").get("tier_2", 0)) / (tiers_dicts.get("2005", "").get("tier_1", 0) + tiers_dicts.get("2005", "").get("tier_2", 0) + tiers_dicts.get("2005", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2006", "").get("tier_2", 0)) / (tiers_dicts.get("2006", "").get("tier_1", 0) + tiers_dicts.get("2006", "").get("tier_2", 0) + tiers_dicts.get("2006", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2007", "").get("tier_2", 0)) / (tiers_dicts.get("2007", "").get("tier_1", 0) + tiers_dicts.get("2007", "").get("tier_2", 0) + tiers_dicts.get("2007", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2008", "").get("tier_2", 0)) / (tiers_dicts.get("2008", "").get("tier_1", 0) + tiers_dicts.get("2008", "").get("tier_2", 0) + tiers_dicts.get("2008", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2009", "").get("tier_2", 0)) / (tiers_dicts.get("2009", "").get("tier_1", 0) + tiers_dicts.get("2009", "").get("tier_2", 0) + tiers_dicts.get("2009", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2010", "").get("tier_2", 0)) / (tiers_dicts.get("2010", "").get("tier_1", 0) + tiers_dicts.get("2010", "").get("tier_2", 0) + tiers_dicts.get("2010", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2011", "").get("tier_2", 0)) / (tiers_dicts.get("2011", "").get("tier_1", 0) + tiers_dicts.get("2011", "").get("tier_2", 0) + tiers_dicts.get("2011", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2012", "").get("tier_2", 0)) / (tiers_dicts.get("2012", "").get("tier_1", 0) + tiers_dicts.get("2012", "").get("tier_2", 0) + tiers_dicts.get("2012", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2013", "").get("tier_2", 0)) / (tiers_dicts.get("2013", "").get("tier_1", 0) + tiers_dicts.get("2013", "").get("tier_2", 0) + tiers_dicts.get("2013", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2014", "").get("tier_2", 0)) / (tiers_dicts.get("2014", "").get("tier_1", 0) + tiers_dicts.get("2014", "").get("tier_2", 0) + tiers_dicts.get("2014", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2015", "").get("tier_2", 0)) / (tiers_dicts.get("2015", "").get("tier_1", 0) + tiers_dicts.get("2015", "").get("tier_2", 0) + tiers_dicts.get("2015", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2016", "").get("tier_2", 0)) / (tiers_dicts.get("2016", "").get("tier_1", 0) + tiers_dicts.get("2016", "").get("tier_2", 0) + tiers_dicts.get("2016", "").get("tier_3", 0)) * 100, 
    ], 
    name='Tier 2 (Common "At-Risk" Formats)'
)

percentage_trace_tier_3 = go.Bar(
    x = [
        1980, 
        1983, 
        1986, 
        1987, 
        1988, 
        1989, 
        1990, 
        1991, 
        1992, 
        1993, 
        1994, 
        1995, 
        1996, 
        1997, 
        1998, 
        1999, 
        2000, 
        2001, 
        2002, 
        2003, 
        2004, 
        2005, 
        2006, 
        2007, 
        2008, 
        2009, 
        2010, 
        2011, 
        2012, 
        2013, 
        2014, 
        2015, 
        2016
    ], 
    y=[
        float(tiers_dicts.get("1980", "").get("tier_3", 0)) / (tiers_dicts.get("1980", "").get("tier_1", 0) + tiers_dicts.get("1980", "").get("tier_2", 0) + tiers_dicts.get("1980", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1983", "").get("tier_3", 0)) / (tiers_dicts.get("1983", "").get("tier_1", 0) + tiers_dicts.get("1983", "").get("tier_2", 0) + tiers_dicts.get("1983", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1986", "").get("tier_3", 0)) / (tiers_dicts.get("1986", "").get("tier_1", 0) + tiers_dicts.get("1986", "").get("tier_2", 0) + tiers_dicts.get("1986", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1987", "").get("tier_3", 0)) / (tiers_dicts.get("1987", "").get("tier_1", 0) + tiers_dicts.get("1987", "").get("tier_2", 0) + tiers_dicts.get("1987", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1988", "").get("tier_3", 0)) / (tiers_dicts.get("1988", "").get("tier_1", 0) + tiers_dicts.get("1988", "").get("tier_2", 0) + tiers_dicts.get("1988", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1989", "").get("tier_3", 0)) / (tiers_dicts.get("1989", "").get("tier_1", 0) + tiers_dicts.get("1989", "").get("tier_2", 0) + tiers_dicts.get("1989", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1990", "").get("tier_3", 0)) / (tiers_dicts.get("1990", "").get("tier_1", 0) + tiers_dicts.get("1990", "").get("tier_2", 0) + tiers_dicts.get("1990", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1991", "").get("tier_3", 0)) / (tiers_dicts.get("1991", "").get("tier_1", 0) + tiers_dicts.get("1991", "").get("tier_2", 0) + tiers_dicts.get("1991", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1992", "").get("tier_3", 0)) / (tiers_dicts.get("1992", "").get("tier_1", 0) + tiers_dicts.get("1992", "").get("tier_2", 0) + tiers_dicts.get("1992", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1993", "").get("tier_3", 0)) / (tiers_dicts.get("1993", "").get("tier_1", 0) + tiers_dicts.get("1993", "").get("tier_2", 0) + tiers_dicts.get("1993", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1994", "").get("tier_3", 0)) / (tiers_dicts.get("1994", "").get("tier_1", 0) + tiers_dicts.get("1994", "").get("tier_2", 0) + tiers_dicts.get("1994", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1995", "").get("tier_3", 0)) / (tiers_dicts.get("1995", "").get("tier_1", 0) + tiers_dicts.get("1995", "").get("tier_2", 0) + tiers_dicts.get("1995", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1996", "").get("tier_3", 0)) / (tiers_dicts.get("1996", "").get("tier_1", 0) + tiers_dicts.get("1996", "").get("tier_2", 0) + tiers_dicts.get("1996", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1997", "").get("tier_3", 0)) / (tiers_dicts.get("1997", "").get("tier_1", 0) + tiers_dicts.get("1997", "").get("tier_2", 0) + tiers_dicts.get("1997", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1998", "").get("tier_3", 0)) / (tiers_dicts.get("1998", "").get("tier_1", 0) + tiers_dicts.get("1998", "").get("tier_2", 0) + tiers_dicts.get("1998", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("1999", "").get("tier_3", 0)) / (tiers_dicts.get("1999", "").get("tier_1", 0) + tiers_dicts.get("1999", "").get("tier_2", 0) + tiers_dicts.get("1999", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2000", "").get("tier_3", 0)) / (tiers_dicts.get("2000", "").get("tier_1", 0) + tiers_dicts.get("2000", "").get("tier_2", 0) + tiers_dicts.get("2000", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2001", "").get("tier_3", 0)) / (tiers_dicts.get("2001", "").get("tier_1", 0) + tiers_dicts.get("2001", "").get("tier_2", 0) + tiers_dicts.get("2001", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2002", "").get("tier_3", 0)) / (tiers_dicts.get("2002", "").get("tier_1", 0) + tiers_dicts.get("2002", "").get("tier_2", 0) + tiers_dicts.get("2002", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2003", "").get("tier_3", 0)) / (tiers_dicts.get("2003", "").get("tier_1", 0) + tiers_dicts.get("2003", "").get("tier_2", 0) + tiers_dicts.get("2003", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2004", "").get("tier_3", 0)) / (tiers_dicts.get("2004", "").get("tier_1", 0) + tiers_dicts.get("2004", "").get("tier_2", 0) + tiers_dicts.get("2004", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2005", "").get("tier_3", 0)) / (tiers_dicts.get("2005", "").get("tier_1", 0) + tiers_dicts.get("2005", "").get("tier_2", 0) + tiers_dicts.get("2005", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2006", "").get("tier_3", 0)) / (tiers_dicts.get("2006", "").get("tier_1", 0) + tiers_dicts.get("2006", "").get("tier_2", 0) + tiers_dicts.get("2006", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2007", "").get("tier_3", 0)) / (tiers_dicts.get("2007", "").get("tier_1", 0) + tiers_dicts.get("2007", "").get("tier_2", 0) + tiers_dicts.get("2007", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2008", "").get("tier_3", 0)) / (tiers_dicts.get("2008", "").get("tier_1", 0) + tiers_dicts.get("2008", "").get("tier_2", 0) + tiers_dicts.get("2008", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2009", "").get("tier_3", 0)) / (tiers_dicts.get("2009", "").get("tier_1", 0) + tiers_dicts.get("2009", "").get("tier_2", 0) + tiers_dicts.get("2009", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2010", "").get("tier_3", 0)) / (tiers_dicts.get("2010", "").get("tier_1", 0) + tiers_dicts.get("2010", "").get("tier_2", 0) + tiers_dicts.get("2010", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2011", "").get("tier_3", 0)) / (tiers_dicts.get("2011", "").get("tier_1", 0) + tiers_dicts.get("2011", "").get("tier_2", 0) + tiers_dicts.get("2011", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2012", "").get("tier_3", 0)) / (tiers_dicts.get("2012", "").get("tier_1", 0) + tiers_dicts.get("2012", "").get("tier_2", 0) + tiers_dicts.get("2012", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2013", "").get("tier_3", 0)) / (tiers_dicts.get("2013", "").get("tier_1", 0) + tiers_dicts.get("2013", "").get("tier_2", 0) + tiers_dicts.get("2013", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2014", "").get("tier_3", 0)) / (tiers_dicts.get("2014", "").get("tier_1", 0) + tiers_dicts.get("2014", "").get("tier_2", 0) + tiers_dicts.get("2014", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2015", "").get("tier_3", 0)) / (tiers_dicts.get("2015", "").get("tier_1", 0) + tiers_dicts.get("2015", "").get("tier_2", 0) + tiers_dicts.get("2015", "").get("tier_3", 0)) * 100, 
        float(tiers_dicts.get("2016", "").get("tier_3", 0)) / (tiers_dicts.get("2016", "").get("tier_1", 0) + tiers_dicts.get("2016", "").get("tier_2", 0) + tiers_dicts.get("2016", "").get("tier_3", 0)) * 100, 
    ], 
    name='Tier 3 (Wierd Stuff)'
)

percentage_data = [percentage_trace_tier_1, percentage_trace_tier_2, percentage_trace_tier_3]
percentage_layout = go.Layout(
    title='<b>Percentage of Original Files per Tier by Last Modified Date in Dark Archive</b> (<i>n</i>=761,942)<br>See <a href="http://bentley.umich.edu/about/what-we-do/digital-curation-strategies-and-procedures/680-2/">Format Conversion Strategies for Long-Term Preservation</a> for More Information',
    barmode='stack',
)

fig4 = go.Figure(data=percentage_data, layout=percentage_layout)

import squarify

x = 0.
y = 0.
width = 100.
height = 100.

values = []
values_text = []

print Counter(tier_3_formats)

for tier_3_format, count in Counter(tier_3_formats).most_common():
    if tier_3_format != "" and count > 100:
        values.append(count)
        values_text.append(tier_3_format)
    
print values
print len(values)
    
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
trace0 = go.Scatter(
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

# With hovertext
fig5 = dict(data=[trace0], layout=layout)

# Without hovertext
# figure = dict(data=[Scatter()], layout=layout)

# py.plot(fig1)
py.plot(fig2)
# py.plot(fig3)
# py.plot(fig4)
# py.plot(fig5)
