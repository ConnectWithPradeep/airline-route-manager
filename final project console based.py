import sys
from trees.general_tree import GeneralTree
from trees.bst import FlightBST
from trees.avl_tree import AirportAVL
from trees.expression_tree import ExpressionTree
from graphs.graph_adt import GraphADT
from graphs.traversals import bfs_shortest_path, dfs_traversal, kosaraju_scc
from graphs.topological import kahns_topological_sort, detect_cycle_and_topological
from graphs.dijkstra import array_based_dijkstra, get_shortest_path, negative_edge_demonstration
from graphs.mst import prim_mst, kruskal_mst
from analysis.benchmarks import run_tree_benchmarks, run_graph_mst_benchmarks
from analysis.theory import THEORETICAL_DOCUMENTATION

def initialize_sample_data(gt, bst, avl, graph, mst_graph):
    gt.insert_airport("USA", "JFK")
    gt.insert_airport("USA", "LAX")
    gt.insert_airport("UK", "LHR")
    gt.insert_airport("UAE", "DXB")

    bst.insert(101, "JFK", 350.0)
    bst.insert(205, "LHR", 450.0)
    bst.insert(150, "DXB", 600.0)
    bst.insert(300, "LAX", 250.0)

    avl.insert(10, "JFK")
    avl.insert(20, "LHR")
    avl.insert(5, "DXB")
    avl.insert(15, "LAX")

    for u, v, w in [("JFK", "LHR", 400), ("LHR", "DXB", 300), ("JFK", "DXB", 750), ("DXB", "LAX", 900), ("LAX", "JFK", 500)]:
        graph.add_edge(u, v, w)

    for u, v, w in [("JFK", "LHR", 400), ("LHR", "DXB", 300), ("JFK", "DXB", 700), ("DXB", "LAX", 900)]:
        mst_graph.add_edge(u, v, w)

