import graphene

from models import Gene

class GeneSchema(graphene.ObjectType):
    geneId = graphene.Int()
    geneName = graphene.String()

class Query(graphene.ObjectType):
    gene = graphene.Field(lambda: GeneSchema, geneId=graphene.Int())

    def resolve_gene(self, info, geneId):
        # gene = Gene(geneId=geneId).fetch()
        gene = Gene().fetch()
        return GeneSchema(**gene.as_dict())


schema = graphene.Schema(query=Query, auto_camelcase=False)