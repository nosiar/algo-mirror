import os
import json
import setup
from problems.models import Problem, User, Source, Category

cur_dir = os.path.dirname(os.path.realpath(__file__))

def update_problem():
    problem_file = os.path.join(cur_dir, 'json/problem.json')

    with open(problem_file, 'r') as f:
        problems = json.loads(f.read())

    for p in problems:
        keyword = p['keyword'][0].strip()
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

        try:
            p = Problem.objects.get(keyword=keyword)
        except:
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

def update_user():
    user_dir = os.path.join(cur_dir, 'json/user')

    user_files = [os.path.join(user_dir, x) for x in os.listdir(user_dir)]

    for user_file in user_files:
        with open(user_file, 'r') as f:
            user = json.loads(f.read())[0]

            uid = user['uid'][0].strip()
            name = user['name'][0].strip()

            try:
                u = User.objects.get(name=name)
            except:
                u = User(uid=uid, name=name)
                u.save()

            for p in user['problems']:
                keyword = p.strip()

                try:
                    p = Problem.objects.get(keyword=keyword)
                except:
                    continue
                u.problem.add(p)

if __name__ == '__main__':
    update_problem()
    update_user()
