from flask import Response
from flask import request
from flask import current_app
import json
import requests


def main():
    msg = "---HEADERS---\n%s\n--BODY--\n%s\n-----\n" % (request.headers, request.get_data())
    current_app.logger.info("Received request: %s" % msg)

    request_json = request.get_json()
    user_name = request_json["result"]["parameters"]["any"]
    current_app.logger.info("username : %s" % user_name)

    content = requests.get("https://api.github.com/repos/fission/fission/issues")
    #current_app.logger.info(content.json())

    # response = json.dumps({
    #     "speech": "Sorry I'm Work In Progress",
    #     "displayText": "Sorry I'm Work In Progress",
    #     "data": {
    #         "google": {
    #             "expect_user_response": False,
    #             "is_ssml": False,
    #         }
    #     }
    # })
    json_obj = {}
    final_response = []
    response_json = content.json()
    for item in response_json:
        current_app.logger.info("login : %s" %item["user"]["login"])
        if item["user"]["login"] == user_name:
            current_app.logger.info("appending json obj")
            final_response.append("%s (%s)" % (item["number"], item["title"][:35]))
    json_obj["response"] = final_response

    # response = json.dumps(json_obj)
    response = json.dumps({
        #"speech": json.dumps(json_obj),
        "speech": ";".join(json_obj["response"]),
        # "messages": [
        #     { "speech": "test1", "type": 0},
        #     {"speech": "test2", "type": 0},
        #     {"speech": "test3", "type": 0},
        # ],
        "displayText": "I'm Work In Progress",
        "data": {
            "google": {
                "expect_user_response": False,
                "is_ssml": False,
            }
        }
    })

    #current_app.logger.info("resp: %s" % response)

    return response, 200, {'Content-Type': 'application/json; charset=utf-8'}