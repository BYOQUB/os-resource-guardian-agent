"""Streamlit dashboard for OS Resource Guardian Agent."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.analyzer import analyze_snapshot
from src.collector import collect_snapshot
from src.recommender import build_genai_prompt, generate_recommendations
from src.reporter import format_report


st.set_page_config(page_title="OS Resource Guardian Agent", page_icon="🛡️", layout="wide")
st.title("🛡️ OS Resource Guardian Agent")
st.caption("An AI-inspired operating system monitoring and troubleshooting assistant")

if "snapshot" not in st.session_state:
    st.session_state.snapshot = None

if st.button("Run System Check", type="primary"):
    with st.spinner("Collecting CPU, memory, disk, and process data..."):
        st.session_state.snapshot = collect_snapshot(limit=5)

if st.session_state.snapshot is None:
    st.info("Click **Run System Check** to start the Observe → Think → Act workflow.")
    st.stop()

snapshot = st.session_state.snapshot
analysis = analyze_snapshot(snapshot)
recommendations = generate_recommendations(snapshot, analysis)

status_color = {"Normal": "green", "Warning": "orange", "Critical": "red"}.get(analysis.status, "gray")
st.markdown(f"### Status: :{status_color}[{analysis.status}]  |  Health Score: **{analysis.score}/100**")

col1, col2, col3 = st.columns(3)
col1.metric("CPU Usage", f"{snapshot.cpu_percent}%")
col2.metric("Memory Usage", f"{snapshot.memory_percent}%", f"{snapshot.memory_available_gb} GB available")
col3.metric("Disk Usage", f"{snapshot.disk_percent}%", f"{snapshot.disk_free_gb} GB free")

st.subheader("Findings")
for finding in analysis.findings:
    st.write(f"- **{finding.level} | {finding.category}:** {finding.message}")

st.subheader("Recommendations")
for rec in recommendations:
    st.success(rec) if analysis.status == "Normal" else st.warning(rec)

st.subheader("Top CPU Processes")
st.dataframe(pd.DataFrame([p.to_dict() for p in snapshot.top_cpu_processes]), use_container_width=True)

st.subheader("Top Memory Processes")
st.dataframe(pd.DataFrame([p.to_dict() for p in snapshot.top_memory_processes]), use_container_width=True)

with st.expander("Show GenAI Prompt"):
    st.code(build_genai_prompt(snapshot, analysis), language="text")

with st.expander("Show Full Text Report"):
    st.code(format_report(snapshot, analysis, recommendations), language="text")
