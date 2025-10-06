from Source.app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Welcome To Home Page!'
    
def test_about():
    response = app.test_client().get('/about')
    assert response.status_code == 200
    assert response.data == b'About Page'