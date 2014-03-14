class CreateTemplate(object):
    def __init__(self, params, template):
        self.template = open('templates/{0}.template'.format(template)).read()
        self.params = params

    def get(self):
        mail = self.template.format(**self.params)

        return mail
