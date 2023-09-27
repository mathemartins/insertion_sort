import sys


def nearest_neighbor(graph):
    num_cities = len(graph)
    visited = [False] * num_cities
    tour = []

    current_city = 0
    tour.append(current_city)
    visited[current_city] = True

    for _ in range(num_cities - 1):
        nearest_city = None
        min_distance = sys.maxsize

        for city in range(num_cities):
            if not visited[city] and graph[current_city][city] < min_distance:
                nearest_city = city
                min_distance = graph[current_city][city]

        tour.append(nearest_city)
        visited[nearest_city] = True
        current_city = nearest_city

    # Return to the starting city to complete the tour
    tour.append(tour[0])

    return tour


# Example usage:
if __name__ == "__main__":
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    # Find the tour using the Nearest Neighbor Algorithm
    tour = nearest_neighbor(distance_matrix)

    print("Optimal Tour Sequence:", tour)

# # The Traveling Salesman Problem (TSP) is a classic optimization problem in computer science and mathematics. The
# problem can be defined as follows: Given a list of cities and the distances between each pair of cities,
# the task is to find the shortest possible route that visits each city exactly once and returns to the original
# city. The TSP is known to be NP-hard, meaning that there is no known efficient algorithm to solve it optimally for
# large instances in polynomial time. Therefore, we often use approximation algorithms to find good solutions.

# One common approach to solving the TSP is the Nearest Neighbor Algorithm, which is a simple and greedy heuristic
# method. Here's an outline of the algorithm:
#
# ### Nearest Neighbor Algorithm for TSP:
#
# 1. Start at a randomly chosen city as the initial city.
# 2. While there are unvisited cities:
#    a. Select the nearest unvisited city to the current city.
#    b. Add the selected city to the tour and mark it as visited.
#    c. Set the selected city as the current city.
# 3. Return to the starting city to complete the tour.
#
# #### Complexity Analysis:
#
# 1. **General Complexity and Efficiency**: The TSP is known to be an NP-hard problem, which means that its
# complexity grows exponentially with the number of cities. Therefore, finding the optimal solution for large
# instances is not practically feasible. Instead, we often resort to approximation algorithms like the Nearest
# Neighbor Algorithm, which provide reasonably good solutions quickly but may not always be optimal.
#
# 2. **Runtime Efficiency (Big O Notation)**: The runtime efficiency of the Nearest Neighbor Algorithm depends on the
# number of cities (n). The algorithm iterates through all cities in each step, and for each city, it calculates
# distances to all unvisited cities. Therefore, the time complexity of this algorithm is O(n^2) in the worst case.
# However, this complexity can be improved using data structures like priority queues to find the nearest neighbor
# more efficiently.
#
# 3. **Complexity Classification of the Algorithm**: The Nearest Neighbor Algorithm is a greedy algorithm,
# which means it makes a series of locally optimal choices at each step without considering the global optimal
# solution. As a result, it can find good solutions quickly but may not always find the best solution. The
# algorithm's complexity classification is typically O(n^2), but with optimizations, it can be made more efficient.
#
# Keep in mind that the TSP is a well-studied problem, and there are various algorithms and techniques for solving
# it, including exact algorithms like branch and bound, dynamic programming, and more sophisticated heuristics and
# metaheuristics. The choice of algorithm depends on the problem size and the trade-off between solution quality and
# computation time.