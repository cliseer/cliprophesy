import requests

from cliprophesy.llms.base import BaseBackend
from typing import List

REMOTE_URL = "https://cliseer-fastapi.fly.dev/v1/completion"

class CLIBuddyInterface(BaseBackend):
    MODE = 'FULL'

    def __init__(self, cfg, url=REMOTE_URL, allow_stdin=True):
        super().__init__(cfg)
        self._url = url
        self._allow_stdin = allow_stdin

    def get_suggestions_internal_extended(self, current_line: str, history: List[str], extended_history: List[str], stdin="", pwd="", status="", env="", test_request: bool = False, debug: bool = False) -> List[str]:
        if not self._allow_stdin:
            stdin = ''
        history = history[-20:] if len(history) > 20 else history

        data = {
            "history": history,
            "enriched_history": [],
            "stdin": str(stdin),
            "pwd": pwd,
            "buffer": current_line,
            "env": env,
            "status": -1 or int(status),
            "test_request": debug
        }
        response = requests.post(self._url, json=data, timeout=self.timeout)
        if (debug or test_request) and not 'completions' in response.json():
            raise Exception(response.text)
        data = response.json()
        return data['completions']
