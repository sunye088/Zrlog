#导入Requests库
import requests
#导入logger对象
from utils.logutil import logger
# 定义HTTP请求类
class RequestSend:
    #封装requests请求
    def api_run(self,url,method,data=None,headers=None,cookies=None):
        #定义变量，获取响应结果
        res = None
        # 打印日志
        logger.info("请求的url为{}，类型为{}".format(url,type(url)))
        # 打印日志
        logger.info("请求的method为{}，类型为{}".format(method,type(method)))
        # 打印日志
        logger.info("请求的data为{}，类型为{}".format(data, type(data)))
        # 打印日志
        logger.info("请求的headers为{}，类型为{}".format(headers, type(headers)))
        # 打印日志
        logger.info("请求的cookies为{}，类型为{}".format(cookies, type(cookies)))
        # 判断请求方法
        if method == "get":
            res = requests.get(url,data=data,headers=headers,cookies=cookies)
        elif method=="post":
            # 判断亲贵的数据类型是否是json格式
                if headers=={"Content-Type":"application/json"}:
                    # 发送HTTP请求，方法为post，参数使用json=data
                    res=requests.post(url,json=data,headers=headers,cookies=cookies)
                elif headers=={"Content-Type":"application/x-www-form-urlencoded"}:
                    # 发送HTTP请求，方法为post。参数使用data=data
                    res=requests.post(url,data=data,headers=headers,cookies=cookies)
        # 获取请求响应的状态码
        code =res.status_code
        # 获取响应的cookies
        cookies=res.cookies.get_dict()
        # 定义字典
        dict1=dict()
        #异常处理
        try:
            # 获取响应结果json格式
            body=res.json()
        # 捕获异常
        except:
            # 获取响应结果text
            body = res.text
        # 自定义参数body写入字典
        dict1['body']=body
        # 自定义cookies写入字典
        dict1['cookies'] = cookies
        # 返回字典定义
        return dict1
    def send(self,url,method,**kwargs):
        return self.api_run(url=url,method=method,**kwargs)
# 测试代码
if __name__ == "__main__":
    url = "http://47.100.37.140/api/admin/login"
    data = {"userName":"admin","password":123456,"https":False,"keyi":1606792942688}
    method = "post"
    headers = {"Content-Type":"application/json"}
    print(RequestSend().send(url=url,method=method,headers=headers,data=data))