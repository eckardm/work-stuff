from tiers import tier_1_list, tier_2_list, tier_3_list

import csv
import plotly.plotly as py
import plotly.graph_objs as go
import pprint

tiers_dict = {}

with open("droid_sho.csv", mode="rb") as droid_sho:
    reader = csv.DictReader(droid_sho)
    for row in reader:
        
        if row.get("LAST_MODIFIED", "").split("-")[0] not in tiers_dict:
            tiers_dict[row.get("LAST_MODIFIED", "").split("-")[0]] = {}
        
        if "." + row.get("EXT", "").lower() in tier_1_list:
            if "tier_1" not in tiers_dict[row.get("LAST_MODIFIED", "").split("-")[0]]:
                tiers_dict[row.get("LAST_MODIFIED", "").split("-")[0]]["tier_1"] = 1
            else:
                tiers_dict[row.get("LAST_MODIFIED", "").split("-")[0]]["tier_1"] += 1
            
        elif "." + row.get("EXT", "").lower() in tier_2_list:
            if "tier_2" not in tiers_dict[row.get("LAST_MODIFIED", "").split("-")[0]]:
                tiers_dict[row.get("LAST_MODIFIED", "").split("-")[0]]["tier_2"] = 1
            else:
                tiers_dict[row.get("LAST_MODIFIED", "").split("-")[0]]["tier_2"] += 1
                
        else:
            if "tier_3" not in tiers_dict[row.get("LAST_MODIFIED", "").split("-")[0]]:
                tiers_dict[row.get("LAST_MODIFIED", "").split("-")[0]]["tier_3"] = 1
            else:
                tiers_dict[row.get("LAST_MODIFIED", "").split("-")[0]]["tier_3"] += 1

