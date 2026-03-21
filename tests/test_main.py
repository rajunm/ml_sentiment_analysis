import pytest 
from main import app 

@pytest.fixture
def client():
    # Set up the Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_endpoint_types(client):
    # Test with a valid input value
    response = client.post('/predict', json={'text': 'I am having a good day!'})
    output_data = response.get_json()

    assert response.status_code == 200
    assert isinstance(output_data['label'], str)
    assert isinstance(output_data['score'], float)
    assert output_data['label'] in ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"]
    assert 0.0 <= output_data['score'] <= 1.0


def test_predict_endpoint_empty_input(client):
    # Test with an empty input value
    response = client.post('/predict', json={'text': ''})
    output_data = response.get_json()

    assert response.status_code == 400
    assert 'error' in output_data
