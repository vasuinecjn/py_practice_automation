import json


def generate_har_file(driver, har_file_path):
    har_data = {
        "log": {
            "version": "1.2",
            "creator": {
                "name": "Selenium Wire",
                "version": "4.6.0"
            },
            "entries": []
        }
    }
    for request in driver.requests:
        if request.response:
            entry = {
                "startedDateTime": request.date.isoformat(),
                "time": (request.response.date - request.date).microseconds / 1000,
                "request": {
                    "method": request.method,
                    "url": request.url,
                    "httpVersion": "HTTP/1.1",
                    "headers": [{"name": k, "value": v} for k, v in request.headers.items()],
                    "queryString": [{"name": k, "value": v} for k, v in request.params.items()],
                    "headersSize": -1,
                    "bodySize": -1
                },
                "response": {
                    "status": request.response.status_code,
                    "statusText": request.response.reason,
                    "httpVersion": "HTTP/1.1",
                    "headers": [{"name": k, "value": v} for k, v in request.response.headers.items()],
                    "content": {
                        "size": len(request.response.body),
                        "mimeType": request.response.headers.get("Content-Type", "")
                    },
                    "redirectURL": "",
                    "headersSize": -1,
                    "bodySize": -1
                },
                "cache": {},
                "timings": {
                    "send": 0,
                    "wait": 0,
                    "receive": 0
                }
            }
            har_data["log"]["entries"].append(entry)

    # Write HAR data to a file
    with open(har_file_path, 'w') as har_file:
        json.dump(har_data, har_file, indent=4)