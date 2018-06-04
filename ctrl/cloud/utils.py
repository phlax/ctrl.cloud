import aiohttp
import async_timeout


class Fetch(object):

    async def fetch(self, session, url, method='get',
                    data=None, verbose=False):
        async with async_timeout.timeout(10):
            if verbose:
                print("API %s: %s" % (method, url))
                if method == 'post':
                    print(">> data: %s" % data)
            return await getattr(session, method)(url, data=data)

    async def delete(self, url, parse=None, headers=None, params=None):
        async with aiohttp.ClientSession(headers=headers) as session:
            response = await self.fetch(session, url, method="delete")
            return await self.parse(response, parse)

    async def get(self, url, parse=None, headers=None, params=None):
        async with aiohttp.ClientSession(headers=headers) as session:
            response = await self.fetch(session, url)
            return await self.parse(response, parse)

    async def post(self, url, parse=None, headers=None, data=None):
        async with aiohttp.ClientSession(headers=headers) as session:
            response = await self.fetch(session, url, method='post', data=data)
            return await self.parse(response, parse)

    async def parse(self, response, parse):
        if parse == 'content':
            return await response.content()
        if parse == 'text':
            return await response.text()
        elif parse == 'json':
            try:
                return await response.json()
            except Exception as e:
                print(e)
                print(await response.text())
                return 'failed'
        return response
