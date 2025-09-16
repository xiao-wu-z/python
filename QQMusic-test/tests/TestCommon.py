from Utils import yamlUtil


class TestCommon:
    '''
    测试logo
    '''
    def test_logo(self, QQMusic_app):
        data = yamlUtil.read_yml("logo")
        logo = QQMusic_app.win.child_window(auto_id = data['auto_id'], control_type = data['ControlType'])
        logo.wait('visible')

    '''
    测试搜索功能
    '''
    def test_search(self, QQMusic_app):
        data = yamlUtil.read_yml("search")
        edit = QQMusic_app.win.child_window(auto_id = data['auto_id'], control_type = data['ControlType'])

        edit.click_input()

        edit.type_keys("^a邓紫棋")

    '''
    测试换皮肤功能
    '''
    def test_skin(self, QQMusic_app):
        data = yamlUtil.read_yml("skin")
        skin = QQMusic_app.win.child_window(auto_id = data['auto_id'], control_type = data['ControlType'])

        skin.click_input()
        warning = QQMusic_app.win.child_window(title="温馨提示", control_type="Window")
        warning.wait("visible")

        warn_text = warning.child_window(control_type = "Text").window_text()

        assert warn_text == "换肤功能小哥哥正在紧急支持中..."

        warning.close()
        warning.wait_not("visible")

    '''
    测试最小化
    '''
    def test_min(self, QQMusic_app):
        data = yamlUtil.read_yml("最小化")
        min = QQMusic_app.win.child_window(auto_id = data['auto_id'], control_type = data['ControlType'])

        min.click_input()
        assert QQMusic_app.win.is_minimized()

        QQMusic_app.win.restore()

    '''
    测试导入音乐
    '''
    def test_importMusic(self, QQMusic_app):
        data = yamlUtil.read_yml("导入音乐")

        import_btn = QQMusic_app.win.child_window(auto_id = data['auto_id'], control_type = data['ControlType'])
        import_btn.click_input()

        import_win = QQMusic_app.win.child_window(title="添加本地下载音乐",control_type="Window")
        music_list = import_win.child_window(title="项目视图", control_type="List")
        music_list.type_keys("^a{ENTER}")

        import_win.wait_not("visible")


