import os
from web_log_parser import *

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

# location
# mode of access
# Google Analytics provides data on technology (browser, operating system) and devices people use when accessing your site. 
# browser family, version
# os family, version
# device (is mobile)

print parser.bounce_rate()


# network domain
# users

