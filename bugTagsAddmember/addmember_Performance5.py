
# encoding: utf-8

from __future__ import division
from bugTagsAddmember import common
import xlwt


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++ 需配参数开始 +++++++++++++++++++++++++++++++++++++++++++

# 在需要增加人员的团队中，创建轻应用，轻应用需有成员信息查看和成员信息变更权限，设置自己是轻应用管理员
# 团队需要开通计费项，开放平台接口调用次数权限和开放平台高级接口权限

# 轻应用的appid和appsecret
app_id = '8891037612'
app_secret = '58da5bd43609402ca96ed5b35e8a401b'

# 团队所在的环境，请注意一定不要将此代码在线上环境执行，模拟的话，将下面字符串中的qa更改为moni
env_url = 'https://moniqtopen.qingtui.im'




if __name__ == '__main__':

    #h = httplib2.Http()

    # 首先获取token
 #   access_token = common.get_access_token(env_url, app_id, app_secret)
   # print(access_token)
    access_token='eyJhbGciOiJIUzI1NiJ9.eyJkb21haW5faWQiOiI0NDQ5Mjk2NzA3ZDU0NzMxYTVkNWIyNmE0MmM4OGEzMyIsImFwcGlkIjoiODg5MTAzNzYxMiIsImV4cGlyZXNfaW4iOjE1MjQ3Mzk0MjE4MDQsImRpc3BhdGNoIjoxNTI0NzMyMjIxODA0fQ.KonMtIXqNZ5D9XVWQ5O9f41c0Aryl2g4CAQ1nMrQ5bg'
    #获取openId
    follower_list=common.get_openid(env_url,access_token)
    followers = set(follower_list)



    #将oenId写入到excel
    i=1
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("openidtest")
    sheet.write(0, 0, 'openids')
    for openid in followers:
        sheet.write(i, 0, openid)
        i+=1
        print(i)
    workbook.save('test.xls')








