import easygui
import json1

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
