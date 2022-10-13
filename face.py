from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import json


def crawl(url, keyword):
    # KHAI BÁO BROWSER
    browser = webdriver.Chrome(executable_path="chromedriver.exe")

    # ĐĂNG NHẬP FACEBOOK
    browser.get("http://www.facebook.com/")
    # Điền thông tin vào ô user và pass
    txtUser = browser.find_element(By.ID, "email")
    txtUser.send_keys("huyenxam2310@gmail.com")  # Lấy tên account từ giao diện đăng nhập, fill tự động

    txtPass = browser.find_element(By.ID, "pass") 
    txtPass.send_keys("abc12345") # Lấy tên password từ giao diện đăng nhập, fill tự động

    # Submit form
    txtPass.send_keys(Keys.ENTER)
    sleep(random.randint(1, 3))


    # MỞ URL CỦA POST
    browser.get(url)
    sleep(random.randint(1, 5))

    # SEARCH
    try:
        d_search = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div[1]/div")
        d_search.click()
        sleep(random.randint(1, 3))
        txtSearch = browser.find_element(By.XPATH, "//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj xsyo7zv xdvlbce xc9qbxq x1g8yoln xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
        txtSearch.send_keys(keyword)
        txtSearch.send_keys(Keys.ENTER)
        sleep(random.randint(2, 5))
    except:
        print("error search")

        
    idx = 0    # Số bài viết cần crawl 
    height = 0
    post_list = []
    while(idx < 55):
        # SCROLL SCREEN
        browser.execute_script("window.scrollTo(0, "+ str(height) + ");")
        y_old = browser.execute_script("return window.scrollY")
        SCROLL_PAUSE_TIME = 0.2
        timeout = time.time() + 3
        # Get scroll height
        last_height = browser.execute_script("return window.scrollY")
        while True:
            # Scroll down to bottom
            browser.execute_script("window.scrollTo(0, window.scrollY + 400);")
            height += 400

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = browser.execute_script("return window.scrollY")

            if new_height == last_height:
                break
            last_height = new_height

            if time.time() > timeout:
                break    

        y_new = browser.execute_script("return window.scrollY")
        # Kiểm tra xem hết bài viết chưa
        if y_old == y_new:
            break

        # LIST POST
        d_post_list = browser.find_elements(By.XPATH, "//div[@class='x193iq5w x1xwk8fm']//div//div[@class='x1ja2u2z xh8yej3 x1n2onr6 x1yztbdb']")
        # print(len(d_post_list))
        for i in range(idx + 1, len(d_post_list) + 1):
            idx = i
            try:
                l_post = "//div[@class='x193iq5w x1xwk8fm']//div[" + str(i) + "]//div[@class='x1ja2u2z xh8yej3 x1n2onr6 x1yztbdb']" 
                d_post = browser.find_element(By.XPATH, l_post)

                browser.execute_script("window.scrollTo(0, window.scrollY + 10);")
                # URL
                url = ""
                try:
                    d_url = d_post.find_element(By.XPATH, ".//span[@class='x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j']//a")
                    url = d_url.get_attribute("href")
                    # print(url)
                except:
                    print("error url")
                    url = ""

                # TIME
                post_date = ""
                try:
                    element_to_hover_over  = d_post.find_element(By.XPATH, ".//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm']")
                    hover = ActionChains(browser).move_to_element(element_to_hover_over )
                    hover.perform()
                    sleep(random.randint(2, 5))
                    # element_to_hover_over.location_once_scrolled_into_view
                    d_date = browser.find_element(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1nxh6w3 x1sibtaa xo1l8bm xzsf02u x1yc453h']")
                    date = d_date.text.split(", ")
                    # date[1].split(" ") ->  ['2', 'Tháng', '10']
                    # date[2].split(" ") ->  ['2022', 'lúc', '20:55']
                    dd = date[1].split(" ")[0]
                    mm = date[1].split(" ")[2]
                    yy = date[2].split(" ")[0]
                    hour = date[2].split(" ")[2]
                    post_date = dd + "-" + mm + "-" + yy + " " + hour
                    print(post_date)
                except:
                    print("error time")
                    post_date = ""

                # SEE MORE CONTENT
                while(True):
                    try:
                        d_see_more = d_post.find_element(By.XPATH, '//div[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"]')
                        browser.execute_script("arguments[0].click();", d_see_more)
                        sleep(random.randint(1, 2))
                    except:
                        print("Not see more")
                        break
                
                element = browser.find_element(By.XPATH, l_post)
                element.location_once_scrolled_into_view
                sleep(4)

                # TITLE, CONTENT, USER, POST_DATE
                content = ""
                user = ""
                title = ""
                try:
                    d_content = d_post.find_element(By.XPATH, ".//div[@class='x9f619 x1n2onr6 x1ja2u2z x2bj2ny x1qpq9i9 xdney7k xu5ydu1 xt3gfkd xh8yej3 x6ikm8r x10wlt62 xquyuld']")
                    # print(d_content.text)
                    post = d_content.text.split("\n")
                    user = post[0]
                    title = post[3]
                    content = " ".join(post[3:-8])
                except:
                    print("error content")

                if content == "":
                    break
                
                # SHARE
                share = 0
                try:
                    d_share = d_post.find_element(By.XPATH, ".//div[@class='x6s0dn4 x78zum5 x2lah0s x17rw0jw']//div[3]//span")
                    # print(d_share.text)
                    share = d_share.text.split(" ")[0]
                    if share.find("K") > -1:
                        share = float(share[:-1].replace(",", ".")) * 1000
                    share = int(share)
                except:
                    print("error share")
                    share = 0

                # LIKE, LOVE, HAHA
                status_dict = {"All": 0, "Like": 0, "Love": 0, "Care": 0, "Haha": 0, "Sad": 0, "Angry": 0, "Wow": 0}
                # click
                try:
                    d_status = d_post.find_element(By.XPATH, ".//span[@class='xrbpyxo x6ikm8r x10wlt62 xlyipyv x1exxlbk']")
                    browser.execute_script("arguments[0].click();", d_status)
                    sleep(random.randint(1, 3))
                except:
                    print("Not see click")

                # More
                try:
                    d_more = d_status.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div')
                    browser.execute_script("arguments[0].click();", d_more)
                    sleep(random.randint(1, 2))
                except:
                    print("Not see more")
                
                # status_dict
                status_en = {"Tất cả": "All", "Thích": "Like", "Yêu thích": "Love", "Thương thương": "Care", "Haha": "Haha", "Buồn": "Sad", "Tức giận" : "Angry", "Wow": "Wow"}
                try:
                    d_status_list = browser.find_elements(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div")
                    for d_status in d_status_list:
                        status = str(d_status.get_attribute("aria-label")).split(", ")
                        if len(status) > 1:
                            p_x = status[1]
                            if p_x.find("K") > -1:
                                p_x = float(p_x[:-1].replace(",", ".")) * 1000
                            status_dict[status_en[status[0]]] = int(p_x)
                    # print(status_dict)
                except:
                    print("Not see like")

                # exist
                while True:
                    try:
                        d_exist = d_status.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div')
                        browser.execute_script("arguments[0].click();", d_exist)
                        sleep(random.randint(1, 2))
                    except:
                        print("Not see exist")
                        break
                
                
                # TOTAL COMMENT
                total_comment = 0
                try:
                    d_t_comment = d_post.find_element(By.XPATH, ".//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xi81zsa']")
                    browser.execute_script("arguments[0].click();", d_t_comment)
                    # print(d_t_comment.text)
                    total_comment = d_t_comment.text.split(" ")[0]
                    if total_comment.find("K") > -1:
                        total_comment = float(total_comment[:-1].replace(",", ".")) * 1000
                    total_comment = int(total_comment)

                    sleep(random.randint(1, 3))
                except:
                    print("error total_comment")
                    total_comment = 0

                
                # MORE COMMENT
                while(True):
                    try:
                        d_comment_more = d_post.find_element(By.XPATH, ".//div[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv']")
                        browser.execute_script("arguments[0].click();", d_comment_more)
                        sleep(random.randint(10, 20))
                    except:
                        print("error more comment")
                        break

                # LIST COMMENT
                comment_list = []
                try:
                    d_list_comment = d_post.find_elements(By.XPATH, ".//div[@class='x1jx94hy x12nagc']//ul//li//div[@class='x1n2onr6']")
                    # print(len(d_list_comment))
                except:
                    print("error comment_list")
                
                for j, d_comment in enumerate(d_list_comment):
                    # CONTENT COMMENT
                    comment_content = ""
                    try:
                        d_comment_content = d_comment.find_element(By.XPATH, ".//div[@class='x1iorvi4 xjkvuk6 x1lliihq']")
                        # print(d_comment_content.text)
                        comment_content = d_comment_content.text
                    except:
                        print("error comment_content")
                        comment_content = ""
                    if comment_content == "":
                        break

                    # TIME COMMENT
                    comment_time = ""
                    try:
                        time_to_hover_over = d_comment.find_element(By.XPATH, ".//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa x1fcty0u']//span")
                        hover = ActionChains(browser).move_to_element(time_to_hover_over)
                        hover.perform()
                        sleep(random.randint(3, 4))
                        time_to_hover_over.location_once_scrolled_into_view
                        browser.execute_script("window.scrollTo(0, window.scrollY + 50);")
                        d_comment_time = browser.find_element(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa xo1l8bm xzsf02u x1yc453h']")
                        comment_time = d_comment_time.text.split(", ")
                        #  date[1].split(" ") ->  ['2', 'Tháng', '10']
                        # date[2].split(" ") ->  ['2022', 'lúc', '20:55']
                        dd = comment_time[1].split(" ")[0]
                        mm = comment_time[1].split(" ")[2]
                        yy = comment_time[2].split(" ")[0]
                        hour = comment_time[2].split(" ")[2]
                        comment_time = dd + "-" + mm + "-" + yy + " " + hour
                        # print(comment_time)
                    except:
                        print("error comment_time")
                        comment_time = ""
                    
                    # LIKE, LOVE, HAHA COMMENT
                    status_dict_comment = {"All": 0, "Like": 0, "Love": 0, "Care": 0, "Haha": 0, "Sad": 0, "Angry": 0, "Wow": 0}
                    try:
                        # click
                        d_status_comment = d_comment.find_element(By.XPATH, ".//div[@class='x1ja2u2z x10l6tqk x177n6bx x1ve5b48 xlshs6z']//div//div//div//span//div")
                        browser.execute_script("arguments[0].click();", d_status_comment)
                        sleep(random.randint(1, 3))
                        
                        # More
                        try:
                            d_more_comment = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div')
                            browser.execute_script("arguments[0].click();", d_more_comment)
                            sleep(random.randint(1, 2))
                        except:
                            print("Not see more")

                        # status_dict
                        try:
                            d_status_list_comment = browser.find_elements(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div")
                            for d_status_comment in d_status_list_comment:
                                status_comment = str(d_status_comment.get_attribute("aria-label")).split(", ")
                                if len(status_comment) > 1:
                                    co_x = status_comment[1]
                                    if co_x.find("K") > -1:
                                        co_x = float(co_x[:-1].replace(",", ".")) * 1000
                                    status_dict_comment[status_en[status_comment[0]]] = int(co_x)
                            # print(status_dict_comment)
                        except:
                            print("Not see like")

                        # exist
                        while True:
                            try:
                                d_exist_comment = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div')
                                browser.execute_script("arguments[0].click();", d_exist_comment)
                                sleep(random.randint(1, 3))
                            except:
                                print("Not see exist")
                                break
                    except:
                        print("error statuc dict comment")
                    
                    # REPLY LIST 1
                    reply_list = []
                    d_reply_list = d_comment.find_elements(By.XPATH, "..//div[@class='xdj266r xexx8yu x4uap5 x18d9i69 xkhd6sd']//ul//li//div[@class='x1n2onr6 x46jau6']") 
                    for k, d_reply in enumerate(d_reply_list):
                        # CONTENT REPLY
                        reply_content = ""
                        try:
                            d_reply_content = d_reply.find_element(By.XPATH,  ".//div[@class='x1iorvi4 xjkvuk6 x1lliihq']")
                            # print(d_reply_content.text)
                            reply_content = d_reply_content.text
                        except:
                            print("error reply content")
                            reply_content = ""

                        if reply_content == "":
                            break
                            
                        #  TIME REPLY
                        reply_time = ""
                        try:
                            timereply_to_hover_over = d_reply.find_element(By.XPATH, ".//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa x1fcty0u']//span")
                            hover = ActionChains(browser).move_to_element(timereply_to_hover_over)
                            hover.perform()
                            sleep(random.randint(3, 4))
                            timereply_to_hover_over.location_once_scrolled_into_view
                            d_reply_time = browser.find_element(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa xo1l8bm xzsf02u x1yc453h']")
                            reply_time = d_reply_time.text.split(", ")
                            # date[1].split(" ") ->  ['2', 'Tháng', '10']
                            # date[2].split(" ") ->  ['2022', 'lúc', '20:55']
                            dd = reply_time[1].split(" ")[0]
                            mm = reply_time[1].split(" ")[2]
                            yy = reply_time[2].split(" ")[0]
                            hour = reply_time[2].split(" ")[2]
                            reply_time = dd + "-" + mm + "-" + yy + " " + hour
                            # print(reply_time)
                        except:
                            print("error reply time")
                            reply_time = ""

                        # LIKE, LOVE, HAHA REPLY
                        status_dict_reply = {"All": 0, "Like": 0, "Love": 0, "Care": 0, "Haha": 0, "Sad": 0, "Angry": 0, "Wow": 0}
                        try:
                            # click
                            d_status_reply = d_reply.find_element(By.XPATH, ".//div[@class='x1ja2u2z x10l6tqk x177n6bx x1ve5b48 xlshs6z']//div//div//div//span//div")
                            browser.execute_script("arguments[0].click();", d_status_reply)
                            sleep(random.randint(1, 3))
                            
                            # More
                            try:
                                d_more_reply = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div')
                                browser.execute_script("arguments[0].click();", d_more_reply)
                                sleep(random.randint(1, 2))
                            except:
                                print("Not see more")

                            # status_dict
                            try:
                                d_status_list_reply = browser.find_elements(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div")
                                for d_status_reply in d_status_list_reply:
                                    status_reply = str(d_status_reply.get_attribute("aria-label")).split(", ")
                                    if len(status_reply) > 1:
                                        re_x = status_reply[1]
                                        if re_x.find("K") > -1:
                                            re_x = float(re_x[:-1].replace(",", ".")) * 1000
                                        status_dict_reply[status_en[status_reply[0]]] = int(re_x)
                                # print(status_dict_reply)
                            except:
                                print("Not see like")

                            # exist
                            while True:
                                try:
                                    d_exist_reply = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div')
                                    browser.execute_script("arguments[0].click();", d_exist_reply)
                                    sleep(random.randint(1, 2))
                                except:
                                    print("Not see exist")
                                    break
                        except:
                            print("error statuc dict reply")

                        # REPLY LIST 2
                        d_reply_list2 = d_reply.find_elements(By.XPATH, "..//div//ul//li//div[@class='x1n2onr6 x1xb5h2r']") 
                        for h, d_reply2 in enumerate(d_reply_list2):
                            # CONTENT REPLY
                            reply_content2 = ""
                            try:
                                d_reply_content2 = d_reply2.find_element(By.XPATH,  ".//div[@class='x1iorvi4 xjkvuk6 x1lliihq']")
                                # print(d_reply_content2.text)
                                reply_content2 = d_reply_content2.text
                            except:
                                print("error reply content 2")
                                reply_content2 = ""
                            
                            if reply_content2 == "":
                                break
                                
                            #  TIME REPLY
                            reply_time2 = ""
                            try:
                                timereply_to_hover_over2 = d_reply2.find_element(By.XPATH, ".//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa x1fcty0u']//span")
                                hover2 = ActionChains(browser).move_to_element(timereply_to_hover_over2)
                                hover2.perform()
                                sleep(random.randint(3, 4))
                                timereply_to_hover_over2.location_once_scrolled_into_view
                                d_reply_time2 = browser.find_element(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa xo1l8bm xzsf02u x1yc453h']")
                                reply_time2 = d_reply_time2.text.split(", ")
                                #  date[1].split(" ") ->  ['2', 'Tháng', '10']
                                # date[2].split(" ") ->  ['2022', 'lúc', '20:55']
                                dd = reply_time2[1].split(" ")[0]
                                mm = reply_time2[1].split(" ")[2]
                                yy = reply_time2[2].split(" ")[0]
                                hour = reply_time2[2].split(" ")[2]
                                reply_time2 = dd + "-" + mm + "-" + yy + " " + hour
                                # print(reply_time2)
                            except:
                                print("error reply time2")
                                reply_time2 = ""

                            # LIKE, LOVE, HAHA REPLY
                            status_dict_reply2 = {"All": 0, "Like": 0, "Love": 0, "Care": 0, "Haha": 0, "Sad": 0, "Angry": 0, "Wow": 0}
                            try:
                                # click
                                d_status_reply2 = d_reply2.find_element(By.XPATH, ".//div[@class='x1ja2u2z x10l6tqk x177n6bx x1ve5b48 xlshs6z']//div//div//div//span//div")
                                browser.execute_script("arguments[0].click();", d_status_reply2)
                                sleep(random.randint(1, 2))
                                
                                # More
                                try:
                                    d_more_reply2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div')
                                    browser.execute_script("arguments[0].click();", d_more_reply2)
                                    sleep(random.randint(1, 2))
                                except:
                                    print("Not see more2")

                                # status_dict
                                try:
                                    d_status_list_reply2 = browser.find_elements(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div")
                                    for d_status_reply2 in d_status_list_reply2:
                                        status_reply2 = str(d_status_reply2.get_attribute("aria-label")).split(", ")
                                        if len(status_reply2) > 1:
                                            re2_x = status_reply2[1]
                                            if re2_x.find("K") > -1:
                                                re2_x = float(re2_x[:-1].replace(",", ".")) * 1000
                                            status_dict_reply2[status_en[status_reply2[0]]] = int(re2_x)
                                    # print(status_dict_reply2)
                                except:
                                    print("Not see like2")

                                # exist
                                while True:
                                    try:
                                        d_exist_reply2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div')
                                        browser.execute_script("arguments[0].click();", d_exist_reply2)
                                        sleep(random.randint(1, 2))
                                    except:
                                        print("Not see exist2")
                                        break
                            except:
                                print("error statuc dict reply2")
                            
                            # APPEND REPLY_LIST
                            reply_list.append({"id_reply": k+h+2,
                                               "id_comment": j+1,
                                               "post_date": reply_time2,
                                               "sentiment": "",
                                               "content": reply_content2,
                                               "status_dict": status_dict_reply2})
                        
                        # APPEND REPLY_LIST
                        reply_list.append({"id_reply": k+1,
                                           "id_comment": j+1,
                                           "post_date": reply_time,
                                           "sentiment": "",
                                           "content": reply_content,
                                           "status_dict": status_dict_reply})
                    
                    # APPEND COMMENT LIST
                    comment_list.append({"id_comment": j+1,
                                         "id_post": i,
                                         "post_date": comment_time,
                                         "sentiment": "",
                                         "content": comment_content,
                                         "status_dict": status_dict_comment,
                                         "replys": reply_list})

                # APPEND POST
                post_list.append({"id_post":i,
                                  "content": content,
                                  "post_date": post_date,
                                  "sentiment": "",
                                  "share": share,
                                  "source_division": 1,
                                  "title": title,
                                  "total comment": total_comment,
                                  "url": url,
                                  "username": user,
                                  "status_dict": status_dict,
                                  "comments": comment_list})
                
                # EXIST MORE COMMENT
                try:
                    d_ex_comment = d_post.find_element(By.XPATH, ".//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xi81zsa']")
                    # print(d_t_comment.text)
                    browser.execute_script("arguments[0].click();", d_ex_comment)
                    sleep(random.randint(1, 2))
                except:
                    print("error total_comment")
                
            except:
                print("error post")
        
        

    with open('face1.json', 'w', encoding='utf-8') as f:
        json.dump(post_list, f, ensure_ascii=False, indent=4)

    # 8. Đóng browser
    browser.close()

    return post_list


crawl("https://www.facebook.com/groups/174764463261090", "fresher")