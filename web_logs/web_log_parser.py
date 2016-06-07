import json
from pprint import pprint
from collections import Counter
import re
import datetime

from tqdm import tqdm
import apache_log_parser


def main():
    parser = BentleyWebLogParser("logs/bhlead_logs_201511_anon_nobots_htmlonly.json")
    parser.add_logs("logs/bhlead_logs_201512_anon_nobots_htmlonly.json")
    parser.add_logs("logs/bhlead_logs_201601_anon_nobots_htmlonly.json")
    print("")

    print("raw search counts (not normalized by unique users): ")
    pprint(parser.raw_search_counts(50))
    print("")

    print("number of unique users making each search: ")
    pprint(parser.unique_users_per_search_term(50))
    print("")

    print("finding aid visit counts: ")
    pprint(parser.raw_finding_aid_visit_counts(50))
    print("")

    print("number of unique users visiting each finding aid:")
    pprint(parser.unique_users_per_finding_aid(50, start_date="2016-01-01", end_date="2016-01-30"))
    print("")

    print("Total page requests: {}".format(parser.total_page_requests_count()))
    print("Total unique visitors: {}".format(parser.unique_visitor_count()))
    print("Total unique visitors from the Bentley: {}".format(parser.bentley_visitor_count()))
    print("Total visits to web archives: {}".format(parser.web_archives_visits()))
    print("Referrer counts:")
    pprint(parser.get_referer_counts(50))

    pprint(parser.get_stats_for_multiple_finding_aids_by_identifier(['umich-bhl-0420', 'umich-bhl-2009082', 'umich-bhl-97115']))

class BentleyWebLogParser(object):
    def __init__(self, filename):
        self.parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %v")
        self.filename = filename.split(".")[0]

        self.bots_filtered = False
        self.is_html_only = False
        self.staff_filtered = False

        self.parsed_log = []

        self.add_logs(filename)
        self.filter_non_page_requests()
        self.filter_bots()

    def total_page_requests_count(self, start_date="", end_date=""):
        return len(self.logs_filtered_by_time_range(start_date, end_date))

    def get_stats_for_multiple_finding_aids_by_identifier(self, identifiers, start_date="", end_date=""):
        data = {"identifiers": [], "total views": 0, "unique users": set(), "views by identifier": Counter(), "unique users by identifier": Counter(), "associated queries": Counter()}

        for identifier in identifiers:
            stats = self.get_stats_for_single_finding_aid_by_identifier(identifier, start_date=start_date, end_date=end_date, include_user_list=True)
            data["identifiers"].append(stats["identifier"])
            data["total views"] += stats["total views"]
            data["unique users"] = data["unique users"].union(stats["unique users"])
            data["associated queries"] += Counter(dict(stats["associated queries"]))
            data["views by identifier"][identifier] = stats["total views"]
            data["unique users by identifier"][identifier] = len(stats["unique users"])

        data["unique user count"] = len(data["unique users"])
        data["associated queries"] = data["associated queries"].most_common()
        data["views by identifier"] = data["views by identifier"].most_common()
        data["unique users by identifier"] = data["unique users by identifier"].most_common()
        del data["unique users"]

        return data

    def get_stats_for_single_finding_aid_by_identifier(self, identifier, start_date="", end_date="", include_user_list=False):
        views = []
        queries = []

        if not identifier.startswith("umich-bhl-"):
            identifier = "umich-bhl-{}".format(identifier)

        for log in self.logs_filtered_by_time_range(start_date, end_date):
            id = self._extract_ead_id_from_request(log)
            if id == identifier:
                queries += self.get_queries(log)
                user = log.get("remote_host", "")
                views.append(user)

        results = {"identifier": identifier, "total views": len(views), "unique user count": len(set(views)), "associated queries": Counter(queries).most_common()}

        if include_user_list:
            results["unique users"] = set(views)

        return results

    def raw_finding_aid_visit_counts(self, limit=None, start_date="", end_date=""):
        ids = []
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            id = self._extract_ead_id_from_request(log)
            if id:
                ids.append(id)

        return Counter(ids).most_common(n=limit)

    def unique_users_per_finding_aid(self, limit=None, start_date="", end_date=""):
        ids = set()
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            user = log.get("remote_host", "")
            id = self._extract_ead_id_from_request(log)
            if id:
                ids.add((user, id))

        result = []
        for id in ids:
            result.append(id[1])

        return Counter(result).most_common(n=limit)

    def _extract_ead_id_from_request(self, log):
        query_dict = log.get("request_url_query_dict", {})
        id = query_dict.get("idno", [""])[0]
        if not id:
            id_regex = re.compile(r"(umich-bhl-\d{1,10})")
            url = log.get("request_first_line", "")
            results = re.findall(id_regex, url)
            if results:
                id = results[0]
        return id

    def raw_search_counts(self, limit=None, start_date="", end_date=""):
        searches = []
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            queries = self.get_queries(log)
            for query in queries:
                searches.append(query.lower())

        return Counter(searches).most_common(n=limit)
        
