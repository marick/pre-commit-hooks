#!/bin/bash
# Prevents force-pushing to production or master.

PATTERN=$1
if [ "$PATTERN" == "" ]; then
    echo "Bad .pre-commit-config.yaml: you must use :args"
    exit 1
fi

echo "PATTERN"

BRANCH=`git rev-parse --abbrev-ref HEAD`

echo $BRANCH to pre-push

if [[ "$BRANCH" =~ $PATTERN ]]; then
  echo "Prevented push to $BRANCH."
  echo "If you really want to do this, use --no-verify to bypass this pre-push hook."
  exit 1
fi

exit 0
