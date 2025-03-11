###技术栈
python + pytest + requests + allure + git + jenkins 
###实现功能
基于requests实现的接口自动化框架,可根据项目组需求进行二次开发；
可集成持续集成工具jenkins、github等实现自动化构建
###设计模式
- POM(page object model)
### 项目结构
- \testcase 测试用例
- \utils 公共、基础方法封装
- \data 参数化测试数据
- \report 测试报告
- \conftest.py 存放夹具、共享测试数据、钩子函数
- \logs 存放日志输出
- \pytest.ini 框架配置文件，设置运行时默认行为
- \requirements.txt 框架依赖安装包
### 