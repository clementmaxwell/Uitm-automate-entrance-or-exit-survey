# Uitm-automate-entrance-or-exit-survey
A web crawler using Selenium to automate the process of filling in radio boxes in UiTm student portal.
V.1.1.0

![Demo](https://github.com/clementmaxwell/Uitm-automate-entrance-or-exit-survey/blob/master/demo.gif)

## Getting Started
I'll be mainly using Brave browser (compatible with ChromeDriver) as my development environment. To set it up with other browser,
please refer to other sources.

## Prerequisites:
[Python 3 and above](https://www.python.org/downloads/) - Pick windows x86-64 executable installer

Selenium web driver for Python:
```
  in terminal, type:
  ~ pip install selenium
  after installing python
```
Web Browser (Chrome/Brave/etc.)

[ChromeDriver](https://chromedriver.chromium.org/downloads) - Pick chromedriver_win32.zip

P.S.Please check your browser version before downloading ChromeDriver. Browser version and ChromeDriver MUST match.

## Configure app properties:
starting from line 107:

write your id
```
stdId = "id"
```
write your pw
```
stdPwd = "pw"
```
setup your box score: range is 1 to 5.
```
stdRadioBoxesKey = 5
```
no. of courses that you have:
```
stdNoOfCourses = 6
```

## Configure path:
Your web driver path:
```
stdWebdriverPath = "C:/Users/Clement/PyProjects/chromedriver.exe"
```
Your browser path:
```
stdBrowserPath = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
```
Your desired type of entrance:
```
student1.launchWebdriver("exit") # 2 options: 'entrance' or 'exit'.
```

## Deployment:
On Windows:
```
cd 'to\installed\folder'
python Uitm_automate_entrance_or_exit_survey.py
```
or sometimes:
```
python3 Uitm_automate_entrance_or_exit_survey.py
```
## License
This project is licensed under GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details
