MATCH (g:Gene)-[a:AssociatesWith]->(d:Disease) DELETE a;

DROP INDEX ON :Gene(geneId);
DROP INDEX ON :Gene(geneName);
DROP INDEX ON :Disease(diseaseId);
DROP INDEX ON :Disease(diseaseName);

MATCH (g:Gene) DELETE g; 
MATCH (d:Disease) DELETE d;