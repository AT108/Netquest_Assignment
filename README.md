# Netquest_Assignment

The Netquest_Assignment is the small service that is exposing the REST API that is giving the possibility to perform
the CRUD operations for the Name and Picture objects. The project contains the following methods:

- `POST` - /v1/api/create - allows the user to add new Name and Picture object
- `GET` - /v1/api - allows the user to display the html simple page presenting all the Name and Picture objects 
- `GET` - /v1/api/find-all - allows the user to display all the Name and Picture objects 
- `GET` - /v1/api/find-by-id/:id - allows the user to display Name and Picture object for given :id
- `PUT` - /v1/api/update/:id - allows the user to update Name and Picture object for given :id
- `DELETE` - /v1/api/delete/:id - - allows the user to delete Name and Picture object for given :id

The Name and Picture object schema is as follows:

```json
{
  "id": "097738ef-aa13-433d-8159-65fe8f29db54",
  "img": "Test 1 - test case object",
  "title": "Test 1 - test case object"
}
```

## Project Setup

To run application on docker please run the following commands:

```commandline
docker-compose up --build
```

To run without using docker 🐋 you need to set up a local database connection:

DB url
DB username
DB password

And create the DB DDL structure, for this, u can use the following SQL script:

```sql
create table NAME_AND_PICTURE (
	id varchar(36) primary key,
	title varchar(255) not null,
	img varchar(255) not null
);
```

Do remember to setup the connection string in the application code (`config.py`), accordingly 
to the database connection properties:

```python
'postgresql://postgres:admin123@localhost:5432/netquest_assignment'
```

## Postman Collection

Project could be opened with PyCharm IDEA. It's flask-based application that requires Python 🐍 3.8.

For testing the Postman, Rester or different REST Client could be used.

<details>
  <summary>🖱️ Click me - Postman Collection</summary>
  
  If you want to use the Postman collection, please save the following json as the file and import it into Postman.

  ```json
  {
	"info": {
		"_postman_id": "6a884326-7ede-4cfa-b071-e1af1510e3fa",
		"name": "Netquest Assignment",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "29982599"
	},
	"item": [
		{
			"name": "create",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"img\": \"test 1\",\n    \"title\": \"test 1\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://{{host}}:{{port}}/v1/api/create",
					"protocol": "http",
					"host": [
						"{{host}}"
					],
					"port": "{{port}}",
					"path": [
						"v1",
						"api",
						"create"
					]
				}
			},
			"response": []
		},
		{
			"name": "findAll",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://{{host}}:{{port}}/v1/api/find-all",
					"protocol": "http",
					"host": [
						"{{host}}"
					],
					"port": "{{port}}",
					"path": [
						"v1",
						"api",
						"find-all"
					]
				}
			},
			"response": []
		},
		{
			"name": "findById",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://{{host}}:{{port}}/v1/api/find-by-id/097738ef-aa13-433d-8159-65fe8f29db54",
					"protocol": "http",
					"host": [
						"{{host}}"
					],
					"port": "{{port}}",
					"path": [
						"v1",
						"api",
						"find-by-id",
						"097738ef-aa13-433d-8159-65fe8f29db54"
					]
				}
			},
			"response": []
		},
		{
			"name": "main",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://{{host}}:{{port}}/",
					"protocol": "http",
					"host": [
						"{{host}}"
					],
					"port": "{{port}}",
					"path": [
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "update",
			"request": {
				"method": "PUT",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"id\": \"4a7ac1fa-2ea6-4418-b22e-9ec2d3f7ae98\",\n    \"img\": \"test 1 - updated\",\n    \"title\": \"test 1 - updated\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://{{host}}:{{port}}/v1/api/update",
					"protocol": "http",
					"host": [
						"{{host}}"
					],
					"port": "{{port}}",
					"path": [
						"v1",
						"api",
						"update"
					]
				}
			},
			"response": []
		},
		{
			"name": "delete",
			"request": {
				"method": "DELETE",
				"header": [],
				"url": {
					"raw": "http://{{host}}:{{port}}/v1/api/delete-by-id/faba2c12-31f2-4570-a216-439405b71070",
					"protocol": "http",
					"host": [
						"{{host}}"
					],
					"port": "{{port}}",
					"path": [
						"v1",
						"api",
						"delete-by-id",
						"faba2c12-31f2-4570-a216-439405b71070"
					]
				}
			},
			"response": []
		}
	]
}
  ```
</details>

## Original Assignment Statement
### Introduction

The purpose of this assignment is to see how you would develop an API. You can do it in the 
language you choose. 

Regarding the code, you must develop, and do it like it was to be on production. Follow your 
own coding conventions but make it coherent through all the code you develop. Write clean, 
maintainable, quality code using all the components you need. Testing is required. 

### Assignment

Build a REST service with a CRUD design to create the following result when requesting a full 
list of records. 

The response of the list endpoint should be something like this: 

```js
[ 
   { 
      "title":"When dreams come true.", 
      "img":"https://i.imgur.com/HJhuWx8.mp4" 
   }, 
   { 
      "title":"This sweet lady was dumped at the lake today. Coldest day of the year.", 
      "img":"https://i.imgur.com/mV9vjmB.jpg" 
   }, 
   {...} # more items 
]
```

Nice to have but not required: 
- Think about implementing an authentication method for the API. 
- Dockerize the API, what does this means? Create an image that holds the API with all the 
libraries and dependencies installed and the API is running and accepting requests. 

# Contact Information

👨 Anastasia Tracewska

☎️ +48 518096899    

📫 tracewska@gmail.com