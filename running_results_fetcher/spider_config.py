class SpiderConfig:
    """It's spider configuration"""

    def __init__(self, **kwargs):
        self.domain_name = kwargs.get('domain_name', '')
        self.protocol = kwargs.get('protocol', 'https://')
        self.next_page_selector = kwargs.get('next_page_selector')
        self.runner = kwargs.get('runner')

    @property
    def domain_name(self):
        return self.__domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        self.name = domain_name.split('.')[0]
        self.__domain_name = domain_name

    @property
    def start_url(self):
        return "{}{}{}".format(self.protocol,
                               self.domain_name,
                               self.url_suffix)
