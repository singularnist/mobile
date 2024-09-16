
import requests
import aiohttp

from src.config.apiconf import Api_Conf

class Request_Mreport():
    def __init__(self) -> None:
        self.url = Api_Conf.API_URL
        self.port = Api_Conf.API_PORT

    async def fetch_data(self, metod):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=f'{self.url}:{self.port}{metod}') as response:
                    response_data = await response.json()
                    return response_data
        except:
            return {'error':'error'}
        
   

    