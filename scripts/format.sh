#!/usr/bin/env bash

set -e
set -x

autoflake --exclude=__init__.py --in-place ../sources --recursive --remove-all-unused-imports --remove-unused-variables
