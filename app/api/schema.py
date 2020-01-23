schema = [
    {
        "entityType" : "Gene",
        "entityIdKey" : "geneId",
        "entityNameKey" : "geneName",
        "properties" : [
            "geneDPI",
            "geneDSI",
            "geneId",
            "genePLI"
        ],
        "relationships" : [
            {
                "NeighborType" : "Disease",
                "NeighborNameKey" : "diseaseName",
                "RelationName" : "AssociatesWith",
                "FromNode" : "Gene"
            }
        ]
    },
    {
        "entityType" : "Disease",
        "entityIdKey" : "diseaseId",
        "entityNameKey" : "diseaseName",
        "properties" : [
            "diseaseType"
        ],
        "relationships" : [
            {
                "NeighborType" : "Gene",
                "NeighborNameKey" : "geneName",
                "RelationName" : "AssociatesWith",
                "FromNode" : "Gene"
            }
        ]
    }
]