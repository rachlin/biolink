from neo4j import GraphDatabase
import pprint

class DB(object):

    def __init__(self, uri='bolt://localhost:7687', user="neo4j", password="admin"):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()


    # @staticmethod
    # def getExactEntity(tx, entityType, entityNameKey, entityName):
    #     """
    #     """
    #     query_string = 'MATCH (e1:'+entityType+') RETURN e1 where e1.' + entityNameKey + '=' + entityName + ';'
    #     result = tx.run(query_string)
    #     return result.data()


    @staticmethod
    def getFilteredEntities(tx, entityType, entityKey, entityValue):
        """
        """
        query_string = 'MATCH (e1:'+entityType+') WHERE e1.' + entityKey + '=~ \".*' + entityValue + '.*\" RETURN e1;'
        print(query_string)
        result = tx.run(query_string)
        return result.data()


    @staticmethod
    def getEntities(tx, entityType, entityIdKey, page=0):
        """
        """
        query_string = 'MATCH (e1:'+entityType+') RETURN e1 ORDER BY e1.'+entityIdKey+' SKIP ' + str(page * 25) + ' LIMIT 25;'
        result = tx.run(query_string)
        return result.data()


    @staticmethod
    def getNeighborsOfCertainType(tx, entityType, entityNameKey, entityName, relationship_details, acceptable_association_score=0.5, num_associations=2):
        """
        """
        neighborType = relationship_details["NeighborType"]

        query_string = 'match (n:'+neighborType+') '

        if relationship_details["FromNode"] == entityType:
            query_string += 'where size((n)<-[:'+relationship_details["RelationName"]+']-(:'+entityType+')) > ' + str(num_associations) + ' with collect(n) as neighbors '
            query_string += 'match (n1:'+neighborType+')<-[a:'+relationship_details["RelationName"]+']-(e:'+entityType+' {'+entityNameKey+': "' + entityName + '"}) '
        
        else:  #from node is neighbor type
            query_string += 'where size((n)-[:'+relationship_details["RelationName"]+']->(:'+entityType+')) > ' + str(num_associations) + ' with collect(n) as neighbors '
            query_string += 'match (n1:'+neighborType+')-[a:'+relationship_details["RelationName"]+']->(e:'+entityType+' {'+entityNameKey+': "' + entityName + '"}) '

        query_string += 'where n1 in neighbors and a.score > ' + str(acceptable_association_score) + ' return n1;'
        result = tx.run(query_string)
        return result.data()


    @staticmethod
    def getSimilarEntitiesBySimilarNeighbors(tx, entityType, entityNameKey, entityName, relationship_details, acceptable_association_score=0.5, num_associations=2):
        """
        """
        neighborType = relationship_details["NeighborType"]

        query_string = 'match (e:'+entityType+') '

        if relationship_details["FromNode"] == entityType:
            query_string += 'where size((e)-[:'+relationship_details["RelationName"]+']->(:'+neighborType+')) > ' + str(num_associations) + ' with collect(e) as entities '
            query_string += 'match (e1:'+entityType+')-[b:'+relationship_details["RelationName"]+']->(n:'+neighborType+')<-[a:'+relationship_details["RelationName"]+']-(target:'+entityType+' {'+entityNameKey+' : "' + entityName + '"}) '

        else:
            query_string += 'where size((e)<-[:'+relationship_details["RelationName"]+']-(:'+neighborType+')) > ' + str(num_associations) + ' with collect(e) as entities '
            query_string += 'match (e1:'+entityType+')<-[b:'+relationship_details["RelationName"]+']-(n:'+neighborType+')-[a:'+relationship_details["RelationName"]+']->(target:'+entityType+' {'+entityNameKey+' : "' + entityName + '"}) '

        query_string += 'where e1 in entities and b.score > ' + str(acceptable_association_score) + ' and a.score > ' + str(acceptable_association_score) + ' return e1;' 
        result = tx.run(query_string)
        return result.data()


    def queryDB_Entities(self, entityType, entityIdKey, entityNameKey, page=0):
        """
        """
        with self._driver.session() as session:
            results = session.write_transaction(
                self.getEntities, entityType, entityIdKey, page)
            return [result["e1"] for result in results]


    def queryDB_EntitiesFilter(self, entityType, entityKey, entityValue):
        """
        """
        with self._driver.session() as session:
            results = session.write_transaction(
                self.getFilteredEntities, entityType, entityKey, entityValue)
            return [result["e1"] for result in results]


    def queryDB_Neighbors(self, entityType, entityNameKey, entityName, relationship_details, acceptable_association_score=0.5, num_associations=2):
        """
        """
        with self._driver.session() as session:
            results = session.write_transaction(
                self.getNeighborsOfCertainType, entityType, entityNameKey, entityName, relationship_details, acceptable_association_score=0.5, num_associations=2)
            return [result["n1"][relationship_details["NeighborNameKey"]] for result in results]


    def queryDB_SimilarByNeighbor(self, entityType, entityNameKey, entityName, relationship_details, acceptable_association_score=0.5, num_associations=2):
        """
        """
        with self._driver.session() as session:
            results = session.write_transaction(
                self.getSimilarEntitiesBySimilarNeighbors, entityType, entityNameKey, entityName, relationship_details, acceptable_association_score=0.5, num_associations=2)
            return [result["e1"][entityNameKey] for result in results]