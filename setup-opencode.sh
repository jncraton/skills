#!/bin/sh
# Create symlinks within opencode configs

ln -s $(realpath AGENTS.md) ~/.config/opencode/AGENTS.md
ln -s $(realpath opencode.json) ~/.config/opencode/opencode.json
ln -s $(realpath skills) ~/.config/opencode/skills
