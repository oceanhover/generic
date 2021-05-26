#!/usr/bin/env python3
# Author: ASML-KCHX
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""
Py_template.py is to help create shebang lines in the beginning of a file,
such that user doesn't need to copy and paste shebange lines everytime.
"""

import os
import sys

def environ_define():
    """Remove python 2.7 from sys.path then add python 3.x paths from user define folder(s)"""

    for item in sys.path:
        if "2.7" in item or "Python27" in item:
            sys.path.remove(item)

    #User define path for sys.path
    python3_lib = [\
    'C:\\Program Files (x86)\\Python37-32\\Lib',\
    'C:\\Users\\kenchan\\OneDrive - ASML\\Desktop\\Python\\Python3\\vermin_python_3.6.7_08\\python-3.6.7.amd64\\DLLs',\
    'C:\\Users\\kenchan\\OneDrive - ASML\\Desktop\\Python\\Python3\\vermin_python_3.6.7_08\\python-3.6.7.amd64\\lib',\
    'C:\\Users\\kenchan\\OneDrive - ASML\\Desktop\\Python\\Python3\\vermin_python_3.6.7_08\\python-3.6.7.amd64',\
    'C:\\Users\\kenchan\\OneDrive - ASML\\Desktop\\Python\\Python3\\vermin_python_3.6.7_08\\python-3.6.7.amd64\\lib\\site-packages',\
    'C:\\Users\\kenchan\\OneDrive - ASML\\Desktop\\Python\\Python3\\vermin_python_3.6.7_08\\python-3.6.7.amd64\\lib\\site-packages\\win32',\
    'C:\\Users\\kenchan\\OneDrive - ASML\\Desktop\\Python\\Python3\\vermin_python_3.6.7_08\\python-3.6.7.amd64\\lib\\site-packages\\win32\\lib',\
    'C:\\Users\\kenchan\\OneDrive - ASML\\Desktop\\Python\\Python3\\vermin_python_3.6.7_08\\python-3.6.7.amd64\\lib\\site-packages\\IPython\\extensions',\
    'C:\\Users\\kenchan\\OneDrive - ASML\\Desktop\\Python\\Python3\\vermin_python_3.6.7_08\\settings\\.ipython'\
    ]

    sys.path = python3_lib + sys.path
    return sys.path

def shebang_line(defalut = True):
    """Add shebang line"""
    if defalut == True:
        try:
            shebang_context = "\
#!/usr/bin/env python3\n\
# Author: ASML / Ken Chang-KCHX \n\
# Date: 2021/05/26 \n\
# This program or module is free software: you can redistribute it and/or\n\
# modify it under the terms of the GNU General Public License as published\n\
# by the Free Software Foundation, either version 3 of the License, or\n\
# (at your option) any later version. It is provided for educational\n\
# purposes and is distributed in the hope that it will be useful, but\n\
# WITHOUT ANY WARRANTY; without even the implied warranty of\n\
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU\n\
# General Public License for more details.\n\n\n\n\n\
def main():\n\
    \"\"\"\"\"\"\n\n\n\n\n\
if __name__ == \"__main__\":\n\
\tmain()\n"
            return shebang_context

        except NameError as e:
            print(e)
        except ValueError as e:
            print(e)
    else:
        pass

def call_vim():
    """call Vim editor and start to edit python script"""

    command =(["vim Untitle.py"] if not sys.platform.startswith("win") else\
            ["C:\\Program Files (x86)\\Vim\\vim82\\Vim.exe","Untitle.py"])
    return command


def main():
    environ_define()
    import subprocess
    for path in sys.path:
        print(path)

    shebang_lines = shebang_line()
    with open("Untitle.py", 'w') as f:
        f.write(shebang_lines)
        f.close
    
    subprocess.call(call_vim())

if __name__ == "__main__":
    main()

