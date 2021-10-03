from pathlib import Path

from project.app import app, init_db

# Index test
def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text") # Get root url
 
    # Check that we get status code 200 back
    assert response.status_code == 200 # 
    # Check that the result is "Hello, World"
    assert response.data == b"Hello, World!"

def test_database():
    init_db()
    assert Path("flaskr.db").is_file()