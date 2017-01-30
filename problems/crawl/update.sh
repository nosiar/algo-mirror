#! /bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

python $DIR/crawl.py
/bin/bash -c ". ~/www/algospot/venv/bin/activate; exec python $DIR/update.py"

