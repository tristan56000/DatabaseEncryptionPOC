#!C:\Users\trist\PycharmProjects\TP2020_ENCRYPTION\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'phe==1.4.0','console_scripts','pheutil'
__requires__ = 'phe==1.4.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('phe==1.4.0', 'console_scripts', 'pheutil')()
    )
