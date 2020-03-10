from requests import get
import requests


class IP_adress:

    def get_external_IP_adress(self):
        external_IP_address = get('https://ipapi.co/ip/').text
        print(external_IP_address)
        return external_IP_address

    def send_IP_address(self):
        # defining the api-endpoint  
        API_ENDPOINT = "http://pastebin.com/api/api_post.php"
  
        # your API key here 
        API_KEY = "XXXXXXXXXXXXXXXXX"
        
        # data to be sent to api 
        data = {'api_dev_key':API_KEY, 
                'api_option':'paste', 
                'api_paste_code':get_external_IP_adress(), 
                'api_paste_format':'python'} 

        r = requests.post(url = API_ENDPOINT, data = data) 

        # extracting response text  
        pastebin_url = r.text 
        print("The pastebin URL is:%s"%pastebin_url) 

IP_adress().get_external_IP_adress()