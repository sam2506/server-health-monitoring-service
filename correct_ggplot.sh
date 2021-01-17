#!/bin/bash
GGPLOT_PATH=$(find "./venv" -name "ggplot")
UTILS_PATH=$GGPLOT_PATH"/utils.py"
SMOOTHERS_PATH=$GGPLOT_PATH"/stats/smoothers.py"
find $UTILS_PATH -type f -exec sed -i 's/pd.tslib.Timestamp,/pd._tslib.Timestamp,/g' {} \;
find $SMOOTHERS_PATH -type f -exec sed -i 's/pandas.lib/pandas/g' {} \;
find $SMOOTHERS_PATH -type f -exec sed -i 's/pd.tslib.Timestamp,/pd.Timestamp,/g' {} \;