import csv
userList = []
finishedUe = []
with open('./tempData/finishedUr.csv', 'r') as f:
    reader = csv.reader(f)
    for im in reader:
        userList.append(im[0])


userListF = []
with open('./data/url_token.csv', 'r+') as f:
    reader = csv.reader(f)
    for im in reader:
        userListF.append(im[0])
try:
    with open('./tempData/ReallyFinishedUr.csv', 'r+') as f:
        reader = csv.reader(f)
        for im in reader:
            finishedUe.append(im[0])
except FileNotFoundError:
    open('./tempData/ReallyFinishedUr.csv', 'w+')
seed = userListF
finished = userList
real = finishedUe


print('seed: ' + str(len(set(seed))))
print('finished: ' + str(len(set(finished))))
print('really: ' + str(len(set(real))))
# print('seed - really = {}, 可能是大V'.format(len(set(seed)) - len(set(real))))
# print('really - finished = {}, 包括11个已注销和一些关注者数为0的用户，合理'.format(len(set(real)) - len(set(finished))))
seed_real = [i for i in set(seed) if i not in real]
real_seed = [i for i in set(real) if i not in seed]
# remain_seed_real = [item for item in remain if item not in seed_real]
print('in seed not in real: {}, 完全没爬到？'.format(len(set(seed_real))))
print('in real not in seed: {}，是{}，哪来的？？？？？'.format(
    len(set(real_seed)), real_seed[0]))

finished_real = [i for i in set(finished) if i not in real]
real_finished = [i for i in set(real) if i not in finished]
print('in finished not in real: {}, 抽样看了，关注数都特大，大几百几千，应该都是403中断的，也应该有大V；合理'.format(
    len(set(finished_real))))
print('in real not in finished: {}, 抽样看了，情况全是：0关注、账户停用、被封；正常。'. format(
    len(set(real_finished))))
# print(set(seed_real))
# taskList = ['gpfvic', 'du-du-du-95', 'ji-wei-73-87', 'zhao-qing-qing-83', 'breaknever', 'c3ea1d88feb5', 'guohengkai', 'xian-cai-tiao', 'heigaga', 'Bluebear', 'reseted1507543358', 'yzd-91', 'mu-qing-18-77', 'feng-jian-da', 'jyo-gan', 'claire-16-43', 'yang-xiao-jie-3-21', 'reseted1512737607632', 'junzhibuqi', 'wang-si-yi-3', 'huan-le-yan', 'delphi', 'loong', 'liu-jia-ming-2', 'fatfox10', 'kanxin-2', 'justin-liu-56', 'li-li-15-9-83', 'qing-shui-yu-47', 'zhang-wei-zhong', 'yao-xing-60-8-41', 'shoudoumaodaifu', 'ma-zi-ran-4', 'mouvant', 'hydfox', 'aige120', 'cnaksun', 'pansz', 'shen-yi-sheng-28', 'neng-dong-de-san-fen-jian', 'li-mu-59-94', 'ursuiand', 'liu-chun-73', 'chi-wan-11', 'clb1020', 'wang-wen-82-59', 'wang-yang-yi', 'xi-ye-24-24',
#             'zhang-qing-feng-60', 'ren-rui-01', 'xu-lei-20-52', 'wu-si-tong-50', 'tong-feng-zhi-you', 'hua-zha-zha-95', 'xu-kang-kang-22', 'kinvy', 'zhu-su-yu', 'zhao-zhou-24-73', 'li-damon', 'a-duan-85-51', 'cangrong', 'wang-hua-90', 'da-jia-yi-lian', 'luoxiaoju', 'song-ing-74', 'katherinepetrova', 'wo-jue-de-xian-zong-zi-hao-chi', 'hou-chen-3', 'huang-long-ju', 'HMS-HOOD', 'wei-zhe-shan', 'brglng', 'aguaithefreak', 'xu-mu-mu-85', 'ling-liang-38-43', 'ben-ni-88-63', 'zuker', 'dao-jie-fu-weng', 'tianyizhongyi', 'xiaoyaosanren', 'ding-wei-3', 'yang-qing-shan-27-77', 'liang-jin-cheng-9', 'huan-yan-88', 'lidang', 'yupeng-jiang', 'yalewei', 'changwei1006', 'zombie', 'dao-dao-jun', 'zhi-neng-shou-heng', 'ruobingshen', 'ya-wei-sang-153', 'liu-zhi-peng-26', 'gao-zuo-wen']
# print('reseted1512737607632' in taskList)
# print('''
# 特殊情况：
# 403没爬完：在finished，不在real
# 大V：在finished，不在real
# 0关注者：在real，不在finished
# 账号被封：在real，不在finished
# time out
# error：如果第一页就timeout，就不在real也不在finished里；如果中途某页timeout，在finished不在real

# 重新运行，待爬列表：userList len: 95, 正是上一次在seed里不在real里的，说明取任务没有问题
# 这次运行了一分钟，一下子又得到6个410，可见剩下的任务中还有很多410
# 想不通的点：
# 1. 为什么之前剩了任务没完成爬虫直接结束了？
# 2. 为什么剩了很多410？

# 现在得到的新信息是：1. 爬虫肯定会在别的情况下直接结束，所有任务并没有爬完…… 2. 有一个timeout error没有考虑到，它应该是网络问题导致连接超时，直接把那个任务放弃掉了
# ''')
#---------------------------------
# print(userList)
# lastTime = []
# with open('./tempData/finishedLastTime.csv', 'r+') as f:
#     reader = csv.reader(f)
#     for im in reader:
#         lastTime.append(im[0])
# print(len(set(lastTime)))
# d = {}
# for i in set(lastTime):
#     d[i] = lastTime.count(i)
# print(d)

# refn = []
# with open('./tempData/ReallyFinishedUe.csv', 'r+') as f:
#     reader = csv.reader(f)
#     for im in reader:
#         refn.append(im[1])
# refn.sort()
# print(refn)
# url_token: 1180
# ee: 1057
# real: 1086
# finished: 1057
# 410: 11
# with open('finishedUe.csv', 'r') as f:
#     reader = csv.reader(f)
#     for im in reader:
#         finishedUe.append(im[0])
# # for i in set(finishedUe):
# #     userList.remove(i)
# A = [item for item in userList if item not in set(finishedUe)]
# print(len(A))


# fList = []
# with open('finishedUe.csv', 'r') as f:
#     reader = csv.reader(f)
#     for im in reader:
#         fList.append(im[0])
# count = fList.count('shuaij')
# print(count)
