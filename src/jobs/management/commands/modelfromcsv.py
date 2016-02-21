from django.core.management.base import BaseCommand, CommandError
from jobs.crunchbase_models import Company
from django.core import serializers
from django.db import models
from dateutil import parser
import os

import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file')
        parser.add_argument('output')


    def handle(self, *args, **options):
        f = options['file']
        output = options['output']

        model_name = f.replace(".csv", "")

        with open(f, 'rb') as file:
            rows = csv.reader(file, delimiter=",", quotechar='"')
            column_names = []
            for row in rows:
              if rows.line_num == 1:
                for name in row:
                    column_names.append(name)
                print "Column Names: " + str(column_names)
              

              if rows.line_num == 2:
                model_definition = []
                for i, name in enumerate(column_names):
                    model_definition.append("    " + name + " = " + _determine_type_from_value( row[i] ) )

                model_definition = "\n".join(model_definition)


                model_code = _read_template("model_template.py")
                model_code = model_code.replace("[[model_name]]", model_name)
                model_code = model_code.replace("[[model_definition]]", model_definition)
                print model_code
                with open(output, 'a') as the_file:
                  the_file.write(model_code)

                break;

def _read_template(f):
  f = os.path.join("jobs", "templates", f)
  with open(f, 'rb') as myfile:
    return myfile.read()

def _determine_type_from_value(v):
  if v.isdigit():
      return "models.IntegerField(null=True)"
  if is_date(v):
      return "models.DateTimeField(null=True)"

  return "models.CharField(max_length=1000)"


def is_date(string):
    try: 
        parser.parse(string)
        return True
    except ValueError:
        return False