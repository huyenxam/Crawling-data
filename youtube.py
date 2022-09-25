from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# 1. KHAI BÁO BROWSER
browser = webdriver.Chrome(executable_path="chromedriver.exe")

# 2. MỞ URL CỦA YOUTUBE
browser.get("https://www.youtube.com/watch?v=La46uttxyQk")
sleep(3)

# 3. SCROLL SCREEN
SCROLL_PAUSE_TIME = 0.2

# Get scroll height
last_height = browser.execute_script("return window.scrollY")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, window.scrollY + 200);")

    # Wait to load page
    sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return window.scrollY")

    if new_height == last_height:
        break
    last_height = new_height
sleep(2)


# 4. POST LIST
post_list = []

# Content
d_content = browser.find_element(By.XPATH, "//div[@id='container']//h1[@class='title style-scope ytd-video-primary-info-renderer']//yt-formatted-string")
# print(d_content.text)
content = d_content.text

# View
d_view = browser.find_element(By.XPATH, "//span[@class='view-count style-scope ytd-video-view-count-renderer']")
# print(d_view.text)
view = d_view.text

# Date
d_date = browser.find_element(By.XPATH, "//div[@class='style-scope ytd-video-primary-info-renderer']//div[@class='style-scope ytd-video-primary-info-renderer']//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']")
# print(d_date.text)
date = d_date.text

# Like
d_like = browser.find_element(By.XPATH, "//div[@id='menu']//ytd-menu-renderer//div//ytd-toggle-button-renderer//a//yt-formatted-string")
# print(d_like.text)
like = d_like.text

# Sum comment
d_total_comment = browser.find_element(By.XPATH, "//h2[@id='count']//yt-formatted-string")
# print(d_total_comment.text)
total_comment = d_total_comment.text

# Comment
l_comment_list = '//*[@id="contents"]/ytd-comment-thread-renderer'
d_comment_list = browser.find_elements(By.XPATH, l_comment_list)

# More reply
for i in range(1, len(d_comment_list) + 1):
    # reply
    try:
        l_reply_more = l_comment_list + "[" + str(i) + "]/div/ytd-comment-replies-renderer/div[1]/div[1]/div[1]/ytd-button-renderer/a"
        d_reply_more = browser.find_element(By.XPATH, l_reply_more)
        d_reply_more.click()
        sleep(0.2)
    except:
        pass
sleep(7)

# List comment
comments_list = []
for i in range(1, len(d_comment_list) + 1):
    # content
    content_comment = ""
    try:
        l_comment = l_comment_list + "[" + str(i) + "]/ytd-comment-renderer/div[3]/div[2]/div[2]"
        d_comment = browser.find_element(By.XPATH, l_comment)
        # print(d_comment.text)
        content_comment = d_comment.text
    except:
        content_comment = ""

    # hour
    time_comment = ""
    try:
        l_time_comment = l_comment_list + "[" + str(i) + "]/ytd-comment-renderer/div[3]/div[2]/div[1]/div[2]/yt-formatted-string/a"
        d_time_comment = browser.find_element(By.XPATH, l_time_comment)
        # print(d_time_comment.text)
        time_comment = d_time_comment.text
    except:
        time_comment = ""

    # like
    like_comment = ""
    try:
        l_like_comment = l_comment_list + "[" + str(i) + "]//div[3]/div[2]/ytd-comment-action-buttons-renderer/div[1]/span[2]"
        d_like_comment = browser.find_element(By.XPATH, l_like_comment)
        # print(d_like_comment.text)
        like_comment = d_like_comment.text
    except:
        like_comment = ""
    
    # List reply
    reply_list = []
    try:
        l_reply_list = l_comment_list + "[" + str(i) + "]/div/ytd-comment-replies-renderer/div[1]/div[2]/div[1]/ytd-comment-renderer"
        d_reply_list = browser.find_elements(By.XPATH, l_reply_list)
        for j in range(1, len(d_reply_list) + 1):
            # content reply
            reply_content = ""
            try:
                l_reply = l_reply_list + "[" + str(j) + "]/div[3]/div[2]/div[2]/ytd-expander/div"
                d_reply = browser.find_element(By.XPATH, l_reply)
                # print(d_reply.text)
                reply_content = d_reply.text
            except:
                reply_content = ""

            # time reply
            reply_time = ""
            try:
                l_reply_time = l_reply_list + "[" + str(j) + "]/div[3]/div[2]/div[1]/div[2]/yt-formatted-string/a"
                d_reply_time = browser.find_element(By.XPATH, l_reply_time)
                # print(d_reply_time.text)
                reply_time = d_reply_time.text
            except:
                reply_time = ""

            # like reply
            reply_like = ""
            try:
                l_reply_like = l_reply_list + "[" + str(j) + "]/div[3]/div[2]/ytd-comment-action-buttons-renderer/div[1]/span[2]"
                d_reply_like = browser.find_element(By.XPATH, l_reply_like)
                # print(d_reply_like.text)
                reply_like = d_reply_like.text
            except:
                reply_like = ""
            
            # Append reply
            reply_list.append({"content": reply_content, "time": reply_time, "like": reply_like})
    except:
        pass
    

    # Append comment
    comments_list.append({"content": content_comment, "time": time_comment, "like": like_comment, "reply": reply_list})


# Add post
post_list.append({"context": content, 
                  "view": view,
                  "time": date, 
                  "like": like,
                  "total comment": total_comment, 
                  "comments": comments_list})

print(post_list)
sleep(10)


# 8. Đóng browser
browser.close()