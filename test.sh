#!/bin/bash
python3 manage.py test >$?

if grep "0"  $?
 then
  python3 manage.py runserver
fi
