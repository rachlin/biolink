from db import DB
import schema as config

class EntityDao(object):

    def __init__(self, entityType):
        self.dbq = DB()
        self.entityType = entityType
        self.schema = None
        for schema in config.schema:
            if schema["entityType"] == self.entityType:
                self.schema = schema


    def getEntities(self, page):
        info = {
            "Entities" : self.dbq.queryDB_Entity(
                entityType=self.schema["entityType"], 
                entityIdKey=self.schema["entityIdKey"], 
                entityNameKey=self.schema["entityNameKey"], 
                page=page),
            "Page" : page
        }

        return info
        

    def getEntityInfo(self, entityName):
        info = {
            "EntityName" : entityName,
            "Neighbors" : {},
            "RelatedGenes" : {}
        }

        for rel in self.schema["relationships"]:
            neighborType = rel["NeighborType"]
            neighborNameKey = rel["NeighborNameKey"]
            info["Neighbors"][neighborType] = self.dbq.queryDB_Neighbors(
                entityType=self.schema["entityType"], 
                entityNameKey=self.schema["entityNameKey"], 
                entityName=entityName, 
                relationship_details=rel)
            info["RelatedGenes"]["RelatedBy" + neighborType] = self.dbq.queryDB_SimilarByNeighbor(
                entityType=self.schema["entityType"], 
                entityNameKey=self.schema["entityNameKey"], 
                entityName=entityName, 
                relationship_details=rel)

        return info