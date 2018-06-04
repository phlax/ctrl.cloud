from zope import component

from ctrl.core.interfaces import (
    ICloudProvider, ICloudSettings, ISettings)


class CloudClient(object):

    def get_provider(self, name):
        return component.getUtility(ICloudProvider, name=name)

    @property
    def settings(self):
        return ICloudSettings(component.getUtility(ISettings))

    async def boot(self, name, wait=False):
        return 'Booooteroooo'

    async def status(self, name=None):
        print(self.settings.servers)
        for name in self.settings.servers:
            server = self.settings.get_server(name)
            return await self.get_provider(server['cloud']).status(name)
