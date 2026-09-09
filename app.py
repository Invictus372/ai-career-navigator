import streamlit as st

from utils.extract_text import extract_text
from utils.preprocess import preprocess_text
from utils.skill_match import SkillMatcher
from utils.match_score import ResumeMatcher
from utils.recommendation import RecommendationEngine
from utils.career_graph import CareerGraph


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Career Navigator",
    page_icon="🧭",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("🧭 AI Career Navigator")

st.write(
    "Upload your resume to analyze your skills, "
    "find suitable job roles, and identify skill gaps."
)


# -----------------------------
# Resume Upload
# -----------------------------

uploaded_file = st.file_uploader(
    "📄 Upload your resume",
    type=["pdf", "docx"]
)


if uploaded_file:

    st.success("Resume uploaded successfully!")


    # -----------------------------
    # Save Uploaded Resume
    # -----------------------------

    file_path = f"uploads/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())


    # -----------------------------
    # Extract Resume Text
    # -----------------------------

    resume_text = extract_text(file_path)

    if not resume_text:

        st.error(
            "Could not extract text from the resume."
        )

        st.stop()


    # -----------------------------
    # Preprocess Resume
    # -----------------------------

    processed_text = preprocess_text(
        resume_text
    )


    # -----------------------------
    # Extract Skills
    # -----------------------------

    skill_matcher = SkillMatcher()

    skills = skill_matcher.extract_skills(
        resume_text
    )


    # -----------------------------
    # Resume Matching
    # -----------------------------

    resume_matcher = ResumeMatcher()

    results = resume_matcher.calculate_similarity(
        resume_text
    )


    # -----------------------------
    # Recommended Role
    # -----------------------------

    best_role = results[0]["Role"]

    best_score = results[0]["Score"]


    # -----------------------------
    # Skill Recommendation
    # -----------------------------

    recommendation = RecommendationEngine()

    matched, missing = recommendation.recommend(
        skills,
        best_role
    )


    # -----------------------------
    # Resume Analysis
    # -----------------------------

    st.divider()

    st.header("📊 Resume Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🎯 Recommended Role",
            best_role
        )

    with col2:

        st.metric(
            "📊 Match Score",
            f"{best_score}%"
        )

    with col3:

        st.metric(
            "🧠 Skills Detected",
            len(skills)
        )


    # -----------------------------
    # Match Score Breakdown
    # -----------------------------

    st.subheader("📊 Match Score Breakdown")

    best_result = results[0]

    text_similarity = best_result[
        "Text Similarity"
    ]

    skill_coverage = best_result[
        "Skill Coverage"
    ]

    final_score = best_result[
        "Score"
    ]


    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📝 Text Similarity",
            f"{text_similarity}%"
        )

    with col2:

        st.metric(
            "🧠 Skill Coverage",
            f"{skill_coverage}%"
        )

    with col3:

        st.metric(
            "🎯 Final Match Score",
            f"{final_score}%"
        )


    st.progress(
        min(int(final_score), 100)
    )

    st.caption(
        "Final Score = 40% Text Similarity + "
        "60% Skill Coverage"
    )


    # -----------------------------
    # Extracted Skills
    # -----------------------------

    st.subheader("🧠 Extracted Skills")

    if skills:

        st.write(
            " • ".join(skills)
        )

    else:

        st.warning(
            "No known skills were detected."
        )


    # -----------------------------
    # Skill Analysis
    # -----------------------------

    st.subheader("🎯 Skill Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            "### ✅ Matched Skills"
        )

        if matched:

            for skill in matched:

                st.success(skill)

        else:

            st.info(
                "No matching skills found."
            )


    with col2:

        st.markdown(
            "### ❌ Missing Skills"
        )

        if missing:

            for skill in missing:

                st.error(skill)

        else:

            st.success(
                "No major required skills are missing!"
            )


    # -----------------------------
    # Top 5 Job Matches
    # -----------------------------

    st.subheader("🏆 Top 5 Job Matches")

    top_results = results[:5]

    chart_data = {
        "Role": [
            result["Role"]
            for result in top_results
        ],

        "Match Score": [
            result["Score"]
            for result in top_results
        ]
    }


    st.bar_chart(
        chart_data,
        x="Role",
        y="Match Score"
    )


    for rank, result in enumerate(
        top_results,
        start=1
    ):

        st.write(
            f"**{rank}. {result['Role']}** - "
            f"{result['Score']}%"
        )


    # -----------------------------
    # Career Path Optimization
    # -----------------------------

    st.divider()

    st.header(
        "🧭 Career Path Optimization"
    )

    st.write(
        "Select a target career role to explore "
        "possible career paths from your "
        "recommended role."
    )


    # Create career graph

    career_graph = CareerGraph()

    reachable_roles = career_graph.get_reachable_roles(
    best_role
    )

    target_options = [
    best_role
   ] + reachable_roles

    target_role = st.selectbox(
    "🎯 Select Target Role",
    target_options
    )
    

    st.write(
        f"**Current Role:** {best_role}"
    )

    st.write(
        f"**Target Role:** {target_role}"
    )


    # -----------------------------
    # Career Algorithms
    # -----------------------------

    if target_role != best_role:

        st.subheader("🔎 Career Paths")


        # -----------------------------
        # BFS
        # -----------------------------

        bfs_path = career_graph.bfs(
            best_role,
            target_role
        )

        st.markdown(
            "### 🔵 BFS Path"
        )

        if bfs_path:

            st.write(
                " → ".join(bfs_path)
            )

            st.caption(
                f"Transitions: {len(bfs_path) - 1}"
            )

        else:

            st.warning(
                "No BFS path found."
            )


        # -----------------------------
        # DFS
        # -----------------------------

        dfs_path = career_graph.dfs(
            best_role,
            target_role
        )

        st.markdown(
            "### 🟢 DFS Path"
        )

        if dfs_path:

            st.write(
                " → ".join(dfs_path)
            )

            st.caption(
                f"Transitions: {len(dfs_path) - 1}"
            )

        else:

            st.warning(
                "No DFS path found."
            )


        # -----------------------------
        # Dijkstra
        # -----------------------------

        dijkstra_path, dijkstra_cost = (
            career_graph.dijkstra(
                best_role,
                target_role,
                skills
            )
        )

        st.markdown(
            "### 🟠 Dijkstra Path"
        )

        if dijkstra_path:

            st.write(
                " → ".join(dijkstra_path)
            )

            st.metric(
                "Total Skill Gap Cost",
                dijkstra_cost
            )

            st.caption(
                f"Transitions: "
                f"{len(dijkstra_path) - 1}"
            )

        else:

            st.warning(
                "No Dijkstra path found."
            )


    else:

        st.info(
            "Select a target role different "
            "from your recommended role."
        )