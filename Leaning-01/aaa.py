import math
import time
from pywinauto import Application,mouse



# #start启动应用程序
# Application(backend="uia").start("D:\Program Files\Sublime Text\sublime_text.exe")
#
# #通过connect连接已经打开的应用程序
# Application(backend="uia").connect(process=4364)


# # 通过句柄连接已经打开的应用程序
# Application(backend="uia").connect(handle=1180332)


# 窗口操作

# app = Application(backend="uia").connect(process=13516)
#
# win = app.window(title_re = ".*Sublime Text.*")
#
# win.wait("exists")
#
# win.maximize()
# print("max result:",win.is_maximized())
#
# win.close()

app = Application(backend="uia").connect(process=28224)

win = app.window(title = "抖音")

win.wait("visible")

# liked_group = win.child_window(title="16.1万", control_type="Group")
#
# # 获取liked_group子控件
# like_icon = liked_group.children()[0]
# # 点赞
# like_icon.click_input()
#
# point = win.rectangle().mid_point()
#
# mouse.scroll(coords=(point.x, point.y), wheel_dist=-500)
#
# win.print_control_identifiers()

for i in range(0,3):
    point = win.rectangle().mid_point()
    time.sleep(2)

    # win.double_click_input()

    mouse.double_click(coords=(point.x, point.y))
    time.sleep(2)

    mouse.scroll(coords=(point.x, point.y), wheel_dist=-500)
