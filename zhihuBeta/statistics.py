import csv


# -------------------------
# print('甲醚er新任务统计')
# userList = []
# finishedUe = []
# with open('./data/userFollower-jm-all.csv', 'r') as f:
#     reader = csv.reader(f)
#     for im in reader:
#         userList.append(im[1])
# with open('./tempData/finishedUinfo.csv', 'r+') as f:
#     reader = csv.reader(f)
#     for im in reader:
#         finishedUe.append(im[0])
# suserList = set(userList)
# sfinishedUe = set(finishedUe)
# print('去重后的er数：{}'.format(len(suserList)))
# print('by the way, 已爬到的用户info数：{}'.format(len(sfinishedUe)))
# newTask = [i for i in suserList if i not in sfinishedUe]
# print('再减去已经爬到的，剩下的新任务：{}'.format(len(set(newTask))))


# -------------------合并finishedinfo
# fin = []
# with open('./tempData/finishedUinfo.csv', 'r')as f:
#     reader = csv.reader(f)
#     for im in reader:
#         fin.append(im[0])
# with open('./tempData/finishedUinfo 2.csv', 'r')as f:
#     reader = csv.reader(f)
#     for im in reader:
#         fin.append(im[0])
# with open('./tempData/finishedUinfo 3.csv', 'r')as f:
#     reader = csv.reader(f)
#     for im in reader:
#         fin.append(im[0])
# fin = set(fin)
# print(len(fin))
# with open('./tempData/finishedUinfo.csv', 'w')as f:
#     for u in fin:
#         f.write(u + '\n')

# -------------------split er task
# print('甲醚er新任务统计')
# userList = []
# finishedUe = []
# with open('./data/userFollower-jm-all.csv', 'r') as f:
#     reader = csv.reader(f)
#     for im in reader:
#         userList.append(im[1])
# with open('./tempData/finishedUinfo.csv', 'r+') as f:
#     reader = csv.reader(f)
#     for im in reader:
#         finishedUe.append(im[0])
# suserList = set(userList)
# sfinishedUe = set(finishedUe)
# print('去重后的er数：{}'.format(len(suserList)))
# print('by the way, 已爬到的用户info数：{}'.format(len(sfinishedUe)))
# newTask = [i for i in suserList if i not in sfinishedUe]
# newTask = set(newTask)
# tt = len(newTask)
# print('再减去已经爬到的，剩下的新任务：{}'.format(tt))
# count = 0
# writer1 = csv.writer(open('./data/userFollower-split-1.csv', 'a+'),
#                      lineterminator='\n')
# writer2 = csv.writer(open('./data/userFollower-split-2.csv', 'a+'),
#                      lineterminator='\n')

# with open('./data/userFollower-split-1.csv', 'w')as f:
#     for u in newTask:
#         count += 1
#         if count < tt / 2:
#             writer1.writerow(['Non', u])
#         else:
#             writer2.writerow(['Non', u])
#--------------------------
# print('ee统计')
# userList = []
# finishedUe = []
# with open('./data/userFollowee.csv', 'r') as f:
#     reader = csv.reader(f)
#     for im in reader:
#         userList.append(im[1])
# with open('./tempData/finishedUinfo.csv', 'r+') as f:
#     reader = csv.reader(f)
#     for im in reader:
#         finishedUe.append(im[0])
# suserList = set(userList)
# sfinishedUe = set(finishedUe)
# print('去重后的ee数：{}'.format(len(suserList)))
# print('已爬到的用户info数：{}'.format(len(sfinishedUe)))
# newTask = [i for i in suserList if i not in sfinishedUe]
# newTask = set(newTask)
# tt = len(newTask)
# print('相减，剩下的新任务：{}'.format(tt))
#--------------------------
# print('url_token去重')
# userList = []
# finishedUe = []
# with open('./data/url_token_口腔医学.csv', 'r') as f:
#     reader = csv.reader(f)
#     for im in reader:
#         userList.append(im[0])
# with open('./data/url_token_健康常识.csv', 'r') as f:
#     reader = csv.reader(f)
#     for im in reader:
#         userList.append(im[0])
# suserList = set(userList)

# print('去重后的种子用户数：{}'.format(len(suserList)))

# with open('./data/url_token.csv', 'w')as f:
#     for u in suserList:
#         f.write(u + '\n')
