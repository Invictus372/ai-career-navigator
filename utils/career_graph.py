from collections import deque
import pandas as pd
import heapq


class CareerGraph:

    def __init__(self):

        self.graph = {
    "Data Analyst": [
        "Business Analyst",
        "Data Scientist"
    ],

    "Business Analyst": [
        "Data Analyst",
        "Data Scientist"
    ],

    "Data Scientist": [
    "Machine Learning Engineer",
    "AI Engineer",
    "Data Engineer",
    "Data Analyst"
   ],

    "Machine Learning Engineer": [
        "AI Engineer",
        "Data Scientist"
    ],

    "AI Engineer": [
        "NLP Engineer",
        "GenAI Engineer"
    ],

    "NLP Engineer": [
        "AI Engineer",
        "GenAI Engineer"
    ],

    "GenAI Engineer": [
        "AI Engineer"
    ],

    "Python Developer": [
        "Backend Developer",
        "Data Engineer",
        "Data Scientist"
    ],

    "Backend Developer": [
    "Software Engineer",
    "Full Stack Developer",
    "Data Engineer"
   ],

    "Java Developer": [
        "Backend Developer",
        "Software Engineer"
    ],

    "Software Engineer": [
        "Backend Developer",
        "Full Stack Developer"
    ],

    "Full Stack Developer": [
        "Software Engineer",
        "Backend Developer"
    ],

    "Data Engineer": [
        "Data Scientist",
        "Machine Learning Engineer"
    ],

    "Cloud Engineer": [
        "Data Engineer",
        "Backend Developer"
    ]
}

    def get_graph(self):
        return self.graph

    def bfs(self, start, target):
        """
        Find the shortest career path using Breadth-First Search.
        """

        if start not in self.graph:
            return []

        queue = deque([[start]])

        visited = {start}

        while queue:

            path = queue.popleft()

            current = path[-1]

            if current == target:
                return path

            for neighbor in self.graph.get(current, []):

                if neighbor not in visited:

                    visited.add(neighbor)

                    new_path = path + [neighbor]

                    queue.append(new_path)

        return []
    def dfs(self, start, target):
        """
        Find a career path using Depth-First Search.
        """

        if start not in self.graph:
            return []

        visited = set()

        def search(current, path):

            if current == target:
                return path

            visited.add(current)

            for neighbor in self.graph.get(current, []):

                if neighbor not in visited:

                    result = search(
                        neighbor,
                        path + [neighbor]
                    )

                    if result:
                        return result

            return []

        return search(start, [start])
    
    def calculate_transition_cost(
        self,
        current_role,
        next_role,
        candidate_skills,
        roles_file="data/roles.csv"
    ):
        """
        Calculate career transition cost based on
        the candidate's missing skills for the next role.
        """

        roles = pd.read_csv(roles_file)

        next_data = roles[
            roles["Role"] == next_role
        ]

        if next_data.empty:
            return float("inf")

        candidate_skills = {
            skill.strip().lower()
            for skill in candidate_skills
        }

        next_skills = {
            skill.strip().lower()
            for skill in next_data.iloc[0]["Skills"].split(",")
        }

        missing_skills = next_skills - candidate_skills

        return len(missing_skills)
    def dijkstra(
        self,
        start,
        target,
        candidate_skills
    ):
        """
        Find the lowest skill-gap career path
        using Dijkstra's algorithm.
        """

        if start not in self.graph:
            return [], float("inf")

        distances = {
            role: float("inf")
            for role in self.graph
        }

        distances[start] = 0

        priority_queue = [
            (0, start, [start])
        ]

        visited = set()

        while priority_queue:

            current_cost, current_role, path = heapq.heappop(
                priority_queue
            )

            if current_role in visited:
                continue

            visited.add(current_role)

            if current_role == target:
                return path, current_cost

            for neighbor in self.graph.get(
                current_role, []
            ):

                transition_cost = (
                    self.calculate_transition_cost(
                        current_role,
                        neighbor,
                        candidate_skills
                    )
                )

                new_cost = (
                    current_cost + transition_cost
                )

                if new_cost < distances.get(
                    neighbor,
                    float("inf")
                ):

                    distances[neighbor] = new_cost

                    heapq.heappush(
                        priority_queue,
                        (
                            new_cost,
                            neighbor,
                            path + [neighbor]
                        )
                    )

        return [], float("inf")
    def get_reachable_roles(self, start):
        """
        Return all roles that can be reached from the start role.
        """

        if start not in self.graph:
            return []

        visited = set()
        queue = deque([start])

        while queue:

            current = queue.popleft()

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.graph.get(
                current,
                []
            ):

                if neighbor not in visited:
                    queue.append(neighbor)

        visited.remove(start)

        return sorted(visited)