print pprint.pprint(tiers_dict)

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
        tiers_dict.get("1980", 0).get("tier_1", ""), 
        tiers_dict.get("1983", 0).get("tier_1", ""), 
        tiers_dict.get("1986", 0).get("tier_1", ""), 
        tiers_dict.get("1987", 0).get("tier_1", ""), 
        tiers_dict.get("1988", 0).get("tier_1", ""), 
        tiers_dict.get("1989", 0).get("tier_1", ""), 
        tiers_dict.get("1990", 0).get("tier_1", ""), 
        tiers_dict.get("1991", 0).get("tier_1", ""), 
        tiers_dict.get("1992", 0).get("tier_1", ""), 
        tiers_dict.get("1993", 0).get("tier_1", ""), 
        tiers_dict.get("1994", 0).get("tier_1", ""), 
        tiers_dict.get("1995", 0).get("tier_1", ""), 
        tiers_dict.get("1996", 0).get("tier_1", ""), 
        tiers_dict.get("1997", 0).get("tier_1", ""), 
        tiers_dict.get("1998", 0).get("tier_1", ""), 
        tiers_dict.get("1999", 0).get("tier_1", ""), 
        tiers_dict.get("2000", 0).get("tier_1", ""), 
        tiers_dict.get("2001", 0).get("tier_1", ""), 
        tiers_dict.get("2002", 0).get("tier_1", ""), 
        tiers_dict.get("2003", 0).get("tier_1", ""), 
        tiers_dict.get("2004", 0).get("tier_1", ""), 
        tiers_dict.get("2005", 0).get("tier_1", ""), 
        tiers_dict.get("2006", 0).get("tier_1", ""), 
        tiers_dict.get("2007", 0).get("tier_1", ""), 
        tiers_dict.get("2008", 0).get("tier_1", ""), 
        tiers_dict.get("2009", 0).get("tier_1", ""), 
        tiers_dict.get("2010", 0).get("tier_1", ""), 
        tiers_dict.get("2011", 0).get("tier_1", ""), 
        tiers_dict.get("2012", 0).get("tier_1", ""), 
        tiers_dict.get("2013", 0).get("tier_1", ""), 
        tiers_dict.get("2014", 0).get("tier_1", ""), 
        tiers_dict.get("2015", 0).get("tier_1", ""), 
        tiers_dict.get("2016", 0).get("tier_1", ""), 
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
        tiers_dict.get("1980", "").get("tier_2", 0) + tiers_dict.get("1980", "").get("tier_1", 0), 
        tiers_dict.get("1983", "").get("tier_2", 0) + tiers_dict.get("1983", "").get("tier_1", 0), 
        tiers_dict.get("1986", "").get("tier_2", 0) + tiers_dict.get("1986", "").get("tier_1", 0), 
        tiers_dict.get("1987", "").get("tier_2", 0) + tiers_dict.get("1987", "").get("tier_1", 0), 
        tiers_dict.get("1988", "").get("tier_2", 0) + tiers_dict.get("1988", "").get("tier_1", 0), 
        tiers_dict.get("1989", "").get("tier_2", 0) + tiers_dict.get("1989", "").get("tier_1", 0), 
        tiers_dict.get("1990", "").get("tier_2", 0) + tiers_dict.get("1990", "").get("tier_1", 0), 
        tiers_dict.get("1991", "").get("tier_2", 0) + tiers_dict.get("1991", "").get("tier_1", 0), 
        tiers_dict.get("1992", "").get("tier_2", 0) + tiers_dict.get("1992", "").get("tier_1", 0), 
        tiers_dict.get("1993", "").get("tier_2", 0) + tiers_dict.get("1993", "").get("tier_1", 0), 
        tiers_dict.get("1994", "").get("tier_2", 0) + tiers_dict.get("1994", "").get("tier_1", 0), 
        tiers_dict.get("1995", "").get("tier_2", 0) + tiers_dict.get("1995", "").get("tier_1", 0), 
        tiers_dict.get("1996", "").get("tier_2", 0) + tiers_dict.get("1996", "").get("tier_1", 0), 
        tiers_dict.get("1997", "").get("tier_2", 0) + tiers_dict.get("1997", "").get("tier_1", 0), 
        tiers_dict.get("1998", "").get("tier_2", 0) + tiers_dict.get("1998", "").get("tier_1", 0), 
        tiers_dict.get("1999", "").get("tier_2", 0) + tiers_dict.get("1999", "").get("tier_1", 0), 
        tiers_dict.get("2000", "").get("tier_2", 0) + tiers_dict.get("2000", "").get("tier_1", 0), 
        tiers_dict.get("2001", "").get("tier_2", 0) + tiers_dict.get("2001", "").get("tier_1", 0), 
        tiers_dict.get("2002", "").get("tier_2", 0) + tiers_dict.get("2002", "").get("tier_1", 0), 
        tiers_dict.get("2003", "").get("tier_2", 0) + tiers_dict.get("2003", "").get("tier_1", 0), 
        tiers_dict.get("2004", "").get("tier_2", 0) + tiers_dict.get("2004", "").get("tier_1", 0), 
        tiers_dict.get("2005", "").get("tier_2", 0) + tiers_dict.get("2005", "").get("tier_1", 0), 
        tiers_dict.get("2006", "").get("tier_2", 0) + tiers_dict.get("2006", "").get("tier_1", 0), 
        tiers_dict.get("2007", "").get("tier_2", 0) + tiers_dict.get("2007", "").get("tier_1", 0), 
        tiers_dict.get("2008", "").get("tier_2", 0) + tiers_dict.get("2008", "").get("tier_1", 0), 
        tiers_dict.get("2009", "").get("tier_2", 0) + tiers_dict.get("2009", "").get("tier_1", 0), 
        tiers_dict.get("2010", "").get("tier_2", 0) + tiers_dict.get("2010", "").get("tier_1", 0), 
        tiers_dict.get("2011", "").get("tier_2", 0) + tiers_dict.get("2011", "").get("tier_1", 0), 
        tiers_dict.get("2012", "").get("tier_2", 0) + tiers_dict.get("2012", "").get("tier_1", 0), 
        tiers_dict.get("2013", "").get("tier_2", 0) + tiers_dict.get("2013", "").get("tier_1", 0), 
        tiers_dict.get("2014", "").get("tier_2", 0) + tiers_dict.get("2014", "").get("tier_1", 0), 
        tiers_dict.get("2015", "").get("tier_2", 0) + tiers_dict.get("2015", "").get("tier_1", 0), 
        tiers_dict.get("2016", "").get("tier_2", 0) + tiers_dict.get("2016", "").get("tier_1", 0), 
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
        tiers_dict.get("1980", "").get("tier_3", 0) + tiers_dict.get("1980", "").get("tier_2", 0) + tiers_dict.get("1980", "").get("tier_1", 0), 
        tiers_dict.get("1983", "").get("tier_3", 0) + tiers_dict.get("1983", "").get("tier_2", 0) + tiers_dict.get("1983", "").get("tier_1", 0), 
        tiers_dict.get("1986", "").get("tier_3", 0) + tiers_dict.get("1986", "").get("tier_2", 0) + tiers_dict.get("1986", "").get("tier_1", 0), 
        tiers_dict.get("1987", "").get("tier_3", 0) + tiers_dict.get("1987", "").get("tier_2", 0) + tiers_dict.get("1987", "").get("tier_1", 0), 
        tiers_dict.get("1988", "").get("tier_3", 0) + tiers_dict.get("1988", "").get("tier_2", 0) + tiers_dict.get("1988", "").get("tier_1", 0), 
        tiers_dict.get("1989", "").get("tier_3", 0) + tiers_dict.get("1989", "").get("tier_2", 0) + tiers_dict.get("1989", "").get("tier_1", 0), 
        tiers_dict.get("1990", "").get("tier_3", 0) + tiers_dict.get("1990", "").get("tier_2", 0) + tiers_dict.get("1990", "").get("tier_1", 0), 
        tiers_dict.get("1991", "").get("tier_3", 0) + tiers_dict.get("1991", "").get("tier_2", 0) + tiers_dict.get("1991", "").get("tier_1", 0), 
        tiers_dict.get("1992", "").get("tier_3", 0) + tiers_dict.get("1992", "").get("tier_2", 0) + tiers_dict.get("1992", "").get("tier_1", 0), 
        tiers_dict.get("1993", "").get("tier_3", 0) + tiers_dict.get("1993", "").get("tier_2", 0) + tiers_dict.get("1993", "").get("tier_1", 0), 
        tiers_dict.get("1994", "").get("tier_3", 0) + tiers_dict.get("1994", "").get("tier_2", 0) + tiers_dict.get("1994", "").get("tier_1", 0), 
        tiers_dict.get("1995", "").get("tier_3", 0) + tiers_dict.get("1995", "").get("tier_2", 0) + tiers_dict.get("1995", "").get("tier_1", 0), 
        tiers_dict.get("1996", "").get("tier_3", 0) + tiers_dict.get("1996", "").get("tier_2", 0) + tiers_dict.get("1996", "").get("tier_1", 0), 
        tiers_dict.get("1997", "").get("tier_3", 0) + tiers_dict.get("1997", "").get("tier_2", 0) + tiers_dict.get("1997", "").get("tier_1", 0), 
        tiers_dict.get("1998", "").get("tier_3", 0) + tiers_dict.get("1998", "").get("tier_2", 0) + tiers_dict.get("1998", "").get("tier_1", 0), 
        tiers_dict.get("1999", "").get("tier_3", 0) + tiers_dict.get("1999", "").get("tier_2", 0) + tiers_dict.get("1999", "").get("tier_1", 0), 
        tiers_dict.get("2000", "").get("tier_3", 0) + tiers_dict.get("2000", "").get("tier_2", 0) + tiers_dict.get("2000", "").get("tier_1", 0), 
        tiers_dict.get("2001", "").get("tier_3", 0) + tiers_dict.get("2001", "").get("tier_2", 0) + tiers_dict.get("2001", "").get("tier_1", 0), 
        tiers_dict.get("2002", "").get("tier_3", 0) + tiers_dict.get("2002", "").get("tier_2", 0) + tiers_dict.get("2002", "").get("tier_1", 0), 
        tiers_dict.get("2003", "").get("tier_3", 0) + tiers_dict.get("2003", "").get("tier_2", 0) + tiers_dict.get("2003", "").get("tier_1", 0), 
        tiers_dict.get("2004", "").get("tier_3", 0) + tiers_dict.get("2004", "").get("tier_2", 0) + tiers_dict.get("2004", "").get("tier_1", 0), 
        tiers_dict.get("2005", "").get("tier_3", 0) + tiers_dict.get("2005", "").get("tier_2", 0) + tiers_dict.get("2005", "").get("tier_1", 0), 
        tiers_dict.get("2006", "").get("tier_3", 0) + tiers_dict.get("2006", "").get("tier_2", 0) + tiers_dict.get("2006", "").get("tier_1", 0), 
        tiers_dict.get("2007", "").get("tier_3", 0) + tiers_dict.get("2007", "").get("tier_2", 0) + tiers_dict.get("2007", "").get("tier_1", 0), 
        tiers_dict.get("2008", "").get("tier_3", 0) + tiers_dict.get("2008", "").get("tier_2", 0) + tiers_dict.get("2008", "").get("tier_1", 0), 
        tiers_dict.get("2009", "").get("tier_3", 0) + tiers_dict.get("2009", "").get("tier_2", 0) + tiers_dict.get("2009", "").get("tier_1", 0), 
        tiers_dict.get("2010", "").get("tier_3", 0) + tiers_dict.get("2010", "").get("tier_2", 0) + tiers_dict.get("2010", "").get("tier_1", 0), 
        tiers_dict.get("2011", "").get("tier_3", 0) + tiers_dict.get("2011", "").get("tier_2", 0) + tiers_dict.get("2011", "").get("tier_1", 0), 
        tiers_dict.get("2012", "").get("tier_3", 0) + tiers_dict.get("2012", "").get("tier_2", 0) + tiers_dict.get("2012", "").get("tier_1", 0), 
        tiers_dict.get("2013", "").get("tier_3", 0) + tiers_dict.get("2013", "").get("tier_2", 0) + tiers_dict.get("2013", "").get("tier_1", 0), 
        tiers_dict.get("2014", "").get("tier_3", 0) + tiers_dict.get("2014", "").get("tier_2", 0) + tiers_dict.get("2014", "").get("tier_1", 0), 
        tiers_dict.get("2015", "").get("tier_3", 0) + tiers_dict.get("2015", "").get("tier_2", 0) + tiers_dict.get("2015", "").get("tier_1", 0), 
        tiers_dict.get("2016", "").get("tier_3", 0) + tiers_dict.get("2016", "").get("tier_2", 0) + tiers_dict.get("2016", "").get("tier_1", 0), 
    ], 
    name='Tier 3 (Wierd Stuff)',
    fill="tonexty"
)

data = [trace_tier_1, trace_tier_2, trace_tier_3]
layout = go.Layout(
    title='<b>Number of Original Files per Tier by Last Modified Date in Dark Archive</b> (<i>n</i>=761,942)<br>See <a href="http://bentley.umich.edu/about/what-we-do/digital-curation-strategies-and-procedures/680-2/">Format Conversion Strategies for Long-Term Preservation</a> for More Information',
)

basic_overlaid_area_chart = go.Figure(data=data, layout=layout)
py.plot(basic_overlaid_area_chart)
