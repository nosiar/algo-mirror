import sys
import os
import django

sys.path.append('/home/raison/www/algospot')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "algospot.settings")
django.setup()

