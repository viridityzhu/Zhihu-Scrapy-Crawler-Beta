两大部分：

1. 话题-》用户-》用户的全部朋友（他、她的整个社交网络）-》朋友的基本信息（回答问题多少，显示在首页的那些变量）
   话题--关注者--关系网络--关注者和关系网络所有的个人页面信息以及参与活动、提问回答等对应的文本？
2. 话题-》问题和回答（文本）-》提问和回答的用户
   话题--参与者--他们的关系网络和所有个人页面信息
3. 虽然有两部分，但这两部分有很大的重合（特别是文本），提高效率的话可以先把两部分的用户和他们的社交网络都抓下来，然后就有了一个用户的合集，基于这个合集再去抓他们的提问和回答的文本

571.50+406.7=978.2

写爬虫：

- [x] 话题页关注者-》只要用户基本信息
- [x] 用户关注者和
- [x] 用户粉丝-》只要用户基本信息
- [x] 用户个人信息
- [x] 用户提问文本
- [x] 用户回答文本
- [x] 话题页答案文本及答题者
- [x] 问题下的回答

运行爬虫：

- [x] topicfollower
- [x] topicdiscussion
- [x] userfollower
- [x] userfollowing
- [x] userinformation
- [x] userquestion
- [x] useranswer
- [x] questionanswer

数据总结：

1. topic follower：178条
2. topic discussion: 245条
3. user follower: 618028条
4. user following: 6923条
5. user information: 618932条
6. user question: 520221条
7. user answer: 2133870条
8. question answer: 31973条

` https://www.zhihu.com/api/v4/members/rocky/answers?include=data%5B*%5D.is_normal,admin_closed_comment,reward_info,is_sticky,comment_count,content,editable_content,voteup_count,reshipment_settings,comment_permission,mark_infos,created_time,updated_time,review_info,question.detail,answer_count,follower_count,excerpt,detail,question_type,title,id,created,updated_time,relevant_info,excerpt,label_info,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized&limit=20&offset=10`



1. 添加爬取的变量：
   1. - [x] 话题id：question  answer？
   2. - [x] 公共编辑: 就是logs_count，误以为是日志数
   3. - [x] 时间戳：question和answer的创建时间和最后更新时间
2. 使用分布式，预算1w
3. 争取第二周期前完成
4. 第二周期后可以开始比较数据



爬虫重构：

1. 添加变量：话题id、公共编辑、时间戳
2. 爬虫合并：把8个爬虫合并成一个，原本的执行逻辑是爬虫1运行完手动运行爬虫2，现在改成数据1获得之后自动请求数据2。方便每周一次调度，同时迎合分布式爬虫的需求
3. 分布式爬虫：把scrapy框架换成scrapy-redis，实现多爬虫分布式爬取，效率提升好几倍
4. 更换数据库方案：sqlite数据库相对于我们这么高级的爬虫来说实在是太弱了，在经费充足的情况下可换成腾讯云数据库

```python
# 打开数据库连接
db = pymysql.connect(
    host='cdb-nran2q00.cd.tencentcdb.com',  # 远程登录主机的ip地址
    port=10041,  # mysql服务器的端口
    user='root',  # mysql的用户
    passwd='Mimashi123',  # 密码
    db='TESTDB'  # 需要的数据库名称
)

# insert 参数
user_id = "test123"
password = "password"

con.execute('insert into Login values( %s,  %s)' % \
             (user_id, password))
```

##xhr

**topic follower**

https://www.zhihu.com/api/v4/topics/19873682/followers?limit=50&offset=0

*limit最多50；offset大于200即失效*

**topic discussion**

讨论区

```xquery
https://www.zhihu.com/api/v4/topics/19873682/feeds/top_activity?include=
data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;
data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;
data[?(target.type=topic_sticky_module)].target.data[?(target.type=article)].target.content,voteup_count,comment_count,voting,author.badge[?(type=best_answerer)].topics;
data[?(target.type=topic_sticky_module)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;
data[?(target.type=answer)].target.annotation_detail,content,hermes_label,is_labeled,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;
data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;
data[?(target.type=article)].target.annotation_detail,content,hermes_label,is_labeled,author.badge[?(type=best_answerer)].topics;
data[?(target.type=question)].target.annotation_detail,comment_count;
&limit=10&after_id=10.00000
```

```xquery
https://www.zhihu.com/api/v4/topics/19873682/feeds/top_activity?include=data[*].target.author%3Bdata[*].target.question.author&limit=10&after_id=10.00000
%3Bdata%5B%3F(target.type%3Dquestion)%5D.target.question.author
```



```xquery
include: data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=article)].target.content,voteup_count,comment_count,voting,author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;data[?(target.type=answer)].target.annotation_detail,content,hermes_label,is_labeled,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;data[?(target.type=article)].target.annotation_detail,content,hermes_label,is_labeled,author.badge[?(type=best_answerer)].topics;data[?(target.type=question)].target.annotation_detail,comment_count;

```







