import json
from typing import Any, Dict

import ollama

from txn_msg_parser.constants import DEFAULT_MODEL


class AIFactory:
    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model

    def ask(self, prompt: str) -> Dict[str, Any]:
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            options={
                "num_predict": -1,
            },
            think=False,
        )

        content = response["message"]["content"]

        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        return json.loads(content)
