#!/usr/bin/env bash
# Lançador do assistente de voz FLOW
source ~/.bashrc >/dev/null 2>&1
exec ~/assistente-flow/venv/bin/python3 ~/assistente-flow/assistente.py "$@"