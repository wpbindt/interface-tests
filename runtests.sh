#!/bin/env sh
docker run -it -v $(pwd):/srv interface-tests python3 -m pytest tests.py
