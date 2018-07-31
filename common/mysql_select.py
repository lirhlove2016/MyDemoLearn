#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
from conf import server_config as device

#import pymysql as MySQLdb  #这里是python3  如果你是python2.x的话，import MySQLdb

'''
#封装sql
'''
#数据库连接信息
host=device.DICT__NTGJ_SERVER_DB['IP']
port=device.DICT__NTGJ_SERVER_DB['PORT']
user=device.DICT__NTGJ_SERVER_DB['USERNAME']
passwd=device.DICT__NTGJ_SERVER_DB['PASSWORD']
db=device.DICT__NTGJ_SERVER_DB['FRAM_DB_NAME']

#sql语句

def  sql_execute(sql): 

    # 创建连接
    conn = pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset='utf8')
    #conn = pymysql.connect(host='10.0.1.5',port=3306,user='work',passwd='srcRwk8WNcZemaSKflE9',db='farmfriend')

    # 创建游标
    cursor = conn.cursor()
      
    #查询第一条
    #cursor.execute("select * from fly_order limit 1")

    # 执行SQL，并返回受影响行数
    #cursor.execute(sql_select_muci)
    cursor.execute(sql)

    # 提交，不然无法保存新建或者修改的数据
    conn.commit()

    #获取所有数据
    results=cursor.fetchall()

    #获取字段信息
    fields=cursor.description
    #print(fields)
    data=[]
    for f in range(0,len(fields)):
        print(fields[f][0],end=' ')
        data.append(fields[f][0])

    print(' ')

    #打印数据    
    for w in results:

        print(w)

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    print(data)
    return data,results

def get_result(sql,filename):

    data,results = sql_execute(sql)


    print('The amount of datas: %d' % (len(results)))
    
    with open(filename, 'w') as f:
        f.write(str(data)+ '\n')
        for result in results:
            f.write(str(result) + '\n')

    print('Data write is over!')

    return results


if __name__=="__main__":

    sql_shapan_finish_areas="""
    SELECT    company.id,company.sonCompany,man.salesman_name,sum(o.final_area) as areas
    FROM fly_order o
    left join b_salesman man     on o.salesmanid=man.id
    Left JOIN sonCompany company   on   man.department=company.id   
    where o.is_show=1 and o.formalType=1 and o.state=7 
    group by company.id
    """
    sql=sql_shapan_finish_areas
    #sql=sql_execute(sql_shapan_finish_areas)
    result=get_result(sql,'sql_data.txt')
    
    #print(result)
