# DingTalk AI Table Plugin



## Introduction

The DingTalk AI Table Plugin is a collection of tools for operating on AI tables (multi-dimensional tables) in DingTalk documents. Through this plugin, you can read, write, and modify DingTalk AI tables on the Dify platform without manually opening DingTalk documents to complete data processing. This plugin supports CRUD operations on Sheets, Fields, and Records within AI tables.



## Prerequisites

Using this plugin requires the following DingTalk permissions:
- **AI表格应用读权限** (AI Table Application Read Permission)
- **AI表格应用写权限** (AI Table Application Write Permission)
- **个人信息权限** (Personal Information Permission)
- **根据手机号获取成员基本信息权限** (Permission to obtain member basic information by phone number)

Configuration method: Log in to the DingTalk developer backend > Enterprise internal development > Find the application that needs to add permissions > Permission management > Address book management page, check enterprise employee phone number information and email and other personal information, click Apply for permission.

**AI Table Reference Documentation**: https://open.dingtalk.com/document/orgapp/notable-data-structure


## Credential Configuration

The following credentials need to be configured to use this plugin:
- `app_key`: The AppKey of the DingTalk application
- `app_secret`: The AppSecret of the DingTalk application



## Feature List

### 1. Get Operator ID (get_operator_id)
Get the DingTalk user's operator ID through their phone number or user ID.

**Parameters**:
- `user_id`: The user ID of the operator (optional, choose one between user_id and mobile)
- `mobile`: User's phone number, such as "+86 13800138000" (optional, choose one between user_id and mobile)

**Example**:
```python
# Get the DingTalk user's operator ID through their phone number
{
  "mobile": "+86 13800138000"
}
```
**Returns**:
- User's operator ID (unionId)



### 2. Create Sheet (create_sheet_ai)
Create a new data table in AI table.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `name`: The name of the sheet to be created
- `fields`: JSON array of field definitions (optional)

**Example**:
```python
# Create a new data table named "Sales Data"
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "name": "Sales Data",
  "fields": "[{\"name\":\"Field1\",\"type\":\"text\"},{\"name\":\"Field2\",\"type\":\"number\"}]"
}
```
**Returns**:
- JSON data of the creation result



### 3. Get All Sheets (get_all_sheets_ai)
Get all data tables in an AI table document.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)

**Example**:
```python
# Get all data tables in the AI table
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz"
}
```
**Returns**:
- JSON array of all data tables



### 4. Get Sheet (get_sheet_ai)
Get basic information about a specific data table.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `sheet_id_or_name`: The ID or name of the sheet

**Example**:
```python
# Get information about the data table named "Sales Data"
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "sheet_id_or_name": "Sales Data"
}
```
**Returns**:
- JSON data of data table information



### 5. Update Sheet (update_sheet_ai)
Update the name of a data table.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `sheet_id_or_name`: The ID or name of the sheet
- `name`: The new name of the sheet

**Example**:
```python
# Update the data table name
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "sheet_id_or_name": "Sales Data",
  "name": "Updated Sales Data"
}
```
**Returns**:
- JSON data of the update result



### 6. Delete Sheet (delete_sheet_ai)
Delete a data table.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `sheet_id_or_name`: The ID or name of the sheet

**Example**:
```python
# Delete the data table
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "sheet_id_or_name": "Sales Data"
}
```
**Returns**:
- JSON data of the deletion result



### 7. Create Field (create_field_ai)
Create a new field in a data table.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `sheet_id_or_name`: The ID or name of the sheet
- `name`: The name of the field
- `type`: The type of the field (text, number, singleSelect, multipleSelect, date, user, department, attachment, unidirectionalLink, bidirectionalLink, url)
- `property`: JSON object of field properties (optional)

**Example**:
```python
# Create a new text field
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "sheet_id_or_name": "Sales Data",
  "name": "Product Name",
  "type": "text"
}
```
**Returns**:
- JSON data of the field creation result



### 8. Get All Fields (get_all_fields_ai)
Get all fields in a data table.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `sheet_id_or_name`: The ID or name of the sheet

**Example**:
```python
# Get all fields in the data table
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "sheet_id_or_name": "Sales Data"
}
```
**Returns**:
- JSON array of all fields



### 9. Update Field (update_field_ai)
Update a field in a data table.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `sheet_id_or_name`: The ID or name of the sheet
- `field_id_or_name`: The ID or name of the field
- `name`: The new name of the field
- `property`: JSON object of field properties (optional)

