import re

file_path = "src/analytics/peer.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Ensure it explicitly saves the excel report in output/
if "to_excel" not in content and "peer_comparison.xlsx" not in content:
    append_code = """

# Auto-export peer comparison Excel report
import os
os.makedirs("output", exist_ok=True)
if hasattr(engine, 'df_peers') and engine.df_peers is not None:
    engine.df_peers.to_excel("output/peer_comparison.xlsx", index=False)
    print("📊 Peer Rankings Excel saved to 'output/peer_comparison.xlsx'")
"""
    content += append_code

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Patched peer.py for Excel output export.")
else:
    print("ℹ️ Peer engine already configured for Excel export.")
