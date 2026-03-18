#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "requests",
#     "pynput",
#     "mss",
#     "customtkinter",
# ]
# ///

import sys
import argparse

from visual.config.visual_config import BASE_URL
from visual.view_model.task_view_model import TaskViewModel


def main():

    parser = argparse.ArgumentParser(description="VLA Desktop Automation Client")
    parser.add_argument("command", help="Command (must be 'run')")
    parser.add_argument("task", help="Task description to execute")

    args = parser.parse_args()

    if args.command != "run":
        print("Unsupported command. Must be 'run'.")
        return 1

    # Create ViewModel
    view_model = TaskViewModel()

    # Initialize task
    if not view_model.init_task(args.task, BASE_URL):
        print("Failed to initialize visualization overlay.")
        # Run task directly without UI
        view_model.model.init_task(args.task, BASE_URL)
        view_model.model.run_automation_task()
        return 0 if view_model.model.state.status == "completed" else 1

    # Run task
    success = view_model.run_task()
    # Clean up resources
    view_model.close()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())