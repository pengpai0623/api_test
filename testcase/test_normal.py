import pytest
import allure
from case.case_demo import func
from business.utils import get_json_data
from business.logger import logger
test_data = [(1, 1), (2, 4)]


@allure.feature('接口测试')
class Test_1:

    @allure.story('test_1接口测试')
    @allure.title('生成接口依赖属性测试')
    @allure.description('用例的详细描述')
    @allure.testcase('www.测试用例存放地址.com')
    @allure.issue('www.bug单地址.com')
    @allure.severity('blocker')
    def test_1(self, request):
        with allure.step('生成依赖属性res'):
            request.session.res = 10
            logger.debug(f'生成接口依赖数据request.session.res:{request.session.res}')
        with allure.step('对依赖属性res进行断言'):
            logger.critical(f'断言接口依赖数据request.session.res的结果:{request.session.res == 10}')
            assert request.session.res == 10

    @allure.story('test_2接口测试')
    @allure.title('获得接口依赖属性测试')
    def test_2(self, request):
        self.num = request.session.res
        assert func(self.num) == 100

    @allure.story('test_3接口测试')
    @allure.title('断言异常类型测试')
    def test_3(self):
        self.str = '10'
        with pytest.raises(ValueError):
            logger.debug(f'断言func函数异常类型是:{ValueError}')
            func(self.str)


    @allure.story('test_4接口测试')
    @allure.title('func函数功能测试')
    @pytest.mark.parametrize('num, res', test_data)
    def test_4(self, num, res):
        assert func(num) == res

    @allure.story('test_5接口测试')
    @allure.title('参数化功能测试')
    @pytest.mark.parametrize('test_get_topics, code, text', get_json_data('test_get_topics'))
    def test_5(self, test_get_topics, code, text):
        if test_get_topics == get_json_data('test_get_topics')[0][0]:
            assert code == get_json_data('test_get_topics')[0][1]
        else:
            assert code == get_json_data('test_get_topics')[1][1]