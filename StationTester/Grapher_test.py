#!/usr/bin/env python3
"""
tests station graphing functionality
"""

# std modules:
import unittest

# dependencies:
from StationTester.Grapher import Grapher, NodeType

class Test_station_graph_basics(unittest.TestCase):

    # tests:
    #########################
    def test_graph_single_station(self):
        """ imars img_publisher station node is created """
        grapher = Grapher()
        grapher.graph_station('imars', 'img_publisher')

        self.assertTrue('img_publisher' in list(grapher.graph.nodes()))

    def test_graph_wildcard_nodes_check(self):
        """ checks for auto-linking wildcard nodes """
        n1 = "imars.test.terra.modis.stuff.and.junk.mapped.png"
        n2 = 'imars.%.mapped.png'
        grapher = Grapher()
        grapher._add_node(
            n1,
            NodeType.PRODUCT,
            None
        )
        grapher._add_node(
            n2,
            NodeType.PRODUCT,
            None
        )

        # check for link btwn nodes
        self.assertTrue(
            grapher.graph.has_edge(n2, n1),
            "wildcard node not auto-linked. edges:" + str(grapher.graph.edges())
        )

    def test_get_nodes_that_match_basic(self):
        """ basic get nodes matching wildcard """
        n1 = "imars.test.terra.modis.stuff.and.junk.mapped.png"
        n2 = 'imars.%.mapped.png'
        grapher = Grapher()
        grapher._add_node(
            n1,
            NodeType.PRODUCT,
            None
        )
        grapher._add_node(
            n2,
            NodeType.PRODUCT,
            None
        )

        self.assertCountEqual([n1, n2], grapher._get_nodes_that_match(n2))
