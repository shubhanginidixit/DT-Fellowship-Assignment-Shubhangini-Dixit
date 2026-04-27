# DT Fellowship Assignment – Daily Reflection Tree

This repository contains my submission for the DeepThought Growth Teams (DT CultureTech) Fellowship Assignment.

## Project Overview
The Daily Reflection Tree is a deterministic reflection agent designed to guide employees through an end-of-day reflection session.

The product uses a structured decision tree and does **not** use any LLM/API at runtime.

The conversation moves through 3 psychological axes:

1. **Locus** – Victim vs Victor  
2. **Orientation** – Contribution vs Entitlement  
3. **Radius** – Self-Centrism vs Altrocentrism  

---

## Repository Structure

```bash
tree/
  reflection-tree.json
  tree-diagram.md

agent/
  main.py

transcripts/
  persona1.md
  persona2.md

write-up.md
README.md
