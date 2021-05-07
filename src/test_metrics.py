#!/usr/bin/env python
import logging
import unittest

import networkx as nx

from itertools_recipes import choose
from lib.graph import set_unit_weights
from metrics_lib import fairness, availability_one_combo
from metrics_lib import link_failure_combinations, fraction_within_latency
from topo.os3e import OS3EGraph
from os3e_weighted import OS3EWeightedGraph

lg = logging.getLogger("test_metrics")

class FairnessTest(unittest.TestCase):

    def test_best(self):
        '''Best case: equal items should have fairness of 1.'''
        cases = [[1, 1, 1], [3, 3, 3, 3]]
        for case in cases:
            self.assertEqual(1, fairness(case))

    def test_worst(self):
        '''Worst case: one nonzero item and the rest zero.'''
        cases = [[1, 0, 0], [3, 0, 0, 0]]
        for case in cases:
            self.assertAlmostEqual(1 / float(len(case)), fairness(case))
    
    def test_mix(self):
        '''Mixed case: should be k/n when k users equally share, 0 others.'''
        cases = [[2, 2, 0], [3, 0, 0, 0], [1, 1, 1, 0]]
        for case in cases:
            lg.debug("considering case: %s" % case)
            nonzeros = len([i for i in case if i != 0])
            exp_fairness = nonzeros / float(len(case))
            self.assertAlmostEqual(exp_fairness, fairness(case))

class AvailabilityTest(unittest.TestCase):

    def test_link_failure_combinations(self):
        '''Ensure number of link failures combinations is reasonable.'''
        g = OS3EWeightedGraph()
        for failures in range(5):
            fail_combos = link_failure_combinations(g, failures)
            self.assertEqual(len(fail_combos), choose(g.number_of_edges(), failures))

    def test_os3e(self):
        '''Validate coverage and availability are reasonable.'''
        link_fail_prob = 0.01
        g = OS3EGraph()
        apsp = dict(nx.all_pairs_shortest_path_length(g))
        apsp_paths = dict(nx.all_pairs_shortest_path(g))
        combos = [["Sunnyvale, CA", "Boston"],
                  ["Portland"],
                  ["Sunnyvale, CA", "Salt Lake City"],
                  ["Seattle", "Boston"],
                  ["Seattle", "Portland"]]
        weighted = False

        '''
        34 nodes
        42 edges
        pfail = 0.01
        p(good) =
            1 * p(success) * p(success) * ... 42 = 0.99 ** 42 =
            0.66228204098398347
        p(1 fail) =
            (42 choose 1) * (p(success) ** (42 - 1)) * p(fail) =
            42 * (0.99 ** 41) * 0.01 =
            0.27815845721
        p(2 fail) =
            (42 choose 2) * (p(success) ** (42 - 2)) * (p(fail) ** 2) =
            861 * (0.99 ** 40) * (0.01 ** 2) =
            0.05759846841
        p(3 fail) =
            (42 choose 3) * (p(success) ** (42 - 3)) * (p(fail) ** 3) =
            22960 * (0.99 ** 39) * (0.01 ** 3) =
            0.01551473896

        sum (0..1 failures) = 
            0.66228204098398347 + 0.27427842101356892 =
            0.93656046199755238
        error bar = 
            0.063439538002447615

        sum (0..2 failures) =
            0.66228204098398347 + 0.27427842101356892 + 0.055409782022943221 =
            0.99197024402049561
        error bar =
            0.00802

        sum (0..3 failures) =
          0.66228204098398347 + 0.27427842101356892 + 0.055409782022943221 +
              0.0072760319828107265 =
          0.99924627600330629
        error bar = 0.00075
        '''
        exp_coverage = {
            0: 0.65565922057,
            1: 0.27815845721,
            2: 0.05759846841,
            3: 0.01551473896
        }

        def get_coverage(f):
            '''Return expected coverage for given number of failures.'''
            return sum([v for k, v in exp_coverage.items() if k <= f])

        for combo in combos:
            for max_failures in range(3):
                a, c = availability_one_combo(g, combo, apsp, apsp_paths,
                                              weighted, link_fail_prob,
                                              max_failures)

                self.assertTrue(a < 1.0)
                self.assertTrue(c < 1.0)
                self.assertAlmostEqual(get_coverage(max_failures), c)

    def test_os3e_weighted(self):
        '''Ensure unit-weighted version of graph yields same availability.'''
        link_fail_prob = 0.01
        g = OS3EGraph()
        g_unit = set_unit_weights(g.copy())
        apsp = dict(nx.all_pairs_shortest_path_length(g))
        apsp_paths = dict(nx.all_pairs_shortest_path(g))

        combos = [["Sunnyvale, CA", "Boston"],
                  ["Portland"],
                  ["Sunnyvale, CA", "Salt Lake City"],
                  ["Seattle", "Boston"],
                  ["Seattle", "Portland"]]     
        for combo in combos:
            for max_failures in range(1, 2):
                a, c = availability_one_combo(g, combo, dict(apsp), apsp_paths,
                    False, link_fail_prob, max_failures)
                a_u, c_u = availability_one_combo(g_unit, combo, apsp,
                    apsp_paths, True, link_fail_prob, max_failures)
                self.assertAlmostEqual(a, a_u)
                self.assertAlmostEqual(c, c_u)


class LatencyTest(unittest.TestCase):

    def test_latency_bound(self):
        '''Ensure fraction of nodes within bound is reasonable.'''
        g = OS3EGraph()
        g_unit = set_unit_weights(g.copy())
        apsp = dict(nx.all_pairs_shortest_path_length(g))
        apsp_paths = dict(nx.all_pairs_shortest_path(g))
        path_lens = []
        for a in apsp:
            for b in apsp:
                path_lens.append(apsp[a][b])
        max_path_len = max(path_lens)
        combos = [["Sunnyvale, CA", "Boston"],
                  ["Portland"],
                  ["Sunnyvale, CA", "Salt Lake City"],
                  ["Seattle", "Boston"],
                  ["Seattle", "Portland"]]
        for combo in combos:
            one = fraction_within_latency(g, combo, apsp, max_path_len + 1.0)
            self.assertEqual(one, 1.0)
            two = fraction_within_latency(g, combo, apsp, 0.000001)
            self.assertEqual(two, len(combo) / float(g.number_of_nodes()))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()