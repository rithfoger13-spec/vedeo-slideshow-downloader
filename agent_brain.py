import time
import json
import os
from google import genai
from google.genai import types
import config

class UniversalAgentBrain:
    def __init__(self):
        # Initialize Gemini Client
        self.client = genai.Client(api_key=config.GEMINI_API_KEY)

    def _get_subbots_context(self) -> str:
        """អានទិន្នន័យ Sub-Bots ទាំងអស់ពី bots_db.json មកធ្វើជា Context"""
        db_path = "bots_db.json"
        if os.path.exists(db_path):
            try:
                with open(db_path, "r", encoding="utf-8") as f:
                    bots = json.load(f)
                    if bots:
                        bot_info = "\n".join([
                            f"- ឈ្មោះ/Username: {v.get('name', 'Sub-Bot')}, តួនាទី: {v.get('role', 'General Assistant')}" 
                            for k, v in bots.items()
                        ])
                        return f"\n\n[បញ្ជី Sub-Bots កូនចៅក្រោមឱវាទរបស់អ្នកមាន៖]\n{bot_info}"
            except Exception:
                pass
        return "\n\n[បច្ចុប្បន្នអ្នកមិនទាន់មាន Sub-Bot ក្រោមឱវាទនៅឡើយទេ]"

    def process_command(self, text: str) -> str:
        subbots_context = self._get_subbots_context()
        
        # កំណត់ System Instruction ឱ្យឆ្លើយតបបានគ្រប់ភាសា
        sys_instruction = (
            "You are a Master AI Agent capable of interacting in any language requested by the user. "
            "You can download media, answer questions, and delegate tasks to subordinate sub-bots."
            f"{subbots_context}\n\n"
            "IMPORTANT LANGUAGE RULE:\n"
            "1. Always detect and reply in the exact language used by the user (e.g., Khmer, English, Chinese, Thai, French, etc.).\n"
            "2. If the user mentions a specific sub-bot (e.g. @Assistant_1Abot), handle and route the request accordingly in the user's language."
        )
        
        models_to_try = ['gemini-2.5-flash', 'gemini-1.5-flash']
        
        for model_name in models_to_try:
            for attempt in range(3):
                try:
                    config_obj = types.GenerateContentConfig(
                        system_instruction=sys_instruction
                    )
                    
                    response = self.client.models.generate_content(
                        model=model_name,
                        contents=text,
                        config=config_obj
                    )
                    
                    if response and response.text:
                        return response.text
                except Exception as e:
                    print(f"Gemini API Error ({model_name}): {e}")
                    time.sleep(1)
                    continue
                        
        return "❌ Server AI កំពុងរវល់! សូមសាកល្បងម្ដងទៀត។ / Unable to connect to AI Server. Please try again!"