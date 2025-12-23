import numpy as np

class ACO:
    def __init__(self, distance_matrix, n_ants, n_iterations, alpha, beta, evaporation_rate, Q):
        self.distances = distance_matrix
        self.n_cities = len(distance_matrix)
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.Q = Q
        self.pheromone = np.ones((self.n_cities, self.n_cities))
        self.best_path = None
        self.best_distance = float('inf')
        self.history = []
    
    def run(self):
        for iteration in range(self.n_iterations):
            paths = []
            path_distances = []
            
            for ant in range(self.n_ants):
                path = self.construct_solution()
                distance = self.calculate_path_distance(path)
                paths.append(path)
                path_distances.append(distance)
                
                if distance < self.best_distance:
                    self.best_distance = distance
                    self.best_path = path
            
            self.update_pheromone(paths, path_distances)
            self.history.append(self.best_distance)
        
        return self.best_path, self.best_distance, self.history
    
    def construct_solution(self):
        path = [0]
        visited = set([0])
        
        while len(visited) < self.n_cities:
            current = path[-1]
            next_city = self.select_next_city(current, visited)
            path.append(next_city)
            visited.add(next_city)
        
        path.append(0)
        return path
    
    def select_next_city(self, current, visited):
        unvisited = [i for i in range(self.n_cities) if i not in visited]
        probabilities = []
        
        for city in unvisited:
            pheromone = self.pheromone[current][city] ** self.alpha
            visibility = (1.0 / self.distances[current][city]) ** self.beta if self.distances[current][city] > 0 else 0
            probabilities.append(pheromone * visibility)
        
        probabilities = np.array(probabilities)
        probabilities = probabilities / probabilities.sum()
        
        return np.random.choice(unvisited, p=probabilities)
    
    def calculate_path_distance(self, path):
        return sum(self.distances[path[i]][path[i+1]] for i in range(len(path)-1))
    
    def update_pheromone(self, paths, path_distances):
        self.pheromone *= (1 - self.evaporation_rate)
        
        for path, distance in zip(paths, path_distances):
            deposit = self.Q / distance
            for i in range(len(path)-1):
                self.pheromone[path[i]][path[i+1]] += deposit
                self.pheromone[path[i+1]][path[i]] += deposit

