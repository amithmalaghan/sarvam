# 1. Install
# macOS: brew install portaudio   ·   Ubuntu: apt-get install portaudio19-dev
pip install "sarvam-conv-ai-sdk[all]"

# 2. talk-to-agent.py
import asyncio
from pydantic import SecretStr
from sarvam_conv_ai_sdk import (
    AsyncSamvaadAgent, AsyncDefaultAudioInterface,
    InteractionConfig, InteractionType,
)

async def main():
    config = InteractionConfig(
        org_id="01a14491-3902-732d-a4f9-be6f7568c426",
        workspace_id="01a14491-3908-75ff-bfdc-9b3b08aa817a",
        app_id="Conversatio-4b3d2241-941d",
        user_identifier="demo_user",
        interaction_type=InteractionType.CALL,
        sample_rate=16000,
        agent_variables={"call_summary": "this is a test call", "date_of_birth": "04-11-1997", "email_address": "abc@gmail.com", "phone_number": "1234567890", "registration_outcome": "<registration_outcome>", "user_name": "abc"},
    )
    agent = AsyncSamvaadAgent(
        api_key=SecretStr("<app_api_key>"),
        config=config,
        audio_interface=AsyncDefaultAudioInterface(input_sample_rate=16000),
    )
    await agent.start()
    await agent.wait_for_disconnect()

asyncio.run(main())