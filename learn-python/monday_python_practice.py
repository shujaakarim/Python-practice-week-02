"""
import os
import json

def main():
    total=4500+12800
    unused = 5
    print( "Total:",total )

main()
"""

"""

# enmus
from enum import StrEnum


class students_work_update(StrEnum):
    TODAY_TASK = "completed task"
    PENDING_TASK = "yes"
    
students_update = students_work_update.PENDING_TASK()
print(students_update)

"""
"""

1. Today's date. Import date from datetime and print Report for 2026-11-02, using today's date. 
Then rewrite your import as import datetime and change the rest of your code to match.
"""

from datetime import date

print(f"report for {date.today()}")
print("report for ", date.today())
