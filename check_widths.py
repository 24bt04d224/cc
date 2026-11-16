import glob
import re

for filepath in glob.glob("d:/Downloads/cc/parts_*.py"):
    with open(filepath, "r", encoding="utf-8") as f:
        txt = f.read()
    matches = re.findall(r'style=["\'][^"\']*(?:min-width|width)\s*:\s*([0-9]+px)[^"\']*["\']', txt)
    large = [m for m in matches if int(m.replace("px", "")) > 340]
    if large:
        print(filepath, set(large))

print("Width inspection finished.")
