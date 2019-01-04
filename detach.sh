#!/usr/bin/env bash
killall  python3
python3 manage.py runserver 0.0.0.0:3000 &
