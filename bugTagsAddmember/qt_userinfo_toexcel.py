
# encoding: utf-8

from __future__ import division
from bugTagsAddmember import common
import xlwt


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++ 需配参数开始 +++++++++++++++++++++++++++++++++++++++++++

# 在需要增加人员的团队中，创建轻应用，轻应用需有成员信息查看和成员信息变更权限，设置自己是轻应用管理员
# 团队需要开通计费项，开放平台接口调用次数权限和开放平台高级接口权限

# 轻应用的appid和appsecret
app_id = '2768191434'
app_secret = 'b96bf5c7af514508a57e10d762db7d5a'

# 团队所在的环境，请注意一定不要将此代码在线上环境执行，模拟的话，将下面字符串中的qa更改为moni
#env_url = 'https://moniqtopen.qingtui.im'
env_url = 'https://open.qingtui.im'




if __name__ == '__main__':

    # 首先获取token
    access_token = common.get_access_token(env_url, app_id, app_secret)
    #print(access_token)
    #access_token='eyJhbGciOiJIUzI1NiJ9.eyJkb21haW5faWQiOiI0NDQ5Mjk2NzA3ZDU0NzMxYTVkNWIyNmE0MmM4OGEzMyIsImFwcGlkIjoiODg5MTAzNzYxMiIsImV4cGlyZXNfaW4iOjE1MjQ3OTY5OTk5OTYsImRpc3BhdGNoIjoxNTI0Nzg5Nzk5OTk2fQ.J416JEFmfMtofz3nla5CTeIWaacWYy_op21hkjSBgFg'
    #获取openId
    result=common.get_openid(env_url,access_token)
    follower_list=result['followers']
    totalcount=result['totalCount']
    print("totalcount:",totalcount)
    followers = set(follower_list)

    #将oenId,user_id,username写入到excel
    i=1
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Sheet1")
    sheet.write(0, 0, 'openid')
    sheet.write(0, 1, 'qt_userid')
    sheet.write(0,2,'qt_username')
    sheet.write(0,3,'mobile')
    for openid in followers:
        print('openid：'+openid)

        #将open_id写入excel
        sheet.write(i, 0, openid)

        #获取user_id,username
        usrinfo = common.get_userinfo(env_url, access_token, openid)
        print('username:'+usrinfo['name'])
        print('user_id:'+usrinfo['user_id'])
        print ('mobile:'+usrinfo['mobile'])

        #将user_id写入excel
        sheet.write(i,1,usrinfo['user_id'])
        # 将username写入excel
        sheet.write(i,2,usrinfo['name'])
        #将mobile写入excel
        sheet.write(i,3,usrinfo['mobile'])
        i += 1

    workbook.save('bugTagsUserInfos.xls')








