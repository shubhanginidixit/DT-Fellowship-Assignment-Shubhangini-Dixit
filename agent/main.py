import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "..", "tree", "reflection-tree.json")

with open(json_path) as f:
    tree = json.load(f)

current = "START"

while current:
    node = tree[current]
    print("\n" + node["text"])

    if node["type"] == "question":
        for i, opt in enumerate(node["options"]):
            print(f"{i+1}. {opt['text']}")
        choice = int(input("Choose option: ")) - 1
        current = node["options"][choice]["next"]
    else:
        current = node.get("next")
