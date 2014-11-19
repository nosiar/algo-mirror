import sys
import os
import json
import django

if __name__ == '__main__':
    sys.path.append('/home/raison/www/algospot')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "algospot.settings")
    from problems.models import Problem, User

    django.setup()

    d = os.path.dirname(os.path.realpath(__file__))
    with open(d + '/user11033.json', 'r') as f:
        user = json.loads(f.read())[0]
    
    uid = user['uid'][0].strip()
    name = user['name'][0].strip()

    u = User(uid=uid, name=name)
    u.save()
    
    for p in user['problems']:
        keyword = p.strip()
        
        p = Problem.objects.get(keyword=keyword)
        u.problem.add(p)