**Example**:
```python
# Update the field name
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "sheet_id_or_name": "Sales Data",
  "field_id_or_name": "Product Name",
  "name": "Updated Product Name"
}
```
**Returns**:
- JSON data of the field update result



### 10. Delete Field (delete_field_ai)
Delete a field from a data table.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `sheet_id_or_name`: The ID or name of the sheet
- `field_id_or_name`: The ID or name of the field

**Example**:
```python
# Delete the field
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "sheet_id_or_name": "Sales Data",
  "field_id_or_name": "Product Name"
}
```
**Returns**:
- JSON data of the field deletion result



### 11. Insert Records (insert_records_ai)
Insert multiple records into a data table.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `sheet_id_or_name`: The ID or name of the sheet
- `records`: JSON array of records to insert

**Example**:
```python
# Insert multiple records
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "sheet_id_or_name": "Sales Data",
  "records": "[{\"fields\":{\"Product Name\":\"Product A\",\"Price\":100}},{\"fields\":{\"Product Name\":\"Product B\",\"Price\":200}}]"
}
```
**Returns**:
- JSON array of created record IDs



### 12. List Records (list_records_ai)
List records in a data table with optional filtering and pagination.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `sheet_id_or_name`: The ID or name of the sheet
- `filter`: Filter conditions for listing records (optional)
- `max_results`: Maximum number of records to return (default 100, max 100)
- `next_token`: Token for pagination (optional)

**Example**:
```python
# List records with filtering
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "sheet_id_or_name": "Sales Data",
  "filter": "{\"combination\":\"and\",\"conditions\":[{\"field\":\"Product Name\",\"operator\":\"equal\",\"value\":[\"Product A\"]}]}",
  "max_results": 50
}
```
**Returns**:
- JSON object with records array and pagination information



### 13. Get Record (get_record_ai)
Get a specific record by its ID.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `sheet_id_or_name`: The ID or name of the sheet
- `record_id`: The ID of the record

**Example**:
```python
# Get a specific record
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "sheet_id_or_name": "Sales Data",
  "record_id": "recG70uhxh"
}
```
**Returns**:
- JSON data of the record



### 14. Update Records (update_records_ai)
Update multiple records in a data table.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `sheet_id_or_name`: The ID or name of the sheet
- `records`: JSON array of records to update (must include record IDs)

**Example**:
```python
# Update multiple records
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "sheet_id_or_name": "Sales Data",
  "records": "[{\"id\":\"recG70uhxh\",\"fields\":{\"Product Name\":\"Updated Product A\",\"Price\":150}}]"
}
```
**Returns**:
- JSON array of updated record IDs



### 15. Delete Records (delete_records_ai)
Delete multiple records from a data table.

**Parameters**:
- `operator_id`: The unionId of the operator
- `base_id`: The ID of the AI Table (baseId)
- `sheet_id_or_name`: The ID or name of the sheet
- `record_ids`: JSON array of record IDs to delete

**Example**:
```python
# Delete multiple records
{
  "operator_id": "your_operator_id",
  "base_id": "jb9Y4gmKWr3DdqP5u3PMmjDLVGXn6lpz",
  "sheet_id_or_name": "Sales Data",
  "record_ids": "[\"recG70uhxh\",\"recG70uhxi\"]"
}
```
**Returns**:
- JSON data of the deletion result



## Supported Field Types

The plugin supports the following field types in AI tables:

- **text**: Text fields
- **number**: Numeric fields with various formatters (INT, FLOAT, THOUSAND, PRESENT, CNY, USD, etc.)
- **singleSelect**: Single selection fields with predefined choices
- **multipleSelect**: Multiple selection fields with predefined choices
- **date**: Date fields with various formatters (YYYY-MM-DD, YYYY/MM/DD, etc.)
- **user**: User fields supporting single or multiple selections
- **department**: Department fields supporting single or multiple selections
- **attachment**: File attachment fields
- **unidirectionalLink**: One-way link fields to other sheets
- **bidirectionalLink**: Two-way link fields to other sheets
- **url**: URL fields with text and link properties

## Contact Us
If you have any questions or suggestions about this, please contact us through the following methods:
- GitHub: https://github.com/Kaillliu/dify-plugins
- Email: kaillliu@163.com

**AI Table Reference Documentation**: https://open.dingtalk.com/document/orgapp/notable-data-structure