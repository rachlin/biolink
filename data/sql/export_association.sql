select geneId, diseaseId, association, associationType, pmid, score, EL, EI, year from geneDiseaseNetwork
left join geneAttributes USING (geneNID)
left join diseaseAttributes USING (diseaseNID)
where association != '\N';