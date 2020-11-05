import os
import sys
sys.path.append('/opt/bitnami/projects/Your_Educator')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/projects/Your_Educator/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Your_Educator.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()