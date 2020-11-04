import requests
url = r'https://www.zhihu.com/api/v4/members/jin-wan-yue-se-zhen-mei-88/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
print(url)
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
           'referer': 'https://www.zhihu.com/people/jin-wan-yue-se-zhen-mei-88/following',
           # 'x-requested-with': 'fetch',
           'x-zse-83': '3_2.0',
           'x-zse-86': '1.0_aXN8nbXynhOp2X28fRF0rQL8FUYf2HYBK_Oy66Xq20Np',
           'x-zst-81': '3_2.0ae3TnRUTEvOOUCNMTQnTSHUZo02p-HNMZBO8YD7qrXtu2RY0K6P0EHuy-LS9-hp1DufI-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_IS4gpr4w0mRPO7HoY70SfquPmz93mhDQyiqV9ebO1hwOYiiR0ELYuUrxmtDomqU7ynXtOnAoTh_PhRDSTFLomAgemKCLGQ7O_eQOf1BtfnUF_OruY6XcskH39ThFOzceGaUt1gcNf1TSTv4VytUNYQMeYlgFfqv91oLHmz9eBRq2qIroBcgFYXuoVkGHBeuXf9gpM6QxBHBHYZvp1fqxLUwXG2qg_Wu3qYGXMHCOyuDpBb0ofbioKJ9SGFu2_VCL0CqkwCgXGqcx0PgeBxhNpJuc9MRY_au3fzBtYFbLZlUSC-BXMECxOcHFORuYYucxKArSMbiV9zUw9xrC_-Uc1rRgLTho8HrVZk8wVHBFOtG30rLXGWhXK-BLC',
           x - zse - 83: 3_2.0
           x - zse - 86: 1.0_a8Y0QQHBHq2XnCtqTqOB6H90nhNxnwS0G0xqk7rqHhxp
           x - zst - 81:   3_2.0ae3TnRUTEvOOUCNMTQnTSHUZo02p - HNMZBO8YD7qrXtu2RY0K6P0EHuy - LS9 - hp1DufI - we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_IS4gpr4w0mRPO7HoY70SfquPmz93mhDQyiqV9ebO1hwOYiiR0ELYuUrxmtDomqU7ynXtOnAoTh_PhRDSTFLomAgemKCLGQ7O_eQOf1BtfnUF_OruY6XcskH39ThFOzceGaUt1gcNf1TSTv4VytUNYQMeYlgFfqv91oLHmz9eBRq2qIroBcgFYXuoVkGHBeuXf9gpM6QxBHBHYZvp1fqxLUwXG2qg_Wu3qYGXMHCOyuDpBb0ofbioKJ9SGFu2_VCL0CqkwCgXGqcx0PgeBxhNpJuc9MRY_au3fzBtYFbLZlUSC - BXMECxOcHFORuYYucxKArSMbiV9zUw9xrC_ - Uc1rRgLTho8HrVZk8wVHBFOtG30rLXGWhXK - BLC
           # 'sec-fetch-dest': 'empty',
           # 'sec-fetch-mode': 'cors',
           # 'sec-fetch-site': 'same-origin',
           # 'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6',
           'cookie': '_zap=34e1804c-ae58-4534-bf2c-21259afa732c; d_c0="AFCiMM_Sjg6PTvsL42OxhcoWzyAzGCTjFxk=|1542882889"; __gads=ID=200b4373ac3305f5:T=1556779991:S=ALNI_MZ6gPAmSbdtv6A9GKR2IuyFQgGotw; _ga=GA1.2.1471823593.1556709603; _xsrf=1bzavO4qMAnIvsLBPqTiqbOD3BTgFpIg; z_c0="2|1:0|10:1588609797|4:z_c0|92:Mi4xMFBCOEFRQUFBQUFBVUtJd3o5S09EaVlBQUFCZ0FsVk5CWkdkWHdEbG9lNVN0ZGZ5ZGl1LXdHZEZBVWNuUkd0ZnB3|ffea583d1ab059ca0a17a771ce7ff8540db0a057f5812677fd431804811cf3e6"; __utma=51854390.1471823593.1556709603.1588604150.1588610094.10; __utmz=51854390.1588610094.10.9.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topic/19873682/newest; __utmv=51854390.100-1|2=registration_date=20150513=1^3=entry_date=20150513=1; q_c1=9f92dfe9edc040e0a8247878750bea39|1593407529000|1542882892000; tst=r; SESSIONID=6QB3Pyzi2A6ebhL6kh6ELe8zc3jzcpqQApSx9x5x7jb; JOID=UVEQBU0yfWI9-6Q2cTcye91ARalmDiAjDq7XQBsFNlhbmclwS37jc2f0ojlyuA5P4XfiB-bK4SxHIdrBGUxnBdo=; osd=U1oWC0IwdmQz9KY9dzk9edZGS6ZkBSYtAazcRhUKNFNdl8ZyQHjtfGX_pDd9ugVJ73jgDODE7i5MJ9TOG0dhC9U=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1594650000,1594737323,1595057555,1595057998; _gid=GA1.2.61923793.1595174707; _gat_gtag_UA_149949619_1=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1595174728; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1595174729|1595174703',

           }

r = requests.get(url, headers=headers)
print(r.status_code)
print(r.text)
