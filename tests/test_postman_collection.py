import json
import pytest


def load_collection():
    with open('postman_collection.json') as f:
        collection = json.load(f)
    return collection['item']


@pytest.mark.parametrize('item', load_collection())
def test_collection_requests(client, item):
    req = item['request']
    method = req['method'].lower()
    raw_url = req['url']['raw']
    path = raw_url.replace('{{base_url}}', '')
    headers = {h['key']: h['value'] for h in req.get('header', [])}
    data = None
    if req.get('body') and req['body'].get('raw'):
        data = req['body']['raw']
    response = client.open(path, method=method, headers=headers, data=data)
    assert response.status_code == 200
    if path == '/ping':
        assert response.get_json() == {'message': 'pong'}
    elif path == '/login':
        assert response.get_json() == {'status': 'success'}
