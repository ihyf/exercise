# -*— coding:utf-8 -*-
from xml.etree import ElementTree
str = """<xml><appid><![CDATA[wx75f891b249a24ff9]]></appid>
<attach><![CDATA[1]]></attach>
<bank_type><![CDATA[CFT]]></bank_type>
<cash_fee><![CDATA[1]]></cash_fee>
<fee_type><![CDATA[CNY]]></fee_type>
<is_subscribe><![CDATA[N]]></is_subscribe>
<mch_id><![CDATA[1358277702]]></mch_id>
<nonce_str><![CDATA[whGBPCsYKgpmio0lsSZqtdmpHAoKB6Y0]]></nonce_str>
<openid><![CDATA[oIC3hvhvMPXjRBYNgc1mB-ah1-8U]]></openid>
<out_trade_no><![CDATA[322-2553e211232232]]></out_trade_no>
<result_code><![CDATA[SUCCESS]]></result_code>
<return_code><![CDATA[SUCCESS]]></return_code>
<sign><![CDATA[B498418F22A8DF8B61B1288B0BA44580]]></sign>
<time_end><![CDATA[20161208142026]]></time_end>
<total_fee>1</total_fee>
<trade_type><![CDATA[NATIVE]]></trade_type>
<transaction_id><![CDATA[4005992001201612082157476933]]></transaction_id>
</xml>"""


"""将xml转为dict"""
array_data = {}
root = ElementTree.fromstring(str)
for child in root:
    value = child.text
    array_data[child.tag] = value
print array_data
