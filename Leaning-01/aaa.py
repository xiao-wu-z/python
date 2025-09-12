from pywinauto import Application


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