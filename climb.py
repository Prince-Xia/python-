from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path=r'C:\Users\DOT-1\Desktop\geckodriver.exe')
driver.get(
    'https://www.airbnb.cn/s/%E6%B7%B1%E5%9C%B3/homes?refinement_paths%5B%5D=%2Fhomes&current_tab_id=home_tab&selected_tab_id=home_tab&screen_size=medium&hide_dates_and_guests_filters=false&place_id=ChIJkVLh0Aj0AzQRyYCStw1V7v0&map_toggle=false')
# 找到页面中所有的租房
rent_list = driver.find_elements_by_css_selector('div._gig1e7')

# 对每个出租房
for eachhouse in rent_list:
    # 找到评论数量
    try:
        comment = eachhouse.find_element_by_css_selector('span._69pvqtq')
        comment = comment.text
    except:
        comment = 0
    # 找到价格
    price = eachhouse.find_element_by_css_selector('div._59f9ic')
    price = price.text.replace('每晚', '').replace('价格', '').replace('\n', '')
    # 找到名称
    name = eachhouse.find_element_by_css_selector('div._qrfr9x5')
    name = name.text
    # 找到房屋类型，大小
    details = eachhouse.find_element_by_css_selector('div._1etkxf1')
    details = details.text
    house_type = details.split(" · ")[0]
    bed_number = details.split(" · ")[1]
    print(comment, price, name, house_type, bed_number)
