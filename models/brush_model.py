# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
# 个人信息
class yonghu(Base_model):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    yonghuzhanghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='用户账号' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    yonghuxingming=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='用户姓名' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    shoujihao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机号' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )

class jingdianleixing(Base_model):
    __doc__ = u'''jingdianleixing'''
    __tablename__ = 'jingdianleixing'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    jingdianleixing=db.Column( db.VARCHAR(255),  nullable=True,unique=True,comment='景点类型' )

class lvyoujingdian(Base_model):
    __doc__ = u'''lvyoujingdian'''
    __tablename__ = 'lvyoujingdian'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='是'
    __intelRecom__='用协'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    jingdianmingcheng=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='景点名称' )
    jingdiantupian=db.Column( db.Text,  nullable=True, unique=False,comment='景点图片' )
    jingdianleixing=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='景点类型' )
    jingdiandengji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='景点等级' )
    kongqiqingkuang=db.Column( db.Text,  nullable=True, unique=False,comment='空气情况' )
    jingdiandizhi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='景点地址' )
    lishiwenhua=db.Column( db.Text,  nullable=True, unique=False,comment='历史文化' )
    xiuxianyule=db.Column( db.Text,  nullable=True, unique=False,comment='休闲娱乐' )
    jingdianjieshao=db.Column( db.Text,  nullable=True, unique=False,comment='景点介绍' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    discussnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )

class jiudianleixing(Base_model):
    __doc__ = u'''jiudianleixing'''
    __tablename__ = 'jiudianleixing'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    jiudianleixing=db.Column( db.VARCHAR(255),  nullable=True,unique=True,comment='酒店类型' )

class jiudianxinxi(Base_model):
    __doc__ = u'''jiudianxinxi'''
    __tablename__ = 'jiudianxinxi'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='是'
    __intelRecom__='用协'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    jiudianmingcheng=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='酒店名称' )
    jiudiantupian=db.Column( db.Text,  nullable=True, unique=False,comment='酒店图片' )
    jiudiandizhi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='酒店地址' )
    jiudianleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='酒店类型' )
    fangxing=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='房型' )
    yiwanjiage=db.Column( db.Float,default=0, nullable=False, unique=False,comment='一晚价格' )
    jiudianjieshao=db.Column( db.Text,  nullable=True, unique=False,comment='酒店介绍' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    discussnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )

class jiudianyuding(Base_model):
    __doc__ = u'''jiudianyuding'''
    __tablename__ = 'jiudianyuding'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    dingdanbianhao=db.Column( db.VARCHAR(255),  nullable=True,unique=True,comment='订单编号' )
    jiudianmingcheng=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='酒店名称' )
    jiudiantupian=db.Column( db.Text,  nullable=True, unique=False,comment='酒店图片' )
    jiudianleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='酒店类型' )
    fangxing=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='房型' )
    yiwanjiage=db.Column( db.Float,default=0, nullable=False, unique=False,comment='一晚价格' )
    ruzhutianshu=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='入住天数' )
    ruzhushijian=db.Column( db.DateTime,  nullable=True, unique=False,comment='入住时间' )
    hejijine=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='合计金额' )
    beizhu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )
    yonghuzhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户账号' )
    yonghuxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户姓名' )
    shoujihao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机号' )
    jiudiandizhi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='酒店地址' )
    ispay=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='是否支付' )

class luxianleixing(Base_model):
    __doc__ = u'''luxianleixing'''
    __tablename__ = 'luxianleixing'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    luxianleixing=db.Column( db.VARCHAR(255),  nullable=True,unique=True,comment='路线类型' )

class lvyouluxian(Base_model):
    __doc__ = u'''lvyouluxian'''
    __tablename__ = 'lvyouluxian'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='是'
    __intelRecom__='用协'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    luxianmingcheng=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='路线名称' )
    jingdianfengmian=db.Column( db.Text,  nullable=True, unique=False,comment='景点封面' )
    luxianleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='路线类型' )
    jingdianxiangmu=db.Column( db.Text,  nullable=True, unique=False,comment='景点项目' )
    juzhujiudian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='居住酒店' )
    jiudianjieshao=db.Column( db.Text,  nullable=True, unique=False,comment='酒店介绍' )
    shihejijie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='适合季节' )
    jiaotongfangshi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='交通方式' )
    qidian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='起点' )
    zhongdian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='终点' )
    xingchengfeiyong=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='行程费用' )
    feiyongxiangxi=db.Column( db.Text,  nullable=True, unique=False,comment='费用详细' )
    xingchengshijian=db.Column( db.Date,  nullable=True, unique=False,comment='行程时间' )
    xingchengluxian=db.Column( db.Text,  nullable=True, unique=False,comment='行程路线' )
    xingchenganpai=db.Column( db.Text,  nullable=True, unique=False,comment='行程安排' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    discussnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )

class yudingluxian(Base_model):
    __doc__ = u'''yudingluxian'''
    __tablename__ = 'yudingluxian'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    luxianmingcheng=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='路线名称' )
    jingdianfengmian=db.Column( db.Text,  nullable=True, unique=False,comment='景点封面' )
    luxianleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='路线类型' )
    jingdianxiangmu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='景点项目' )
    juzhujiudian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='居住酒店' )
    jiudianjieshao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='酒店介绍' )
    jiaotongfangshi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='交通方式' )
    qidian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='起点' )
    zhongdian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='终点' )
    xingchengfeiyong=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='行程费用' )
    yudingshuliang=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='预订数量' )
    hejifeiyong=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='合计费用' )
    feiyongxiangxi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='费用详细' )
    xingchengshijian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='行程时间' )
    xingchengluxian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='行程路线' )
    yudingshijian=db.Column( db.Date,  nullable=True, unique=False,comment='预定时间' )
    yonghuzhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户账号' )
    yonghuxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户姓名' )
    shoujihao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机号' )
    ispay=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='是否支付' )

class chat(Base_model):
    __doc__ = u'''chat'''
    __tablename__ = 'chat'



    __authTables__={}
    __foreEndListAuth__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    adminid=db.Column( db.BigInteger,default=0,  nullable=True, unique=False,comment='管理员id' )
    ask=db.Column( db.Text,  nullable=True, unique=False,comment='提问' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复' )
    isreply=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='是否回复' )

class newstype(Base_model):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    typename=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='分类名称' )

class news(Base_model):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'
    __intelRecom__='是'
    __browseClick__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    introduction=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    typename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='分类名称' )
    name=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='发布人' )
    headportrait=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )

class storeup(Base_model):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    refid=db.Column( db.BigInteger,default=0,  nullable=True, unique=False,comment='商品id' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='表名' )
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    type=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='类型' )
    inteltype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='推荐类型' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )

class aboutus(Base_model):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )

class systemintro(Base_model):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )

class discusslvyoujingdian(Base_model):
    __doc__ = u'''discusslvyoujingdian'''
    __tablename__ = 'discusslvyoujingdian'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    score=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='评分' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )

class discussjiudianxinxi(Base_model):
    __doc__ = u'''discussjiudianxinxi'''
    __tablename__ = 'discussjiudianxinxi'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    score=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='评分' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )

class discusslvyouluxian(Base_model):
    __doc__ = u'''discusslvyouluxian'''
    __tablename__ = 'discusslvyouluxian'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    score=db.Column( db.Float,default=0,  nullable=True, unique=False,comment='评分' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )

