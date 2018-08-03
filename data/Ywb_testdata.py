# -*- coding:utf8 -*-

# ------------------------------ case:  account----------------------

testdata_YWB_login_userdata_001= {
            'phone':'18301212965',
            "passWord":"123qwe",
    }
# ------------------------------ case: ----------------------

testdata_YWB_salesmanquery_data_001= {
			"salesmanId":"s1520841050603Sbb9ed6f5-91f5-4989-b14b-3aeafd7031fc",
			"number":0,
    }
# ------------------------------ case: ----------------------
testdata_ywb_addorder_001={"accountId":"809","address":"北京市市辖区朝阳区还得大家庭教育基金会","area":"75.0","b_dosage":"","city":"市辖区","cityCode":"110100","county":"朝阳区","countyCode":"110105","cropId":"2","crops_highly":"1.5米及其以下","crops_name":"中稻","customer":"3","detailsAddress":"伊顿慧智双语幼儿园北京宝星校园","drugType":"0,1,2,6","farmlandArea":"75.0","farmlands":"F1528783867698","formalType":"1","guideName":"小八路","guidePhone":"14430036003","invoice":"2","latitude":"39.999785686240536","longitude":"116.48228599399104","discountRatio":"100","assembledAddress":"北京市北京市朝阳区朝阳区","isLongReserve":"1","imgNote":"[]","medicineService":"0","salesmanNote":"备注","settlementPrice":"10.0","assembledAddressLatitude":"39.92147","assembledAddressLongitude":"116.443108","days":"4","sprayingTimeStamp":"1532188800","medicineUrl":"","name":"小八路","orderNote":"业务宝，正式，拜访人","orderType":"1","order_money":"750","phone":"14430036003","province":"北京市","provinceCode":"110000","salesmanId":"s1520841050603Sbb9ed6f5-91f5-4989-b14b-3aeafd7031fc","spraying_time":"2018-08-02  至2018-08-05 ","teleAddress":"北京市朝阳区望京街道伊顿慧智双语幼儿园北京宝星校园","transitionsNumber":"0","type":"1","unit_price":"10.0","userType":"0","weatherId":"32e4cc07-f79a-4add-ac3e-56469992514a"}


payload = "data=%7B%22accountId%22%3A%22809%22%2C%22address%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%E5%B8%82%E8%BE%96%E5%8C%BA%E6%9C%9D%E9%98%B3%E5%8C%BA%E8%BF%98%E5%BE%97%E5%A4%A7%E5%AE%B6%E5%BA%AD%E6%95%99%E8%82%B2%E5%9F%BA%E9%87%91%E4%BC%9A%22%2C%22area%22%3A%2275.0%22%2C%22b_dosage%22%3A%22%22%2C%22city%22%3A%22%E5%B8%82%E8%BE%96%E5%8C%BA%22%2C%22cityCode%22%3A%22110100%22%2C%22county%22%3A%22%E6%9C%9D%E9%98%B3%E5%8C%BA%22%2C%22countyCode%22%3A%22110105%22%2C%22cropId%22%3A%222%22%2C%22crops_highly%22%3A%221.5%E7%B1%B3%E5%8F%8A%E5%85%B6%E4%BB%A5%E4%B8%8B%22%2C%22crops_name%22%3A%22%E4%B8%AD%E7%A8%BB%22%2C%22customer%22%3A%223%22%2C%22detailsAddress%22%3A%22%E4%BC%8A%E9%A1%BF%E6%85%A7%E6%99%BA%E5%8F%8C%E8%AF%AD%E5%B9%BC%E5%84%BF%E5%9B%AD%E5%8C%97%E4%BA%AC%E5%AE%9D%E6%98%9F%E6%A0%A1%E5%9B%AD%22%2C%22drugType%22%3A%220%2C1%2C2%2C6%22%2C%22farmlandArea%22%3A%2275.0%22%2C%22farmlands%22%3A%22F1528783867698%22%2C%22formalType%22%3A%221%22%2C%22guideName%22%3A%22%E5%B0%8F%E5%85%AB%E8%B7%AF%22%2C%22guidePhone%22%3A%2214430036003%22%2C%22invoice%22%3A%222%22%2C%22latitude%22%3A%2239.999785686240536%22%2C%22longitude%22%3A%22116.48228599399104%22%2C%22discountRatio%22%3A%22100%22%2C%22assembledAddress%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%E5%8C%97%E4%BA%AC%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E6%9C%9D%E9%98%B3%E5%8C%BA%22%2C%22isLongReserve%22%3A%221%22%2C%22imgNote%22%3A%22%5B%5D%22%2C%22medicineService%22%3A%220%22%2C%22salesmanNote%22%3A%22%E5%A4%87%E6%B3%A8%22%2C%22settlementPrice%22%3A%2210.0%22%2C%22assembledAddressLatitude%22%3A%2239.92147%22%2C%22assembledAddressLongitude%22%3A%22116.443108%22%2C%22days%22%3A%224%22%2C%22sprayingTimeStamp%22%3A%221532188800%22%2C%22medicineUrl%22%3A%22%22%2C%22name%22%3A%22%E5%B0%8F%E5%85%AB%E8%B7%AF%22%2C%22orderNote%22%3A%22%E4%B8%9A%E5%8A%A1%E5%AE%9D%EF%BC%8C%E6%AD%A3%E5%BC%8F%EF%BC%8C%E6%8B%9C%E8%AE%BF%E4%BA%BA%22%2C%22orderType%22%3A%221%22%2C%22order_money%22%3A%22750%22%2C%22phone%22%3A%2214430036003%22%2C%22province%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%22%2C%22provinceCode%22%3A%22110000%22%2C%22salesmanId%22%3A%22s1520841050603Sbb9ed6f5-91f5-4989-b14b-3aeafd7031fc%22%2C%22spraying_time%22%3A%222018-07-22%20%20%E8%87%B32018-07-25%20%22%2C%22teleAddress%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E6%9C%9B%E4%BA%AC%E8%A1%97%E9%81%93%E4%BC%8A%E9%A1%BF%E6%85%A7%E6%99%BA%E5%8F%8C%E8%AF%AD%E5%B9%BC%E5%84%BF%E5%9B%AD%E5%8C%97%E4%BA%AC%E5%AE%9D%E6%98%9F%E6%A0%A1%E5%9B%AD%22%2C%22transitionsNumber%22%3A%220%22%2C%22type%22%3A%221%22%2C%22unit_price%22%3A%2210.0%22%2C%22userType%22%3A%220%22%2C%22weatherId%22%3A%2232e4cc07-f79a-4add-ac3e-56469992514a%22%7D"
# ------------------------------ case: ----------------------
#1,正式，2演示，3测试 4长预约单
#formalType=1
ywb_formalType_list={
	"normal":"1","yanshi":"2","test":"3","longreserve":"4",
}
ywb_order_work_time={"spraying_time":"2018-08-01  至2018-08-01 ","days":"1",}

