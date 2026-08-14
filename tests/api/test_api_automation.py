from utils import readDatFromJson

def test_register_user(api_request):
    test_data_register = readDatFromJson.read_json_file("data/test_register_user.json")
    response = api_request.post("register", data=test_data_register[0])
    print(response.status)
    test_user = readDatFromJson.read_json_file("data/test_user_login.json")
    user_resp = api_request.post("login", data=test_user[0])
    print(user_resp.status)
    print(user_resp.json())
