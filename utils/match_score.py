import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.preprocess import preprocess_text
from utils.skill_match import SkillMatcher


class ResumeMatcher:

    def __init__(
        self,
        jobs_file="data/jobs.csv",
        roles_file="data/roles.csv"
    ):

        self.jobs = pd.read_csv(jobs_file)
        self.roles = pd.read_csv(roles_file)

        self.vectorizer = TfidfVectorizer()

        self.skill_matcher = SkillMatcher()

        # Preprocess all job descriptions once
        self.job_texts = [
            preprocess_text(text)
            for text in self.jobs["Job Description"]
        ]

        # Create TF-IDF representation for all jobs
        self.job_vectors = self.vectorizer.fit_transform(
            self.job_texts
        )

    def calculate_similarity(self, resume_text):

        cleaned_resume = preprocess_text(resume_text)

        # Convert resume into TF-IDF vector
        resume_vector = self.vectorizer.transform(
            [cleaned_resume]
        )

        # Compare resume with every job description
        similarities = cosine_similarity(
            resume_vector,
            self.job_vectors
        )[0]

        # Extract normalized skills from resume
        resume_skills = self.skill_matcher.extract_skills(
            resume_text
        )

        resume_skills = {
            skill.lower()
            for skill in resume_skills
        }

        scores = []

        for index, row in self.jobs.iterrows():

            role = row["Role"]

            # -----------------------------
            # 1. Text Similarity
            # -----------------------------

            text_similarity = similarities[index] * 100

            # -----------------------------
            # 2. Required Skills
            # -----------------------------

            role_data = self.roles[
                self.roles["Role"] == role
            ]

            required_skills = []

            if not role_data.empty:

                required_skills = [
                    skill.strip().lower()
                    for skill in role_data.iloc[0]["Skills"].split(",")
                ]

            # -----------------------------
            # 3. Matched & Missing Skills
            # -----------------------------

            matched_skills = [
                skill
                for skill in required_skills
                if skill in resume_skills
            ]

            missing_skills = [
                skill
                for skill in required_skills
                if skill not in resume_skills
            ]

            # -----------------------------
            # 4. Skill Coverage
            # -----------------------------

            if required_skills:

                skill_coverage = (
                    len(matched_skills)
                    / len(required_skills)
                ) * 100

            else:

                skill_coverage = 0

            # -----------------------------
            # 5. Final Score
            # -----------------------------

            final_score = (
                (text_similarity * 0.40)
                + (skill_coverage * 0.60)
            )

            scores.append({
                "Role": role,
                "Score": float(round(final_score, 2)),
                "Text Similarity": float(
                    round(text_similarity, 2)
                ),
                "Skill Coverage": float(
                    round(skill_coverage, 2)
                ),
                "Matched Skills": matched_skills,
                "Missing Skills": missing_skills
            })

        return sorted(
            scores,
            key=lambda x: x["Score"],
            reverse=True
        )