from selenium import webdriver
from time import sleep
import random
import json
from selenium.webdriver.common.by import By

# KHAI BÁO BROWSER
browser = webdriver.Chrome(executable_path="chromedriver.exe")

# MỞ URL CỦA YOUTUBE
browser.get("https://www.youtube.com/watch?v=-Wduzor_Y1Q")
sleep(random.randint(2, 5))

# POST LIST
post_list = []
idx = 0
comments_list = []

# CONTENT
d_content = browser.find_element(By.XPATH, "//div[@id='container']//h1[@class='title style-scope ytd-video-primary-info-renderer']//yt-formatted-string")
# print(d_content.text)
content = d_content.text

# VIEW
d_view = browser.find_element(By.XPATH, "//span[@class='view-count style-scope ytd-video-view-count-renderer']")
# print(d_view.text)
view = d_view.text

# DATE
d_date = browser.find_element(By.XPATH, "//div[@class='style-scope ytd-video-primary-info-renderer']//div[@class='style-scope ytd-video-primary-info-renderer']//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']")
# print(d_date.text)
date = d_date.text

# LIKE
d_like = browser.find_element(By.XPATH, "//div[@id='menu']//ytd-menu-renderer//div//ytd-toggle-button-renderer//a//yt-formatted-string")
# print(d_like.text)
like = d_like.text

browser.execute_script("window.scrollTo(0, 300);")
sleep(random.randint(3, 7))
# TOTAL COMMENT
d_total_comment = browser.find_element(By.XPATH, "//h2[@id='count']//yt-formatted-string")
# print(d_total_comment.text)
total_comment = d_total_comment.text



while True:
    # SCROLL SCREEN
    SCROLL_PAUSE_TIME = 0.2
    # Get scroll height
    last_height = browser.execute_script("return window.scrollY")
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, window.scrollY + 300);")

    # Wait to load page
    sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return window.scrollY")

    if new_height == last_height:
        break
    last_height = new_height
    sleep(random.randint(2, 5))


    # LIST COMMENT
    l_comment_list = './/*[@id="contents"]/ytd-comment-thread-renderer'
    d_comment_list = browser.find_elements(By.XPATH, l_comment_list)

    # MORE REPLY
    for i in range(idx+1, len(d_comment_list) +1):
        try:
            l_reply_more = l_comment_list + "[" + str(i) + "]/div/ytd-comment-replies-renderer/div[1]/div[1]/div[1]/ytd-button-renderer/a"
            d_reply_more = browser.find_element(By.XPATH, l_reply_more)
            d_comment_list[i-1].location_once_scrolled_into_view
            d_reply_more.click()
            sleep(2)
        except:
            pass
    sleep(random.randint(1, 3))


    # FOR COMMENT
    for i in range(idx + 1, len(d_comment_list) + 1):
        idx = i
        # CONTENT
        content_comment = ""
        try:
            d_comment = d_comment_list[i-1].find_element(By.XPATH, './/*[@id="content-text"]')
            # print(d_comment.text)
            content_comment = d_comment.text
        except:
            print("error content_comment")
            content_comment = ""

        # TIME
        time_comment = ""
        try:
            d_time_comment = d_comment_list[i-1].find_element(By.XPATH, './/*[@id="header-author"]/yt-formatted-string/a')
            # print(d_time_comment.text)
            time_comment = d_time_comment.text
        except:
            print("error time_comment")
            time_comment = ""

        # LIKE
        like_comment = ""
        try:
            d_like_comment = d_comment_list[i-1].find_element(By.XPATH, './/*[@id="vote-count-middle"]')
            # print(d_like_comment.text)
            like_comment = d_like_comment.text
        except:
            print("error like_comment")
            like_comment = ""
        

        # LIST REPLY
        reply_list = []
        try:
            d_reply_list = d_comment_list[i-1].find_elements(By.XPATH, './/div//ytd-comment-replies-renderer//div[1]//div[2]//div[1]//ytd-comment-renderer')
            for j in range(len(d_reply_list)):
                # CONTENT REPLY
                reply_content = ""
                try:
                    d_reply = d_reply_list[j].find_element(By.XPATH, './/*[@id="content-text"]')
                    # print(d_reply.text)
                    reply_content = d_reply.text
                except:
                    print("error reply_content")
                    reply_content = ""

                # TIME REPLY
                reply_time = ""
                try:
                    d_reply_time = d_reply_list[j].find_element(By.XPATH, './/*[@id="header-author"]/yt-formatted-string/a')
                    # print(d_reply_time.text)
                    reply_time = d_reply_time.text
                except:
                    print("error reply_time")
                    reply_time = ""

                # LIKE REPLY
                reply_like = ""
                try:
                    d_reply_like = d_reply_list[j].find_element(By.XPATH, './/*[@id="vote-count-middle"]')
                    # print(d_reply_like.text)
                    reply_like = d_reply_like.text
                except:
                    print("error reply_like")
                    reply_like = ""
                
                # APPEND REPLY
                reply_list.append({"content": reply_content, "time": reply_time, "like": reply_like})
        except:
            print("a")
            pass
    
        # APPEND COMMENT
        comments_list.append({"content": content_comment, "time": time_comment, "like": like_comment, "reply": reply_list})


# ADD POST
post_list.append({"context": content, 
                    "view": view,
                    "time": date, 
                    "like": like,
                    "total comment": total_comment, 
                    "comments": comments_list})

# print(post_list)
sleep(random.randint(1, 3))

# SAVE FILE
with open('youtube3.json', 'w', encoding='utf-8') as f:
    json.dump(post_list, f, ensure_ascii=False, indent=4)

# CLOSE
browser.close()