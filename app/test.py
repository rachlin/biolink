from proc import CommonDiseaseProcedure

cdp = CommonDiseaseProcedure('bolt://localhost:7687', "neo4j", "admin")
cdp.print_diseases("Asthma", 0.5, 2)