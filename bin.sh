# shellcheck disable=SC2164
export python='/opt/homebrew/bin/python3'
export pytest='/Library/Frameworks/Python.framework/Versions/3.12/bin/pytest'
export pip='/opt/homebrew/bin/pip3'

rm -rf reports
rm -rf screenshots
mkdir screenshots
cd src/tests/
echo `pwd`
pytest test_login.py -sv -n 2 --browser chrome --html=../../reports/report.html