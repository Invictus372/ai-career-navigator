import pandas as pd


class SkillMatcher:

    def __init__(self, skills_file="data/skills.csv"):

        self.skills = (
            pd.read_csv(skills_file)["skill"]
            .str.lower()
            .tolist()
        )

        self.aliases = {
            "ml": "machine learning",
            "machine-learning": "machine learning",
             "powerbi": "power bi",
            "power-bi": "power bi",
    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",
    "restapi": "rest api",
    "restful api": "rest api",
    "restful apis": "rest api",
    "postgres": "postgresql",
    "tensorflow": "tensorflow",
    "pytorch": "pytorch"
        }

    def extract_skills(self, text):

        text = text.lower()

        matched = []

        # Check standard skills
        for skill in self.skills:

            if skill in text:
                matched.append(skill.title())

        # Check aliases
        for alias, standard_skill in self.aliases.items():

            if alias in text:

                matched.append(
                    standard_skill.title()
                )

        return sorted(set(matched))