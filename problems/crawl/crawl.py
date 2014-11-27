import os
import json
from glob import glob
from subprocess import call, check_call

cur_dir = os.path.dirname(os.path.realpath(__file__))
json_dir = os.path.join(cur_dir, 'json')
user_dir = os.path.join(json_dir, 'user')

try:
    check_call(['rm'] + glob(os.path.join(json_dir, '*.json')))
    check_call(['rm'] + glob(os.path.join(user_dir, '*.json')))
except:
    pass

with open(os.path.join(cur_dir, 'users'),'r') as f:
    uids = json.loads(f.read())

os.chdir(os.path.join(cur_dir, 'algo-crawl'))
call(['scrapy', 'crawl', '-o',
      os.path.join(json_dir, 'problem.json'), 'problem'])
for uid in uids:
    call(['scrapy', 'crawl', '-o',
          os.path.join(user_dir, '%d.json'%uid), '-a', 'uid=%d'%uid, 'user'])
