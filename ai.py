import json
import subprocess
from typing import Any, Dict

from constants import DEFAULT_MODEL


class AIFactory:

    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model

    def ask(self, prompt: str) -> Dict[str, Any]:
        content = subprocess.check_output(
            ["ollama", "run", DEFAULT_MODEL, "--think=false", prompt],
        ).decode("utf-8")

        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        return json.loads(content)
