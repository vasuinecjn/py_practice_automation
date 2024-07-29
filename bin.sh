# shellcheck disable=SC2164
python3 -m venv selenium_env
. selenium_env/bin/activate
pip3 install -r requirements.txt

rm -rf reports
rm -rf screenshots
mkdir screenshots
pytest src/tests/test_login.py -sv -n 2 --browser chrome --html=reports/report.html


#python3 -m venv selenium_env
#. selenium_env/bin/activate
#pip3 install -r requirements.txt
#rm -rf reports
#rm -rf screenshots
#mkdir screenshots
#cd src/tests/
#echo `pwd`
#pytest test_login.py -sv -n 2 --browser chrome --html=../../reports/report.html