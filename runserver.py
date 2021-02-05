import os
import sys

print("[x] Example of usage : python runserver.py 0.0.0.0:8080")

try :
    sep = sys.argv[1].find(":")
    ip = sys.argv[1][:sep]
    port = sys.argv[1][sep+1:]

    os.system(f"python {os.path.dirname(os.path.abspath(__file__))}/mapyto_django/manage.py runserver {ip}:{port}")

except IndexError:
    os.system(f"python {os.path.dirname(os.path.abspath(__file__))}/mapyto_django/manage.py runserver 127.0.0.1:8080")
