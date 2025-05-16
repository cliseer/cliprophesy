import argparse
import signal

from cliprophesy import common
from cliprophesy.inputs import ShellReader, formatting

def get_completions(command, shell, backend, debug):
    reader = ShellReader.FishShellReader() if shell == 'fish' else ShellReader.ZshShellReader()
    context = reader.get_context()
    if not command and not context['history']:
        return ["Shell integration failed"]
    return backend.get_suggestions(command, test_request=False, debug=debug, **context)

def format_suggestions(suggestions, debug):
    return formatting.PrettySuggestionFormatter.format_suggestions(suggestions, debug)

def suggestion_flow(current_line, shell, backend, config_fname, debug):
    backend = common.get_backend_from_args(backend, config_fname)
    for suggestion in format_suggestions(get_completions(current_line, shell, backend, debug), debug=debug):
        print(suggestion)

def run():
    # Ignore SIGINT (Ctrl-C)
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)


    parser = argparse.ArgumentParser()
    parser.add_argument("current_line")
    parser.add_argument("--shell", default="fish")
    parser.add_argument("--backend", default=False)
    parser.add_argument("--config", default="~/.config/cliseer/settings.cfg")
    parser.add_argument("--debug", action='store_true')

    args = parser.parse_args()
    try:
        if args.debug:
            import time
            import logging
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
            start = time.time()
        suggestion_flow(args.current_line, args.shell, args.backend, args.config, args.debug)
        if args.debug:
            latency = time.time() - start
            print(f"Overall latency {latency}")
        return 0
    except KeyboardInterrupt as e:
        if args.debug:
            print(e)
        return 1
    except BrokenPipeError as e:
        if args.debug:
            print(e)
        return 1
    except Exception as e:
        if args.debug:
            print(e)
        return 1


if __name__ == '__main__':
    run()
