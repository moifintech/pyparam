from pyparam import Client
import uuid
API_URL = "https://test-dmz.param.com.tr/turkpos.ws/service_turkpos_test.asmx?wsdl"
CLIENT_CODE = "10738"
GUID = "0c13d406-873b-403b-9c09-a5766840d98c"
CLIENT_USERNAME = "Test"
CLIENT_PASSWORD = "Test"

def generate_random_reference_id():
    return str(uuid.uuid4())

client = Client(api_url=API_URL, client_code=CLIENT_CODE, client_username=CLIENT_USERNAME,
                client_password=CLIENT_PASSWORD)


res_ns = client.pos_ns(
    merchant_guid=GUID,
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
    order_id="123456"
)

ref_id = generate_random_reference_id()
order_id = "123456"

res_3d = client.pos_3d(
    merchant_guid=GUID,
    card_holder="test",
    card_number="4446763125813623",
    card_expiration_month="12",
    card_expiration_year="2026",
    card_cvc="000",
    customer_gsm="5551231212",
    fail_url="https://example.com/error",
    success_url="https://example.com/success",
    reference_id=ref_id,
    description="Test Order",
    installment="1",
    amount="100,00",
    total_amount="100,00",
    ip_address="127.0.0.1",
    ref_url="https://example.com",
    data1="a",
    data2="a",
    data3="a",
    data4="a",
    data5="a",
    order_id=order_id
)

print(res_3d)


res_bkm = client.bkm_express(
    merchant_guid=GUID,
    customer_gsm="5551231212",
    fail_url="http://localhost:8000/error",
    success_url="http://localhost:8000/success",
    reference_id=generate_random_reference_id(),
    amount="100,00",
    ip_address="127.0.0.1",
    customer_info="",
    description="Test Order",
    order_id="",
    ref_url="")

print(res_bkm)
