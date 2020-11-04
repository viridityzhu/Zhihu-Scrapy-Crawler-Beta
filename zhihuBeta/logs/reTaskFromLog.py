'''
功能：从log文件中取403的userinfo任务，生成uinfo403.csv（覆盖原文件），且将这些任务从finishedUinfo.csv中去掉
操作：
1. 把待取的log文件名写进LOGFILELIST
2. 运行此程序
3. 运行zhui403爬虫，即可重新爬它们
'''
userList = []
LOGFILELIST = ['log-7-13-13.txt']
uselessInfo = ['Crawled (200)', 'Scraped from <200',
                                'Crawled (410)',
               'INFO: Ignoring response <410',
               'INFO: Ignoring response <404',
               'Traceback', 'list.remove(x):', 'File "/', 'spider.userList.remove(u)', 'result = g.send(', 'spider=spider',
               'task over. trying to',
               'INFO: Crawled']
for LOGFILE in LOGFILELIST:
    with open(LOGFILE, 'r') as f:
        for line in f.readlines():
            flag = 1
            for info in uselessInfo:
                if info in line:
                    flag = 0
            if flag:
                if 'Error downloading <GET' in line or 'INFO: Ignoring response <403' in line:
                    userList.append(line.split('/')[6].split('?')[0])
                else:
                    print(line)

print(len(set(userList)))


with open('../tempData/finishedUinfo.csv', 'r') as r:
    lines = r.readlines()
with open('../tempData/finishedUinfo.csv', 'w') as w:
    for l in lines:
        if l[:-1] not in userList:
            w.write(l)

with open('../data/uinfo403.csv', 'w')as f:
    for u in userList:
        f.write(u + '\n')
print('finished.')