data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=article)].target.content,voteup_count,comment_count,voting,author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;data[?(target.type=answer)].target.annotation_detail,content,hermes_label,is_labeled,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;data[?(target.type=article)].target.annotation_detail,content,hermes_label,is_labeled,author.badge[?(type=best_answerer)].topics;data[?(target.type=question)].target.annotation_detail,comment_count;

https://www.zhihu.com/api/v4/topics/19873682/feeds/essence?include=data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=article)].target.content,voteup_count,comment_count,voting,author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;data[?(target.type=answer)].target.annotation_detail,content,hermes_label,is_labeled,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;data[?(target.type=article)].target.annotation_detail,content,hermes_label,is_labeled,author.badge[?(type=best_answerer)].topics;data[?(target.type=question)].target.annotation_detail,comment_count&limit=5&offset=0

**user followee**

https://www.zhihu.com/api/v4/members/zhu-zhu-31-4-82/followees?limit=20&offset=0

**user followee**

https://www.zhihu.com/api/v4/members/zhu-zhu-31-4-82/followers?limit=20&offset=0

**user question**

https://www.zhihu.com/api/v4/members/rocky/questions?include=data%5B*%5D.created,topics,detail,answer_count,follower_count,author,admin_closed_comment&limit=20&offset=0



**user information**

https://www.zhihu.com/api/v4/members/rocky?include=data[*].locations,employments,gender,educations,business,voteup_count,thanked_count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,columns_count,commercial_question_count,favorite_count,favorited_count,logs_count,included_answers_count,included_articles_count,included_text,message_thread_token,is_active,sina_weibo_url,sina_weibo_name,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics&limit=10&offset=0

```xquery
https://www.zhihu.com/api/v4/members/rocky?include=data[*].gender,voteup_count,thanked_count,follower_count,following_count,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,columns_count,favorite_count,favorited_count,logs_count,included_answers_count,included_articles_count,included_text,message_thread_token,is_active,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,hosted_live_count,participated_live_count,allow_message
```



meta_related_topics?include=%24.data%5B*%5D.vote,meta.avatar,title,description1,description2,scores,tags,summary,pub_info



**user answer**

https://www.zhihu.com/api/v4/members/rocky/answers?include=data%5B*%5D.is_normal,admin_closed_comment,reward_info,is_sticky,comment_count,content,editable_content,voteup_count,reshipment_settings,comment_permission,mark_infos,created_time,updated_time,review_info,question.detail,topics,answer_count,follower_count,excerpt,detail,question_type,title,id,created,updated_time,relevant_info,excerpt,label_info,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized&limit=20&offset=0

**question answer**

https://www.zhihu.com/api/v4/questions/50557697/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question.topics,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=5&platform=desktop&sort_by=default&offset=5



* `https://www.zhihu.com/api/v4/topics/19873682/feeds/essence?include=data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,question.detail;data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,is_normal,comment_count,voteup_count,relevant_info,question.detail,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;data[?(target.type=answer)].target.annotation_detail,content,hermes_label,is_labeled,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,question.detail;data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;data[?(target.type=question)].target.annotation_detail,comment_count&limit=5&offset=0`

question.detail

`                 'https://www.zhihu.com/api/v4/topics/19873682/feeds/essence?include=data%5B*%5D.is_normal,admin_closed_comment,reward_info,is_sticky,comment_count,content,editable_content,voteup_count,reshipment_settings,comment_permission,mark_infos,created_time,updated_time,review_info,question.detail,answer_count,follower_count,excerpt,detail,question_type,title,id,created,updated_time,relevant_info,excerpt,label_info,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized&limit=20&offset=0']`

* 参数：
  * `limit`：数量，最大 20
  * `offset`：起始位置，从零开始
  * `include`：额外信息，包括`data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=article)].target.content,voteup_count,comment_count,voting,author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;data[?(target.type=answer)].target.annotation_detail,content,hermes_label,is_labeled,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;data[?(target.type=article)].target.annotation_detail,content,hermes_label,is_labeled,author.badge[?(type=best_answerer)].topics;data[?(target.type=question)].target.annotation_detail,comment_count`

https://www.zhihu.com/api/v4/topics/19873682/feeds/essence?include=data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type=answer)].target.annotation_detail,content,hermes_label,is_labeled,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics&limit=5&offset=0

https://www.zhihu.com/api/v4/topics/19873682/feeds/essence?include=data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content;data[?(target.type=answer)].target.annotation_detail,content,hermes_label,is_labeled,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp&limit=5&offset=0

https://www.zhihu.com/api/v4/topics/19873682/feeds/essence?&limit=5&offset=0

每周运行爬虫步骤：

1. 初始化redis：清空上一次爬虫遗留的urls任务，初始化urls

2. 新建数据库：

   1. 在gerapy中两个爬虫的settings中更新数据库名称
   2. 运行CreateDB.py，（创建新的数据库）

