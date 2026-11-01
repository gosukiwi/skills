#!/usr/bin/env python3
"""Resolve a model tier into dispatch options. Requires Python 3.11+."""

import argparse
import json
from pathlib import Path
import sys

if sys.version_info < (3, 11):
    sys.exit('error: model resolution requires Python 3.11+')

import tomllib

TIERS = ('small', 'medium', 'large')
CLAUDE_MODELS = dict(zip(TIERS, ('haiku', 'sonnet', 'opus')))


def table(value, allowed, location):
    if not isinstance(value, dict):
        raise ValueError(f'{location} must be a table')
    unknown = value.keys() - allowed
    if unknown:
        raise ValueError(f'{location}: unknown keys: {", ".join(sorted(unknown))}')


def model_options(value):
    if isinstance(value, str):
        value = {'model': value}
    table(value, {'model', 'reasoning_effort'}, 'model entry')
    if 'model' not in value:
        raise ValueError('model entry requires model')
    for key, item in value.items():
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f'{key} must be a nonempty string')
    return value


def validate_models(models):
    table(models, set(TIERS), 'models')
    for value in models.values():
        model_options(value)


def load_config(project_root):
    for root in (project_root, Path.home()):
        path = root / '.agents' / 'gosumode.toml'
        try:
            with path.open('rb') as stream:
                config = tomllib.load(stream)
        except FileNotFoundError:
            continue
        table(config, {'models', 'hosts'}, str(path))
        validate_models(config.get('models', {}))
        hosts = config.get('hosts', {})
        if not isinstance(hosts, dict):
            raise ValueError('hosts must be a table')
        for host, settings in hosts.items():
            table(settings, {'models'}, f'hosts.{host}')
            validate_models(settings.get('models', {}))
        return config
    return {}


def resolve(config, host, tier):
    host_models = config.get('hosts', {}).get(host, {}).get('models', {})
    flat_models = config.get('models', {})
    if tier in host_models:
        return model_options(host_models[tier])
    if tier in flat_models:
        return model_options(flat_models[tier])
    if host == 'claude-code':
        return {'model': CLAUDE_MODELS[tier]}
    return {}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', required=True, help='harness key, e.g. codex, claude-code, pi')
    parser.add_argument('--tier', required=True, choices=TIERS)
    parser.add_argument('--project-root', type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        options = resolve(load_config(args.project_root), args.host, args.tier)
    except (OSError, ValueError) as error:
        parser.exit(2, f'error: {error}\n')
    print(json.dumps(options))


if __name__ == '__main__':
    main()
