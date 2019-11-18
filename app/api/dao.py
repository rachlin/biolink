from db import DB

class GeneDao(object):

    def __init__(self):
        self.dbq = DB()

    
    def getNeighborTypes(self):
        return ["Disease"]


    def getGenes(self, page):
        info = {
            "Genes" : self.dbq.queryDB_Entity(entityType="Gene", entityIdKey="geneId", entityNameKey="geneName", page=page),
            "Page" : page
        }

        return info

    def getGeneInfo(self, geneName):
        info = {
            "GeneName" : geneName,
            "AssociatedDiseases" : renderDiseases(self.dbq.queryDB("g_ad", geneName)),
            "RelatedGenes" : {
                "RelatedByDisease" : renderGenes(self.dbq.queryDB("g_ag", geneName))
            }
        }

        return info


class DiseaseDao(object):

    def __init__(self):
        self.dbq = DB()

    def getNeighborTypes(self):
        return ["Gene"]


    def getDiseases(self, page):
        info = {
            "Diseases" : self.dbq.queryDB_Entity(entityType="Disease", entityIdKey="diseaseId", entityNameKey="diseaseName", page=page),
            "Page" : page
        }

        return info


    def getDiseaseInfo(self, diseaseName):
        info = {
            "DiseaseName" : diseaseName,
            "Neighbors" : {},
            "RelatedDiseases" : {}
        }

        for neighborType in self.getNeighborTypes():
            info["Neighbors"][neighborType] = self.dbq.queryDB_Neighbors(entityType="Disease", entityNameKey="diseaseName", entityName=diseaseName, neighborType=neighborType, neighborNameKey="geneName")
            info["RelatedDiseases"]["RelatedBy" + neighborType] = self.dbq.queryDB_SimilarByNeighbor(entityType="Disease", entityNameKey="diseaseName", entityName=diseaseName, neighborType=neighborType)

        return info


def renderDiseases(results):
    return [result['e1']['diseaseName'] for result in results]

def renderGenes(results):
    return [result['e1']['geneName'] for result in results]