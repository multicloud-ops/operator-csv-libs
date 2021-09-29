import logging, sys, copy, yaml

class CustomResourceDefinition:
    
    def __init__(self, crd, logger=None):
        self.crd = copy.deepcopy(crd)
        self.properties = {}

        self.fullName = self.crd['metadata']['name']
        self.name = self.fullname.split('.')[0]
        self.operator = self.crd['metadata']['labels']['name']
        self.namespaced = True if self.crd['spec']['scope'] == 'Namespaced' else False

        self._get_properties()
    
    def _get_properties(self):
        for v in self.crd['spec']['versions']:
            if 'schema' in v:
                if 'openAPIV3Schema' in v['schema']:
                    pass
            for p in v['schema']['openAPIV3Schema']['properties']['spec']['properties']:
                self.properties[p] = v['schema']['openAPIV3Schema']['properties']['spec']['properties']['p']
        
    def get_properties(self):
        return self.properties
