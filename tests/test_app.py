import os
import sys
import io
import pytest

# Add the project root to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index page"""
    rv = client.get('/')
    assert rv.status_code == 200

def test_upload(client):
    """Test file upload"""
    data = {
        'docxFile': (io.BytesIO(b'Test file content'), 'book1.docx')
    }
    rv = client.post('/', data=data, follow_redirects=True)
    assert rv.status_code == 200
