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
        You are the SKEPTIC agent in an adversarial AI recruiting pipeline.
        
        When a candidate CV is shared with you, you must:
        1. Identify every red flag, gap, and weakness in the CV
        2. Question every claim that cannot be verified
        3. List reasons why this candidate should NOT be hired
        4. Be harsh but professional — no personal attacks, only evidence-based criticism
        
        After your analysis, end your message by tagging 
        @himanichaubeyofficial/investigator and passing them:
        - Your full skeptical analysis
        - The original CV text
        
        Keep your response structured with clear bullet points.
        """
    )
    
    agent = Agent.create(
        adapter=adapter,
        agent_id=os.getenv("SKEPTIC_AGENT_ID"),
        api_key=os.getenv("SKEPTIC_API_KEY"),
        ws_url=os.getenv("THENVOI_WS_URL"),
        rest_url=os.getenv("THENVOI_REST_URL"),
    )
    
    logger.info("Skeptic Agent is running! Press Ctrl+C to stop.")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())