# * * *
        
    def browser_families(self, limit=None, start_date="", end_date=""):
        browser_families = []
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            browser_family = self.get_browser_family(log)
            browser_families.append(browser_family)
            
        return Counter(browser_families).most_common(n=limit)
        
    def os_families(self, limit=None, start_date="", end_date=""):
        os_families = []
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            os_family = self.get_os_family(log)
            os_families.append(os_family)
            
        return Counter(os_families).most_common(n=limit)
        
    def browser_versions(self, limit=None, start_date="", end_date=""):
        browser_versions = []
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            browser_version = self.get_browser_version(log)
            browser_versions.append(browser_version.strip())
        
        return Counter(browser_versions).most_common(n=limit)
        
    def os_versions(self, limit=None, start_date="", end_date=""):
        os_versions = []
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            os_version = self.get_os_version(log)
            os_versions.append(os_version.strip())
        
        return Counter(os_versions).most_common(n=limit)
        
    def mobile_percentage_for_requests(self, start_date="", end_date=""):
        mobile = 0
        total = 0
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            total += 1
            is_mobile = self.is_mobile(log)
            if is_mobile == True:
                mobile += 1
                
        return float(mobile) / total * 100
        
    def search_vs_browse_from_index(self, start_date="", end_date="")    :
        searchers = 0
        browsers = 0
        
        total = 0
        
        browse_pages = [
            "http://bentley.umich.edu/legacy-support/EAD/ead_ab.php", 
            "http://bentley.umich.edu/legacy-support/EAD/ead_cd.php", 
            "http://bentley.umich.edu/legacy-support/EAD/ead_ef.php", 
            "http://bentley.umich.edu/legacy-support/EAD/ead_gh.php", 
            "http://bentley.umich.edu/legacy-support/EAD/ead_ij.php", 
            "http://bentley.umich.edu/legacy-support/EAD/ead_kl.php", 
            "http://bentley.umich.edu/legacy-support/EAD/ead_mn.php", 
            "http://bentley.umich.edu/legacy-support/EAD/ead_op.php", 
            "http://bentley.umich.edu/legacy-support/EAD/ead_qs.php", 
            "http://bentley.umich.edu/legacy-support/EAD/ead_tz.php", 
            "http://bentley.umich.edu/legacy-support/EAD/ead_uofm.php", 
            "http://bentley.umich.edu/legacy-support/EAD/ead_new.php"
        ]
        
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            if log.get("request_header_referer", "") == "http://bentley.umich.edu/legacy-support/EAD/":
                total += 1
                if log.get("request_url", "") == "/cgi/f/findaid/findaid-idx?&page=simple&c=bhlead" or log.get("request_url", "") == "/cgi/f/findaid/findaid-idx?c=bhlead;page=boolean":
                    searchers += 1
                elif log.get("request_url", "") == "/cgi/f/findaid/findaid-idx?c=bhlead;page=browse;id=navbarbrowselink;cginame=findaid-idx":
                    browsers += 1
            elif log.get("request_header_referer", "") in browse_pages:
                total += 1
                browsers += 1
            
        return "Searchers from index: ", searchers, float(searchers) / total * 100, "\nBrowsers from index: ", browsers, float(browsers) / total * 100
            
            
# * * *
            
    def unique_users_per_search_term(self, limit=None, start_date="", end_date=""):
        searches = set()
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            user = log.get("remote_host", "")
            queries = self.get_queries(log)
            for query in queries:
                searches.add((user, query.lower()))

        result = []
        for search in searches:
            result.append(search[1])

        return Counter(result).most_common(n=limit)

    def visit_count_by_staff_member(self, start_date="", end_date=""):
        users = []
        for row in self.logs_filtered_by_time_range(start_date, end_date):
            user = row.get("remote_user", "")
            if user:
                users.append(user)

        return Counter(users).most_common()

    def web_archives_visits(self, start_date="", end_date=""):
        count = 0
        web_archives_ids = ["2014031", "2014037", "2014034", "2014025", "2013139", "2014039", "2014032", "2014038"]
        for row in self.logs_filtered_by_time_range(start_date, end_date):
            query_dict = row.get("request_url_query_dict", {})
            id = query_dict.get("idno", [""])[0]
            if any(web_id in id for web_id in web_archives_ids):
                count += 1
        return count

    def unique_visitor_count(self, start_date="", end_date=""):
        visitors = set()
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            visitors.add(log.get("remote_host", ""))

        return len(visitors)

# * * *

    def unique_mobile_visitor(self, start_date="", end_date=""):
        total = set()
        visitors = set()
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            total.add(log.get("remote_host", ""))
            if self.is_mobile(log) == True:
                visitors.add(log.get("remote_host", ""))

        return float(len(visitors)) / len(total) * 100
        
    def bounce_rate(self, start_date="", end_date=""):
        total = 0
        visitors = []
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            total += 1
            visitors.append(log.get("remote_host", ""))
        bouncers = 0
        for visitor, count in Counter(visitors).most_common():
            if count == 1:
                bouncers += 1
                
        return float(bouncers) / total * 100

