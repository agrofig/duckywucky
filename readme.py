from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    if "<iframe" in flow.response.text:
        print(f"Blocked iframe in: {flow.request.pretty_url}")
        flow.response.text = "Blocked by Securly"
