from cliprophesy.llms import anthropic_backend, openai_backend, clibuddy, ollama
import configparser
from pathlib import Path

def get_backend_from_args(user_requested, config):
    parser = configparser.ConfigParser({'timeout': 3, 'provider': 'clibuddy', 'history_len': 3})
    parser.read(Path(config).expanduser())
    if user_requested:
        return get_backend(user_requested, parser['settings'])
    elif parser:
        return get_backend(parser['settings']['provider'], parser['settings'])
    else:
        return clibuddy.CLIBuddyInterface(allow_stdin=True)

def get_backend(llm_str, cfg):
    if llm_str == 'anthropic':
        return anthropic_backend.AnthropicBackend(cfg)
    elif llm_str == 'openai':
        return openai_backend.OpenAIBackend(cfg)
    elif llm_str == 'ollama':
        return ollama.OllamaBackend(cfg)
    elif llm_str in ('clibuddy', 'cliseer'):
        return clibuddy.CLIBuddyInterface(cfg, allow_stdin=True)
    return clibuddy.CLIBuddyInterface(cfg, allow_stdin=True)
