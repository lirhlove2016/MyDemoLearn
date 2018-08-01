#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

"""
data:
ordernumber,phone,ids,area,msg_id,token
84331533102756156,18301212965,300,2187,100000002682324,59c4a437c8084b4d8a0a1f90d2d28cfb

"""

#读取数据函数,返回list类型的训练数据集和测试数据集
def read_from_txt(filename):   

    datalist=[]  #保存所有的job
    lines=[]
    with open(filename,encoding='UTF-8') as fr:
        lines2=fr.readlines()
        for line in lines2:
            #去掉空行
            if line=='\n':
                line=line.strip('\n')
            else:
                lines.append(line)
        
    #print('line---------',lines,'\n',len(lines))
    return lines
        


def take_orderdata_from_readtxt(lines):
    orderlist=[]
    for i in range(1,len(lines)):
        listdatas=lines[i].strip().split(',') #去除空白和逗号“,”
        orderdata={}   #每一条保存到一个字典里
        #print('lines----------',lines)
                        
        if len(listdatas)>=1:                     
            orderdata['ordername']=listdatas[0]
            orderdata['flyuser_phone']=listdatas[1]   
            orderdata['ids']=listdatas[2]
            orderdata['area']=listdatas[3]
            orderdata['msg_id']=listdatas[4]
            orderdata['token']=listdatas[5]

        orderlist.append(orderdata)                         
        
    #print('orderlist--',orderlist)
    return orderlist



#打印信息
def print_info(datas):   
    print('this is your order datas：')
    print('---------------------------------------------------------------------------')
    print('no     orderNumber   phone   ids    area    msg_id       token             ')
    print('---------------------------------------------------------------------------')

    res=datas
    #print(datas)
    for i  in range(len(res)):
            print(i+1,res[i]['ordername'],res[i]['flyuser_phone'],res[i]['ids'],res[i]['area'],res[i]['msg_id'],res[i]['token'])

            
    print('-------------------------------------------------------------------------\n')




filename=os.getcwd()+'/flyuser_submit_order.txt'
print("this is your orderdata filename:%s \n"%filename)

    

if __name__=='__main__':
    
		
    lines=read_from_txt(filename)
    res=take_orderdata_from_readtxt(lines)
    print_info(res)


  



