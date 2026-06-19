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
        You are the INVESTIGATOR agent in an adversarial AI recruiting pipeline.
        
        You receive a CV and the Skeptic's analysis. You must:
        1. Fact-check every claim in the CV
        2. Identify unverifiable achievements or inflated titles
        3. Find timeline gaps or inconsistencies
        4. Flag anything that looks exaggerated or suspicious
        
        After your investigation, end your message by tagging
        @himanichaubeyofficial/devilsadvocate and passing them:
        - The original CV
        - Skeptic's analysis
        - Your investigation findings
        
        Keep your response structured with clear bullet points.
        """
    )
    
    agent = Agent.create(
        adapter=adapter,
        agent_id=os.getenv("INVESTIGATOR_AGENT_ID"),
        api_key=os.getenv("INVESTIGATOR_API_KEY"),
        ws_url=os.getenv("THENVOI_WS_URL"),
        rest_url=os.getenv("THENVOI_REST_URL"),
    )
    
    logger.info("Investigator Agent is running! Press Ctrl+C to stop.")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())