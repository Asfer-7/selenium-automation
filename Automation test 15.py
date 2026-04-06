import pytest
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://jsonplaceholder.typicode.com/"

#GET requests

def test_get_all_posts():
    """GET all posts should return 200 and 100 items"""
    response = requests.get(f"{BASE_URL}/posts", verify=False)
    assert response.status_code == 200
    data = response.json()
    assert len(data)==100
    print(f"\n Total posts returned: {len(data)}")

def test_get_single_post():
    """GET a single post should return correct data"""
    response = requests.get(f"{BASE_URL}/posts/1", verify=False)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    print(f"\n Post title: {data['title']}")

def test_get_post_not_found():
    """GET a non-existent post should return 404"""
    response = requests.get(f"{BASE_URL}/post/9999", verify=False)
    assert response.status_code ==404
    print(f"\n Status code for missing post: {response.status_code}")

def test_get_comments_for_post():
    """GET comments for a specific post"""
    response = requests.get(f"{BASE_URL}/posts/1/comments", verify=False)
    assert response.status_code ==200
    data = response.json()
    assert len(data)>0
    assert "email" in data[0]
    print(f"\n Comments returned: {len(data)}")

#POST requests (creating data)

def test_create_post():
    """POST a new post should return 201 and the created data"""
    payload = {"title": "Automation test post", "body" : "this post was created by selenium automation testing", "userId":1}
    response = requests.post(f"{BASE_URL}/posts", json=payload,verify=False)
    assert response.status_code==201
    data=response.json()
    assert data["title"]=="Automation test post"
    assert "id"in data
    print(f"\n Created post ID: {data['id']}")

def test_create_post_missing_fields():
    """POST with empty body should still return 201 form this API"""
    response = requests.post(f"{BASE_URL}/posts", json={},verify=False)
    assert response.status_code==201
    print(f"\n empty post response status: {response.status_code}")

# PUT requests (updating data)

def test_update_post():
    """PUt should update an existing post and return updated data"""
    payload = {"id":1,"title":"Updated title", "body":"updated body content","userID":1}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload,verify=False)
    assert response.status_code==200
    data=response.json()
    assert data["title"]=="Updated title"
    print(f"\n Updated title: {data['title']}")

#DELETE requests (deleting data)

def test_delete_post():
    """DELETE should remove a post and return 200"""
    response=requests.delete(f"{BASE_URL}/posts/1",verify=False)
    assert response.status_code==200
    print(f"\n Delete status code:{response.status_code}")

# Response validation

def test_response_time():
    """Response time should be under 3 seconds"""
    response=requests.get(f"{BASE_URL}/posts/1",verify=False)
    assert response.elapsed.total_seconds()<3
    print(f"\n Response time: {response.elapsed.total_seconds():2f}s")

def test_response_headers():
    """Response headers should return JSON content type"""
    response=requests.get(f"{BASE_URL}/posts/1",verify=False)
    assert "application/json" in response.headers["Content-Type"]
    print(f"\n Content-type: {response.headers['Content-Type']}")
