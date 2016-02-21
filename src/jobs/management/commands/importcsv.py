from django.core.management.base import BaseCommand, CommandError
from jobs.crunchbase_models import Company
from django.core import serializers
from django.db import models
from dateutil import parser
import sys
import types
import importlib

import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file')
        parser.add_argument('class_name')

    def handle(self, *args, **options):
        f = options['file']
        class_name = options['class_name']
        obj_class = load_class(class_name)

        total_row_count = 0
        count = 1

        with open(f, 'rb') as file:
            rows = csv.reader(file, delimiter=",", quotechar='"')
            total_row_count = sum(1 for row in rows) - 1
            print "Total Rows: " + str(total_row_count) 

        with open(f, 'rb') as file:
            rows = csv.reader(file, delimiter=",", quotechar='"')
            column_names = []
            for row in rows:
              if rows.line_num == 1:
                 for name in row:
                    column_names.append(name)
                 print "Column Names: " + str(column_names)
                 continue

              obj = load_class(class_name)()

              for i, cell_data in enumerate(row):
                column_name = column_names[i]
                if hasattr(obj, column_name):
                    if obj._meta.get_field(column_name).get_internal_type() == 'DateTimeField':
                        try:
                            cell_data = parser.parse(cell_data)
                        except:
                            pass
                    setattr(obj, column_name, cell_data)

                else:
                    print "Could not find column " + column_names[i] + " in definition" + str(obj)

              try:
                obj.save()
                print ".",

                if count % 1000 == 1:
                    print ""
                    print str(count) + "/" + str(total_row_count)
                    print ""

                #print str(count) + "/" + str(total_row_count) + ": " + serializers.serialize('json', [ obj, ])
              except Exception as e:
                pass
                #print str(e)
              count += 1

def load_class(full_class_string):
    """
    dynamically load a class from a string
    """

    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]

    module = importlib.import_module(module_path)
    # Finally, we retrieve the Class
    return getattr(module, class_str)