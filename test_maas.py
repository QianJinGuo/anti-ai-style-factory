#!/usr/bin/env python3
"""Test MaaS API connectivity using CHATXUNFEI key from ~/.zshenv."""
import subprocess, sys
from pathlib import Path

# Read key from .zshenv
zshenv = Path.home() / ".zshenv"
api_key = ""
for line in zshenv.read_text().splitlines():
    if line.startswith("export CHATXUNFEI=") or line.startswith("CHATXUNFEI="):
        api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
        break

if not api_key:
    print("ERROR: CHATXUNFEI not found in ~/.zshenv")
    sys.exit(1)

print(f"Key: {api_key[:8]}...{api_key[-4:]} (len={len(api_key)})")

from openai import OpenAI

client = OpenAI(
    api_key=api_key,
    base_url="http://maas-api.cn-huabei-1.xf-yun.com/v1"
)

try:
    resp = client.chat.completions.create(
        model="xopqwen36v35b",
        messages=[{"role": "user", "content": "Say hello in 3 words"}],
        max_tokens=20,
        temperature=0.7,
        extra_headers={"lora_id": "0"},
    )
    print(f"SUCCESS: {resp.choices[0].message.content}")
except Exception as e:
    print(f"FAILED: {e}")
    sys.exit(1)
