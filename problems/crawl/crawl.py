import os
import json
from glob import glob
from subprocess import call, check_call

try:
    check_call(['rm'] + glob(os.path.join('json/', '*.json')))
    check_call(['rm'] + glob(os.path.join('json/user/', '*.json')))
except:
    pass

with open('users','r') as f:
    uids = json.loads(f.read())

os.chdir("algo-crawl")
call(["scrapy", "crawl", "-o", "../json/problem.json", "problem"])
for uid in uids:
    call(["scrapy", "crawl", "-o", "../json/user/%d.json"%uid, "-a", "uid=%d"%uid, "user"])
