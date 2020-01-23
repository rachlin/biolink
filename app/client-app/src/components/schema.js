const schema = [
    {
        entityType: "gene",
        propertiesOfImportance: [
            "geneName", "geneId"
        ],
        nameKey: "geneName"
    },
    {
        entityType: "disease",
        propertiesOfImportance: [
            "diseaseName", "diseaseId"
        ],
        nameKey: "diseaseName"
    }
]

export default schema