def main():
    gt = GeneralTree()
    bst = FlightBST()
    avl = AirportAVL()
    graph = GraphADT(directed=True)
    mst_graph = GraphADT(directed=False)

    initialize_sample_data(gt, bst, avl, graph, mst_graph)

    while True:
        print("\n" + "="*50)
        print("       AIRLINE ROUTE MANAGER – DSA PROJECT")
        print("="*50)
        print(" 1. Manage Country and Airport Tree")
        print(" 2. Manage Flight BST")
        print(" 3. Manage Airport AVL Tree")
        print(" 4. Fare Expression Calculator")
        print(" 5. Build/Edit Airline Flight Network")
        print(" 6. BFS and DFS Traversals")
        print(" 7. Strongly Connected Components (Kosaraju)")
        print(" 8. Topological Sorting and Cycle Detection")
        print(" 9. Cheapest Route – Dijkstra")
        print("10. Minimum Spanning Tree – Prim")
        print("11. Minimum Spanning Tree – Kruskal")
        print("12. Compare Prim and Kruskal & Benchmarks")
        print("13. Algorithm Analysis & Theory Documentation")
        print("14. Run Automated Tests")
        print("15. Exit")
        print("="*50)

        choice = input("Enter your choice (1-15): ").strip()

        if choice == '1':
            print("\n--- Country & Airport General Tree ---")
            print("1. Insert Airport\n2. Delete Node\n3. Display Hierarchy\n4. Traversals")
            sub = input("Select option: ").strip()
            if sub == '1':
                c = input("Enter Country Name: ")
                a = input("Enter Airport Name: ")
                if gt.insert_airport(c, a):
                    print(f"Successfully added airport {a} under {c}.")
                else:
                    print("Airport already exists.")
            elif sub == '2':
                name = input("Enter Country or Airport name to delete: ")
                if gt.delete_node(name):
                    print(f"Successfully deleted {name}.")
                else:
                    print("Node not found or cannot delete root.")
            elif sub == '3':
                gt.display_hierarchy()
            elif sub == '4':
                print("Preorder:", gt.preorder())
                print("Postorder:", gt.postorder())
                print("Level-order:", gt.level_order())

        elif choice == '2':
            print("\n--- Flight BST Manager ---")
            print("1. Insert Flight\n2. Search Flight\n3. Delete Flight\n4. Range Query\n5. Min/Max & Tree Stats")
            sub = input("Select option: ").strip()
            if sub == '1':
                try:
                    fn = int(input("Enter Flight Number (integer): "))
                    dest = input("Enter Destination: ")
                    fare = float(input("Enter Fare: "))
                    bst.insert(fn, dest, fare)
                    print(f"Flight {fn} inserted.")
                except ValueError:
                    print("Invalid input format.")
            elif sub == '2':
                try:
                    fn = int(input("Enter Flight Number to search: "))
                    node = bst.search(fn)
                    if node:
                        print(f"Found! Flight {node.flight_number} -> {node.destination} ($ {node.fare})")
                    else:
                        print("Flight not found.")
                except ValueError:
                    print("Invalid flight number.")
            elif sub == '3':
                try:
                    fn = int(input("Enter Flight Number to delete: "))
                    if bst.delete(fn):
                        print(f"Flight {fn} deleted.")
                    else:
                        print("Flight not found.")
                except ValueError:
                    print("Invalid number.")
            elif sub == '4':
                try:
                    low = int(input("Enter lower bound flight number: "))
                    high = int(input("Enter upper bound flight number: "))
                    results = bst.range_query(low, high)
                    print("Flights in range:", results)
                except ValueError:
                    print("Invalid bounds.")
            elif sub == '5':
                mi = bst.find_min()
                ma = bst.find_max()
                print(f"Min Flight: {mi.flight_number if mi else 'None'}")
                print(f"Max Flight: {ma.flight_number if ma else 'None'}")
                print(f"Tree Height: {bst.get_height()}")

        elif choice == '3':
            print("\n--- Airport AVL Tree Manager ---")
            print("1. Insert Airport\n2. Delete Airport\n3. Verify AVL Consistency\n4. View Rotation Traces")
            sub = input("Select option: ").strip()
            if sub == '1':
                try:
                    aid = int(input("Enter Airport numeric ID: "))
                    name = input("Enter Airport Name: ")
                    avl.insert(aid, name)
                    print(f"Inserted {aid} ({name}).")
                except ValueError:
                    print("Invalid ID.")
            elif sub == '2':
                try:
                    aid = int(input("Enter Airport numeric ID to delete: "))
                    avl.delete(aid)
                    print(f"Deleted (if existed).")
                except ValueError:
                    print("Invalid ID.")
            elif sub == '3':
                valid = avl.verify()
                print(f"AVL Tree Verification (BST order + balance factors): {'PASSED' if valid else 'FAILED'}")
            elif sub == '4':
                print("Rotation Traces:", avl.rotation_trace)

        elif choice == '4':
            print("\n--- Fare Expression Calculator ---")
            expr = input("Enter postfix expression (e.g., 'distance rate * surcharge +'): ")
            try:
                et = ExpressionTree(expr)
                print(f"Infix Expression: {et.to_infix()}")
                dist = float(input("Enter distance: "))
                rate = float(input("Enter rate per unit: "))
                surcharge = float(input("Enter surcharge: "))
                ans = et.evaluate({"distance": dist, "rate": rate, "surcharge": surcharge})
                print(f"Evaluated Fare Total: $ {ans:.2f}")
            except Exception as e:
                print("Error:", e)

        elif choice == '5':
            u = input("Enter source airport: ")
            v = input("Enter destination airport: ")
            try:
                w = float(input("Enter fare/weight: "))
                graph.add_edge(u, v, w)
                mst_graph.add_edge(u, v, w)
                print("Flight route added successfully.")
            except ValueError:
                print("Invalid weight.")

        elif choice == '6':
            print("\n--- BFS and DFS Traversals ---")
            start = input("Enter start airport: ")
            target = input("Enter target airport for BFS route: ")
            path = bfs_shortest_path(graph, start, target)
            print(f"BFS Fewest Layovers Route: {path}")
            dfs_res = dfs_traversal(graph)
            print("DFS Discovery Times:", dfs_res['discovery'])
            print("DFS Edge Classifications:", dfs_res['edges'])

        elif choice == '7':
            sccs = kosaraju_scc(graph)
            print("Strongly Connected Components:", sccs)

        elif choice == '8':
            print("\n--- Topological Sorting & Cycle Detection ---")
            order, err = kahns_topological_sort(graph)
            if err:
                print("Kahn's Sort Notice:", err)
                _, cycle = detect_cycle_and_topological(graph)
                print("Detected Cycle Path:", cycle)
            else:
                print("Topological Order:", order)

        elif choice == '9':
            print("\n--- Dijkstra's Shortest Path ---")
            start = input("Enter start airport: ")
            target = input("Enter target airport: ")
            dist, pred, _ = array_based_dijkstra(graph, start)
            if dist and target in dist:
                print(f"Cheapest Fare to {target}: $ {dist[target]}")
                print(f"Complete Route: {get_shortest_path(pred, start, target)}")
            else:
                print("No path found.")
            print("\nNegative Edge Demo:", negative_edge_demonstration())

        elif choice == '10':
            edges, cost = prim_mst(mst_graph)
            print(f"Prim's MST Total Cost: {cost}")
            print("Edges:", edges)

        elif choice == '11':
            edges, cost = kruskal_mst(mst_graph)
            print(f"Kruskal's MST Total Cost: {cost}")
            print("Edges:", edges)

        elif choice == '12':
            print("\n--- Benchmarking Suite ---")
            print("Running tree benchmarks (BST vs AVL)...")
            tree_res = run_tree_benchmarks()
            for r in tree_res:
                print(r)
            print("Running MST benchmarks...")
            mst_res = run_graph_mst_benchmarks()
            for r in mst_res:
                print(r)

        elif choice == '13':
            print(THEORETICAL_DOCUMENTATION)

        elif choice == '14':
            import unittest
            from tests.test_suite import AirlineRouteManagerTestSuite
            suite = unittest.TestLoader().loadTestsFromTestCase(AirlineRouteManagerTestSuite)
            unittest.TextTestRunner().run(suite)

        elif choice == '15':
            print("Exiting Airline Route Manager. Have a safe flight!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select between 1 and 15.")

if __name__ == "__main__":
    main()
