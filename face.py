from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

# 1.KHAI BÁO BROWSER
browser = webdriver.Chrome(executable_path="chromedriver.exe")

# 2. ĐĂNG NHẬP FACEBOOK
browser.get("http://www.facebook.com/")
# Điền thông tin vào ô user và pass
txtUser = browser.find_element(By.ID, "email")
txtUser.send_keys("quynd20032310@gmail.com")

txtPass = browser.find_element(By.ID, "pass")
txtPass.send_keys("abc12345")

# Submit form
txtPass.send_keys(Keys.ENTER)
sleep(3)


# 3. MỞ URL CỦA POST
browser.get("https://www.facebook.com/halotravel.hanoi")
sleep(5)


# 4. SCROLL SCREEN
SCROLL_PAUSE_TIME = 0.2
timeout = time.time() + 5
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

    if time.time() > timeout:
        break
    
sleep(2)

# 5.  MORE COMMENT
timeout_comment = time.time() + 10
while(True):
    try:
        d_comment_more = browser.find_element(By.XPATH, "//div[@class='qi72231t nu7423ey tav9wjvu flwp5yud tghlliq5 gkg15gwv s9ok87oh s9ljgwtm lxqftegz bf1zulr9 frfouenu bonavkto djs4p424 r7bn319e bdao358l fsf7x5fv tgm57n0e s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk dnr7xe2t aeinzg81 srn514ro rl78xhln nch0832m om3e55n1 cr00lzj9 rn8ck1ys s3jn8y49 g4tp4svg o9erhkwx dzqi5evh hupbnkgi hvb2xoa8 fxk3tzhb jl2a5g8c f14ij5to icdlwmnq i85zmo3j rtxb060y cgu29s5g i15ihif8 i5oewl5a cxfqmxzd']")
        browser.execute_script("arguments[0].click();", d_comment_more)
        sleep(2)
    except:
        break
    
    if time.time() > timeout_comment:
        break
sleep(3)


# 6. SEE MORE CONTENT
while(True):
    try:
        d_see_more = browser.find_element(By.XPATH, '//div[contains(text(), "See more")]')
        browser.execute_script("arguments[0].click();", d_see_more)
    except:
        print("Not see more")
        break

# 7. LIST POST
post_list = []
l_post_list = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[2]/div/div/div"
d_post_list = browser.find_elements(By.XPATH, l_post_list)

