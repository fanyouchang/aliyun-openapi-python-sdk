# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkvpc.endpoint import endpoint_data

class CreateExpressCloudConnectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateExpressCloudConnection','vpc')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PortType(self):
		return self.get_query_params().get('PortType')

	def set_PortType(self,PortType):
		self.add_query_param('PortType',PortType)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_RedundantEccId(self):
		return self.get_query_params().get('RedundantEccId')

	def set_RedundantEccId(self,RedundantEccId):
		self.add_query_param('RedundantEccId',RedundantEccId)

	def get_PeerLocation(self):
		return self.get_query_params().get('PeerLocation')

	def set_PeerLocation(self,PeerLocation):
		self.add_query_param('PeerLocation',PeerLocation)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_Bandwidth(self):
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self,Bandwidth):
		self.add_query_param('Bandwidth',Bandwidth)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_PeerCity(self):
		return self.get_query_params().get('PeerCity')

	def set_PeerCity(self,PeerCity):
		self.add_query_param('PeerCity',PeerCity)

	def get_IDCardNo(self):
		return self.get_query_params().get('IDCardNo')

	def set_IDCardNo(self,IDCardNo):
		self.add_query_param('IDCardNo',IDCardNo)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ContactMail(self):
		return self.get_query_params().get('ContactMail')

	def set_ContactMail(self,ContactMail):
		self.add_query_param('ContactMail',ContactMail)

	def get_ContactTel(self):
		return self.get_query_params().get('ContactTel')

	def set_ContactTel(self,ContactTel):
		self.add_query_param('ContactTel',ContactTel)

	def get_IdcSP(self):
		return self.get_query_params().get('IdcSP')

	def set_IdcSP(self,IdcSP):
		self.add_query_param('IdcSP',IdcSP)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)