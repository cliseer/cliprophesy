import argparse
import logging

import common
from inputs import ShellReader, formatting



def get_completions(command, backend, debug):
    backend = common.get_backend(backend)
    reader = ShellReader.FishShellReader()
    context = reader.get_context()
    return backend.get_suggestions(command, test_request=False, **context)

def format_suggestions(suggestions):
    return formatting.PrettySuggestionFormatter.format_suggestions(suggestions)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("current_line")
    parser.add_argument("--shell", default="fish")
    parser.add_argument("--backend", default="anthropic")
    parser.add_argument("--debug", action='store_true')

    args = parser.parse_args()
    if args.debug:
        import time
        import logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        start = time.time()
    for suggestion in format_suggestions(get_completions(args.current_line, args.backend, args.debug)):
        print(suggestion)
    if args.debug:
        latency = time.time() - start
        logging.info(f"Latency {latency}")
        #logging.INFO(f"Total elapsed time {latency}")
