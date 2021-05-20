#!/usr/bin/env python
'''Generate a network topology corresponding to the Internet2 OS3E.

Info: at http://www.internet2.edu/network/ose

Graph source: http://www.internet2.edu/pubs/OS3Emap.pdf

34 nodes, 42 edges

May not be 100% accurate: 
    Vancouver, Miami are dashed links
    New York is two parallel links between two nodes
    Houston to Baton Rouge has two parallel links
    Sunnyvale, CA to [Portland, Salt Lake] may share a span
'''
import networkx as nx

def OS3EGraph():
    g = nx.Graph()
    nx.add_path(g, ["Vancouver", "Seattle"])
    nx.add_path(g, ["Seattle", "Missoula", "Minneapolis", "Chicago"])
    nx.add_path(g, ["Seattle", "Salt Lake City"])
    nx.add_path(g, ["Seattle", "Portland", "Sunnyvale, CA"])
    nx.add_path(g, ["Sunnyvale, CA", "Salt Lake City"])
    nx.add_path(g, ["Sunnyvale, CA", "Los Angeles"])
    nx.add_path(g, ["Los Angeles", "Salt Lake City"])
    nx.add_path(g, ["Los Angeles", "Tucson", "El Paso, TX"])
    nx.add_path(g, ["Salt Lake City", "Denver"])
    nx.add_path(g, ["Denver", "Albuquerque", "El Paso, TX"])
    nx.add_path(g, ["Denver", "Kansas City, MO", "Chicago"])
    nx.add_path(g, ["Kansas City, MO", "Dallas", "Houston"])
    nx.add_path(g, ["El Paso, TX", "Houston"])
    nx.add_path(g, ["Houston", "Jackson, MS", "Memphis", "Nashville"])
    nx.add_path(g, ["Houston", "Baton Rouge", "Jacksonville"])
    nx.add_path(g, ["Chicago", "Indianapolis", "Louisville", "Nashville"])
    nx.add_path(g, ["Nashville", "Atlanta"])
    nx.add_path(g, ["Atlanta", "Jacksonville"])
    nx.add_path(g, ["Jacksonville", "Miami"])
    nx.add_path(g, ["Chicago", "Cleveland"])
    nx.add_path(g, ["Cleveland", "Buffalo", "Boston", "New York", "Philadelphia", "Washington DC"])
    nx.add_path(g, ["Cleveland", "Pittsburgh", "Ashburn, VA", "Washington DC"])
    nx.add_path(g, ["Washington DC", "Raleigh, NC", "Atlanta"])
    return g
