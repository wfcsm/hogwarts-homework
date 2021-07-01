import allure


def test_attach_text():
    allure.attach('这是一个文本',
                  name='这是一个文本',
                  attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach('<div>html代码块</div>',
                  name='这是一个html代码块',
                  attachment_type=allure.attachment_type.HTML)

def test_attach_phote():
    allure.attach.file(source='./datas/demo.png',
                       name='这是一张图片',
                       attachment_type=allure.attachment_type.PNG)


def test_attach_video():
    allure.attach.file(source='./datas/demo_video.mp4',
                       name='这是一个视频',
                       attachment_type=allure.attachment_type.MP4)
