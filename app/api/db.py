from neo4j import GraphDatabase
import pprint

class DB(object):

    def __init__(self, uri='bolt://localhost:7687', user="neo4j", password="admin"):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def queryDB(self, query_func, node_name, acceptable_association_score=0.5, num_associations=2):

        query_funcs = {
            "g_ad" : self._gene_get_related_diseases,
            "g_ag" : self._gene_get_common_genes,
            "d_ag" : self._disease_get_related_genes,
            "d_ad" : self._disease_get_common_diseases
        }

        if query_func in query_funcs:
            with self._driver.session() as session:
                results = session.write_transaction(
                    query_funcs[query_func], 
                    node_name, acceptable_association_score, num_associations)
                return results

        return {}


    @staticmethod
    def _disease_get_related_genes(tx, disease_name, acceptable_association_score, min_num_associations):
        query_string = 'match (g:Gene) where size((g)-[:AssociatesWith]->(:Disease)) > ' + str(min_num_associations) + ' with collect(g) as genes match (g1:Gene)-[a:AssociatesWith]->(d:Disease {diseaseName: "' + disease_name + '"}) where g1 in genes and a.score > ' + str(acceptable_association_score) + ' return g1;'
        result = tx.run(query_string)
        return result.data()


    @staticmethod
    def _gene_get_related_diseases(tx, gene_name, acceptable_association_score, min_num_associations):
        query_string = 'match (d:Disease) where size((d)<-[:AssociatesWith]-(:Gene)) > ' + str(min_num_associations) + ' with collect(d) as diseases match (d1:Disease)<-[a:AssociatesWith]-(g:Gene {geneName:"' + gene_name + '"}) where d1 in diseases and a.score > ' + str(acceptable_association_score) + ' return d1;'
        result = tx.run(query_string)
        return result.data()


    @staticmethod
    def _disease_get_common_diseases(tx, disease_name, acceptable_association_score, min_num_associations):
        query_string = 'match (d:Disease) where size((d)<-[:AssociatesWith]-(:Gene)) > ' + str(min_num_associations) + ' with collect(d) as diseases match (d1:Disease)<-[b:AssociatesWith]-(g:Gene)-[a:AssociatesWith]->(target:Disease {diseaseName : "' + disease_name + '"}) where d1 in diseases and b.score > ' + str(acceptable_association_score) + ' and a.score > ' + str(acceptable_association_score) + ' return d1;' 
        result = tx.run(query_string)
        return result.data()


    @staticmethod
    def _gene_get_common_genes(tx, gene_name, acceptable_association_score, min_num_associations):
        query_string = 'match (g:Gene) where size((g)-[:AssociatesWith]->(:Disease)) > ' + str(min_num_associations) + ' with collect(g) as genes match (g1:Gene)-[b:AssociatesWith]->(d:Disease)<-[a:AssociatesWith]-(target:Gene {geneName : "' + gene_name + '"}) where g1 in genes and b.score > ' + str(acceptable_association_score) + ' and a.score > ' + str(acceptable_association_score) + ' return g1;'
        result = tx.run(query_string)
        return result.data()
