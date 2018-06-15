# Python SES DynamoDB Contact Form

[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)

AWS SES DYNAMODB tutorial using Serverless Framework written in Python

## How to Deploy

```
$ git clone https://github.com/faizanbashir/python-ses-dynamodb-contactform.git
$ cd python-ses-dynamodb-contactform
$ npm install
$ sls deploy -v
```

## How to Use
The service exposes 2 REST API endpoints:

| **Endpoint** |**Description**|**Parameters**|
|-------|------|------|
| `POST /sendMail` | Submit the data from contact form  | `{"firstname": "John", "lastname": "Doe", "email": "john@doe.com", "message": "Hi there"}` |
| `GET /list` | Retrieves all the contact form submissions | - |

# Usage
## Setup
| **Step** | **Command** |**Description**|
|---|-------|------|
|  1. | `npm install -g serverless` | Install Serverless CLI  |
|  2. | `npm install` | Install Serverless dependencies  |
|  3. | Set up an AWS account with admin permissions | [Documentation](https://serverless.com/framework/docs/providers/aws/guide/credentials/)  |

## Deployment

	sls deploy -v

### Invocation

	curl ---header "Content-Type: application/json" \
        --request POST \
        --data '{"firstname": "John", "lastname": "Doe", "email": "john@doe.com", "message": "Hi there"}'\
        <host>/sendMail
	curl <host>/list

# Tips & Tricks

### `help` command
Just use it on anything:

	sls  help
or

	sls <command> --help

### `deploy function` command
Deploy only one function:

	sls deploy function -f <function-name> -v

### `logs` command
Tail the logs of a function:

	sls logs -f <function-name> -t

### `info` command
Information about the service (stage, region, endpoints, functions):

	sls info

### `invoke` command
Run a specific function with a provided input and get the logs

	sls invoke -f <function-name> -p event.json -l
Run a specific function without input and get the logs
	sls invoke -f <function-name> -l