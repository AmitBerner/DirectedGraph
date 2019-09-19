import networkx as nx
import Messages as msg


class GraphHandler:

    def __init__(self, rules: list):
        self.rules_graph = nx.DiGraph()

        """ going over each row (rule), parsing it and inserting it into the graph """
        for rule in rules:
            node_a, rule_sign, node_b = rule
            self.add_rule_to_graph(node_a, rule_sign, node_b)

        """ checking if the graph doesnt have any loops, if there are loops the input is invalid and the program ends """
        self.check_for_deduced_loops()

    def add_rule_to_graph(self, node_a: str, rule_sign: str, node_b: str):
        """Adding a parsed rule to the graph

            Args:
                node_a (str): first node to add
                rule_sign (str): edge orientation
                node_b (str): second node to add
        """
        if node_a not in self.rules_graph:
            self.rules_graph.add_node(node_a)
        if node_b not in self.rules_graph:
            self.rules_graph.add_node(node_b)
        if rule_sign == '>':
            self.rules_graph.add_edge(node_b, node_a)
        else:
            self.rules_graph.add_edge(node_a, node_b)
        self.check_for_conflict_type1(node_a, node_b)

    def check_for_conflict_type1(self, node_a: str, node_b: str):

        """Checking for A>B,B>A type of error

            Args:
                node_a (str): first node to add
                node_b (str): second node to add
        """
        if node_a in self.rules_graph.predecessors(node_b) and node_a in self.rules_graph.successors(node_b):
            print(msg.ERROR_CONFLICT_TYPE_1)
            exit(1)

    def check_for_deduced_loops(self):

        """Checking for deduced relations type of error"""
        try:
            nx.find_cycle(self.rules_graph)
            print(msg.ERROR_CONFLICT_TYPE_2)
            exit(1)
        except nx.exception.NetworkXNoCycle:
            pass

    def print_paths(self):

        """Printing all the relations in the graph"""
        # getting all  the nodes that are the "smallest" and "biggest" in terms of the rules in the file
        start_nodes = [x for (x, d) in self.rules_graph.in_degree() if d == 0]
        end_nodes = [x for (x, d) in self.rules_graph.out_degree() if d == 0]

        # going over each of the "smallest" nodes and getting all of their routes in the graph
        for source in start_nodes:
            for path in nx.all_simple_paths(self.rules_graph, source, end_nodes):
                for node in path[:-1]:
                    print(node, '< ', end='')
                print(path[-1])

    def print_immediate(self):

        """Printing all the immediate relations of a node"""
        node = input("enter a key value:\n")
        if not self.rules_graph.has_node(node):
            print("value not in the rules!")
            return
        print("for the key value \"%s\"" % node)
        if any(self.rules_graph.predecessors(node)):
            for smaller_values in self.rules_graph.predecessors(node):
                print("\"%s\" " % smaller_values, end='')
            print("smaller than \"%s\" and " % node, end='')
        else:
            print("no one is smaller than \"%s\", " % node, end='')
        if any(self.rules_graph.successors(node)):
            for bigger_values in self.rules_graph.successors(node):
                print("\"%s\" " % bigger_values, end='')
            print("bigger.")
        else:
            print("no one is bigger than \"%s\"." % node)
