#! /bin/bash

python crawl.py
/bin/bash -c ". ~/py3env/bin/activate; exec python update.py"

