import easygui
import json
import time

def TeenagerSetup():
    try:
        # 制作待保存数据
        h = easygui.enterbox(title="青少年模式设置", msg="请设置每日所能游玩时间(时)")
        m = easygui.enterbox(title="青少年模式设置", msg="请设置每日所能游玩时间(分)")
        time = {
            "hour": h,
            "minute": m
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
    else:
        easygui.msgbox(title="青少年模式设置", msg="明天即可生效")

def Execute_01():
    # 得出游玩当日的日期并生成字典
    month = time.ctime().split(" ")[0]
    date = time.ctime().split(" ")[1]
    weekdays = time.ctime().split(" ")[2]
    year = time.ctime().split(" ")[4]
    md = {
        "weekdays": weekdays,
        "month": month,
        "date": date,
        "year": year
    }
    # 读取文件中上次游玩日期
    with open("Save/TeenagerMode/DateMonthYear.json", "r", encoding="utf-8") as f:
        mdf = json.load(f)
    # 读取文件中存放的每日游玩时间
    with open("Save/TeenagerMode/Time.json", "r", encoding="utf-8") as f:
        dic = json.load(f)
    h = int(dic["hour"])
    m = int(dic["minute"])
    # 得出起始时间
    if not md is mdf:
        tbg = time.time()
    else:
        tbg = ted["tbg"]

    # 算出间隔时间
    global tbe
    tbe = time.time() - tbg
    # 计算出终止时间
    global te
    if not md is mdf:
        te = time.time() + h * 3600 + m * 60
        NeedNt = True
    else:
        with open("Save/TeenagerMode/NewTime.json", "r", encoding="utf-8") as f:
            ted = json.load(f)
        te = ted["te"]

def Execute_02():
    tbg = time.time() - tbe
    # 保存下次起点时间和终止时间
    md = {
        "tbg": tbg,
        "te": te
    }
    with open("Save/TeenagerMode/NewTime.json", "w", encoding="utf-8") as f:
        json.dump(md, f)
    # 保存日期
    dic = {
        "weekdays": time.ctime().split(" ")[0],
        "month": time.ctime().split(" ")[1],
        "date": time.ctime().split(" ")[2],
        "year": time.ctime().split(" ")[4]
    }
    with open("Save/TeenagerMode/DateMonthYear.json", "w", encoding="utf-8") as f:
        json.dump(dic, f)

def Execute_03():
    tbg = time.time() - tbe
    if tbg == te:
        easygui.msgbox(title="警告", msg="游玩时间超时")
        pygame.quit()
        sys.exit()
