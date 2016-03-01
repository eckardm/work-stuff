import os
from web_log_parser import *
from collections import Counter

path_to_logs = r"C:\Users\eckardm\work-stuff\bhlead\logs"

for log in os.listdir(path_to_logs):
    if log.endswith(".json") or log + "_nobots_htmlonly.json" in os.listdir(path_to_logs):
        continue
    else:

        parser = BentleyWebLogParser(os.path.join(path_to_logs, log))
        parser.save_log_to_json()
        
parser = BentleyWebLogParser(r"C:\Users\eckardm\work-stuff\bhlead\logs\bhlead_logs_201511_anon_nobots_htmlonly.json")

for log in os.listdir(path_to_logs):
    if log.endswith(".json") and log != "bhlead_logs_201511_anon_nobots_htmlonly.json":
        
        parser.add_logs(os.path.join(path_to_logs, log))
        
parser.filter_staff_visits()

raw_finding_aid_visit_counts_list = parser.raw_finding_aid_visit_counts(result_limit=10000)

total = 0
mode_list = []
for a,b in raw_finding_aid_visit_counts_list:
    total += b
    mode_list.append(b)

print "\n"    
print "total"    
print "====="
print "mean: ", total / len(raw_finding_aid_visit_counts_list)
print "median: ", raw_finding_aid_visit_counts_list[len(raw_finding_aid_visit_counts_list) / 2][1]
print "mode: ", Counter(mode_list).most_common(1)[0][0]

print "\n"
print "web archives"
print "============"

total_web = 0
web_mode_list = []
for i in ["2014031", "2014037", "2014034", "2014025", "2013139", "2014039", "2014032", "2014038"]:
    total_web += parser.get_stats_for_single_finding_aid_by_identifier(i)["total views"]
    web_mode_list.append(parser.get_stats_for_single_finding_aid_by_identifier(i)["total views"])
    
print "mean: ", total_web / 8
print "median: ", sorted(web_mode_list)[4]
print "mode: ", Counter(web_mode_list).most_common(1)[0][0]

parser.get_stats_for_multiple_finding_aids_by_identifier(["2014031", "2014037", "2014034", "2014025", "2013139", "2014039", "2014032", "2014038"])
