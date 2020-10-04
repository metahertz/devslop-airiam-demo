import json
import os

def test(event, context):
    retVal = {
        "devices": [{
            "deviceLastIp": "192.168.0.193",
	    "welcomeToThe": "Function",
	    "weveGotFunAnd": "games",
            "hello": "world",
	    "some": "important-data"
        },
        {
            "deviceLastIp": "192.168.0.191",
            "so": "wow",
	    "much": "test"
    }]},
    response = {
        "statusCode": 200,
        'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Headers': '*'
        },
        "body": json.dumps(retVal)
    }
    return response

