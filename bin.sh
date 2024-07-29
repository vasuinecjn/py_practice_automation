# shellcheck disable=SC2164
pip install -r requirements.txt
rm -rf reports
rm -rf screenshots
mkdir screenshots
cd src/tests/
pytest test_login.py -sv -n 2 --browser chrome --html=../../reports/report.html