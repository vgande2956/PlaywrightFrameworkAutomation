from utils import readDatFromJson

def test_register_user(api_request):
    test_data_register = readDatFromJson.read_json_file("data/test_register_user.json")
    response = api_request.post("register", data=test_data_register[0])
    print(response.status)
    test_user = readDatFromJson.read_json_file("data/test_user_login.json")
    user_resp = api_request.post("login", data=test_user[0])
    print(user_resp.status)
    print(user_resp.json())

def test_get_collections(api_request_without_content_type):
    response = api_request_without_content_type.get("collections/products/objects")
    print(response.status)
    print(response.json())
    json_data = response.json()
    products_list = []
    for x in json_data:
        count = 0
        if x["name"] not in products_list:
            products_list.append(x["name"])
            for y in json_data:
                if x["name"] == y["name"]:
                    count += 1
            print(f"Value: {x['name']} - Count: {count}")

def test_post_collections(api_request):
    test_data_collections = readDatFromJson.read_json_file("data/test_data_collections.json")
    for i in range(len(test_data_collections)):
        response = api_request.post("collections/products/objects", data=test_data_collections[i])
        print(response.status)
        print(response.json())