import json
import re
from typing import Any, Dict, List, Optional

import httpx

from dify_plugin.errors.tool import ToolProviderCredentialValidationError


def auth(credentials):
    app_key = credentials.get("app_key")
    app_secret = credentials.get("app_secret")
    if not app_key or not app_secret:
        raise ToolProviderCredentialValidationError("Client ID and Client Secret is required")
    try:
        assert DingTalkRequest(app_key, app_secret).access_token is not None
    except Exception as e:
        raise ToolProviderCredentialValidationError(str(e))
  

class DingTalkRequest:
    """钉钉API请求工具类"""
    
    def __init__(self, app_key: str, app_secret: str, operator_id: str = ''):
        self.app_key = app_key
        self.app_secret = app_secret
        self.operator_id = operator_id
        self._access_token = None
    
    @property
    def access_token(self):
        """获取访问令牌"""
        if not self._access_token:
            res = self.get_access_token(self.app_key, self.app_secret)
            self._access_token = res.get("accessToken")
        return self._access_token
    
    def _send_request(
        self,
        url: str,
        method: str = "POST",
        require_token: bool = True,
        payload: Optional[dict] = None,
        params: Optional[dict] = None,
    ):
        """发送HTTP请求"""
        headers = {
            "Content-Type": "application/json",
            "user-agent": "Dify",
        }
        if require_token:
            headers["x-acs-dingtalk-access-token"] = f"{self.access_token}"
        
        try:
            response = httpx.request(
                method=method, 
                url=url, 
                headers=headers, 
                json=payload, 
                params=params, 
                timeout=30
            )
            response.raise_for_status()
            res = response.json()
            
            # 钉钉API返回格式检查
            if "code" in res and res["code"] != 0:
                raise Exception(f"API error: {res}")
                
            return res
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            raise Exception(f"Request error: {str(e)}")
    
    def get_access_token(self, app_key: str, app_secret: str) -> dict:
        """
        获取钉钉访问令牌
        文档: https://open.dingtalk.com/document/orgapp-server/obtain-orgapp-token
        """
        url = "https://api.dingtalk.com/v1.0/oauth2/accessToken"
        payload = {
            "appKey": app_key,
            "appSecret": app_secret
        }
        return self._send_request(url, require_token=False, payload=payload)
    
    # AI表格 API - 数据表操作
    def create_sheet(self, base_id: str, name: str, fields: List[Dict[str, Any]] = None) -> dict:
        """
        创建数据表
        文档: https://open.dingtalk.com/document/orgapp/api-createsheet
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets"
        payload = {
            "name": name
        }
        if fields:
            payload["fields"] = fields
            
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, payload=payload, params=params)
    
    def get_all_sheets(self, base_id: str) -> dict:
        """
        获取所有数据表
        文档: https://open.dingtalk.com/document/orgapp/api-notable-getallsheets
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets"
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, method="GET", params=params)
    
    def get_sheet(self, base_id: str, sheet_id: str) -> dict:
        """
        获取数据表信息
        文档: https://open.dingtalk.com/document/orgapp/api-notable-getsheet
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets/{sheet_id}"
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, method="GET", params=params)
    
    def update_sheet(self, base_id: str, sheet_id_or_name: str, name: str) -> dict:
        """
        更新数据表
        文档: https://open.dingtalk.com/document/orgapp/api-noatable-updatesheet
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets/{sheet_id_or_name}"
        payload = {
            "name": name
        }
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, method="PUT", payload=payload, params=params)
    
    def delete_sheet(self, base_id: str, sheet_id_or_name: str) -> dict:
        """
        删除数据表
        文档: https://open.dingtalk.com/document/orgapp/api-noatable-deletesheet
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets/{sheet_id_or_name}"
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, method="DELETE", params=params)
    
    # AI表格 API - 字段操作
    def create_field(self, base_id: str, sheet_id_or_name: str, name: str, field_type: str, property: Dict[str, Any] = None) -> dict:
        """
        新增字段
        文档: https://open.dingtalk.com/document/orgapp/api-noatable-createfield
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets/{sheet_id_or_name}/fields"
        payload = {
            "name": name,
            "type": field_type
        }
        if property:
            payload["property"] = property
            
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, payload=payload, params=params)
    
    def get_all_fields(self, base_id: str, sheet_id_or_name: str) -> dict:
        """
        获取所有字段
        文档: https://open.dingtalk.com/document/orgapp/api-noatable-getallfields
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets/{sheet_id_or_name}/fields"
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, method="GET", params=params)
    
    def update_field(self, base_id: str, sheet_id_or_name: str, field_id_or_name: str, name: str = None, property: Dict[str, Any] = None) -> dict:
        """
        更新字段
        文档: https://open.dingtalk.com/document/orgapp/api-noatable-updatefield
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets/{sheet_id_or_name}/fields/{field_id_or_name}"
        payload = {}
        if name:
            payload["name"] = name
        if property:
            payload["property"] = property
            
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, method="PUT", payload=payload, params=params)
    
    def delete_field(self, base_id: str, sheet_id_or_name: str, field_id_or_name: str) -> dict:
        """
        删除字段
        文档: https://open.dingtalk.com/document/orgapp/api-noatable-deletefield
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets/{sheet_id_or_name}/fields/{field_id_or_name}"
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, method="DELETE", params=params)
    
    # AI表格 API - 记录操作
    def insert_records(self, base_id: str, sheet_id_or_name: str, records: List[Dict[str, Any]]) -> dict:
        """
        新增多行记录
        文档: https://open.dingtalk.com/document/orgapp/api-notable-insertrecords
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets/{sheet_id_or_name}/records"
        payload = {
            "records": records
        }
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, payload=payload, params=params)
    
    def list_records(self, base_id: str, sheet_id_or_name: str, max_results: int = 100, next_token: str = None, filter: dict = None) -> dict:
        """
        列出多行记录
        文档: https://open.dingtalk.com/document/orgapp/api-notable-listrecords
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets/{sheet_id_or_name}/records/list"
        payload = {
            "maxResults": max_results
        }
        if next_token:
            payload["nextToken"] = next_token
        if filter:
            payload["filter"] = filter
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, payload=payload, params=params)
    
    def get_record(self, base_id: str, sheet_id_or_name: str, record_id: str) -> dict:
        """
        获取记录
        文档: https://open.dingtalk.com/document/orgapp/api-getrecord
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets/{sheet_id_or_name}/records/{record_id}"
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, method="GET", params=params)
    
    def update_records(self, base_id: str, sheet_id_or_name: str, records: List[Dict[str, Any]]) -> dict:
        """
        更新多行记录
        文档: https://open.dingtalk.com/document/orgapp/api-noatable-updaterecords
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets/{sheet_id_or_name}/records"
        payload = {
            "records": records
        }
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, method="PUT", payload=payload, params=params)
    
    def delete_records(self, base_id: str, sheet_id_or_name: str, record_ids: List[str]) -> dict:
        """
        删除多条记录
        文档: https://open.dingtalk.com/document/orgapp/api-noatable-deleterecords
        """
        url = f"https://api.dingtalk.com/v1.0/notable/bases/{base_id}/sheets/{sheet_id_or_name}/records/delete"
        payload = {
            "recordIds": record_ids
        }
        params = {
            "operatorId": self.operator_id
        }
        return self._send_request(url, payload=payload, params=params)
    
    def get_user_info(self, user_id: str) -> dict:
        """
        获取用户信息
        文档: https://open.dingtalk.com/document/orgapp/query-user-details
        """
        url = f"https://oapi.dingtalk.com/topapi/v2/user/get"
        params = {
            "access_token": self.access_token
        }
        payload = {
            "userid": user_id
        }
        return self._send_request(url, method="POST", params=params, payload=payload)

    def get_user_id_by_mobile(self, mobile: str) -> Optional[str]:
        """
        通过手机号获取用户ID
        文档: https://open.dingtalk.com/document/orgapp/query-users-by-phone-number
        
        Args:
            mobile: 用户手机号
            
        Returns:
            用户ID，如果未找到则返回None
        """
        url = f"https://oapi.dingtalk.com/topapi/v2/user/getbymobile"
        params = {
            "access_token": self.access_token
        }
        payload = {
            "mobile": mobile
        }
        try:
            print(self.access_token)
            response = self._send_request(url, method="POST", params=params, payload=payload)
            print(response)
            return response.get("result", {}).get("userid")
        except Exception:
            return None
    