import json
import time
from collections import defaultdict
from datetime import datetime

data_store={}
flag=True
def init_data():
    f= json.load(open('dingxiangyuan'))
    for i in f['data']['getAreaStat']:
        adress = i['provinceName'].replace('市','')
        adress = adress.replace('省','')
        data_store[adress] = defaultdict(str)
        data_store[adress]['确诊']=i['confirmedCount']
        data_store[adress]['疑似']=i['suspectedCount']
        data_store[adress]['治愈']=i['curedCount']
        data_store[adress]['死亡']=i['deadCount']
        for j in i['cities']:
            adress = j['cityName'].replace('市','')
            adress = adress.replace('省','')
            data_store[adress] = defaultdict(str)
            data_store[adress]['确诊']=j['confirmedCount']
            data_store[adress]['疑似']=j['suspectedCount']
            data_store[adress]['治愈']=j['curedCount']
            data_store[adress]['死亡']=j['deadCount']
    
    data_store['general']= f['data']['getStatisticsService']['countRemark']
    return data_store




def get_detail_info(address):
    ds = {}
    if len(ds) == 0:
        ds=init_data()
    a = int(time.time())    #当前时间
    c = datetime.fromtimestamp(a+43200).strftime('%H:%M')    #格式转换
    
    if c.split(':')[1][-1]=='0':
        ds = init_data()
    if address=='general':
        try:
            return "(由于某些原因，本数据已经停止更新，请到官方渠道查询)整体的情况是：确诊：{}, 疑似：{}, 治愈：{}, 死亡：{}。请不要紧张，一切都会好的".format(ds[address]['确诊'], ds[address]['疑似'], ds[address]['治愈'],ds[address]['死亡'])
        except:
            return "暂时没有你所查找的信息，请换一种说法说出你要查询的城市名称"

    try:
        return "(由于某些原因，本数据已经停止更新，请到官方渠道查询){} 的情况是：确诊：{}, 疑似：{}, 治愈：{}, 死亡：{}。请不要紧张，一切都会好的".format(address, ds[address]['确诊'], ds[address]['疑似'], ds[address]['治愈'],ds[address]['死亡'])
    except:
        return "暂时没有你所查找的信息，请换一种说法说出你要查询的城市名称"

if __name__ == '__main__':
    
    d = get_detail_info('武汉')
    print(d)
