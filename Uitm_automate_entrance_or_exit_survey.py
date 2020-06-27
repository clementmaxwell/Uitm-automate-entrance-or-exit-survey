from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class User:
  def __init__(self, userId, password, noOfCourses, radioBoxesKey, webDriverPath, browserPath):
      self.userId = userId
      self.password = password
      self.radioBoxesKey = radioBoxesKey # 1 - 5
      self.noOfCourses = noOfCourses
      self.webDriverPath = webDriverPath
      self.browserPath = browserPath
    
  def launchWebdriver(self, typeOfSurvey):
      option = webdriver.ChromeOptions()
      option.binary_location = self.browserPath
      browser = webdriver.Chrome(executable_path=self.webDriverPath,
      chrome_options=option)
      browser.get('https://i-learn.uitm.edu.my/login')

      def logIn():
          student_box = browser.find_element_by_link_text("Student")
          student_box.click()

          username_box = browser.find_element_by_id("UserUsername") 
          username_box.send_keys(self.userId)

          password_box = browser.find_element_by_id("UserPassword")
          password_box.send_keys(self.password)

          login = browser.find_element_by_xpath("//*[@id='UserLoginFormForm']"
          +"/div[3]/button")
          login.click()
        
      def logOut():
          browser.get("https://i-learn.uitm.edu.my/logout")
        
      def closeBrowser():
          browser.close()
          browser.quit()

      def clickMyCourse(): # Click on 'myCourse'
          myCourse = browser.find_element_by_xpath("//*[@id='myCourse']")
          myCourse.click()

      def fillInForm():
          def findUpperBoundOfRadioBoxes(): # find no. of columns of boxes.
              totalRadioBoxes = 0
              # assuming max possible box is 30
              for i in range(1, 31): # Can be tweaked
                  try:
                      browser.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/div/div/div/div[1]/table/tbody/tr[{i}]/td[3]/input")
                      totalRadioBoxes += 1
                  except NoSuchElementException: 
                      pass
              return totalRadioBoxes
  
          def tickTheRadioBoxes(numOfRadioBoxes):
              for col in range(1, numOfRadioBoxes+1): # iterate thru n columns of boxes.
                  # 'self.radioBoxesKey + 2' is to get the actual n value of td[n]. say, i want my score to be 1.
                  # so the actual td in the site is 1 + 2 = 3.
                  # refer to the website for a clearer explaination.
                  tickRadioBoxes = browser.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/div/div/div/div[1]/table/tbody/tr[{col}]/td[{self.radioBoxesKey + 2}]/input")
                  browser.execute_script("arguments[0].click();", tickRadioBoxes)
                  time.sleep(0.5)

          greyEntrancePos = 1 # default is 1. must be equal to x (range('x', y)) in line 69.
          totalNumberOfRadioBoxes = 0
          # can be tweaked when testing. default: range(1, x + 1)
          for course in range(1, self.noOfCourses + 1):
              courseTitle = browser.find_element_by_xpath(f"/html/body/div[2]/div[1]/div[1]/ul/li[1]/ul/li[{course}]/a/span")
              courseTitle.click()

              # why? its a dynamic page.
              time.sleep(1) # so this is a must! else, won't work.

              GreyEntranceLink = browser.find_element_by_xpath(f"/html/body/div[2]/div[1]/div[1]/ul/li[1]/ul/li[{greyEntrancePos}]/ul/li[5]/a")
              GreyEntranceLink.click()

              if (typeOfSurvey == "entrance"):
                  greenBox = browser.find_element_by_xpath("/html/body/div[2]/div[2]"
                  +"/div[2]/div/div[3]/div/a")
                  greenBox.click()
              else:
                  blueBox = browser.find_element_by_xpath("/html/body/div[2]/div[2]"
                  +"/div[2]/div/div[5]/div/a")
                  blueBox.click()


              totalNumberOfRadioBoxes = findUpperBoundOfRadioBoxes()
              tickTheRadioBoxes(totalNumberOfRadioBoxes)

              time.sleep(1) # same reason as above.
              sumbit_button = browser.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/div/div/div/div[1]/table/tbody/tr[{totalNumberOfRadioBoxes+1}]/td/button")
              browser.execute_script("arguments[0].click();", sumbit_button)

              totalNumberOfRadioBoxes = 0 # reset variables.
              greyEntrancePos += 1
              time.sleep(0.5)
        
      logIn()
      clickMyCourse()
      fillInForm()
      logOut()
      closeBrowser()

stdId = "2019225186"    # write id
stdPwd = "241001"       # write pw
stdRadioBoxesKey = 5    # box score: range is 1 to 5.
stdNoOfCourses = 6      # no. of courses
stdWebdriverPath = "C:/Users/Clement/PyProjects/chromedriver.exe"
stdBrowserPath = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

student1 = User(stdId, stdPwd, stdNoOfCourses, stdRadioBoxesKey, stdWebdriverPath, stdBrowserPath)
student1.launchWebdriver("exit") # 2 options: 'entrance' or 'exit'.