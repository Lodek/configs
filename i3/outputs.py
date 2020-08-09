#!/usr/bin/env python
import argparse, json, sys


def get_workspaces():
    return json.load(sys.stdin)


def get_outputs(workspaces):
    return {workspace['output'] for workspace in workspaces}


def get_active_workspace(workspaces):
    return next(filter(lambda workspace: workspace['focused'], workspaces))


def get_next_output(active, outputs):
    if len(outputs) > 1:
        return next(filter(lambda output: output != active, sorted(outputs)))
    else:
        return active

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices='output workspace'.split())
    return parser.parse_args()


def main():
    args = parse_args()
    workspaces = get_workspaces()
    outputs = get_outputs(workspaces)
    active_workspace = get_active_workspace(workspaces)
    next_output = get_next_output(active_workspace['output'], outputs)
    if args.action == 'output':
        print(next_output)
    elif args.action == 'workspace':
        filtered = filter(lambda workspace: workspace['visible'] 
                and workspace['output'] == next_output, workspaces)
        print(next(filtered)['num'])




if __name__ == '__main__':
    main()
