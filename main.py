from selenium import webdriver
import json
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

def get_instagram_datas(driver, stores):
    id = "Room_282828"
    pw = "Tt12241509!@"
    
    instagram_datas = []
    
    action_chains = ActionChains(driver)
    
    # Go to instagram page
    driver.implicitly_wait(10)
    driver.get('https://www.instagram.com/')
    # id, pw 입력
    id_input = driver.find_element("css selector", "#loginForm > div > div:nth-child(1) > div > label > input")
    pw_input = driver.find_element("css selector", "#loginForm > div > div:nth-child(2) > div > label > input")     #비밀번호 입력창
    id_input.send_keys(id)
    pw_input.send_keys(pw)
    pw_input.send_keys(Keys.RETURN)
    time.sleep(5)
    # 나중에 하기 입력
    # btn_later1.click()
    # btn_later1 = driver.find_element("xpath", "//*[contains(@class, '_ac8f')]")
    # btn_later1.click()
    # time.sleep(2)
    # 알림 설정 ("나중에 하기 버튼 클릭")
    btn_later2 = driver.find_element("css selector", '._a9--._a9_1')
    btn_later2.click()
    time.sleep(2)
    
    for store in stores:
        print(store)
        data = {}
        data['brandName'] = store
        driver.implicitly_wait(5)
        driver.get('https://www.instagram.com/')
        # 검색 버튼
        btn_search = driver.find_elements("css selector", '._ab6-')[1]
        btn_search.click()
        time.sleep(2)
        #검색 입력
        search_input = driver.find_element("css selector", "._aawg > input")
        search_input.send_keys(store)
        time.sleep(2)
        search_input.send_keys(Keys.RETURN)
        time.sleep(2)
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)
        #게시물 개수 가져오기
        infos = driver.find_elements("css selector", "._ac2a > span")
        count = infos[0].text
        data['count'] = count
        posts_list = []
        # Do-something to count 카운트 개수에 변화가 있는지 없는지 여부를 검사하는 function
        # modify
        count = 6 if int(count) >= 6 else int(count)
        is_changed = True
        if(is_changed):
            posts = driver.find_elements("css selector", "._aagw")
            for idx in range(count):
                post_data = {}
                #img url 가져오기
                post_info_img = driver.find_elements("css selector", "._aagv > img")[idx].get_attribute('src') if driver.find_elements("css selector", "._aagv > img") else '' 
                posts[idx].click()
                time.sleep(5)
                post_info_text = driver.find_elements("css selector", "._a9zs > h1")[0].text if driver.find_elements("css selector", "._a9zs > h1") else ''
                post_url = driver.current_url
                time_stamp = driver.find_elements("css selector", "._aaqe")[0].get_attribute('datetime') if driver.find_elements("css selector", "._aaqe") else ''
                post_data['content'] = post_info_text
                post_data['imgURL'] = post_info_img
                post_data['postURL'] = post_url
                post_data['timeStamp'] = time_stamp
                # 'ESC' 키 누르기
                action_chains.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                posts_list.append(post_data)
                # Do something to database
        data['post'] = posts_list
        instagram_datas.append(data)
        time.sleep(3)
    return instagram_datas

def get_donut_revenge_datas(headers):
    # get response from url
    res = requests.get('https://fingerpress.kr/apis/mall/shop/products-catalog?page=0&npp=20&categories=563657&customerGradeNo=-2&orderType=PRODUCT_ORDER_NO&useSortedBySoldOutAllPage=undefined&customerNo=0', headers=headers)
    datas = json.loads(res.text)['content']
    
    # productName
    # productImageURL
    # productPrice
    # productURL
    
    donut_revenge_datas = []
    for data in datas:
        dic = {}
        tmp = {}
        dic['brandName'] = 'donut_revenge'
        tmp['productName'] = data['name']
        tmp['productURL'] = "https://fingerpress.kr/product/" + data['address']
        tmp['productImageURL'] = 'https://contents.sixshop.com/thumbnails' + data['thumbnails'][0].split('.')[0] + '_1000.jpg'
        tmp['productPrice'] = data['price']['regularPrice']
        dic['brandProduct'] = tmp
        donut_revenge_datas.append(dic)
    
    return donut_revenge_datas

def main():
    #driver
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
    # user-agent
    headers = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    # Authorization 
    headers.update({
        'Authorization': 'Basic MTkwMDg4'
    })
    
    stores = [
    'tilllate.official',
    '8lackout.secret',
    'sandpiper_seoul',
    'fierceville',
    'thelastats',
    'finger_press',
    'vlindfiles',
    'wrath_made',
    'reover.official',
    'satineyez'
    ]
    
    res = get_instagram_datas(driver, stores)
    with open('list.json', 'w') as f:
        json.dump(res, f)
    
    res = get_donut_revenge_datas(headers)
    with open('donut_revenge.json', 'w') as f:
        json.dump(res,f)

if __name__ == "__main__":
    main()
