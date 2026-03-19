# # MaccabiDent Mobile Automation


## Install
pip install -r requirements.txt

## Run Appium
appium

## Run tests
pytest

 pytest --env=test         
 pytest --env=prod

## Run tests with HTML report
pytest --html=reports/report.html --self-contained-html

 ## restore to last commit:

 git reset --hard HEAD

 ## Run GUI:
python test_gui.py

## freeze requirements:
pip freeze > requirements.txt

## Requirements

Appium server
Android SDK
Python 3.x