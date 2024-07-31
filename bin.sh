# shellcheck disable=SC2164
python3 -m venv selenium_env
. selenium_env/bin/activate
pip3 install -r requirements.txt

rm -rf reports
rm -rf screenshots
rm -rf logs

mkdir reports
mkdir screenshots
mkdir logs

#pytest src/tests/test_login.py -sv -n 2 --browser chrome --html=reports/report.html
#pytest src/tests/test_add_recruitment.py -n 2 --browser firefox --click_screenshot yes --html=reports/report.html
pytest src/tests/test_add_recruitment.py -n 1 --browser chrome --click_screenshot yes --html=reports/report.html