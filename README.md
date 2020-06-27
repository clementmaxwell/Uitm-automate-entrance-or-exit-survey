# Uitm-automate-entrance-or-exit-survey
A web crawler using Selenium to automate the process of filling in radio boxes in a site.

## Getting Started
I'm mainly using Brave browser (compatible with ChromeDriver) my dev. environment. To set it up with other browser,
please refer to other sources.

## Prerequisites:
[Python 3 and above](https://www.python.org/downloads/) - Pick windows x86-64 executable installer
```
Selenium web driver:
  in terminal, type:
  ~ pip install selenium
  after installing python
```
```
Web Browser (Chrome/Brave/etc.)
```
[ChromeDriver](https://chromedriver.chromium.org/downloads) - Pick chromedriver_win32.zip
P.S.Please check your browser version before downloading ChromeDriver

## Configure app properties:
write id
```
stdId = "id"
```
write pw
```
stdPwd = "pw"
```
setup box score: range is 1 to 5.
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
## License
This project is licensed under GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details