print(len(d_post_list))
for i, d_post in enumerate(d_post_list):
    # TIME
    date = ""
    try:
        d_date = d_post.find_element(By.XPATH, ".//span[@class='f7rl1if4 adechonz f6oz4yja dahkl6ri axrg9lpx rufpak1n qtovjlwq qbmienfq rfyhaz4c rdmi1yqr ohrdq8us nswx41af fawcizw8 l1aqi3e3 sdu1flz4']//a[@class='qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq jxuftiz4 cxfqmxzd tes86rjd']")
        # print(d_time.text)
        date = d_date.text
    except:
        date = ""

    # CONTENT
    content = ""
    try:
        d_content = d_post.find_element(By.XPATH, ".//span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas m2nijcs8 hxfwr5lz k1z55t6l oog5qr5w tes86rjd pbevjfx6 ztn2w49o']")
        print(d_content.text)
        content = d_content.text
    except:
        content = ""

    # TOTAL COMMENT
    total_comment = ""
    try:
        # d_t_comment = d_post.find_element(By.XPATH, ".//div[@class='i85zmo3j alzwoclg jez8cy9q epnzikpj']//div[2]//span")
        d_t_comment = d_post.find_element(By.XPATH, ".//span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas m2nijcs8 hxfwr5lz k1z55t6l oog5qr5w tes86rjd rtxb060y']")
        # print(d_t_comment.text)
        total_comment = d_t_comment.text
    except:
        total_comment = ""
    
    # SHARE
    share = ""
    try:
        d_share = d_post.find_element(By.XPATH, ".//div[@class='i85zmo3j alzwoclg jez8cy9q epnzikpj']//div[3]//span")
        # print(d_share.text)
        share = d_share.text
    except:
        share = ""

    # LIKE, LOVE, HAHA
    status_dict = {}
    try:
        # click
        try:
            d_status = d_post.find_element(By.XPATH, ".//span[@class='cxfqmxzd k0kqjr44 o3hwc0lp nws3uo2z']")
            browser.execute_script("arguments[0].click();", d_status)
            sleep(2)
        except:
            print("Not see more")

        # More
        try:
            d_more = d_status.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div/div[1]/span')
            browser.execute_script("arguments[0].click();", d_more)
        except:
            print("Not see more")
        sleep(5)
        
        # status_dict
        d_status_list = browser.find_elements(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[@class='qi72231t n3hqoq4p r86q59rh b3qcqh3k fq87ekyn s5oniofx s3jn8y49 o9erhkwx dzqi5evh hupbnkgi hvb2xoa8 f14ij5to l3ldwz01 icdlwmnq qgrdou9d nu7423ey t7k66tzq s9ok87oh s9ljgwtm lxqftegz bf1zulr9 frfouenu bonavkto djs4p424 r7bn319e bdao358l jxuftiz4 fsf7x5fv m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m om3e55n1 cr00lzj9 rn8ck1ys b0ur3jhr fxk3tzhb o3hwc0lp a26p89d5 gewbibgg']")
        for d_status in d_status_list:
            status = d_status.get_attribute("aria-label").split(", ")
            status_dict[status[0]] = status[1]

        # exist
        d_exist = d_status.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div')
        browser.execute_script("arguments[0].click();", d_exist)
        sleep(3)
    except:
        print("Not see more")

    # LIST COMMENT
    comment_list = []
    try:
        l_comment_list = l_post_list + "[" + str(i+1) +  "]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li"
        d_comment_list = d_post.find_elements(By.XPATH, l_comment_list)
        # print(len(d_comment_list))
    except:
        pass

    for j, d_comment in enumerate(d_comment_list):
        # CONTENT COMMENT
        comment_content = ""
        try:
            d_comment_content = d_comment.find_element(By.XPATH, ".//div[@class='m8h3af8h l7ghb35v kjdc1dyq kmwttqpk gh25dzvf']//div")
            # print(d_comment_content.text)
            comment_content = d_comment_content.text
        except:
            comment_content = ""

        # TIME COMMENT
        comment_time = ""
        try:
            d_comment_time = d_comment.find_element(By.XPATH, ".//a//span[@class='f7rl1if4 adechonz f6oz4yja dahkl6ri axrg9lpx rufpak1n qtovjlwq qbmienfq rfyhaz4c rdmi1yqr ohrdq8us nswx41af fawcizw8 l1aqi3e3 sdu1flz4']")
            # print(d_comment_time.text)
            comment_time = d_comment_time.text
        except:
            comment_time = ""

        # LIKE COMMENT
        comment_like = ""
        try:
            d_comment_like = d_comment.find_element(By.XPATH, ".//span[@class='f7rl1if4 adechonz f6oz4yja dahkl6ri axrg9lpx rufpak1n qtovjlwq qbmienfq rfyhaz4c rdmi1yqr ohrdq8us nswx41af fawcizw8 l1aqi3e3 sdu1flz4']//div")
            # print(d_comment_like.get_attribute("aria-label"))
            comment_like = d_comment_like.get_attribute("aria-label")
        except:
            print(1)
            comment_like = ""

        # REPLY LIST
        reply_list = []
        l_reply_list = l_comment_list + "[" + str(j) + "]/div[2]/div/ul/li"
        d_reply_list = browser.find_elements(By.XPATH, l_reply_list)

        for k, d_reply in enumerate(d_reply_list):
            # CONTENT REPLY
            reply_content = ""
            try:
                d_reply_content = d_reply.find_element(By.XPATH,  ".//div[@class='m8h3af8h l7ghb35v kjdc1dyq kmwttqpk gh25dzvf']//div")
                # print(d_reply_content.text)
                reply_content = d_reply_content.text
            except:
                reply_content = ""

            # TIME REPLY
            reply_time = ""
            try:
                d_reply_time = d_reply.find_element(By.XPATH, ".//a//span[@class='f7rl1if4 adechonz f6oz4yja dahkl6ri axrg9lpx rufpak1n qtovjlwq qbmienfq rfyhaz4c rdmi1yqr ohrdq8us nswx41af fawcizw8 l1aqi3e3 sdu1flz4']")
                # print(d_reply_time.text)
                reply_time = d_reply_time.text
            except:
                reply_time = ""

            # LIKE REPLY
            reply_like = ""
            try:
                d_reply_like = browser.find_element(By.XPATH, ".//span[@class='f7rl1if4 adechonz f6oz4yja dahkl6ri axrg9lpx rufpak1n qtovjlwq qbmienfq rfyhaz4c rdmi1yqr ohrdq8us nswx41af fawcizw8 l1aqi3e3 sdu1flz4']//div")
                # print(d_reply_like.get_attribute("aria-label"))
                reply_like = d_reply_like.get_attribute("aria-label")
            except:
                reply_like = ""
            
            
            # APPEND REPLY_LIST
            if reply_content == "":
                pass
            else:    
                reply_list.append({"content": reply_content, "time": reply_time, "like": reply_like})
        
        # APPEND COMMENT_LIST
        if comment_content == "":
            pass
        else:
            comment_list.append({"content": comment_content,
                                "time": comment_time,
                                "like": comment_like,
                                "reply": reply_list})
    # APPEND POST_LIST
    if content == "":
        pass
    else:
        post_list.append({"status": status_dict,
                          "time": date,
                          "content": content,
                          "total comment": total_comment,
                          "share": share,
                          "comments": comment_list})

import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(post_list, f, ensure_ascii=False, indent=4)

# print(post_list)

sleep(4)

# 8. Đóng browser
browser.close()