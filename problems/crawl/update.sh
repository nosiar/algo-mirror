#! /bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

python $DIR/crawl.py
/bin/bash -c ". ~/py3env/bin/activate; exec python $DIR/update.py"

