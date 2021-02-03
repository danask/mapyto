import os
import sys

try:
    sep = sys.argv[1].find(":")
    ip = sys.argv[1][:sep]
    port = sys.argv[1][sep+1:]

    os.system(f"python {os.path.dirname(os.path.abspath(__file__))}/mapyto_django/manage.py runserver {ip}:{port}")

except IndexError:
    print("Example of usage : python runserver.py 0.0.0.0:8080")