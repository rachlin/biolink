from proc import BipartiteProcedure

bp = BipartiteProcedure('bolt://localhost:7687', "neo4j", "admin")
bp.print_diseases("Asthma", 0.5, 2)
bp.print_genes("IL4", 0.5, 2)