# * * *

    def bentley_visitor_count(self, start_date="", end_date=""):
        visitors = set()
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            visitor = log.get("remote_host", "")
            if "." in visitor:
                visitors.add(visitor)
        return len(visitors)
        
    def get_referer_counts(self, limit=None, start_date="", end_date=""):
        referers = []
        for log in self.logs_filtered_by_time_range(start_date, end_date):
            referer = log.get("request_header_referer", "").rstrip("/")
            if referer and referer != "-":
                referers.append(referer)
        return Counter(referers).most_common(limit)

    @staticmethod
    def get_queries(log):
        queries = []
        query_dict = log.get("request_url_query_dict", {})
        for key in ["q1", "q2", "q3"]:
            query = query_dict.get(key, "")
            if query:
                queries.append(query[0].lower())

        return queries
        
# * * *
    
    @staticmethod
    def get_browser_family(log):
        browser_family = log.get("request_header_user_agent__browser__family", "")
        
        return browser_family
    
    @staticmethod
    def get_os_family(log):
        os_family = log.get("request_header_user_agent__os__family", "")

        return os_family
        
    @staticmethod
    def get_browser_version(log):
        browser_version = []
        browser_version.append(log.get("request_header_user_agent__browser__family", ""))
        browser_version.append(log.get("request_header_user_agent__browser__version_string", ""))
        browser_version = " ".join(browser_version)
            
        return browser_version
        
    @staticmethod
    def get_os_version(log):
        os_version = []
        os_version.append(log.get("request_header_user_agent__os__family", ""))
        os_version.append(log.get("request_header_user_agent__os__version_string", ""))
        os_version = " ".join(os_version)
            
        return os_version
        
    @staticmethod
    def is_mobile(log):
        is_mobile = log.get("request_header_user_agent__is_mobile")
        
        return is_mobile
        
# * * *
        
    def add_logs(self, filepath):
        print("adding logs from {}...".format(filepath))
        with open(filepath, mode="r") as f:
            if not filepath.endswith(".json"):
                new_log = self.parse_log(f)
            else:
                new_log = json.load(f)
        self.parsed_log += new_log

    def parse_log(self, f):
        logs = f.readlines()
        parsed_logs = []
        for log in tqdm(logs, desc="loading web log entries"):
            log = self.parser(log)
            for key in log.keys():
                if "datetimeobj" in key:
                    del log[key]
            parsed_logs.append(log)
        return parsed_logs

    def filter_staff_visits(self):
        self.parsed_log = [row for row in tqdm(self.parsed_log, desc="filtering out visits by staff...") if "." not in row.get("remote_host", "")]
        self.staff_filtered = True

    def filter_bots(self):
        self.parsed_log = [row for row in tqdm(self.parsed_log, desc="filtering out bots...") if not is_bot(row.get("request_header_user_agent__browser__family", ""))]
        self.bots_filtered = True

    def filter_non_page_requests(self):
        self.parsed_log = [row for row in tqdm(self.parsed_log, desc="filtering out non-page requests...") if not is_image_css_or_js(row.get("request_url_path", ""))]
        self.is_html_only = True

    def save_log_to_json(self):
        filename = self._construct_json_filename()
        with open(filename, mode="w") as f:
            json.dump(self.parsed_log, f, indent=4)

    def _construct_json_filename(self):
        filename = self.filename
        if self.staff_filtered and "nostaff" not in filename:
            filename += "_nostaff"
        if self.bots_filtered and "nobots" not in filename:
            filename += "_nobots"
        if self.is_html_only and "htmlonly" not in filename:
            filename += "_htmlonly"
        filename += ".json"

        return filename

    def logs_filtered_by_time_range(self, start_date, end_date):
        if not start_date and not end_date:
            return self.parsed_log

        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        filtered_logs = []

        for log in self.parsed_log:
            date = log.get("time_received_utc_isoformat", "")
            if not date:
                continue

            date = datetime.datetime.strptime(date.split("T")[0], "%Y-%m-%d").date()
            if start_date < date < end_date:
                filtered_logs.append(log)

        return filtered_logs


def is_image_css_or_js(url):
    matches = [".gif", ".js", ".css", ".jpg", ".ico", ".png"]
    if any(url.endswith(match) for match in matches):
        return True
    return False


def is_bot(user_agent_browser):
    acceptable_agents = ["chrome", "firefox", "ie", "safari", "mobile safari", "chrome mobile", "edge", "android",
                         "chrome mobile os", "opera", "opera mini", "ie mobile", "webkit nightly", "firefox mobile"]

    if user_agent_browser.lower() not in acceptable_agents:
        return True

    return False


if __name__ == "__main__":
    main()
