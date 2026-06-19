import asyncio
import os
import logging
from dotenv import load_dotenv
from band import Agent
from band.adapters import GoogleADKAdapter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    load_dotenv()
    
    adapter = GoogleADKAdapter(
        model="gemini-2.5-flash",
        custom_section="""
        You are the RECRUITER agent — the final decision-maker in an adversarial 
        AI recruiting pipeline.
        
        You receive the full debate: the original CV, Skeptic's red flags,
        Investigator's fact-check, and Devil's Advocate's defense.
        
        You must:
        1. Summarize the key arguments from all three agents
        2. Weigh the evidence objectively
        3. Give a final structured verdict:
        
        CANDIDATE: [Name]
        ROLE APPLIED FOR: [Role]
        OVERALL SCORE: [X/10]
        
        STRENGTHS:
        - [bullet points]
        
        WEAKNESSES:
        - [bullet points]
        
        FINAL DECISION: HIRE / NO HIRE / MAYBE
        REASONING: [2-3 sentences explaining your decision]
        
        Your verdict is final. Be decisive and professional.
        """
    )
    
    agent = Agent.create(
        adapter=adapter,
        agent_id=os.getenv("RECRUITER_AGENT_ID"),
        api_key=os.getenv("RECRUITER_API_KEY"),
        ws_url=os.getenv("THENVOI_WS_URL"),
        rest_url=os.getenv("THENVOI_REST_URL"),
    )
    
    logger.info("Recruiter Agent is running! Press Ctrl+C to stop.")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())