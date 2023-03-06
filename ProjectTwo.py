import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random



productReviewURL = "https://www.amazon.com/All-new-Kindle-Paperwhite-adjustable-Ad-Supported/product-reviews/B08W4J6PBL/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

count = 1 #num of reviews scraped   
page = 1 #num of pages scraped
pageIncrement = 11 #how many reviews per page
maxRetrieves = 11 #maximum number of reviews

numValid = 0
impactScores = []
i = 0

url = productReviewURL + str(page)
print(url)
options = Options()
options.headless = False
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.maximize_window()


browser.get(url)
xpathNumOfReview = '/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[4]/div'
numOfReviewsObject = browser.find_element(By.XPATH,(xpathNumOfReview))
numOfReviewsString = numOfReviewsObject.text
""" numOfReviewOne = numOfReviewsString.split(', ',1)[1]
numOfReviewTwo = numOfReviewOne.split('with',1)[0]
numOfReviewTwo = numOfReviewTwo.replace(',','') """
numOfReviews = numOfReviewsString.split(', ',1)[1].split('with',1)[0].replace(',','')
print(f"The total number of reviews: {numOfReviews}")





""" browser.get(url) """
"""  browser.set_page_load_timeout(10)  """







# Get number of reviews
# reviewNumPath = '/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[4]/div/div'
# reviewNum = browser.find_element(By.XPATH,(reviewNumPath))
# print("\n" + reviewNum + "\n")

while True:
    try:
        if i >= int(numOfReviews):
            break
        
        if count > pageIncrement:
            count = 1
            page += 1 

        url = productReviewURL + "&pageNumber=" + str(page)
        time.sleep(1)
        browser.get(url)
        #browser.set_page_load_timeout(10)          
        
        # Get Title
        #xPathTitle = '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[' + str(count) + ']/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span'
        #xPathTitle  = './/a[contains(@href,"/profile/")]/parent::span//text()'
        
        xPathProfile = '/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[' + str(count) + ']/div/div/div[1]/a'
        profile = browser.find_element(By.XPATH,(xPathProfile))
        print(f"{i}: {profile.text}")
        profile.click()
        
        # Get Impact
        #xPathImpact = '/html/body/div[1]/div[2]/div/div/div[4]/div[2]/div[1]/div[2]/div/div/span' 

        xPathImpact = '//*[@id="profile_v5"]/div/div/div[4]/div[2]/div[1]/div[2]/div/div/span'
        impact = browser.find_element(By.XPATH,(xPathImpact))
       
        print(f"Impact score: {impact.text}")


        impactScores.append(impact.text.replace(',',''))
        
        #impactScores[i] = impact
        
        count += 1
        i += 1

        browser.implicitly_wait(10)
        #time.sleep(rand(2,3))
        
    except Exception as e:
        #print("Exception On Count", count)
        count += 1

        if i >= int(numOfReviews):
            break
        
        if count > pageIncrement:
            count = 1
            page += 1
    #print(f"i = {i}")  
""" url = "https://www.amazon.com/Dell-Inspiron-Touchscreen-i5-1035G1-Windows/product-reviews/B09Z37QYFB/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews" + "&pageNumber=" + str(page)
browser.get(url)
        
browser.set_page_load_timeout(10) """





""" i vs numValid  """


browser.quit()

for x in range(len(impactScores)):
    if(int(impactScores[x]) > 50):
        numValid += 1

if(numValid < i / 2):
    print(f"Since the number of highly impactful reviewers is {numValid} out of {i}, the overall quality of the reviews for the product are unsatisfactory")
else:
    print(f"Since the number of highly impactful reviewers is {numValid} out of {i}, the overall quality of the reviews for the product are satisfactory")



"""  print("IMPACTSCORES")
for x in impactScores:
print(impactScores[x])
return impactScores """
