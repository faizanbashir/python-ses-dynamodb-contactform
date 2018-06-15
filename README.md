# Python SES DynamoDB Contact Form

[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT)

AWS SES DYNAMODB tutorial using Serverless Framework written in Python

## Application Architecture
[![Serverless Application Architecture](architecture.png)]

## Serverless Framework Setup
| **Command** |**Description**|
|-------|------|
| `npm install -g serverless` | Install Serverless CLI  |
| `npm install` | Install Serverless dependencies  |
| Set up an AWS account with admin permissions | [Documentation](https://serverless.com/framework/docs/providers/aws/guide/credentials/)  |

## How to Deploy
```
$ git clone https://github.com/faizanbashir/python-ses-dynamodb-contactform.git
$ cd python-ses-dynamodb-contactform
$ npm install
$ sls deploy -v
```

## Service Endpoints
The service exposes 2 REST API endpoints:

| **Endpoint** |**Description**|**Parameters**|
|-------|------|------|
| `POST /sendMail` | Submit the data from contact form  | `{"firstname": "John", "lastname": "Doe", "email": "john@doe.com", "message": "Hi there"}` |
| `GET /list` | Retrieves all the contact form submissions | - |

## Invocation
	curl ---header "Content-Type: application/json" \
        --request POST \
        --data '{"firstname": "John", "lastname": "Doe", "email": "john@doe.com", "message": "Hi there"}'\
        <host>/sendMail
	curl <host>/list

# `sls` or `serverless` CLI Usage

### `deploy function` command
Deploy only one function:

	sls deploy function -f <function-name> -v

### `invoke` command
Run a specific function with a provided input and get the logs

	sls invoke -f <function-name> -p event.json -l
Run a specific function without input and get the logs

	sls invoke -f <function-name> -l

### `logs` command
Tail the logs of a function:

	sls logs -f <function-name> -t

### `info` command
Information about the service (stage, region, endpoints, functions):

	sls info

### `help` command
Just use it on anything:

	sls  help
or

	sls <command> --help