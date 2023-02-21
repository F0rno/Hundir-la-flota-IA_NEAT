import pydot

# Crea una instancia de un grafo dirigido
graph = pydot.Dot(graph_type='digraph')

# Agrega nodos al grafo
input_node = pydot.Node("Input")
hidden_node = pydot.Node("Hidden", style="filled", fillcolor="lightblue")
output_node = pydot.Node("Output")

graph.add_node(input_node)
graph.add_node(hidden_node)
graph.add_node(output_node)

# Agrega conexiones entre los nodos
graph.add_edge(pydot.Edge(input_node, hidden_node))
graph.add_edge(pydot.Edge(hidden_node, output_node))

# Genera la imagen del grafo
graph.write_png('test.png')



