from py2neo.ogm import GraphObject, Property, RelatedTo
from py2neo import Graph
from graphql import GraphQLError


graph = Graph(
    "bolt://localhost:7687",    
    auth=("neo4j", "admin"))


class BaseModel(GraphObject):

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)


    @property
    def all(self):
        return self.match(graph)

    # def save(self):
    #     graph.push(self)


class Gene(BaseModel):
    __primarykey__ = 'geneId'

    geneId = Property()
    geneName = Property()
    genePLI = Property()
    geneDSI = Property()
    geneDPI = Property()

    def fetch(self):
        # gene = self.match(graph).first()
        gene = self.match(graph, self.geneId).first()

        if gene is None:
            raise GraphQLError(f'"{self.geneId}" has not been found in our gene list.')

    def as_dict(self):
        return {
            'geneId': self.geneId,
            'geneName': self.geneName
    }

    # associations = RelatedTo('Disease', 'AssociatesWith')



