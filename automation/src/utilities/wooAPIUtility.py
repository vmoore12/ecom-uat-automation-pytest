import logging as logger
import os
from automation.src.configs.MainConfigs import MainConfigs
from automation.src.utilities.credentialsUtility import CredentialsUtility
from woocommerce import API 

"""
    Utilities helpers from the Woocomerce API Python Library

"""

class WooAPIUtility:

    def __init__(self):
        wc_creds = CredentialsUtility.get_woo_api_keys()

        self.base_url = MainConfigs.get_base_url()

        self.wcapi = API(
            url = self.base_url,
            consumer_key=wc_creds['woo_key'],
            consumer_secret=wc_creds['woo_secret'],
            version='wc/v3'

            )
        

    def assert_status_code(self):

        assert self.status_code == self.expected_status_code, f'Bad Status Code.'\
        f'Expected {self.expected_status_code}, Actual status code {self.status_code},'\
        f'URL: {self.url}, Response Json: {self.rs_json}'
        
    def post(self, wc_endpoint, params=None, expected_status_code=201):


        rs_api = self.wcapi.post(wc_endpoint, data=params)

        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.url = rs_api.url
        self.assert_status_code()

        return self.rs_json


    def get(self, woo_endpoint, params=None, return_headers=False, expected_status_code=200):

        rsp_api = self.wcapi.get(woo_endpoint, params=params)
        self.status_code = rsp_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rsp_api.json()
        self.endpoint = woo_endpoint
        self.url = rsp_api.url
        self.assert_status_code()

        logger.debug(f'Get API response: {self.rs_json}')
        if return_headers:
            return{'response_json': self.rs_json, 'headers': rsp_api.headers}
        else:
            return self.rs_json
            
    def put(self, wc_endponit, params=None, expected_status_code=200):

        rs_api = self.wcapi.put(wc_endponit, data=params)
        self.status_code = rs_api.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endponit
        self.url = rs_api.url
        self.assert_status_code()

        logger.debug(f'Put API response: {self.rs_json}')

        return self.rs_json
        
    def delete(self, wc_endponit, params=None, expected_status_code=200):

        rs_api = self.wcapi.delete(wc_endponit,params=params)
        self.status_code = rs_api.status_code
        self.status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endponit
        self.url = rs_api.url
        self.assert_status_code()

        logger.debug(f'Delete API response:{self.rs_json}')


        return self.rs_json
        

if __name__ == '__main__':

    obj = WooAPIUtility()
    rs_api = obj.get('products')
    print(rs_api.json)
    import pdb; pdb.set_trace()



        
