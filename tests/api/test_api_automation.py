from conftest import api_request
from utils import readDatFromJson
from utils.email_automated_email import refresh_register_user_file
from utils.response_json_parser import parse_json_response


def test_register_user(api_request):
    refresh_register_user_file("data/test_register_user.json")
    test_data_register = readDatFromJson.read_json_file("data/test_register_user.json")
    response = api_request.post("register", data=test_data_register[0])
    print(response.status)
    register_json = parse_json_response(response, "Register")
    print(register_json)

    test_user = readDatFromJson.read_json_file("data/test_user_login.json")
    user_resp = api_request.post("login", data=test_user[0])
    print(user_resp.status)
    login_json = parse_json_response(user_resp, "Login")
    print(login_json)


def test_get_collections(api_request_without_content_type):
    response = api_request_without_content_type.get("collections/products/objects")
    print(response.status)
    json_data = parse_json_response(response, "Get Collections")
    print(json_data)
    products_list = []
    for x in json_data:
        count = 0
        if x["name"] not in products_list:
            products_list.append(x["name"])
            for y in json_data:
                if x["name"] == y["name"]:
                    count += 1
            print(f"Value: {x['name']} - Count: {count}")

# collectionstype = readDatFromJson.read_json_file("data/test_data_collections.json")
# //Storing the type of collections in a list
# for collection in collectionstype:
#     collection_type = collection.get("type")
#     if collection_type:
#         print(f"Collection Type: {collection_type}")
#     else:
#         print("Collection Type not found.")

def test_post_collections(api_request):
    test_data_collections = readDatFromJson.read_json_file("data/test_data_collections.json")
    for i in range(len(test_data_collections)):
        collection_type = test_data_collections[i].get("type")
        response = api_request.post(f"collections/{collection_type}/objects", data=test_data_collections[i])
        print(response.status)
        collection_json = parse_json_response(response, f"Post Collections {i + 1}")
        print(collection_json)
        print(f"Collection Type: {collection_type}")

# //Getting the count of each collection type and printing the count of each collection type

    count = sum(1 for x in test_data_collections if x.get("type") == collection_type)
    print(f"Count of Collection Type '{collection_type}': {count}")




# def test_post_collections_withnames(Collectionname, api_request_without_content_type):
#     response = api_request.get("collections/{Collectionname}/objects", data={"name": "Test Product", "description": "This is a test product."})
#     print(response.status)
#     collection_json = parse_json_response(response, "Get Collections By Name")
#     print(collection_json)


