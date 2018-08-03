# -*- coding:utf8 -*-

# ------------------------------ case: system management account----------------------
testdata_system_login_userdata_001 = {
        "userName":"lirunhua",
        "passWord":"123456",
}

testdata_system_login_userdata_002 = {
        "userName":"lirunhua",
        "passWord":"12345",
}

# ------------------------------ case: city management account----------------------
testdata_001_city_account_001 = {
        "userName":"lirunhua",
        "passWord":"123456",
}

# ------------------------------ case: add salesman----------------------
testdata_001_add_salesman_001 = {
        "email":"test@farmfriend.cn",
        "department":"10",
        "managerId":"72",
        "address":"江苏省徐州市鼓楼区黄楼街道华联社区",
}

# ------------------------------ case: system query fly user----------------------
testdata_001_system_query_flyuser_001 = {
        "phone":"14200010006",
}

# ------------------------------ case: system fly user auth----------------------
testdata_001_system_flyuser_auth_001 = {
        "authState":"3",
}

# ------------------------------ case: system freez flyuser----------------------
testdata_system_freeze_flyuser = {
        "id":"2785",
        "state":"3",
}

# ------------------------------ case: system freez flyuser state----------------------
testdata_system_freez_flyuser_auth = {
        "flyAuthState":"3",
}

#---------------------------------sys query auth----------------------------------------
testdata_sys_query_auth_001={
        "phone":"14923607195",
        "liableName":"",
        "teamName":"",
        "address":"",
        "roleId":"-1",
        "label":"-1",
        "authState":"-1",
        "isBlacklist":"2",
        "state":"-1",
        "flyAuthState":"",
        "page":"1",
        "rows":"30",
        "sort":"",
        "order":"",
}
#---------------------------sys user auth---------------------------------------------
testdata_fly_user_auth_001={
        "id":"2651",
        "authState":"3",
        "check":"true",
        "noPassReason":"",
}
#------------------------sys fly auth---------------------------------------------
testdata_fly_auth_001={
        "flyUserId":"2651",
        "flyAuthState":"3",
        "noPassReason":"",
}


#---------------------------------sys query flyuser assign----------------------------------------
testdata_sys_query_assignflyuser_001={
		"id":"17580",
		"time":"2018-08-01",
		"page":"1",
		"rows":"50",
		"sort":"xy",
		"order":"asc",
		"teamName":"",
		"name":"",
		"phone":"18301212965",
		"address":"",
		"isInnerUser":"-1",
		"label":"-1",
		"region":"-1",
		"role":"-1",
		"isAll":"1",
		"reserveRole":"-1",
		"isBusy":"-1",
		}
#---------------------------------sys publishorder ----------------------------------------
testdata_sys_assign_flyuser_001={
            "id":"17580",
            "orderNumber":"72601532947245724",
            "extractingPercentage":"2.7",
            "subsidyPercentage":"1",
            "flyUser":2187,
            "workStartTime":"2018-08-01",
            "days":"1",
            "sendType":"1",
            "isTeam":"0",
            "teamUserNum":"1",
            "planeNum":"0",
            "isAll":"1",
		}
#---------------------------------sys  联合作业派单 ----------------------------------------
testdata_sys_addjoinoperation_flyuser_001={
            "orderNumber":72601532947245724,
            "extractingPercentage":2.7,
            "subsidyPercentage":1,
            "userIdList":2187,
			"heroPostLabel":"英雄帖标题",
			"heroPostAbstract":"英雄帖摘要",
			"heroPostPicUrl": "http://farmlandbuckets.oss-cn-beijing.aliyuncs.com/3f40dbdc-b18e-4346-8193-10e7cd3d04b6.png",
			"remark":"备注",
            "inquiryType":0,
			"stipulateWorkTime":"2018-08-01",
			"stipulateWorkDays":4,
		}
		
# ------------------------------ case: system asgin order and flyuser submit order----------------------
testdata_001_query_ordernumber="55891533227302876"
testdata_001_flyuser_phone='18301212965'
testdata_001_flyuser_submit_order_area=300