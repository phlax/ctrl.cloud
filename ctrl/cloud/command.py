
from zope import interface

from ctrl.core.interfaces import ISubcommand


@interface.implementer(ISubcommand)
class CloudSubcommand(object):

    def __init__(self, context):
        self.context = context

    async def handle(self, command, *args, loop=None):
        return await getattr(self, 'handle_%s' % command)(*args, loop=loop)
