# Adversarial AI Recruiting Council

A multi-agent recruiting evaluation system built on [Band](https://band.ai), where four AI agents debate a candidate's CV through structured adversarial deliberation before reaching a final hiring verdict.

## How It Works

Instead of a single AI giving a one-shot opinion, this system runs a candidate's CV through four distinct agents who each play a different role in the debate — similar to how a real hiring committee deliberates.

CV submitted

↓

Skeptic        → finds every red flag and reason NOT to hire

↓ (@mentions)

Investigator   → fact-checks claims, finds gaps and inconsistencies

↓ (@mentions)

DevilsAdvocate → defends the candidate, counters the criticism

↓ (@mentions)

Recruiter      → weighs all sides, gives final HIRE / NO HIRE verdict

Each agent only sees the conversation when explicitly @mentioned, and passes full context (CV + all prior analysis) forward to the next agent — powered by Band's real-time agent-to-agent messaging.

## Tech Stack

- **Band SDK** — agent orchestration, WebSocket-based agent-to-agent communication
- **Google Gemini 2.5 Flash** — reasoning engine for all 4 agents (via Google ADK Adapter)
- **Python** — agent runtime

## Why This Matters

Most AI recruiting tools give a single confident answer. This system surfaces disagreement on purpose — a candidate's CV is attacked, defended, and only then judged, producing a more transparent and defensible hiring recommendation.

## Setup

1. Clone this repo
2. Install dependencies:
   - pip install uv
   - uv add "band-sdk[google-adk]"
   - uv add python-dotenv
3. Copy `.env.example` to `.env` and fill in your own keys (Google Gemini API key, Band agent IDs/keys)
4. Copy `agent_config.example.yaml` to `agent_config.yaml` and fill in your Band agent credentials
5. Run each agent in a separate terminal:
   - uv run python skeptic_agent.py
   - uv run python investigator_agent.py
   - uv run python da_agent.py
   - uv run python recruiter_agent.py
6. In Band, create a chat room, add all 4 agents, and @mention the Skeptic with a candidate CV to start the pipeline.

## Demo

https://drive.google.com/file/d/1vm7Dq3jkWU9X6Y8Z_KwQRLa-9ai4CtC-/view?usp=drive_link

## Built For

LabLab Band of Agents Hackathon — built by Himani Chaubey & Bhavya Chokshi
