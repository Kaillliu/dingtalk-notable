# DingTalk Spreadsheet Plugin Privacy Policy



## Introduction

The DingTalk Multi-dimensional (AI) Table Plugin is a set of tools for operating on AI tables (multi-dimensional tables) in DingTalk documents on the Dify platform. Through this plugin, you can read, write, and modify DingTalk AI tables on the Dify platform without manually opening DingTalk documents to complete data processing. This plugin supports CRUD operations on Sheets, Fields, and Records within AI tables.



## Information We Collect

When using the DingTalk Multi-dimensional (AI) Table Plugin, we do not collect any personal information. The plugin only processes data that you explicitly provide through the Dify platform interface. All data operations are performed through DingTalk's official API endpoints with proper authentication.



## User Permission Requirements

Using this plugin requires the following DingTalk permissions:


Configuration method: Log in to the DingTalk developer backend > Enterprise internal development > Find the application that needs to add permissions > Permission management > Address book management page, check enterprise employee phone number information and email and other personal information, click Apply for permission.


## Data Processing

This plugin operates on the following data structures within DingTalk AI tables:

- **Base**: AI table documents identified by `baseId`
- **Sheet**: Data tables within AI table documents
- **Field**: Columns in data tables (text, number, single select, multiple select, date, user, department, attachment, unidirectional link, bidirectional link, URL)
- **Record**: Rows in data tables

All data operations are performed through DingTalk's official API endpoints with proper access token authentication and operator identification.



## User Control

You can protect your data through the following methods:
1. Revoke the application's API permissions at any time through the DingTalk developer backend
2. Modify the application's permission scope in the DingTalk developer backend
3. Control data access through DingTalk's built-in permission management system
4. Monitor API usage and data access through DingTalk's developer console



## Security

- All API calls require proper authentication using DingTalk access tokens
- Data transmission is encrypted using HTTPS protocols
- The plugin does not store any data locally
- All operations are logged and can be audited through DingTalk's developer console



## Contact Us

If you have any questions or suggestions about this privacy policy, please contact us through the following methods:
- GitHub: https://github.com/Kaillliu/dify-plugins
- Email: kaillliu@163.com

**AI Table Reference Documentation**: https://open.dingtalk.com/document/orgapp/notable-data-structure

Last updated: July 18, 2025