
from zope import component

from ctrl.core.extension import CtrlExtension
from ctrl.core.interfaces import (
    ICommandRunner, ICloudctl, ICloudSettings,
    ICtrlExtension, IFetch, ISettings, ISubcommand)

from .client import CloudClient
from .command import CloudSubcommand
from .settings import CloudSettings
from .utils import Fetch


class CtrlCloudExtension(CtrlExtension):

    @property
    def requires(self):
        return ['config', 'command']

    def register_adapters(self):
        component.provideAdapter(
            factory=CloudSubcommand,
            adapts=[ICommandRunner],
            provides=ISubcommand,
            name='cloud')

        component.provideAdapter(
            factory=CloudSettings,
            adapts=[ISettings],
            provides=ICloudSettings)

    async def register_utilities(self):
        component.provideUtility(
            CloudClient(),
            ICloudctl)

        component.provideUtility(
            Fetch(),
            IFetch)


# register the extension
component.provideUtility(
    CtrlCloudExtension(),
    ICtrlExtension,
    'cloud')
