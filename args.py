import os
from datetime import datetime

now = datetime.now()
nowStr = now.strftime("%Y%m%d-%H%M%S")

# More Information http://celestrak.com/NORAD/documentation/gp-data-formats.php
# url = "http://celestrak.com/NORAD/elements/gp.php?GROUP=gps-ops&FORMAT=tle

# Define params to get information from http://celestrak.com/
args = {
    'url_main': "http://celestrak.com/NORAD/elements/gp.php?CATNR=",
    'url_test': "http://celestrak.com/NORAD/elements/gp.php?{QUERY}=VALUE[&FORMAT=VALUE]",
    'query': "",
    'norad_id': "",
    'output_csv': os.path.join(os.path.dirname(os.path.realpath(__file__)) + "/csv_files/" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv")
}

