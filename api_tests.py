import pycurl
from io import BytesIO
import json


def test_api(endpoint, expected_status, key_elements):
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, endpoint)

    buffer = BytesIO()
    curl.setopt(pycurl.WRITEDATA, buffer)

    curl.perform()

    status_code = curl.getinfo(pycurl.RESPONSE_CODE)
    curl.close()

    if status_code != expected_status:
        return f"Test {endpoint}: FAILED (Status code: {status_code})"

    response_data = buffer.getvalue().decode('utf-8')
    data = json.loads(response_data)

    for element in key_elements:
        if element not in data:
            return f"Test {endpoint}: FAILED (Missing key: {key})"
    return f"Test {endpoint}: PASSED"


def main():
    tests = [
        {"endpoint": "https://jsonplaceholder.typicode.com/posts/1", "expected_status": 200,
         "key_elements": ["userId", "id", "title", "body"]},
        {"endpoint": "https://jsonplaceholder.typicode.com/users/1", "expected_status": 200,
         "key_elements": ["id", "name", "username", "email", "address"]},
        {"endpoint": "https://jsonplaceholder.typicode.com/comments/1", "expected_status": 200,
         "key_elements": ["postId", "id", "name", "email", "body"]},
    ]

    for test in tests:
        result = test_api(**test)
        print(result)


if __name__ == "__main__":
    main()
