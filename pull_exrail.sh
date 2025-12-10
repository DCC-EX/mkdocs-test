#!/bin/bash
MACROBASE="EXRAIL2MacroBase.h"
BRANCH="devel"
OUTPUT="snippets/exrail/exrail-ref.md"

curl -s "https://raw.githubusercontent.com/DCC-EX/CommandStation-EX/refs/heads/${BRANCH}/${MACROBASE}" > "$MACROBASE"
if test -s "$MACROBASE" ; then
    : all well
else
    echo "ERROR: no input in $MACROBASE ABORTING"
    exit 255
fi
mkdir -p snippets/exrail
awk -f pull-exrail.awk "$MACROBASE" > "$OUTPUT"
rm -f "$MACROBASE"
if test -s "$OUTPUT" ; then
    : all well
else
    echo "ERROR: no output in $OUTPUT ABORTING"
    exit 255
fi
exit 0


