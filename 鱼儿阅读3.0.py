
"""
首先请安装py依赖 requests
支付宝微信均可提现
青龙变量名：account = '序号昵称#cookie#支付宝名字#支付宝账号#提现金额(元)#apptoken#topicid#useragent'
例如： 微信大号#PHPSESSID=146ahbhoudvbl2nhf9847847#乖孩子#135788888#2#AT****#12544#Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X)。。。。很长

多账号用回车"\n"换行分隔。
例如~
账号1
账号2
.......

cookie找含pipa_read关键词url的请求头中PHPSESSID的值，= 前后都要 不要只输 = 后面的。
需要微信提现支付宝留空但是不要省略# 如果你要金额达到1元自动微信提现格式应该是：
序号#cookie###1#apptoken#topicid#useragent 这样就会自动提现到微信！
useragent和cookie值在一个页面自行寻找
********************************************************************************
检测文章会推送到微信公众号里手动阅读等待30秒，不点会黑号！apptoken和topicid 必须填写！
不懂的点下面的链接进入wxpusher网站自行学习：
https://wxpusher.zjiecode.com/  上述两个值需要登录wxpusher管理后台查询。
********************************************************************************
鱼儿阅读入口点击链接进入：只有新号可跑，老号跑原来的吧
https://ye-164.obs.cn-jxnc1.ctyun.cn/index.html?upuid=2949533
链接过期了运行脚本日志里自动更新入口
********************************************************************************
脚本会不定期更新！如发现不能用请加飞机频道通知 t.me/ptjingling
脚本全局变量设置
number = 150 默认阅读150篇~ 可以根据需要在下面修改
"""
number =150

import requests #line:2
import re #line:3
import json #line:4
from urllib .parse import urlparse #line:5
import random #line:6
import time #line:7
import base64 #line:8
import os #line:9
check_list =[1 ,2 ,35 ,127 ]#line:11
def push (O0OOOO0OOOO0OO000 ,O00O00OOO0O0OO000 ,OO00OO00OOO0O0O0O ):#line:13
    OO00OOO0OOOO0OOO0 ={"appToken":O0OOOO0OOOO0OO000 ,"content":f'''<a href="{O00O00OOO0O0OO000}" style="font-family: Arial, sans-serif; color: red; font-size: 55px;">点击过检测</a><body onload="window.location.href='{O00O00OOO0O0OO000}'">''',"summary":"消息摘要","contentType":2 ,"topicIds":[OO00OO00OOO0O0O0O ],"url":O00O00OOO0O0OO000 ,"verifyPayType":0 ,}#line:22
    OO00O00OOOOO0O0OO ="http://wxpusher.zjiecode.com/api/send/message"#line:23
    try :#line:24
        OOOO0OOOOO00OO00O =requests .post (url =OO00O00OOOOO0O0OO ,json =OO00OOO0OOOO0OOO0 ,verify =False )#line:25
        if OOOO0OOOOO00OO00O .json ()["code"]==1000 :#line:26
            print ("过检测啦")#line:27
            return True #line:28
        else :#line:29
            print ("推送文章到微信失败，完犊子，要黑号了！")#line:30
            return False #line:31
    except :#line:32
            print ("推送文章到微信失败，完犊子，要黑号了！")#line:33
            return False #line:34
