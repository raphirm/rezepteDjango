#!/usr/bin/env bash
killall -9 node
python3 manage.py runserver 0.0.0.0:3000 &
