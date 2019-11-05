from db import DB

class GeneDao(object):

    def __init__(self):
        self.dbq = DB()

    def getGeneInfo(self, geneName):
        info = {
            "Associated Diseases" : renderDiseases(self.dbq.queryDB("g_ad", geneName)),
            "Related Genes" : {
                "Related by Diseases" : renderGenes(self.dbq.queryDB("g_ag", geneName))
            }
        }

        return info


class DiseaseDao(object):

    def __init__(self):
        self.dbq = DB()

    def getDiseaseInfo(self, diseaseName):
        info = {
            "Associated Genes" : renderGenes(self.dbq.queryDB("d_ag", diseaseName)),
            "Related Diseases" : {
                "Related by Genes" : renderDiseases(self.dbq.queryDB("d_ad", diseaseName))
            }
        }

        return info


def renderDiseases(results):
    return [result['d1']['diseaseName'] for result in results]

def renderGenes(results):
    return [result['g1']['geneName'] for result in results]