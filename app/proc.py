from neo4j import GraphDatabase
import pprint

class BipartiteProcedure(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_diseases(self, disease_name, acceptable_association_score, num_genes):
        with self._driver.session() as session:
            diseases = session.write_transaction(self._get_common_diseases, disease_name, acceptable_association_score, num_genes)
            pprint.pprint(diseases)

    def print_genes(self, gene_name, acceptable_association_score, num_diseases):
        with self._driver.session() as session:
            genes = session.write_transaction(self._get_common_genes, gene_name, acceptable_association_score, num_diseases)
            pprint.pprint(genes)

    def vis_diseases(self, disease_name, acceptable_association_score, num_genes):
        import matplotlib.pyplot as plt
        import networkx as nx
        import networkx.algorithms.bipartite as bp

        with self._driver.session() as session:
            results = session.write_transaction(self._get_common_diseases, disease_name, acceptable_association_score, num_genes)
            diseases = []
            genes = []
            edges = []
            for result in results:
                diseases.append(result["d1"])
                genes.append(result["g"])
                edges.append([result["d1"], result["g"]])

            G=nx.Graph()
            G.add_nodes_from(diseases, bipartite=0)
            G.add_nodes_from(genes, bipartite=1)
            G.add_edges_from(edges)
            # from https://stackoverflow.com/questions/27084004/bipartite-graph-in-networkx
            pos = dict()
            pos.update( (n, (1, i)) for i, n in enumerate(diseases) ) # put nodes from X at x=1
            pos.update( (n, (2, i)) for i, n in enumerate(genes) ) # put nodes from Y at x=2
            nx.draw(G, pos=pos)
            plt.show()



    @staticmethod
    def _get_common_diseases(tx, disease_name, acceptable_association_score, num_genes):
        query_string = 'match (d:Disease) where size((d)<-[:AssociatesWith]-(:Gene)) > ' + str(num_genes) + ' with collect(d) as diseases match (d1:Disease)<-[b:AssociatesWith]-(g:Gene)-[a:AssociatesWith]->(target:Disease {diseaseName : "' + disease_name + '"}) where d1 in diseases and b.score > ' + str(acceptable_association_score) + ' and a.score > ' + str(acceptable_association_score) + ' return d1, g, target' 
        result = tx.run(query_string)

        return result.data()

    @staticmethod
    def _get_common_genes(tx, gene_name, acceptable_association_score, num_diseases):
        query_string = 'match (g:Gene) where size((g)-[:AssociatesWith]->(:Disease)) > ' + str(num_diseases) + ' with collect(g) as genes match (g1:Gene)-[b:AssociatesWith]->(d:Disease)<-[a:AssociatesWith]-(target:Gene {geneName : "' + gene_name + '"}) where g1 in genes and b.score > ' + str(acceptable_association_score) + ' and a.score > ' + str(acceptable_association_score) + ' return g1, d, target;'
        result = tx.run(query_string)

        return result.data()
