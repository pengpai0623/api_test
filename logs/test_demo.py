import pytest


@pytest.fixture()
def fixture1():
    a, b = 10, 20
    return a, b


@pytest.fixture()
def fixture2():
    a, b = 10, 20
    print('开始执行')
    yield a, b
    print('结束执行')


# @pytest.fixture(scope='class')
# def fixture3():
#     b = 20
#     return b


class Test_1:
    def test_1(self):
        print('---test_1执行中---')
        try:

            assert isinstance(fixture2, tuple)
        except AssertionError as e:
            print('报错信息是', repr(e))
        # assert fixture2[0] == 10, '值不相等'
        # assert fixture2[1] == 20, '值不相等'

    # 另外test_2虽然没用到fixture2，但是也不会报错
    def test_2(self):
        print('---test_2执行中---')
        # assert isinstance(fixture2, tuple)  # 报错
        # assert fixture2[0] == 10, '值不相等'  # 报错


if __name__ == '__main__':
    pytest.main(['-vs', 'test_33.py'])
