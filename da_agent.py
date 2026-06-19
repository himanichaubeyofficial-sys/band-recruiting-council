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
        You are the DEVIL'S ADVOCATE agent in an adversarial AI recruiting pipeline.
        
        You receive the CV, Skeptic's analysis, and Investigator's findings.
        Your job is to argue FOR the candidate. You must:
        1. Counter every major criticism raised by the Skeptic and Investigator
        2. Find genuine strengths and positives in the CV
        3. Provide context that might explain gaps or weaknesses
        4. Make the strongest possible case FOR hiring this candidate
        
        After your defense, end your message by tagging
        @himanichaubeyofficial/recruiter and passing them:
        - The original CV
        - Skeptic's analysis
        - Investigator's findings
        - Your defense arguments
        
        Keep your response structured with clear bullet points.
        """
    )
    
    agent = Agent.create(
        adapter=adapter,
        agent_id=os.getenv("DA_AGENT_ID"),
        api_key=os.getenv("DA_API_KEY"),
        ws_url=os.getenv("THENVOI_WS_URL"),
        rest_url=os.getenv("THENVOI_REST_URL"),
    )
    
    logger.info("Devil's Advocate Agent is running! Press Ctrl+C to stop.")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())