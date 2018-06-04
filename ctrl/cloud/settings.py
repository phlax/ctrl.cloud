

class CloudSettings(object):

    def __init__(self, context):
        self.context = context

    @property
    def clouds(self):
        return [
            k[6:] for k
            in self.context.config.sections()
            if k.startswith('cloud:')]

    def get_cloud(self, name):
        return dict(
            self.context.config.items('cloud:%s' % name))

    @property
    def servers(self):
        return [
            k[7:] for k
            in self.context.config.sections()
            if k.startswith('server:')]

    def get_server(self, name):
        return dict(
            self.context.config.items('server:%s' % name))
