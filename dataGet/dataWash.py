import json

with open(r'C:\Users\admin\PycharmProjects\Cloudlyric\data\dirtydata.json', 'r',encoding='utf-8') as f:
    read_dict = json.load(f)
# print(read_dict)

def city_analyze(dirtydata):
    city_list={
        "北京":0,
        "上海":0,
        "广州":0,
        "深圳":0,
        "成都":0,
        "苏州":0,
        "重庆":0,
        "武汉":0,
        "南京":0,
        "青岛":0,
        "沈阳":0,
        "长沙":0,
        "郑州":0,
        "兰州":0,
    }
    for i in city_list:
        city_list[i]=dirtydata[i]
    return city_list

def season_analyze(dirtydata):
    season_list={
        "春天":0,
        "夏天":0,
        "秋天":0,
        "冬天":0
    }
    for i in season_list:
        season_list[i] = dirtydata[i]
    return season_list

def time_analyze(dirtydata):
    time_list={
        "昨天":0,
        "今天":0,
        "明天":0
    }
    for i in time_list:
        time_list[i] = dirtydata[i]
    return time_list

def color_analyze(dirtydata):
    color_list={
        "红色":0,
        "黄色":0,
        "黑色":0,
        "绿色":0,
        "蓝色":0,
        "白色":0
    }
    for i in color_list:
        color_list[i] = dirtydata[i]
    return color_list

print(city_analyze(read_dict))
print(season_analyze(read_dict))
print(time_analyze(read_dict))
print(color_analyze(read_dict))
