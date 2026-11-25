#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt.
"""
import os

EXCUSE = "I sneezed so hard my back filed for workers' comp, so I'm taking the day off to negotiate with it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
