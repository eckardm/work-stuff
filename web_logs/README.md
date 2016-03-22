#Exploring the Bentley's web logs
A relatively simple interface to extract summarized info from the Bentley's server logs. Brought to you by Walker! I'm trying to add to it using [Best Practices for Google Analytics in Digital Libraries](https://docs.google.com/document/d/1QmiLJEZXGAY-s7BG_nyF6EUAqcyH0mhQ7j2VPpLpxCQ/edit#) as a guide.

##Requirements:

* [apache-log-parser](https://github.com/rory/apache-log-parser)
* [tqdm](https://github.com/noamraph/tqdm)

##Usage

###Loading data
First, load an initial web log:
```python
parser = BentleyWebLogParser("path/to/log/file")
```

The parser will automatically remove all bot entries, as well as requests that were not to html pages (like for css, js, or image files)

You can load additional log data if you want to process data from multiple exports:
```python
parser.add_logs("path/to/new/log/file")
```

You can save a lot of future loading time by saving a parsed raw log file in json format, then loading from that instead 
in the future. All you need to make this happen is to run the ```save_log_to_json()``` method:
```python
parser.save_log_to_json()
```

This will output a .json file. You can load these directly into the parser just as you would the normal raw-text server log files:
```python
parser = BentleyWebLogParser("path/to/json/file")

parser.add_logs("path/to/json/file")
```

The json files load much faster, since the parser doesn't need to manually process each individual line.


###Summarizations

#### Content Use and Access Counts

##### Bounce Rate

Get a bounce rate (percent of total number of logs/requests where only one page is viewed by a user):
```python
>>> parser.bounce_rate()
13.9890619821
```

##### Download Counts

N/A

##### Time

##### Pageviews

##### Sessions

Any summarization method can take an optional ```start_date``` and ```end_date``` argument (which must be ```yyyy-mm-dd```), which will filter the data to be summarized by those dates:
```python
>>> parser.unique_visitor_count(start_date="2016-01-01", end_date="2016-01-15")
6021
```

Get a count of total page requests made:
```python
>>> parser.total_page_requests_count()
87552
```

Get a sorted list of most-searched-for search terms. Search terms are all normalized to lowercase.
```python
>>> parser.raw_search_counts()
[(u'republican', 285),
 (u'john harvey kellogg', 245),
 (u'duderstadt', 235),
 (u'democratic', 234),
 (u'radio', 217),
 (u'albert kahn papers', 204),
 (...)
]
```

For any method that returns a list of items, you can limit the length of what is returned to the top n items by using the optional ```limit``` argument:
```python
>>> parser.raw_search_counts(limit=2)
[(u'republican', 285),
 (u'john harvey kellogg', 245)
]
```

Get a sorted list of search terms ordered by number of unique users making that search:
```python
>>> parser.unique_users_per_search_term()
[(u'keijo', 104),
 (u'albert kahn papers', 74),
 (u'bells', 40),
 (u'mercywood', 36),
 (u'albert kahn', 32),
 (u'duderstadt', 22),
 (u'william lebaron jenney', 21),
 (u'reginald malcolmson', 20),
 (...)
]
```

Get a sorted list of most-visited finding aids
```python
>>> parser.raw_finding_aid_visit_counts()
[(u'umich-bhl-0420', 1925),
 (u'umich-bhl-97105', 756),
 (u'umich-bhl-943', 711),
 (u'umich-bhl-0081', 636),
 (u'umich-bhl-2014106', 541),
 (...)
]
```

Get a sorted list of finding aids ordered by number of unique visitors
```python
>>> parser.unique_users_per_finding_aid()
[(u'umich-bhl-0420', 656),
 (u'umich-bhl-97105', 307),
 (u'umich-bhl-9915', 260),
 (u'umich-bhl-0081', 197),
 (u'umich-bhl-850', 179),
 (...)
]
```

Get a summary of data for a single finding aid by its identifier
```python
>>> parser.get_stats_for_single_finding_aid_by_identifier('umich-bhl-0420')
{'identifier': 'umich-bhl-0420',
 'total views': 1925,
 'unique user count': 656,
 'associated queries': [(u'albert kahn papers', 146),
                        (u'albert kahn', 86),
                        (u'willow run', 28),
                        (u'durant', 26),
                        (u'hill', 21),
                        (u'russia', 17),
                        (...)]
}

# you can also just pass a number instead of the full "umich-bhl-####" string, eg:
>>> parser.get_stats_for_single_finding_aid_by_identifier('0420')
```

Get a summary for a set of finding aids by a list of identifiers
```python
>>> parser.get_stats_for_multiple_finding_aids_by_identifier(['umich-bhl-0420', 'umich-bhl-2009082', 'umich-bhl-97115'])
{'identifiers': ['umich-bhl-0420', 'umich-bhl-2009082', 'umich-bhl-97115'],
 'total views': 2129,
 'unique user count': 785,
 'unique users by identifier': [('umich-bhl-0420', 656),
                                ('umich-bhl-97115', 77),
                                ('umich-bhl-2009082', 77)],
 
 'views by identifier': [('umich-bhl-0420', 1925),
                         ('umich-bhl-97115', 112),
                         ('umich-bhl-2009082', 92)]}
 
 'associated queries': [(u'albert kahn papers', 146),
                        (u'albert kahn', 86),
                        (u'willow run', 28),
                        (u'durant', 26),
                        (u'hill', 21),
                        (u'russia', 17),
                        (...)]
}
```

Get a list of where our traffic is coming from:
```python
>>> parser.get_referer_counts()
[(u'https://www.google.com', 8643),
 (u'http://bentley.umich.edu/legacy-support/EAD', 2977),
 (u'http://quod.lib.umich.edu/cgi/f/findaid/findaid-idx?&page=simple&c=bhlead', 1964),
 (u'http://bentley.umich.edu/legacy-support/EAD/ead_uofm.php', 1549),
 (u'http://quod.lib.umich.edu', 969),
 (u'http://bentley.umich.edu/legacy-support/EAD/ead_ab.php', 579),
 (u'http://quod.lib.umich.edu/b/bhlead?page=simple', 451),
 (u'http://quod.lib.umich.edu/cgi/f/findaid/findaid-idx?c=bhlead;page=simple', 344),
 (u'http://quod.lib.umich.edu/cgi/f/findaid/findaid-idx?c=bhlead;page=boolean', 301),
 (u'http://bentley.umich.edu/legacy-support/EAD/ead_kl.php', 298),
 (u'https://www.google.ca', 286),
 (...)
]
```

#### Audience Metrics

##### Location

I don't think we can get this info...

##### Mode of Access

Get a list of browser families:
```python
>>> parser.browser_families()
[(u'Chrome', 51484), 
 (u'Firefox', 34241), 
 (u'IE', 12089), 
 (u'Safari', 11996), 
 (u'Mobile Safari', 6212), 
 (u'Chrome Mobile', 2106), 
 (u'Opera', 859), 
 (u'Edge', 719), 
 (u'Android', 432), 
 (u'WebKit Nightly', 310), 
 (u'Opera Mini', 94), 
 (u'IE Mobile', 88), 
 (u'Firefox Mobile', 50)
]
```

Get a list of browser versions:
```python
>>> parser.browser_versions()
[(u'Chrome 47.0.2526', 15826), 
(u'Chrome 46.0.2490', 13171), 
(u'Chrome 48.0.2564', 11697), 
(u'Firefox 38', 11325), 
(u'IE 11', 7195), 
(u'Firefox 21', 4106), 
(u'Mobile Safari 9', 3244), 
(u'Firefox 43', 2840), 
(u'Firefox 42', 2642), 
(u'Safari9.0.1', 2319), 
(u'Firefox 36', 2000), 
(u'Chrome 27.0.1453', 1976), 
]
```

Get a list of operating system families:
```python
>>> parser.os_families()
[(u'Windows 7', 57137), 
 (u'Mac OS X', 26435), 
 (u'Windows 8.1', 7116), 
 (u'iOS', 212), 
 (u'Windows 10', 5710), 
 (u'Windows XP', 5373), 
 (u'Android', 3179), 
 (u'Windws 8', 2448), 
 (u'Linux', 2229), 
 (u'Ubuntu', 1744), 
]
```

Get a list of operating system versions:
```python
>>> parser.os_versions()
 [(u'Windows 7', 57137), 
 (u'Windows 8.1', 7116), 
 (u'Mac OS X 10.10.5', 5916), 
 (u'Windows 10', 5710), 
 (u'Windows XP', 5373), 
 (u'Mac OS X 10.9.5', 3304), 
 (u'Mac OS X 10.11.1', 2674), 
 (u'Windows 8', 2448), 
 (u'Linux', 2229), 
]
```

Get a percentage of mobile requests:
```python
>>> parser.mobile_percentage_for_requests()
5.1143520053
```

Get a percentage of unique mobile users:
```python
>>> parser.unique_mobile_visitor()
13.5064935065
```

##### Network Domain / ISP Name

TBD

##### Users

Get a count of all unique visitors:
```python
>>> parser.unique_visitor_count()
18754
```