3. 部署项目新版本：

   1. 本地运行gerapy runserver
   2. 打开localhost:8000网页，将新项目打包并部署

4. 调度爬虫：quickStart.py 运行task 1

   



slaver conf:

1. ` vim ../etc/supervisor/supervisord.conf`
2. comment spiderkeeper and redis    change /tmp/ to /var/run/
3. ` vim ../etc/supervisord.conf`
4. change /tmp/ to /var/run/
5. ….like the web
6. ` ps aux | grep supervisord` find it and ` kill -9 xxxx`
7. `supervisord -c /etc/supervisord.conf`
8. if unlink :`sudo unlink /var/run/supervisor.sock`



重启服务器之后的操作：

1. 重启supervisord:`supervisord -c /etc/supervisord.conf`
2. redis设置密码：` redis-cli`
3. `config set requirepass NDYwdmms(4r3e2w1q!!)`
4. `/redis-4.0.6/redis.conf`配置文件里改密码



爬虫数据下载及期数记录：

1. Master的sqlite数据库

   ```
   scp root@129.28.28.203:/etc/zhihu_crawl.db /Volumes/zhangpig/zhihu_crawl.db
   ```

2. MySQL的test

3. m6d22

4. m7d26

5. t2m8d13

6. m9d14

7. m10d27 10.31

scp root@129.28.28.203:/etc/test.csv /Users/jiayinzhu/Downloads/test.csv



老师~我们发现了一个叫scrapinghub的云爬虫服务，可以取代之前所用的云服务器爬虫部署方案，同时有三个好处：

1. 取代代理ip方案，彻底解决ip被封的问题：scrapinghub每次运行爬虫任务时随机分配ip，被封的话只需要关掉爬虫启动一个新的即可，不再需要代理ip，代理ip带来的速度下降问题就得到了解决；
2. 价格合理：在scrapinghub上租用3个爬虫单元，需要3×9=27美元/月(187.46元/月)；但可以减少3台腾讯云服务器的租用(187.5元/月)和代理ip的购买(170元/月），总的来说更便宜了（3个爬虫单元187.46+云数据库89+redis云服务器193.9=470.36元/月）；
3. 方便定期爬虫任务：scrapinghub有定期任务功能，可以方便地设置时间间隔定期运行爬虫

昨天我们已经尝试了更改爬虫代码，并且在scrapinghub的试用单元上成功运行了爬虫，发现它因为服务器在国外的缘故，相比于腾讯云速度略有下降，但比代理ip快得多，总体来说影响不大





supervisor web ui conf:

![image-20191023141952863](/Users/jiayinzhu/Desktop/笔记/放图/image-20191023141952863.png)



mysql root 's password: Mimashi123)

master's password: wkBDHS1314!



本地测试爬虫时，要改数据库名：

`scrapy crawl zhihunoqat1 -s DATABASE_NAME=m1d18`

监控linux进程：`ps aux`

杀掉某进程：`kill -9 进程号`



- [x] 完成的user要写到新的表里才行，不然中途302的就爬不全了
- [ ] 代理池要merge
- [x] 用户信息爬虫要写完
- [x] 大V抽取

- [x] user information order strange
- [x] usfer/usfee read when file not exist, copying the resolution from usinfo is ok.
- [x] not test the situation when uinfo task is over

4369911+107865

###大V抽取方法：

大于10万的抽1000（1%），1\~10万抽（3%），5000\~1万（10%）

###话题页：

专业：口腔医学 19589126 妇产科学 21199525 内科学 19628411

非专业：养生 19555542 ，生活习惯 19557781 ，健康常识 19651260

`https://www.zhihu.com/api/v4/topics/19628411/feeds/top_activity?include=data[*].target.author%3Bdata[*].target.question.author&limit=10&after_id=10.00000`

## data record：

data文件夹中：

1. url_token: 话题页关注者，种子用户url token
2. user_followee: 种子用户的关注的人的url token
3. user_follower: 种子用户粉丝的ut
4. userInfo: 所有用户的用户信息

tempData中：

1. finishedFe:爬取fe的时候，对每个种子用户，每爬一个，就写一次种子用户ut进去，用来数已爬数与应爬数
2. reallyFinishedFe: 爬取fe的时候，每个种子用户如果已完成其二级用户的爬取，就写进ut；用来去掉已完成任务
3. finishedFr：同4
4. reallyFinishedFr: 同5
5. finishedUinfo: 完成用户信息爬取的用户，用来去掉重复认为





todo：

- [x] ~~403：写page数进reallyFinished第二列~~
- [x] ~~爬虫构造url的时候改逻辑：如果reallyFinished第二列有值，就作为起始页数；如果没有，起始页数默认0~~
- [x] 410：用户不存在，也把urltoken放进reallyFinished里
- [ ] ~~403：重爬~~
- [ ] info的403处理：被记成已完成.从log里找出403的info，写进新任务表里，单独重爬