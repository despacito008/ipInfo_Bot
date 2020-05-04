import httplib2
import json
from urllib.parse import urlencode
from config import link114_id, link114_sign


def api_get_ip(url):
    print("进入函数，查看取得的URL")
    print(url)
    params = urlencode({'func':'ip', 'site':url, 'id':link114_id, 'sign':link114_sign, 'signtype':'1'})
    API_URl = 'http://api.link114.cn/get.php?'+params
    http = httplib2.Http()
    response, content = http.request(API_URl,'GET',headers={})
    response_json = content.decode("utf-8")
    response_dic = json.loads(response_json)
    print('打印114接口返回dic数据')
    print(response_dic)
    response_status = (json.loads(response_json))['status']
    if response_status == "1":
        print("打印114接口返回的状态码: " + response_status)
        response_result = (json.loads(response_json))['result']
        response_ip = response_result['data']
        return_data = {'status': response_status, 'ip': response_ip}
        print("函数执行完毕，打印返回字典")
        print(return_data)
    else:
        return_data = {'status': response_status}
    return return_data


def get_ip_info(ip):
    params = urlencode(
        {
            'lang':'zh-CN', 
            'fields':'status,message,country,countryCode,city,isp,org,as,query'
            }
            )
    API_URl = 'http://ip-api.com/json/' +ip +'?' +params
    http = httplib2.Http()
    response, content = http.request(API_URl,'GET',headers={})
    response_json = content.decode("utf-8")
    print(response_json)
    response_dic = json.loads(response_json)
    response_status = response_dic['status']
    print('get_ip_info 函数 ip-api 状态返回')
    print(response_status)
    if response_status == "fail":
        ip_info_data = {
        'status':'fail',
        }
    else:
        ip_info_data = {
            'ip':ip,
            'status':'success',
            'country':response_dic['country'],
            'countryCode':response_dic['countryCode'],
            'isp':response_dic['isp'],
            'org':response_dic['org'],
            'as':response_dic['as']
            }
    return ip_info_data
