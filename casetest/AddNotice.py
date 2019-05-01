import unittest
# from RunMainTest import RunMainTest
# from mock import mock
import json
import requests

class AddNotice(unittest.TestCase):
	def setUp(self):
		pass
	
	def tearDown(self):
		pass
		
	def test_success(self):
		url = 'http://test.admin-purchase-platform.lvyuetravel.com/mng/api/pimp/platform/notice/add.json'
		headers = {'Cookie':'ly_admin_token=ea384c808d45e0847b777c34534313e99704122eb81c394ee7b523c956e7d0d2198c1818b0023e7fcd0d3cd0f81a6cbae0f0d81d69d8802312dac617bb5e6f67'}
		data = {'titleName':'标题','noticeTypeName':'业务通知','importantTypeName':'紧急','status':'1','noticeContent':'内容','objectTypeName':'供应商','noticeTypeId':'2','importantTypeId':'1','busiSystem':'pimp'}
		# mock_data = mock.Mock(return_value=data)
		res = requests.post(url,data=data,headers=headers)
		print(res)
		
		#data = {'titleName':'标题','noticeTypeName':'业务通知','importantTypeName':'紧急','status':'1','noticeContent':'内容','objectTypeName':'供应商','noticeTypeId':'2','importantTypeId':'1','busiSystem':'pimp'}
		#self.run.run_main = mock.Mock(return_value=data)
		#res = self.run.run_main(self.url,'POST',self.headers)
		#print(res)
		
if __name__ == '__main__':
	unittest.main()