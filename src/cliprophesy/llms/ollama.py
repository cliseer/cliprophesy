import os
import requests
from typing import List
from cliprophesy.llms import base

class OllamaBackend(base.BaseBackend):
    def __init__(self, cfg, model="llama3:latest"):
        super().__init__(cfg)
        self.model = cfg.get('model', model)
        self.url = cfg.get('url', 'http://localhost:11434/api/generate')

    def get_suggestions_internal(self, prompt:str) -> List[str]:
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=self.timeout
        )
        data = response.json()
        text = data["response"].strip()
        return [line.strip("1234567890.:- ").strip()
                for line in text.splitlines() if line.strip()]
