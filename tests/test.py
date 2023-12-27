import extract
from unittest.mock import Mock, patch
import requests

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, content, status_code):
            self.content = content
            self.status_code = status_code

        def raise_for_status(self):
            if self.status_code != 200:
                raise requests.exceptions.HTTPError

    if args[0] == "https://tonestro.com/":
        return MockResponse(b"<p>Learn to play instruments with tonestro</p>", 200)
    elif args[0] == "https://sendtrumpet.com/":
        return MockResponse(b"<p>LOVED BY SALES, CUSTOMER SUCCESS & MARKETING TEAMS.</p>", 200)
    elif args[0] == "https://www.prewave.com/":
        return MockResponse(b"<p>Not AI Risk and Sustainability Monitoring</p>", 404)

    return MockResponse(None, 404)




