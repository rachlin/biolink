from neo4j import GraphDatabase
import pprint

class DB(object):

    def __init__(self, uri='bolt://localhost:7687', user="neo4j", password="admin"):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()


    @staticmethod
    def getEntities(tx, entityType, entityIdKey, page=0):
        """
        """
        query_string = 'MATCH (e1:'+entityType+') RETURN e1 ORDER BY e1.'+entityIdKey+' SKIP ' + str(page * 25) + ' LIMIT 25;'
        result = tx.run(query_string)
        return result.data()


    @staticmethod
    def getNeighborsOfCertainType(tx, entityType, entityNameKey, entityName, neighborType, acceptable_association_score=0.5, num_associations=2):
        """
        """
        query_string = 'match (n:'+neighborType+') where size((n)-[:AssociatesWith]->(:'+entityType+')) > ' + str(num_associations) + ' with collect(n) as neighbors match (n1:'+neighborType+')-[a:AssociatesWith]->(e:'+entityType+' {'+entityNameKey+': "' + entityName + '"}) where n1 in neighbors and a.score > ' + str(acceptable_association_score) + ' return n1;'
        result = tx.run(query_string)
        return result.data()


    @staticmethod
    def getSimilarEntitiesBySimilarNeighbors(tx, entityType, entityNameKey, entityName, neighborType, acceptable_association_score=0.5, num_associations=2):
        """
        """
        query_string = 'match (e:'+entityType+') where size((e)<-[:AssociatesWith]-(:'+neighborType+')) > ' + str(num_associations) + ' with collect(e) as entities match (e1:'+entityType+')<-[b:AssociatesWith]-(n:'+neighborType+')-[a:AssociatesWith]->(target:'+entityType+' {'+entityNameKey+' : "' + entityName + '"}) where e1 in entities and b.score > ' + str(acceptable_association_score) + ' and a.score > ' + str(acceptable_association_score) + ' return e1;' 
        result = tx.run(query_string)
        return result.data()


    def queryDB_Entity(self, entityType, entityIdKey, entityNameKey, page=0):
        """
        """
        with self._driver.session() as session:
            results = session.write_transaction(
                self.getEntities, entityType, entityIdKey, page)
            return [result["e1"][entityNameKey] for result in results]


    def queryDB_Neighbors(self, entityType, entityNameKey, entityName, neighborType, neighborNameKey, acceptable_association_score=0.5, num_associations=2):
        """
        """
        with self._driver.session() as session:
            results = session.write_transaction(
                self.getNeighborsOfCertainType, entityType, entityNameKey, entityName, neighborType, acceptable_association_score=0.5, num_associations=2)
            return [result["n1"][neighborNameKey] for result in results]


    def queryDB_SimilarByNeighbor(self, entityType, entityNameKey, entityName, neighborType, acceptable_association_score=0.5, num_associations=2):
        """
        """
        with self._driver.session() as session:
            results = session.write_transaction(
                self.getSimilarEntitiesBySimilarNeighbors, entityType, entityNameKey, entityName, neighborType, acceptable_association_score=0.5, num_associations=2)
            return [result["e1"][entityNameKey] for result in results]


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
        query_string = 'match (g:Gene) where size((g)-[:AssociatesWith]->(:Disease)) > ' + str(min_num_associations) + ' with collect(g) as genes match (e1:Gene)-[a:AssociatesWith]->(d:Disease {diseaseName: "' + disease_name + '"}) where e1 in genes and a.score > ' + str(acceptable_association_score) + ' return e1;'
        result = tx.run(query_string)
        return result.data()


    @staticmethod
    def _gene_get_related_diseases(tx, gene_name, acceptable_association_score, min_num_associations):
        query_string = 'match (d:Disease) where size((d)<-[:AssociatesWith]-(:Gene)) > ' + str(min_num_associations) + ' with collect(d) as diseases match (e1:Disease)<-[a:AssociatesWith]-(g:Gene {geneName:"' + gene_name + '"}) where e1 in diseases and a.score > ' + str(acceptable_association_score) + ' return e1;'
        result = tx.run(query_string)
        return result.data()


    @staticmethod
    def _gene_get_common_genes(tx, gene_name, acceptable_association_score, min_num_associations):
        query_string = 'match (g:Gene) where size((g)-[:AssociatesWith]->(:Disease)) > ' + str(min_num_associations) + ' with collect(g) as genes match (e1:Gene)-[b:AssociatesWith]->(d:Disease)<-[a:AssociatesWith]-(target:Gene {geneName : "' + gene_name + '"}) where e1 in genes and b.score > ' + str(acceptable_association_score) + ' and a.score > ' + str(acceptable_association_score) + ' return e1;'
        result = tx.run(query_string)
        return result.data()
