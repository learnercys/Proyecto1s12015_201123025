#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "users_system.settings")

    from django.core.management import execute_from_command_line

    # predefine a value if the port does not exist
    if sys.argv.__len__() == 2:
        sys.argv.append('8080')
    execute_from_command_line(sys.argv)
