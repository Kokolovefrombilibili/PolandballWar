import easygui
import json
import time
import pygame

def TeenagerSetup():
    try:
        # 制作待保存数据
        h = easygui.enterbox(title="青少年模式设置", msg="请设置每日所能游玩时间(时)")
        m = easygui.enterbox(title="青少年模式设置", msg="请设置每日所能游玩时间(分)")
        time = {
            "hour" : h,
            "minute" : m
        }
        # 录入信息进行保存
        with open("Save/TeenagerMode/Time.json", "w", encoding="utf-8") as f:
            if (int(h) < 24 and int(m) < 60) or (int(h) == 24 and int(m) == 0):
                json.dump(time, f)
            # 对用户输入时间非合理情况时的bug处理
            else:
                easygui.msgbox(title="警告", msg="您设置的时间不合理")
                TeenagerSetup()
    # 对用户输入非int数据类型是的bug处理
    except ValueError:
        easygui.msgbox(title="警告", msg="出现了数据类型错误，一定要输入数字哦")
        TeenagerSetup()
    # 对用户不输入内容时的bug处理
    except TypeError:
        easygui.msgbox(title="警告", msg="不能不输入内容")
        TeenagerSetup()

def Execute():
    # 得出游玩当日的日期
    weekdays = time.ctime().split(" ")[0]
    month = time.ctime().split(" ")[1]
    date = time.ctime().split(" ")[2]
    year = time.ctime().split(" ")[4]
    # 储存日期
    md = {
        "weekdays" : weekdays,
        "month" : month,
        "date" : date,
        "year" : year
    }
    with open("Save/TeenagerMode/DateMonthYear.json") as f:
        json.dump(md, f)
    # 读取文件中存放的每日游玩时间
    with open("Save/TeenagerMode/Time.json") as f:
        dic = json.load(f)
    h = int(dic["hour"])
    m = int(dic["minute"])
    # 计算出终止时间
    tb = time.time()
    te = tb + h * 3600 + m * 60
    while True:
        tbg = time.time()
        if tbg == te:
            easygui.msgbox(title="游戏终止", msg="游戏时间结束")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dt = {
                    "tb" : tb,
                    "tbg" : tbg
                }

                with open("Save/TeenagerMode/NewTime.json", "w", encoding="utf-8") as f:
                    json.dump(dt, f)

