#!C:\Users\trist\PycharmProjects\TP2020_ENCRYPTION\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'screed==1.0.4','console_scripts','screed'
__requires__ = 'screed==1.0.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('screed==1.0.4', 'console_scripts', 'screed')()
    )
