USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:/home/krishna/dev/biolink/data/csv/gene.csv" AS row
CREATE (:Gene {geneId: row.geneId, geneName: row.geneName, genePLI : row.genePLI, geneDSI : row.geneDSI, geneDPI : row.geneDPI});

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:/home/krishna/dev/biolink/data/csv/disease.csv" AS row
CREATE (:Disease {diseaseId: row.diseaseId, diseaseName: row.diseaseName, diseaseType : row.diseaseType});

CREATE INDEX ON :Gene(geneId);
CREATE INDEX ON :Gene(geneName);
CREATE INDEX ON :Disease(diseaseId);
CREATE INDEX ON :Disease(diseaseName);

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:/home/krishna/dev/biolink/data/csv/association.csv" AS row
MATCH (gene:Gene {geneId: row.geneId})
MATCH (disease:Disease {diseaseId: row.diseaseId})
MERGE (gene)-[a:AssociatesWith]->(disease)
ON CREATE SET a.score = toFloat(row.score);

