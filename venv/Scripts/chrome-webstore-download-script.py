#!D:\test\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'chrome-webstore-download==0.1.3','console_scripts','chrome-webstore-download'
__requires__ = 'chrome-webstore-download==0.1.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('chrome-webstore-download==0.1.3', 'console_scripts', 'chrome-webstore-download')()
    )
