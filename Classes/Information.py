class Information(object):
    """docstring for Information"""
    def __init__(self, references = 0, selfReferences = 0, links = []):
        self.references = references
        self.selfReferences = selfReferences
        self.links = links

    def getReferences(self):
        return self.references

    def getSelfReferences(self):
        return self.selfReferences

    def getLinks(self):
        return self.links
