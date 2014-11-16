import sys
import os
import json
import django

if __name__ == '__main__':
    sys.path.append('/home/raison/www/algospot')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "algospot.settings")
    from problems.models import Problem, Category, Source

    django.setup()

    d = os.path.dirname(os.path.realpath(__file__))
    with open(d + '/problems.json', 'r') as f:
        problems = json.loads(f.read())

    for p in problems:
        keyword = p['uid'][0].strip()
        name = p['name'][0].strip()
        if p['source']:
            source = p['source'][0].strip()
        else:
            source = '기타'
        category = [c.strip() for c in p['category']]
        submitted = int(p['submitted'][0])
        accepted = int(p['accepted'][0])

        try:
            s = Source.objects.get(name=source)
        except Source.DoesNotExist:
            s = Source(name=source)
            s.save()

        p = Problem(keyword=keyword, name=name, source=s,
                submitted=submitted, accepted=accepted)
        p.save()
        
        for c in category:
            try:
                c = Category.objects.get(name=c)
            except Category.DoesNotExist:
                c = Category(name=c)
                c.save()
            p.category.add(c)
