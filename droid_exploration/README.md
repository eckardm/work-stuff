Droid Exploration
=================

A series of scripts that makes visualizations from [DROID](https://www.nationalarchives.gov.uk/information-management/manage-information/preserving-digital-records/droid/) output(s) and file format policies using [Plotly](https://plot.ly/).

You'll need:
  * CSV report(s) from DROID
  * Python
  * Plotly
  * Counter
  * Squarify
  
Preliminaries
-------------

**make_droid_sho.py** can be pointed at a folder of DROID reports in CSV format and creates one big CSV. Currently there's a couple Bentley-specific lines but it should be very easy to modify.

**tiers.py** contains lists of file extensions in the various tiers the Bentley has defined as part of their [Format Conversion Strategies for Long-Term Preservation](http://bentley.umich.edu/about/what-we-do/digital-curation-strategies-and-procedures/680-2/). These could be adapted to fit your policy.

Making Visualizations
---------------------

Pie Charts
###

![Tiers of Original Files in Dark Archive](https://plot.ly/~eckardm/150.png)

**make_basic_pie_chart.py** takes a DROID export (or the big CSV created by make_droid_sho.py) and creates a basic pie chart for the various tiers. *Note: The tiers are currently hard-coded.*

**make_donut_chart.py** creates pie charts for file formats in each of the tiers. *Note: The tiers are currenlty hard-coded, and this code assumes you have three tiers and want to look at the top five formats in each.*

Filled Area Plots
###

![Number of Original Files per Tier by Last Modified Date in Dark Archive](https://plot.ly/~eckardm/154.png)

**make_basic_overlaid_area_chart.py** creates a filled area plot that shows the accumulation of tiers over time, by last modified date. *Note: The tiers are currenlty hard-coded, as are the last modified dates, and the code manually cleans outliers.*

Bar Charts
###

![Percentage of Original Files per Tier by Last Modified Date in Dark Archive](https://plot.ly/~eckardm/156.png)

**make_stacked_bar_chart.py** creates a stacked bar chart that shows the percentage of the total that different tiers make up over time, by last modified date. *Note: The tiers are currently hard-coded, as are the last modified dates, and the code manually cleans outliers*

Treemaps
###

**make_treempa.py** creates a tree map that visualizes the formats in Tier 3, making individual squares sized according to their portion of the whole. *Note: The tier is currently hard-coded.*
