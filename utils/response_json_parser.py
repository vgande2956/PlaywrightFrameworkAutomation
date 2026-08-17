def parse_json_response(response, request_name):
    """Parse the response body as JSON only for success responses.

    If the API returns a non-JSON body such as a rate-limit error, this function
    raises a clear assertion instead of crashing with JSONDecodeError.
    """
    if response.status not in (200, 201):
        raise AssertionError(f"{request_name} failed with status {response.status}: {response.text()}")

    return response.json()
