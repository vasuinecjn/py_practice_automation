# shellcheck disable=SC2164
python3 -m venv selenium_env
. selenium_env/bin/activate
pip3 install -r requirements.txt

rm -rf reports
rm -rf screenshots
rm -rf logs

mkdir -p reports
mkdir -p screenshots
mkdir -p logs

### for report do the followinbg:
###-------------------------------------------------------------------------------
### 1. # pytest-html
##        --html parameter as --html=reports/report.html
### 2. # allure report
##        --alluredir=reports and run `allure serve reports` to generate reports

#pytest src/tests/test_login.py -sv -n 2 --browser chrome --click_screenshot yes --html=reports/report.html
pytest src/tests/test_add_recruitment.py -sv -n 2 --browser firefox --click_screenshot yes --html=reports/report.html
#pytest src/tests/test_login.py -sv -n 2 --browser firefox --click_screenshot yes --html=reports/report.html

#pytest src/tests/test_add_recruitment.py -n 1 --browser chrome --click_screenshot yes --alluredir=reports
#allure serve reports