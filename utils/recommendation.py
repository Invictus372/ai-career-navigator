import pandas as pd


class RecommendationEngine:

    def __init__(self,
                 roles_file="data/roles.csv"):

        self.roles = pd.read_csv(roles_file)

    def recommend(self,
                  extracted_skills,
                  top_role):

        role_data = self.roles[
            self.roles["Role"] == top_role
        ]

        if role_data.empty:
            return [], []

        required_skills = role_data.iloc[0]["Skills"]

        required_skills = [
            skill.strip()
            for skill in required_skills.split(",")
        ]

        matched = []

        missing = []

        for skill in required_skills:

            if skill.lower() in [
                s.lower() for s in extracted_skills
            ]:
                matched.append(skill)

            else:
                missing.append(skill)

        return matched, missing