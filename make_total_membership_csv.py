# -*- coding: utf-8 -*-

from collections import OrderedDict
import csv
from datetime import datetime

changes_by_date = {}
with open('member-info.csv') as file:
    for row in csv.DictReader(file):
        initiation_number = int(row['Initiation No.'])
        # Initiation numbers between 365 and 474 are for former ΘΚΝs initiated
        # as alumni.
        if 365 <= initiation_number and initiation_number <= 474:
            continue

        class_year = int(row['Estimated Class Year'])

        initiation_date = row['Initiation Date']
        if initiation_date:
            initiation_date = datetime.strptime(initiation_date, '%m/%d/%Y')
        else:
            # If the initiation date is unknown, assume the initiation number
            # was assigned to a brother initiated as a freshman during the fall
            # term.
            initiation_date = datetime(class_year - 4, 12, 1)

        # Determine an “exit date” – a date on which the member with this
        # initiation number can no longer be considered part of the active
        # chapter. Assume that this initiation number belongs to a brother who
        # was in good standing at the time of graduation. This brother would’ve
        # become an alumnus upon graduating, so for the exit date use
        # Commencement, which at U-M is usually at the end of April or the
        # beginning of May.
        exit_date = datetime(class_year, 5, 1)
        # If the exit date is before the initiation date, the member is probably
        # an honorary initiate.
        if exit_date < initiation_date:
            continue
        # If the initiation number belongs to an expelled member, assume the
        # expulsion occurred halfway between initiation and graduation.
        if row['Expelled/Suspended']:
            exit_date = initiation_date + (exit_date - initiation_date) / 2

        # Increment the change in membership on the initiation date.
        changes_by_date[initiation_date] = changes_by_date.get(initiation_date, 0) + 1
        # Decrement the change in membership on the exit date.
        changes_by_date[exit_date] = changes_by_date.get(exit_date, 0) - 1

# Sort the changes by date.
changes_by_date = OrderedDict(sorted(changes_by_date.items(), key=lambda item: item[0]))

# Accumulate the changes in membership to get total membership by date.
total_membership = 0
with open('total-membership.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Total'])
    for date, change in changes_by_date.items():
        # Force total membership to be 0 from 1994–97, when the chapter was
        # dormant.
        if 1994 <= date.year and date.year <= 1997:
            total_membership = 0
        else:
            total_membership += change
        writer.writerow([date.strftime('%m/%d/%Y'), total_membership])
