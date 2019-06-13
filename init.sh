#!/bin/bash

cp -r /srv/* /work/
./transform.py
gitbook init
gitbook serve
