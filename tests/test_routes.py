def test_report(client):
    response = client.get('/report/')
    assert response.status_code == 200
    assert b'Daniel Ricciardo' in response.data


def test_drivers(client):
    response = client.get('/report/drivers/')
    assert response.status_code == 200
    assert b'Daniel Ricciardo' in response.data


def test_get_driver(client):
    response = client.get('/report/drivers/?driver_id=SVF')
    assert response.status_code == 200
    assert b'Sebastian Vettel' in response.data


def test_api_xml(client):
    response = client.get('/api/v1/report/?format=xml')
    assert response.status_code == 200
    assert b'Sebastian Vettel' in response.data
    assert response.mimetype == "application/xml"


def test_api_json(client):
    response = client.get('/api/v1/report/?format=json')
    assert response.status_code == 200
    assert b'Sebastian Vettel' in response.data
    assert response.mimetype == "application/json"


def test_site_map(client):
    response = client.get('/site-map')
    assert response.status_code == 200
