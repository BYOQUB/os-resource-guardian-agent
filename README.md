# OS Resource Guardian Agent

**An AI-inspired Operating System monitoring and troubleshooting assistant**

This project was created for the Operating Systems course project milestone. It demonstrates an **Observe → Think → Act** agentic workflow using real operating system resource data.

## Project Overview

Many users experience a slow computer but do not know the exact reason. The issue may be caused by high CPU usage, high memory usage, low disk space, or a process consuming too many system resources.

**OS Resource Guardian Agent** solves this problem by monitoring system resources, analyzing the current condition, and generating safe recommendations for the user.

## Real-World Problem It Solves

When a computer becomes slow, a normal user may not know whether the problem is caused by:

- CPU overload
- High RAM usage
- Low disk space
- Heavy background processes
- Too many applications running at the same time

This agent helps by collecting OS-level data and explaining the problem in simple language.

## Why This Project Is Related to Operating Systems

The project uses important OS concepts:

- Process monitoring
- CPU usage
- Memory usage
- Disk usage
- Resource allocation
- System performance analysis
- Safe user-level troubleshooting

## Agentic AI Workflow

The project follows the **Observe → Think → Act** structure.

### 1. Observe

The agent collects real-time system data:

- CPU usage
- Memory usage
- Disk usage
- Running processes
- Top CPU-consuming processes
- Top memory-consuming processes

### 2. Think

The agent analyzes the collected data and classifies the system status as:

- Normal
- Warning
- Critical

### 3. Act

The agent generates safe recommendations and creates a system health report. It does not automatically delete files or terminate processes without user permission.

## System Architecture Diagram

![System Diagram](assets/system_diagram.png)

## Features

- Real-time CPU monitoring
- Real-time RAM monitoring
- Disk usage monitoring
- Top process detection
- Rule-based agent decision-making
- Safe troubleshooting recommendations
- System health report generation
- CLI demo
- Optional Streamlit dashboard
- GenAI prompt generator for ChatGPT / Claude / Perplexity explanations

## Tech Stack

| Part | Technology |
|---|---|
| Programming Language | Python |
| OS Monitoring | psutil |
| Data Handling | pandas |
| Dashboard | Streamlit |
| Report Format | TXT / JSON |
| GenAI Support | ChatGPT / Claude / Perplexity prompt generation |

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/os-resource-guardian-agent.git
cd os-resource-guardian-agent
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

For Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run CLI Demo

```bash
python cli.py
```

Save reports:

```bash
python cli.py --save
```

Show GenAI prompt:

```bash
python cli.py --genai-prompt
```

## Run Dashboard

```bash
streamlit run app.py
```

## Example Output

```text
OS Resource Guardian Agent - System Health Report
==========================================================
CPU Usage: 45.2%
Memory Usage: 68.1%
Disk Usage: 72.0%
Overall Status: Normal
Health Score: 95/100
Recommendation: No urgent action is required.
```

## 4-Week Milestone Plan

| Week | Milestone |
|---|---|
| Week 1 | Project idea, real-world problem, system architecture, and initial resource collector |
| Week 2 | CPU, memory, disk, and process monitoring; rule-based analysis engine |
| Week 3 | Recommendation generator, report generation, and Streamlit dashboard |
| Week 4 | Testing, GitHub upload, demo video, LinkedIn post, final presentation |

## Current Milestone 2 Status

- Project topic finalized
- Real-world problem defined
- System architecture designed
- Python project structure created
- OS monitoring code implemented
- Agent analysis engine implemented
- Recommendation system implemented
- Report generator implemented
- GitHub-ready project prepared
- Demo video script prepared
- LinkedIn post prepared

## Safety Design

The agent is designed to be safe. It recommends actions but does not automatically kill processes, delete files, or modify system settings without user confirmation.

## Author

**Boymuratov Yokubjon Usmonovich**  
Operating Systems Course Project  
Spring 2026

## License

This project is released under the MIT License.
