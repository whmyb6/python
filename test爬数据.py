# encoding: utf-8
'''
find_element_by_xpath()的几种方法

Xpath (XML Path Language)，是W3C定义的用来在XML文档中选择节点的语言
一：从根目录/开始
有点像Linux的文件查看，/代表根目录，一级一级的查找，直接子节点，相当于css_selector中的>号
/html/body/div/p
二. 根据元素属性选择：
查找具体的元素，必须在前面输入标准开头//，表示从当前节点寻找所有的后代元素
//div/* div下面的所有的元素
//div//p 先在整个文档里查找div，再在div里查找p节点(只要在内部，不限定是否紧跟) ；等价于 css_selector里的('div p')
//div/p p是div的直接子节点； 等价于 css_selector里的('div > p')
//*[@style] 查找所有包含style的所有元素，所有的属性要加@； 等价于 css_selector里的('*[style]')
//p[@spec='len'] 必须要加引号；等价于 css_selector里的("p[spec='len']")
//p[@id='kw'] xpath中对于id,class与其他元素一视同仁，没有其他的方法
三. 选择第几个节点
//div/p[2] 选择div下的第二个p节点 ；等价于css_selector里的div>p:nth-of-type(2) 符合p类型的第二个节点
//div/*[2] 选择div下第二个元素
//div/p[position()=2] position()=2 指定第二个位置； 等价于上面的 //div/p[2]
position()>=2 位置大于等于2
position()<2 位置小于2
position()！=2 位置不等于2
//div/p[last()] 选择div下的倒数第一个p节点； last()倒数第一个
//div/p[last()-1] 选择div下的倒数第二个p节点；
//div/p[position()=last()] 倒数第一个
//div/p[position()=last()-1] 倒数第二个
//div/p[position()>=last()-2] 倒数第一个，第二个，第三个
四. 组合选择
//p | //button 选择所有的p和button，等价于css_selector里的 p, button
//input[@id='kw' and @class='su'] 选择id=kw 并且 class="su"的input元素
五. 兄弟节点的选择
相邻后面的兄弟节点的选择：following-sibling:: 两个冒号
//div/following-sibling::p 选择div里相邻的p节点
相邻前面的兄弟节点的选择：preceding-sibling:: 此方法在css_selector中没有
//div/preceding-sibling::p[2] 选择div里前面相邻的第二个节点，不加[2]选择的是前面的所有的p节点
六. 选择父节点
//p[@spec='len']/.. 选择p节点的上层节点 此方法在css_selector中没有
//p[@spec='len']/../.. 上层节点的上层节点
七. 在webelement对象里面使用查找Xpath 查找时，必须使用.指明当前节点
food = driver.find_element_by_id('food')
eles = food.find_elements_by_xpath(".//p") .指明当前节点
eles = food.find_elements_by_xpath("..") 查找当前节点的父节点

'''




from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import io
import sys
reload(sys)
sys.setdefaultencoding('utf8')

file_dir = r'D:/chromedriver_win32/Files/'  #数据文件存取位置


browser = webdriver.Chrome(executable_path=r'D:/chromedriver_win32/chromedriver.exe') #该路径指向Chromedriver.exe的位置
browser.get(
    'https://www.tripadvisor.cn/Restaurant_Review-g186338-d12801049-Reviews-Core_by_Clare_Smyth-London_England.html'
)
browser.maximize_window()          #打开目标餐厅的主页面

en = browser.find_element_by_xpath(
    "//input[@id='filters_detail_language_filterLang_en']"
)
if not en.is_selected():
    browser.execute_script("arguments[0].click()", en)
    #使用Javascript语言模拟点击（因为实验时发现element.click()无效），切换至英语评论
time.sleep(6)#等待评论切换完毕

'''下面3行加载代码，在程序报错时使用，将其中的链接修改为程序报错时Chromedriver停留的页面（即正在爬取却报错的页面）的链接，
并这3行的注释。目的是从报错的评论页开始继续爬取评论。'''
# browser.get(
#     'https://www.tripadvisor.cn/Restaurant_Review-g186338-d719242-Reviews-or730-Restaurant_Gordon_Ramsay-London_England.html'
# )

eatery_name = browser.find_element_by_xpath(
    "//h1[@class='ui_header h1']"
).text

#获取餐厅名
print("filename = %s" % file_dir+eatery_name+'.txt')
f=io.open(file_dir+eatery_name+'.txt','a+',encoding='utf-8')
                                  #在指定的文件夹下创建一个以餐厅名命名的txt文件，如果该文件已存在则以追加形式打开该文件
last=browser.find_element_by_xpath(
    "//a[@class='pageNum last taLnk ']"
)
page_num = int(last.get_attribute('data-page-number'))           #获取评论页数


time.sleep(3)
for j in range(page_num-1):
    #每个评论页中爬取评论。
    #特别注意当程序报错时，如果报错的是第74（此时Chromedriver停留的页面应该是**730**）页评论，则修改为range(73，page_num-1)
    #修改的目的是从报错的评论页开始继续爬取评论。
    for k in range(3,14):
        block = browser.find_element_by_xpath(
            "//div[@class='listContainer hide-more-mobile']/div[{}]".format(k)
        )                        #定位到每个评论块
        if block.get_attribute('class') not in ['see-more-mobile ui_button primary',
                                                    'cms-wrapper']:
            user_name = block.find_element_by_xpath(
                ".//div[@class='info_text']/div"
            ).text               # 用户名

            rating = block.find_element_by_xpath(
                ".//span[contains(@class,'ui_bubble_rating')]"
            ).get_attribute('class')
            rating = int(rating[rating.rfind('_') + 1:]) / 10
                            # 数字评分
            try:

                more_comment=block.find_element_by_xpath(
                    ".//span[@class='taLnk ulBlueLinks']"
                )
                if '更多' in more_comment.text:
                    more_comment.click()
                    time.sleep(1)      # 展开折叠的评论
            except NoSuchElementException:
                print(NoSuchElementException)
            finally:
                comment = block.find_element_by_xpath(
                    ".//p[@class='partial_entry']"
                ).text      # 评论
            f.write(user_name + '##' + str(rating) + '##' + comment.replace('\n','').replace('\r','') + '\n')
            #将评论写入文件，形式为 用户名##评分##评论
    print("         餐厅{}的第{}页评论".format(eatery_name,j+1))
    next_button=browser.find_element_by_xpath("//a[contains(text(),'下一页')]")
    browser.execute_script("arguments[0].click()", next_button) #进入下一个评论页
    time.sleep(2)

f.close()
print("餐厅{}的评论挖取完毕".format(eatery_name))


