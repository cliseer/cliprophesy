import requests

from typing import List

REMOTE_URL = "https://www.shbuddy.com/v1/completion"

class CLIBuddyInterface:
    STYLE = 'FULL'

    def __init__(self, url, allow_stdin=False):
        self._url = REMOTE_URL
        self._allow_stdin = allow_stdin

    def get_suggestions_internal_extended(self, current_line: str, history: List[str], extended_history: List[str]=[], stdin="", pwd="", test_request: bool = False, debug: bool = False) -> List[str]:
        if not self._allow_stdin:
            stdin = ''
        history = history[-20:] if len(history) > 20 else history
        data = {
            "history": history,
            "enriched_history": [],
            "stdin": str(stdin),
            "pwd": pwd,
            "buffer": current_line,
            "test_request": debug
        }
        response = requests.post(self._url, json=data, timeout=10)
        data = response.json()
        return data['completions']
