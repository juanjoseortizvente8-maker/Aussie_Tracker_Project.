# 🇦🇺 Aussie Tracker Project

A personal development system designed to manage and visualize my journey to Australia. This project unifies my four growth pillars into a single Command Line Interface (CLI) tool.

## 🚀 Project Pillars
- **🏋️ Physical:** Detailed tracking of PPL (Push/Pull/Legs) workout sessions, including volume and weight progression.
- **💰 Financial:** "Aussie Fund" tracker with real-time currency conversion (PEN to USD) using the Open Exchange Rates API.
- **✅ Habits:** Daily accountability system for English fluency, Programming (Python/SQL), and Mental health.
- **💻 Programming:** A full-stack CLI application built with Python 3.13 and an Oracle XE Database.

## 🛠️ Tech Stack
- **Language:** Python 3.13
- **Database:** Oracle Database (via `oracledb`)
- **API Integration:** Real-time Exchange Rate JSON API
- **Version Control:** Git & GitHub

## 📂 Project Structure
- `main.py`: The "Command Center" or orchestrator of the entire system.
- `log_session.py`: Handles complex gym data entry (sets, reps, and RPE).
- `log_money.py`: Fetches internet rates to convert local savings into USD automatically.
- `view_*.py`: Data visualization scripts to track progress over time.

## ⚙️ How to Run

### 1. Prerequisites
- **Python 3.10+** installed.
- **Oracle Database XE** installed and running locally.

### 2. Install Dependencies
Open your terminal and run:
```bash
pip install oracledb requests
---
*Created with focus on consistency, discipline, and the Australian dream.*