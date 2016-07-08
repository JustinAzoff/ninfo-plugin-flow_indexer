import requests
from ninfo import PluginBase
            
class flow_indexer(PluginBase):
    """This plugin checks to see if the ip was seen at all in the netflow index"""

    name = "flow_indexer"
    title = "Flow Indexer"
    description = "Flow Indexer stats"
    cache_timeout = 60*10
    types = ['ip','ip6','cidr','cidr6']

    def setup(self):
        self.base_url = self.plugin_config['base_url']
        self.index = self.plugin_config['index']
        self.url = self.base_url + "v1/stats"

    def get_info(self, ip):
        params = {'i': self.index, 'q': ip}
        resp = requests.get(self.url, params=params)
        stats = resp.json()
        return stats

plugin_class = flow_indexer
