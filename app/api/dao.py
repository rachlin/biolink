from db import DB

class GeneDao(object):

    def __init__(self):
        self.dbq = DB()


    def getGenes(self, page):
        info = {
            "Genes" : renderGenes(self.dbq.queryDB_simple("gene", True, page)),
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


    def getDiseases(self, page):
        info = {
            "Diseases" : renderDiseases(self.dbq.queryDB_simple("disease", True, page)),
            "Page" : page
        }

        return info


    def getDiseaseInfo(self, diseaseName):
        info = {
            "DiseaseName" : diseaseName,
            "AssociatedGenes" : renderGenes(self.dbq.queryDB("d_ag", diseaseName)),
            "RelatedDiseases" : {
                "RelatedByGene" : renderDiseases(self.dbq.queryDB("d_ad", diseaseName))
            }
        }

        return info


def renderDiseases(results):
    return [result['d1']['diseaseName'] for result in results]

def renderGenes(results):
    return [result['g1']['geneName'] for result in results]