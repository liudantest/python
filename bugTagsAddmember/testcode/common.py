
# encoding: utf-8
from __future__ import division

import httplib2
import json



# 组合get方法所需的参数
def method_get_param(kwargs):
    params = []
    for key, value in kwargs.items():
        params.append(key + '=' + value)
    params = '&'.join(params)
    return '?' + params


# 根据appid和secret获取access_token
def get_access_token(env_url, app_id, app_secret):

    h = httplib2.Http()

    req_data = {
        'appid': app_id,
        'secret': app_secret,
        'grant_type': 'client_credential',
    }
    # 拼接URL
    url = '%s/v1/token' % env_url + method_get_param(req_data)
    resp, content = h.request(url, 'GET')
    return json.loads(content)['access_token']


def get_openid(env_url,access_token):
    h=httplib2.Http()

    req_data={
        'access_token':access_token,
        'page_size':'100',
        'request_page':'1',
    }

    # 拼接URL
    url = '%s/v1/app/followers' % env_url + method_get_param(req_data)
    resp, content = h.request(url, 'GET')
    return json.loads(content)


def get_userinfo(env_url,access_token,openid):
    h=httplib2.Http()
    req_data={
        'access_token':access_token,
        'open_id':openid,
    }

    # 拼接URL
    url='%s/team/member/openid/detail' % env_url + method_get_param(req_data)
    resp, content = h.request(url, 'GET')
    return json.loads(content)



