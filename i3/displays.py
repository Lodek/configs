#!/usr/bin/python
import json, sys


def get_workspaces():
    return json.load(sys.stdin)


def get_outputs(workspace):
    return {workspace['output'] for workspace in workspaces}


def get_active_output(workspaces):
    return next(filter(lambda workspace: workspace['focused'], workspaces))['output']


def next_output(active, outputs):
    if len(outputs) > 1:
        return next(filter(lambda output: output != active, sorted(outputs)))
    else:
        return active

def main():
    workspaces = get_workspaces()
    outputs = get_outputs(workspaces)
    active_output = get_active_output(workspaces)
    next = next_output(active_output, outputs)
    print(next)


if __name__ == '__main__':
    main()
