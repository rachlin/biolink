from neo4j import GraphDatabase
import pprint

class CommonDiseaseProcedure(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_diseases(self, disease_name, acceptable_association_score, num_genes):
        with self._driver.session() as session:
            diseases = session.write_transaction(self._get_common_diseases, disease_name, acceptable_association_score, num_genes)
            pprint.pprint(diseases)

    @staticmethod
    def _get_common_diseases(tx, disease_name, acceptable_association_score, num_genes):
        query_string = 'match (d:Disease) where size((d)<-[:AssociatesWith]-(:Gene)) > ' + str(num_genes) + ' with collect(d) as diseases match (d1:Disease)<-[b:AssociatesWith]-(g:Gene)-[a:AssociatesWith]->(asthma:Disease {diseaseName : "' + disease_name + '"}) where d1 in diseases and b.score > ' + str(acceptable_association_score) + ' and a.score > ' + str(acceptable_association_score) + ' return d1, g, asthma' 
        result = tx.run(query_string)

        return result.data()