#! /bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

/bin/bash -c ". ~/www/algospot/venv/bin/activate; exec python $DIR/crawl.py; exec python $DIR/update.py"

