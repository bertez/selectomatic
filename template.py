class CreateTemplate(object):
    def __init__(self, params):
        self.template = open('templates/{0}.template'.format(params['template'])).read()
        self.params = {key: value for key, value in params.items() if key != 'template'}

    def get(self):
        mail = self.template.format(**self.params)

        return mail
