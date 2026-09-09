from utils.match_score import ResumeMatcher
from utils.career_graph import CareerGraph
from utils.skill_match import SkillMatcher
from utils.recommendation import RecommendationEngine


resume = """
Python
SQL
Git
Linux
"""


# -----------------------------
# Extract Skills
# -----------------------------

skill_matcher = SkillMatcher()

skills = skill_matcher.extract_skills(resume)

print("\nExtracted Skills")
print(skills)


# -----------------------------
# Resume Matching
# -----------------------------

resume_matcher = ResumeMatcher()

results = resume_matcher.calculate_similarity(resume)

print("\nTop Matching Roles")

for result in results[:5]:

    print(
        f"\n{result['Role']}"
    )

    print(
        f"Final Score: {result['Score']}%"
    )

    print(
        f"Text Similarity: "
        f"{result['Text Similarity']}%"
    )

    print(
        f"Skill Coverage: "
        f"{result['Skill Coverage']}%"
    )

    print(
        f"Matched Skills: "
        f"{result['Matched Skills']}"
    )

    print(
        f"Missing Skills: "
        f"{result['Missing Skills']}"
    )


# -----------------------------
# Best Role
# -----------------------------

best_role = results[0]["Role"]

print("\nRecommended Role")
print(best_role)


# -----------------------------
# Matched / Missing Skills
# -----------------------------

engine = RecommendationEngine()

matched, missing = engine.recommend(
    skills,
    best_role
)

print("\nMatched Skills")
print(matched)

print("\nMissing Skills")
print(missing)


# -----------------------------
# Career Graph
# -----------------------------

print("\nCareer Graph")

career_graph = CareerGraph()

graph = career_graph.get_graph()

for role, transitions in graph.items():

    print(
        f"{role} -> {transitions}"
    )


# -----------------------------
# BFS Career Path
# -----------------------------

print("\nBFS Career Path")

path = career_graph.bfs(
    best_role,
    "GenAI Engineer"
)

print(path)

        # -----------------------------
# DFS Career Path
# -----------------------------

print("\nDFS Career Path")

path = career_graph.dfs(
    best_role,
    "GenAI Engineer"
)

print(path)

# -----------------------------
# Career Transition Cost
# -----------------------------

print("\nCareer Transition Cost")

cost = career_graph.calculate_transition_cost(
    "Data Analyst",
    "Data Scientist",
    skills
)

print(
    f"Data Analyst -> Data Scientist: "
    f"Cost = {cost}"
)

# -----------------------------
# Dijkstra Career Path
# -----------------------------

print("\nDijkstra Career Path")

path, cost = career_graph.dijkstra(
    best_role,
    "GenAI Engineer",
    skills
)

print(
    f"Path: {path}"
)

print(
    f"Total Skill Gap Cost: {cost}"
)

# -----------------------------
# Reachable Career Roles
# -----------------------------

print("\nReachable Career Roles")

reachable_roles = career_graph.get_reachable_roles(
    best_role
)

print(reachable_roles)