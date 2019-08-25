import json
from mock import patch
from app.models import Orders

def get_orders():
    with open('tests/fixtures/orders.json', 'r') as json_file:
        return json.loads(json_file.read())

ORDERS = get_orders()

@patch("app.models.connection.Manager.execute")
def test_get_order(mock_execute_query):
    instance = Orders()
    response = instance.get_order()

    assert response == {}
    mock_execute_query.assert_not_called()

@patch("app.models.connection.Manager.execute", return_value=[ORDERS[1]])
def test_get_order(mock_execute_query):
    instance = Orders()

    order_id = 1
    response = instance.get_order(order_id)

    called_query = "SELECT * FROM orders WHERE `id` = '{}'".format(order_id)
    mock_execute_query.assert_called_once_with(called_query)
    assert response == ORDERS[1]