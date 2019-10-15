USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:/home/krishna/dev/biolink/data/csv/gene.csv" AS row
CREATE (:Gene {geneId: row.geneId, geneName: row.geneName, genePLI : row.genePLI, geneDSI : row.geneDSI, geneDPI : row.geneDPI});

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:/home/krishna/dev/biolink/data/csv/disease.csv" AS row
CREATE (:Disease {diseaseId: row.diseaseId, diseaseName: row.diseaseName, diseaseType : row.diseaseType});

CREATE INDEX ON :Product(geneId);
CREATE INDEX ON :Product(geneName);
CREATE INDEX ON :Product(diseaseId);
CREATE INDEX ON :Product(diseaseName);

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:/home/krishna/dev/biolink/data/csv/association.csv" AS row
MATCH (gene:Gene {geneId: row.geneId})
MATCH (disease:Disease {diseaseId: row.diseaseId})
MERGE (gene)-[associated:DISEASE]->(disease)
ON CREATE SET associated.score = toFloat(row.score);

