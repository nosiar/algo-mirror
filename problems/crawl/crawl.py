import os
from glob import glob
from subprocess import call, check_call

try:
    check_call(['rm'] + glob(os.path.join('json/', '*.json')))
    check_call(['rm'] + glob(os.path.join('json/user/', '*.json')))
except:
    pass

os.chdir("algo-crawl")
call(["scrapy", "crawl", "-o", "../json/problem.json", "problem"])
for uid in [9324,11033,36,764,2,1337,200]:
    call(["scrapy", "crawl", "-o", "../json/user/%d.json"%uid, "-a", "uid=%d"%uid, "user"])
