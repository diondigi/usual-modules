
import requests
import xlwt #xls文本写入模块
from urllib.parse import urlencode  #url 请求编码转换模块
import time

######## 配置  ##############
content = '金融' #搜索内容
page = 2  #爬取多少页的内容
sleep = 10  #爬取每页数据后，休息多少秒【防封】
delay = 9  #超时时间
name = '信息' #保存数据的文件名称

##########################
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet_1')
search = urlencode({'':'content'},encoding='utf-8')[1:]  #搜索内容
referer = 'https://www.lagou.com/jobs/list_'+ search +'?px=new&city=%E5%85%A8%E5%9B%BD#order'



##########################################################
sheet.write(0, 0, '公司名')  # 公司名
sheet.write(0, 1, '发布时间')  # 发布时间
sheet.write(0, 2, '招聘职位')  # 招聘职位
sheet.write(0, 3, '招聘页面id')  # 招聘页面id
sheet.write(0, 4, '学位要求')  # 学位要求
sheet.write(0, 5, '工作经验要求')  # 工作经验要求
sheet.write(0, 6, '全职/兼职')  # 全职/兼职
sheet.write(0, 7, '所在城市')  # 所在城市
sheet.write(0, 8, '技能要求')  # 技能要求
sheet.write(0, 9, '第一类型')  # 第一类型
sheet.write(0, 10, '第二类型')  # 第二类型
sheet.write(0, 11, '融资情况')  # 融资情况
sheet.write(0, 12, '工资')  # 工资
sheet.write(0, 13, '公司类型')  # 公司类型
sheet.write(0, 14, '公司主营方向')  # 公司主营方向
sheet.write(0, 15, '公司规模')  # 公司规模
sheet.write(0, 16, '公司福利')  # 公司福利
####################################################

s = 1
for i in range(1,page+1):
    time.sleep(sleep)   #睡
    try:
        data = requests.post('https://www.lagou.com/jobs/positionAjax.json',timeout=delay,
                          headers={
                                'Host':'www.lagou.com',
                                'Referer':referer,
                                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3163.100 Safari/537.36',
                                'X-Anit-Forge-Code':'0',
                                'X-Anit-Forge-Token':'None',
                                'X-Requested-With':'XMLHttpRequest'
                          },data={
                'first': 'false',
                'pn': '%s'%i,  #页码
                'kd': search,   #搜索内容
            })
############################# 写入 ###################################################
        for temp in data.json()['content']['positionResult']['result']:
            s += 1
            print(s)
            sheet.write(s, 0, temp.get('companyFullName'))  # 公司名
            sheet.write(s, 1, temp.get('createTime'))  # 发布时间
            sheet.write(s, 2, temp.get('positionName'))  # 招聘职位
            sheet.write(s, 3, temp.get('positionId'))  # 招聘页面id
            sheet.write(s, 4, temp.get('education'))  # 学位要求
            sheet.write(s, 5, temp.get('workYear'))  # 工作经验要求
            sheet.write(s, 6, temp.get('jobNature'))  # 全职/兼职
            sheet.write(s, 7, temp.get('city'))  # 所在城市
            sheet.write(s, 8, temp.get('positionLables'))  # 技能要求
            sheet.write(s, 9, temp.get('firstType'))  # 第一类型
            sheet.write(s, 10, temp.get('secondType'))  # 第二类型
            sheet.write(s, 11, temp.get('financeStage'))  # 融资情况
            sheet.write(s, 12, temp.get('salary'))  # 工资
            sheet.write(s, 13, temp.get('industryField'))  # 公司类型
            sheet.write(s, 14, temp.get('positionAdvantage'))  # 公司主营方向
            sheet.write(s, 15, temp.get('companySize'))  # 公司规模
            sheet.write(s, 16, temp.get('companyLabelList'))  # 公司福利
    except:
        print('错误页码：',i)
##################################################################

wbk.save('%s.xls'%name)
