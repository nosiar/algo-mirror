import os
import json
import setup
from problems.models import Problem, User


def update_problem():
    pass

def update_user():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
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
