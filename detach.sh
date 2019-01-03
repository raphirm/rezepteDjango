#!/usr/bin/env bash
killall -9  python3
python3 manage.py runserver 0.0.0.0:3000 &
