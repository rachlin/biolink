from db import DB

class GeneDao(object):

    def __init__(self):
        self.dbq = DB()
        self.entityType = "Gene"
        self.entityIdKey = "geneId"
        self.entityNameKey = "geneName"
        self.relationships = [
            {
                "NeighborType" : "Disease",
                "NeighborNameKey" : "diseaseName",
                "FromNode" : self.entityType,
                "ToNode" : "Disease"
            }
        ]


    def getGenes(self, page):
        info = {
            "Genes" : self.dbq.queryDB_Entity(entityType=self.entityType, entityIdKey=self.entityIdKey, entityNameKey=self.entityNameKey, page=page),
            "Page" : page
        }

        return info
        

    def getGeneInfo(self, geneName):
        info = {
            "GeneName" : geneName,
            "Neighbors" : {},
            "RelatedGenes" : {}
        }

        for rel in self.relationships:
            neighborType = rel["NeighborType"]
            neighborNameKey = rel["NeighborNameKey"]
            info["Neighbors"][neighborType] = self.dbq.queryDB_Neighbors(entityType=self.entityType, entityNameKey=self.entityNameKey, entityName=geneName, relationship_details=rel)
            info["RelatedGenes"]["RelatedBy" + neighborType] = self.dbq.queryDB_SimilarByNeighbor(entityType=self.entityType, entityNameKey=self.entityNameKey, entityName=geneName, relationship_details=rel)

        return info


class DiseaseDao(object):

    def __init__(self):
        self.dbq = DB()
        self.entityType = "Disease"
        self.entityIdKey = "diseaseId"
        self.entityNameKey = "diseaseName"
        self.relationships = [
            {
                "NeighborType" : "Gene",
                "NeighborNameKey" : "geneName",
                "FromNode" : "Gene",
                "ToNode" : self.entityType
            }
        ]


    def getDiseases(self, page):
        info = {
            "Diseases" : self.dbq.queryDB_Entity(entityType=self.entityType, entityIdKey=self.entityIdKey, entityNameKey=self.entityNameKey, page=page),
            "Page" : page
        }

        return info


    def getDiseaseInfo(self, diseaseName):
        info = {
            "DiseaseName" : diseaseName,
            "Neighbors" : {},
            "RelatedDiseases" : {}
        }

        for rel in self.relationships:
            neighborType = rel["NeighborType"]
            neighborNameKey = rel["NeighborNameKey"]
            info["Neighbors"][neighborType] = self.dbq.queryDB_Neighbors(entityType=self.entityType, entityNameKey=self.entityNameKey, entityName=diseaseName, relationship_details=rel)
            info["RelatedDiseases"]["RelatedBy" + neighborType] = self.dbq.queryDB_SimilarByNeighbor(entityType=self.entityType, entityNameKey=self.entityNameKey, entityName=diseaseName, relationship_details=rel)

        return info


def renderDiseases(results):
    return [result['e1']['diseaseName'] for result in results]

def renderGenes(results):
    return [result['e1']['geneName'] for result in results]