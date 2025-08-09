# TEKNOFEST E-Commerce Datathon Specification

## 1. Competition Structure
- Two phases: 
  1. Datathon (Kaggle product ranking)
  2. Hackathon (term-product matching, UI, etc.)
- This document focuses on the Datathon phase.

## 2. Datathon Phase Goals
- Predict, for each session:
  - Which products will be clicked
  - Which product will be purchased
- Data provided:
  - Product info
  - User info
  - User session logs and statistics
- Evaluation:
  - Weighted Recall@K (click + purchase) per session
  - Final ranking based on Kaggle private leaderboard

## 3. Rules & Logistics
- Teams: 2–5 people, no individual participation
- No pre-existing projects allowed
- All code/models must be open and reproducible (no closed/proprietary solutions)
- No paid AI services (e.g., paid ChatGPT, Gemini) for the solution itself
- All team members must be registered on Kaggle with the same team
- No compute resources provided; use your own machines
- Data will be released right before the competition starts

## 4. Data Handling
- Raw data (~5GB) must be placed in `data/raw/` and is excluded from GitHub via `.gitignore`.
- Download via Kaggle CLI or manually, as described in the README.
- For EDA, use data samples for speed.
- Do not commit raw data to Git.

## 5. Collaboration & Best Practices
- Use GitHub for code sharing and version control.
- Assign roles: EDA, feature engineering, modeling, code review, etc.
- Use branches for experiments and review each other's code.
- Communicate regularly (chat, meetings).

## 6. Evaluation Metric
- Weighted Recall@K for both click and purchase predictions per session.
- Use the provided metric implementation in `src/evaluation/metrics.py`.

## 7. References
- For more details, see the official PDF in the root directory (excluded from GitHub).
- If stuck, review this file and the README, or consult the team.

---

*This file summarizes the main requirements and rules for the datathon phase. For the hackathon phase and further updates, refer to the official documentation and announcements.*
