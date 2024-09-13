import pytest
from unittest.mock import patch
from pyparam import Client
import uuid


@pytest.fixture
def client():
    API_URL = "https://test-dmz.param.com.tr/turkpos.ws/service_turkpos_test.asmx?wsdl"
    CLIENT_CODE = "10738"
    CLIENT_USERNAME = "Test"
    CLIENT_PASSWORD = "Test"
    return Client(api_url=API_URL, client_code=CLIENT_CODE, client_username=CLIENT_USERNAME,
                  client_password=CLIENT_PASSWORD)


def generate_random_reference_id():
    return str(uuid.uuid4())


@patch('param.client.zeep.Client.service.TP_WMD_UCD')
def test_pos_ns(mock_service, client):
    mock_service.return_value = {'Sonuc': 1}

    res = client.pos(
        merchant_guid="0c13d406-873b-403b-9c09-a5766840d98c",
        card_holder="test",
        card_number="4446763125813623",
        card_expiration_month="12",
        card_expiration_year="2026",
        card_cvc="000",
        customer_gsm="5551231212",
        fail_url="http://localhost:8000/error",
        success_url="http://localhost:8000/success",
        reference_id=generate_random_reference_id(),
        description="Test Order",
        installment="1",
        amount="100,00",
        total_amount="100,00",
        ip_address="127.0.0.1",
        ref_url="http://localhost:8000/ref",
        data1="a",
        data2="a",
        data3="a",
        data4="a",
        data5="a",
        order_id="123456",
        is_3d=False
    )

    assert res['Sonuc'] > 0
    mock_service.assert_called_once()


@patch('param.client.zeep.Client.service.TP_WMD_UCD')
def test_pos_3d(mock_service, client):
    mock_service.return_value = {'Sonuc': 1}

    res = client.pos(
        merchant_guid="0c13d406-873b-403b-9c09-a5766840d98c",
        card_holder="test",
        card_number="4446763125813623",
        card_expiration_month="12",
        card_expiration_year="2026",
        card_cvc="000",
        customer_gsm="5551231212",
        fail_url="http://localhost:8000/error",
        success_url="http://localhost:8000/success",
        reference_id=generate_random_reference_id(),
        description="Test Order",
        installment="1",
        amount="100,00",
        total_amount="100,00",
        ip_address="127.0.0.1",
        ref_url="http://localhost:8000/ref",
        data1="a",
        data2="a",
        data3="a",
        data4="a",
        data5="a",
        order_id="123456",
        is_3d=True
    )

    assert res['Sonuc'] > 0
    mock_service.assert_called_once()
