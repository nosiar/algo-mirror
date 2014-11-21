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
    with open(d + '/json/user/9324.json', 'r') as f:
        user = json.loads(f.read())[0]
    
    uid = user['uid'][0].strip()
    name = user['name'][0].strip()

    u = User(uid=uid, name=name)
    u.save()
    
    for p in user['problems']:
        keyword = p.strip()
        
        try:
            p = Problem.objects.get(keyword=keyword)
        except:
            continue
        u.problem.add(p)


