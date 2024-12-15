import zeep


class Client:
    def __init__(self, api_url, client_code, client_username, client_password):
        self.api_url = api_url
        self.client_code = client_code
        self.client_username = client_username
        self.client_password = client_password
        self.G = {
            'CLIENT_CODE': client_code,
            'CLIENT_USERNAME': client_username,
            'CLIENT_PASSWORD': client_password
        }
        self.client = zeep.Client(api_url, settings=zeep.Settings(strict=False, xml_huge_tree=True))

    def _request(self, method, is_hashed=False, **kwargs):
        if is_hashed:
            kwargs['G'] = self.G
        return self.client.service[method](**kwargs)

    def calc_hash(self, data):
        return self._request('SHA2B64', is_hashed=False, Data=data)

    def pos_ns(self, merchant_guid, card_holder, card_number, card_expiration_month, card_expiration_year, card_cvc,
            fail_url, success_url, reference_id, installment, amount, total_amount, ip_address, ref_url="",
            data1="", data2="", data3="", data4="", data5="", customer_gsm="", description="", order_id=""):
        hashed_string = self.calc_hash(
            self.client_code + merchant_guid + installment + amount + total_amount + reference_id)
        data = {
            'GUID': merchant_guid,
            'KK_Sahibi': card_holder,
            'KK_No': card_number,
            'KK_SK_Ay': card_expiration_month,
            'KK_SK_Yil': card_expiration_year,
            'KK_CVC': card_cvc,
            'KK_Sahibi_GSM': customer_gsm,
            'Hata_URL': fail_url,
            'Basarili_URL': success_url,
            'Siparis_ID': reference_id,
            'Siparis_Aciklama': description,
            'Taksit': installment,
            'Islem_Tutar': amount,
            'Toplam_Tutar': total_amount,
            'Islem_Hash': hashed_string,
            'Islem_Guvenlik_Tip': 'NS',
            'Islem_ID': order_id,
            'IPAdr': ip_address,
            'Ref_URL': ref_url,
            'Data1': data1,
            'Data2': data2,
            'Data3': data3,
            'Data4': data4,
            'Data5': data5
        }
        return self._request('TP_WMD_UCD', is_hashed=True, **data)

    def pos_3d(self, merchant_guid, card_holder, card_number, card_expiration_month, card_expiration_year, card_cvc,
            fail_url, success_url, reference_id, installment, amount, total_amount, ip_address, ref_url="",
            data1="", data2="", data3="", data4="", data5="", customer_gsm="", description="", order_id=""):
        hashed_string = self.calc_hash(
            self.client_code + merchant_guid + installment + amount + total_amount + reference_id)
        data = {
            'GUID': merchant_guid,
            'KK_Sahibi': card_holder,
            'KK_No': card_number,
            'KK_SK_Ay': card_expiration_month,
            'KK_SK_Yil': card_expiration_year,
            'KK_CVC': card_cvc,
            'KK_Sahibi_GSM': customer_gsm,
            'Hata_URL': fail_url,
            'Basarili_URL': success_url,
            'Siparis_ID': reference_id,
            'Siparis_Aciklama': description,
            'Taksit': installment,
            'Islem_Tutar': amount,
            'Toplam_Tutar': total_amount,
            'Islem_Hash': hashed_string,
            'Islem_Guvenlik_Tip': '3D',
            'Islem_ID': order_id,
            'IPAdr': ip_address,
            'Ref_URL': ref_url,
            'Data1': data1,
            'Data2': data2,
            'Data3': data3,
            'Data4': data4,
            'Data5': data5
        }
        print(data)
        return self._request('TP_WMD_UCD', is_hashed=True, **data)

    def pos_3d_complete(self, merchant_guid, bank_md, reference_id, order_id):
        data = {
            'GUID': merchant_guid,
            'UCD_MD': bank_md,
            'Islem_GUID': reference_id,
            'Siparis_ID': order_id
        }
        return self._request('TP_WMD_Pay', is_hashed=True, **data)



    def bkm_express(self, merchant_guid, customer_gsm, fail_url, success_url, reference_id, amount, ip_address,
                    customer_info="",
                    description="", order_id="", ref_url=""):
        hashed_string = self.calc_hash(
            self.client_code + merchant_guid + amount + reference_id + fail_url + success_url)
        data = {
            'GUID': merchant_guid,
            'Customer_Info': customer_info,
            'Customer_GSM': customer_gsm,
            'Error_URL': fail_url,
            'Success_URL': success_url,
            'Order_ID': reference_id,
            'Order_Description': description,
            'Amount': amount,
            'Payment_Hash': hashed_string,
            'Transaction_ID': order_id,
            'IPAddress': ip_address,
            'Referrer_URL': ref_url

        }
        return self._request('TP_Islem_Odeme_BKM', is_hashed=True, **data)



    def add_card(self, merchant_guid, card_holder, card_number, card_expiration_month, card_expiration_year, card_alias, transaction_id):
        data = {
            'GUID': merchant_guid,
            'KK_Sahibi': card_holder,
            'KK_No': card_number,
            'KK_SK_Ay': card_expiration_month,
            'KK_SK_Yil': card_expiration_year,
            'KK_Kart_Adi': card_alias,
            'KK_Islem_ID': transaction_id
        }
        return self._request('KS_Kart_Ekle', is_hashed=True, **data)



    def verify_card(self, card_number, card_expiration_month, card_expiration_year, card_cvc, return_url, data1="", data2="", data3="", data4="", data5=""):
        data = {
            'KK_No': card_number,
            'KK_SK_Ay': card_expiration_month,
            'KK_SK_Yil': card_expiration_year,
            'KK_CVC': card_cvc,
            'Return_URL': return_url,
            'Data1': data1,
            'Data2': data2,
            'Data3': data3,
            'Data4': data4,
            'Data5': data5

        }
        return self._request('TP_KK_Verify', is_hashed=True, **data)


    def pay_with_card(self, merchant_guid, card_guid, customer_gsm, fail_url, success_url, reference_id, amount, total_amount, ip_address, kk_transaction_id,installment=1, is_3d=False, ref_url="", data1="", data2="", data3="", data4="", data5="", description="", order_id=""):
        data = {
            'GUID': merchant_guid,
            'KS_GUID': card_guid,
            'KK_Sahibi_GSM': customer_gsm,
            'Hata_URL': fail_url,
            'Basarili_URL': success_url,
            'Siparis_ID': reference_id,
            'Siparis_Aciklama': description,
            'Taksit': installment,
            'Islem_Tutar': amount,
            'Toplam_Tutar': total_amount,
            'Islem_Guvenlik_Tip': '3D' if is_3d else 'NS',
            'Islem_ID': order_id,
            'IPAdr': ip_address,
            'Ref_URL': ref_url,
            'Data1': data1,
            'Data2': data2,
            'Data3': data3,
            'Data4': data4,
            'KK_Islem_ID': kk_transaction_id
        }
        print(data)
        return self._request('KS_Tahsilat', is_hashed=True, **data)
