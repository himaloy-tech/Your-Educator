import os
import sys
sys.path.append('/home/bitnami/projects/Your_Educator')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/bitnami/projects/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Your_Educator.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()