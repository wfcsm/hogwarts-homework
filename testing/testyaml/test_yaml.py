
import yaml


def test_demo():
    with open(file='./datas.yml') as f:
        # safe_load 将文件流转成python 对象
        datas = yaml.safe_load(f)
    print(datas)