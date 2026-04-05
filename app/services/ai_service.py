import httpx
from app.core.config import settings

OPENAI_URL = "https://api.openai.com/v1/chat/completions"

async def generate_questions(role:str):
    try:
        prompt=f"""
        Generate 5 questions for a {role} role in a software company.

        Rules:
        - Medium difficulty
        - No explanations
        - return strictly in JSON formate:

        [
          {{"question":"..."},
            {"question":"..."}}
        ]
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                OPENAI_URL,
                headers={
                    "Authorization":f"Bearer {settings.OPENAI_API_KEY}",
                    "Content-Type":"application/json"

                },

                json={
                    "model":"gpt-4o-mini",
                    "message":[
                        {"role":"system","content":"You are an expert interviewer."},
                        {"role":"user","content":prompt}
                    ],
                    "temperature":0.5
                }
            )

            data=response.json()

            return data["choices"][0]["message"]["content"]
        
    except Exception as e:
        raise Exception(f"Ai generation failed":{str(e)})
    

        