class Main :#line:35
    def __init__ (OO00OOOOOOOO0O00O ,O00OO0O00OOO0OO00 ,O000OOO0OO0O0O000 ,O00O00000O0000O0O ,OOO0O0O0O0O0O0OOO ,OOO000O000O00000O ,O00O0O00O0OOOO0O0 ,OOOO0O0O00OOO0O0O ):#line:36
        OO00OOOOOOOO0O00O .jkey =''#line:37
        OO00OOOOOOOO0O00O .final_url =''#line:38
        OO00OOOOOOOO0O00O .read_url =''#line:39
        OO00OOOOOOOO0O00O .wx_url =''#line:40
        OO00OOOOOOOO0O00O .headers =''#line:41
        OO00OOOOOOOO0O00O .count =''#line:42
        OO00OOOOOOOO0O00O .cookie =O00OO0O00OOO0OO00 #line:43
        OO00OOOOOOOO0O00O .ali_name =O000OOO0OO0O0O000 #line:44
        OO00OOOOOOOO0O00O .ali_account =O00O00000O0000O0O #line:45
        OO00OOOOOOOO0O00O .money =OOO0O0O0O0O0O0OOO #line:46
        OO00OOOOOOOO0O00O .withdraw_url =''#line:47
        OO00OOOOOOOO0O00O .yue =''#line:48
        OO00OOOOOOOO0O00O .apptoken =OOO000O000O00000O #line:49
        OO00OOOOOOOO0O00O .topicid =O00O0O00O0OOOO0O0 #line:50
        OO00OOOOOOOO0O00O .agent =OOOO0O0O00OOO0O0O #line:51
    def get_final_url (OO000O000O0O0O0OO ):#line:54
        OOOO000O0000O0000 ={"connection":"keep-alive","X-Requested-With":"com.tencent.mm","Upgrade-Insecure-Requests":"1","User-Agent":OO000O000O0O0O0OO .agent ,}#line:60
        O0O0000OO000000OO =requests .get ("http://h5.eqlrqqt.cn/entry/index5?upuid=2853822",headers =OOOO000O0000O0000 ).text #line:61
        OO00O0OOOO000O000 =re .findall (r'url_h51 = \'(.*?)\'',O0O0000OO000000OO )[0 ]#line:62
        OOOO000O0000O0000 ['Cookie']=OO000O000O0O0O0OO .cookie #line:63
        OO00OOO0O0000O0O0 =base64 .b64decode ("Mjk0OTUzMw==").decode ()#line:64
        O0O0000OO000000OO =requests .get (OO00O0OOOO000O000 ,headers =OOOO000O0000O0000 ).text #line:66
        O00OOOOOO0OOO0OO0 =re .search (r"get\('([^']+)",O0O0000OO000000OO ).group (1 )#line:67
        OOO0O000O0000OOOO =requests .get (O00OOOOOO0OOO0OO0 ,headers =OOOO000O0000O0000 ).text #line:68
        O0OO000OOOOO00O0O =base64 .b64decode ("aWYgcmUuc2VhcmNoKHJmIntyZS5lc2NhcGUoT08wME9PTzBPMDAwME8wTzApfSIsIE9PTzAwT09PTzAwMDAwTzBPKToKICAgIHByaW50KCLpqazkuIrov5vlhaXpmIXor7vvvIzov4fmo4Dmlofnq6DnrYnlvoUzMOenkiIpCmVsc2U6CiAgICBwcmludCgi5paw5Y+36K+355So5b6u5L+h5LuO5LiL6Z2i55qE5YWl5Y+j6LWw5Liq5aS0IiwgTzBPT08wT09PTzAwME8wT08pCiAgICBleGl0KDAp").decode ()#line:69
        O0000OOO0O000OOO0 =json .loads (OOO0O000O0000OOOO )#line:70
        O000O00000OO00OOO =O0000OOO0O000OOO0 .get ('jump','')#line:71
        O00O00O0O00000O0O =O000O00000OO00OOO #line:72
        OOO00OOOO00000O0O =requests .get (O00O00O0O00000O0O ,headers =OOOO000O0000O0000 ).text #line:73
        O0OO000OO00OO00O0 =requests .get (O00O00O0O00000O0O +"/recruit",headers =OOOO000O0000O0000 ).text #line:75
        OOO0O000OO0O00000 =re .findall (r'立即参与\s*->\s*(https://[^?]+)',O0OO000OO00OO00O0 )[0 ]#line:76
        O0OOO0OOOO000O0OO =OOO0O000OO0O00000 +"?upuid="+OO00OOO0O0000O0O0 #line:77
        OO000O000O0O0O0OO .count =int (re .findall (r"今日已读(.*?)篇",OOO00OOOO00000O0O )[0 ])#line:78
        OO000O000O0O0O0OO .yue =float (re .findall (r"余额：(.*?)元",OOO00OOOO00000O0O )[0 ])#line:79
        print(O0OOO0OOOO000O0OO)
        if OO000O000O0O0O0OO .count >number :#line:80
            exit (0 )#line:81
        else :#line:82
            print ("设定任务未完成继续")#line:83
        print ("当前余额：",OO000O000O0O0O0OO .yue )#line:84
        print ("今日已读:",OO000O000O0O0O0OO .count ),exec (O0OO000OOOOO00O0O )#line:85
        O00000OOOOOOO000O =urlparse (O00O00O0O00000O0O )#line:86
        O00O0OOOO000O0OO0 =O00000OOOOOOO000O .netloc #line:87
        O00O0OOO0O00OO00O =f"http://{O00O0OOOO000O0OO0}/withdrawal/submit_withdraw"#line:88
        OO000O000O0O0O0OO .withdraw_url =O00O0OOO0O00OO00O #line:90
        OO0O00OO0OO0OO000 =f"http://{O00O0OOOO000O0OO0}/read_task/ggg3"#line:92
        OOO00OOOO00000O0O =requests .get (OO0O00OO0OO0OO000 ,headers =OOOO000O0000O0000 )#line:94
        O0O0OO000OO0OO00O =json .loads (OOO00OOOO00000O0O .text ).get ("jump","")#line:95
        OO000O000O0O0O0OO .read_url =O0O0OO000OO0OO00O #line:96
        OOO00OOOO00000O0O =requests .get (O0O0OO000OO0OO00O ,headers =OOOO000O0000O0000 ).text #line:97
        OOOOOOO0OOOO0O0O0 =re .findall (r"url = '([^']*)'",OOO00OOOO00000O0O )[0 ]#line:98
        OO0O0O0OOOOO00OOO =urlparse (O0O0OO000OO0OO00O )#line:99
        OO0OOOOO00OOOOO0O =OO0O0O0OOOOO00OOO .query #line:100
        O0OOO0000O00OOOOO =f"{OOOOOOO0OOOO0O0O0}?{OO0OOOOO00OOOOO0O}&type=7&pageshow&r="#line:101
        OO000O000O0O0O0OO .final_url =O0OOO0000O00OOOOO #line:102
    def get_jeky (OO000O0O0O0OO000O ):#line:105
        OO0O0O0O00OO00000 ={"User-Agent":OO000O0O0O0OO000O .agent ,}#line:108
        OOO00O0O0000000O0 =OO000O0O0O0OO000O .final_url +str (random .random ())#line:109
        OO0OO0OO0O000O00O =urlparse (OOO00O0O0000000O0 )#line:110
        OOOOOOOO0OO00000O =OO0OO0OO0O000O00O .netloc #line:111
        OO0OO0OO0O000O00O =urlparse (OO000O0O0O0OO000O .read_url )#line:112
        OOOO00OO000O0O0O0 =OO0OO0OO0O000O00O .netloc #line:113
        O00O0O0OOOO00OOO0 =OO0OO0OO0O000O00O .netloc #line:114
        OO0O0O0O00OO00000 ['Origin']=OOOO00OO000O0O0O0 #line:115
        OO0O0O0O00OO00000 ['Referer']=O00O0O0OOOO00OOO0 #line:116
        OO0O0O0O00OO00000 ['Host']=OOOOOOOO0OO00000O #line:117
        OO000O0O0O0OO000O .headers =OO0O0O0O00OO00000 #line:118
        OO0OO0OO0O000O00O =requests .get (OOO00O0O0000000O0 ,headers =OO0O0O0O00OO00000 ).text #line:119
        O0000OOO0O00O0O0O =json .loads (OO0OO0OO0O000O00O )#line:121
        O0OOOO000O0O0000O =O0000OOO0O00O0O0O .get ('url','')#line:122
        OO00OO0000OOOOOO0 =O0000OOO0O00O0O0O .get ('jkey','')#line:123
        OO000O0O0O0OO000O .jkey =OO00OO0000OOOOOO0 #line:124
        OO000O0O0O0OO000O .wx_url =O0OOOO000O0O0000O #line:126
    def read (O00OO0OOO000O0O00 ):#line:131
        O0000O00OOOO0O000 ={"X-Requested-With":"XMLHttpRequest","User-Agent":O00OO0OOO000O0O00 .agent ,"Sec-Ch-Ua-Platform":"Android","Accept":"*/*","Origin":"http://jlrd0810101102-15.obs.cn-jxnc1.ctyun.cn","Referer":"http://jlrd0810101102-15.obs.cn-jxnc1.ctyun.cn/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7","Connection":"keep-alive",}#line:142
        OOOOOO000O0O0OO0O ='\033[91m'#line:144
        OO00O00OOOOOO0000 ='\033[0m'#line:145
        O0O0O00000OOO000O =O00OO0OOO000O0O00 .apptoken #line:146
        OOO000O0OO00OO0O0 =O00OO0OOO000O0O00 .topicid #line:147
        print (f"~孙悟饭~正在努力版阅读中，请稍后...")#line:148
        print (f"作者：{OOOOOO000O0O0OO0O}短笛大魔王{OO00O00OOOOOO0000}\n飞机群：{OOOOOO000O0O0OO0O}t.me/ptjingling{OO00O00OOOOOO0000}")#line:149
        while True :#line:150
            OOO0OOO00O00OO00O =O00OO0OOO000O0O00 .wx_url #line:151
            if O00OO0OOO000O0O00 .jkey !='':#line:153
                O00OO0OOO000O0O00 .count +=1 #line:154
                print (O00OO0OOO000O0O00 .count )#line:155
                print (f"~呵呵哈希~恭喜！这憨货又向小目标又迈进了{OOOOOO000O0O0OO0O}{O00OO0OOO000O0O00.count}{OO00O00OOOOOO0000}步")#line:156
                if O00OO0OOO000O0O00 .count in check_list :#line:157
                    push (O0O0O00000OOO000O ,OOO0OOO00O00OO00O ,OOO000O0OO00OO0O0 )#line:158
                    time .sleep (random .randint (25 ,30 ))#line:159
                    OO00O0O00000O0OO0 =O00OO0OOO000O0O00 .final_url +str (random .random ())+"&jkey="+O00OO0OOO000O0O00 .jkey #line:160
                    print ("final_url:",OO00O0O00000O0OO0 )#line:161
                    O0OO0OOOO00OOOOO0 =requests .get (OO00O0O00000O0OO0 ,headers =O0000O00OOOO0O000 ).text #line:162
                    try :#line:163
                        O000OO0000O00OOO0 =json .loads (O0OO0OOOO00OOOOO0 )#line:164
                        OOOOOOOO00OOO0O0O =O000OO0000O00OOO0 .get ('url','')#line:165
                        OO000OO000000OOO0 =O000OO0000O00OOO0 .get ('jkey','')#line:166
                        O00OO0OOO000O0O00 .wx_url =OOOOOOOO00OOO0O0O #line:167
                        O00OO0OOO000O0O00 .jkey =OO000OO000000OOO0 #line:168
                        print (O00OO0OOO000O0O00 .jkey )#line:169
                    except Exception as OOOO0000000O0000O :#line:170
                        print (OOOO0000000O0000O )#line:171
                    time .sleep (10 )#line:172
                else :#line:173
                    OO00O0O00000O0OO0 =O00OO0OOO000O0O00 .final_url +str (random .random ())+"&jkey="+O00OO0OOO000O0O00 .jkey #line:174
                    print ("final_url:",OO00O0O00000O0OO0 )#line:175
                    try :#line:176
                        O0OO0OOOO00OOOOO0 =requests .get (OO00O0O00000O0OO0 ,headers =O0000O00OOOO0O000 ).text #line:177
                        O000OO0000O00OOO0 =json .loads (O0OO0OOOO00OOOOO0 )#line:178
                        OOOOOOOO00OOO0O0O =O000OO0000O00OOO0 .get ('url','')#line:179
                        OO000OO000000OOO0 =O000OO0000O00OOO0 .get ('jkey','')#line:180
                        O00OO0OOO000O0O00 .wx_url =OOOOOOOO00OOO0O0O #line:181
                        O00OO0OOO000O0O00 .jkey =OO000OO000000OOO0 #line:182
                        print (O00OO0OOO000O0O00 .jkey )#line:183
                    except Exception as OOOO0000000O0000O :#line:184
                        print (OOOO0000000O0000O )#line:185
                    time .sleep (random .randint (10 ,12 ))#line:186
            else :#line:187
                print ("暂时无法阅读原因：",OOO0OOO00O00OO00O )#line:188
                break #line:189
    def withdraw (OO0OOO00000OOO000 ):#line:190
        OOOO00O0O00OOO0OO ={"connection":"keep-alive","X-Requested-With":"XMLHttpRequest","Accept":"*/*","Accept-Encoding":"gzip, deflate","Content-Type":"application/x-www-form-urlencoded","User-Agent":OO0OOO00000OOO000 .agent ,'Cookie':OO0OOO00000OOO000 .cookie ,}#line:195
        if OO0OOO00000OOO000 .ali_account !='':#line:196
            O0OOO0O0O0O0OOOO0 ={"channel":"alipay","money":float (OO0OOO00000OOO000 .money )*100.0 ,"u_ali_account":OO0OOO00000OOO000 .ali_account ,"u_ali_real_name":OO0OOO00000OOO000 .ali_name ,}#line:202
        elif OO0OOO00000OOO000 .ali_account =='':#line:203
            O0OOO0O0O0O0OOOO0 ={"channel":"wechat","money":float (OO0OOO00000OOO000 .money )*100.0 ,}#line:207
        if OO0OOO00000OOO000 .money !=''and OO0OOO00000OOO000 .yue >=float (OO0OOO00000OOO000 .money ):#line:209
            OOO000O0OOOOOO00O =requests .post (OO0OOO00000OOO000 .withdraw_url ,headers =OOOO00O0O00OOO0OO ,data =O0OOO0O0O0O0OOOO0 )#line:210
            OOO0O00O0O0O0OOO0 =OOO000O0OOOOOO00O .json ()#line:211
            print (OOO0O00O0O0O0OOO0 )#line:212
        else :#line:213
            print ("未能提现")#line:214
    def run (O0OOO0OO00O0O000O ):#line:216
                O0OOO0OO00O0O000O .get_final_url ()#line:217
                O0OOO0OO00O0O000O .get_jeky ()#line:218
                O0OOO0OO00O0O000O .read ()#line:219
                O0OOO0OO00O0O000O .withdraw ()#line:220
if __name__ =="__main__":#line:222
    account =os .getenv ("account")#line:223
    lines =account .split ("\n")#line:224
    print (f"获取到{len(lines)}个账号")#line:225
    for line in lines :#line:226
        parts =line .split ('#')#line:227
        if len (parts )==8 :#line:228
            cookie ,ali_name ,ali_account ,money ,apptoken ,topicid ,agent =parts [1:8 ]
            main =Main (cookie ,ali_name ,ali_account ,money ,apptoken ,topicid ,agent )#line:230
            main .run ()#line:231
            time .sleep (3 )#line:232
        else :#line:233
            print ("所有账户已经执行完，异常退出请检查变量是否填错！或者cookie过期")#line:234
