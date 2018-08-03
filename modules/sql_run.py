#!/usr/bin/env python
# -*- coding:utf-8 -*-


#sql语句

from common.mysql_select import *



sql_shapan_finish_areas="""
    SELECT    company.id,company.sonCompany,man.salesman_name,sum(o.final_area) as areas
    FROM fly_order o
    left join b_salesman man     on o.salesmanid=man.id
    Left JOIN sonCompany company   on   man.department=company.id   
    where o.is_show=1 and o.formalType=1 and o.state=7 
    group by company.id
    """
sql=sql_shapan_finish_areas

result=get_result(sql,'sql_resrultdata.txt')
    
print(result)
