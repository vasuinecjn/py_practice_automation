# shellcheck disable=SC2164
rm -rf reports
rm -rf screenshots
mkdir screenshots
cd src/tests/
echo `pwd`
pytest test_login.py -sv -n 2 --browser chrome --html=../../reports/report.html