# 🚗 GTA 6: Autonomous AI Agent Sandbox

An offline, open-world GTA-6 "minor 2D sandbox" powered by an **Autonomous AI Agent**! Designed to run with **zero technical setup, API keys, or coding**. Download, execute, and inspect the sandbox anywhere!

---

## 🌟 Capabilities
*   **🤖 Full AI Agent Mode:** Toggle Autopilot `[TAB]` to let **Tommy AI** roam, make pathfinding decisions, avoid building colliders, hijack vehicles, trigger pursuits, and use adaptive tactics.
*   **🎮 Manual Controls:** Play yourself! Shoot targets, hijack cars `[F]`, and inspect boundaries.
*   **⚔️ Active Wanted & Squad Systems:** Star Ratings (⭐ - ⭐⭐⭐⭐⭐) spawn patrol squads as your wanted level rises.
*   **📟 Natural Commander Overrides:** Control the AI Agent directly by typing targets into your terminal shell: `survive`, `fight cops`, `steal car`, `roam`, or `flee`.

---

## 🚀 Instant Launch (For Non-Technical Users)

No Python or console code is required. Double-click to run!

1. Check the right sidebar of this page and open **Releases**.
2. Download the version specifically matched with your Operating System:
    *   💻 **Windows:** `GTA_AI_Agent_Sandbox.exe`
    *   🍏 **macOS:** `GTA_AI_Agent_Sandbox.app` (or zip bundle)
    *   🐧 **Linux:** `GTA_AI_Agent_Sandbox`
3. Just double-click the file to open and inspect!

*(Note for Mac Users: If a security prompt appears, Ctrl+Click the download and press "Open", or allow it in Mac System Settings > Privacy & Security).*

---

## 🛠️ Code Setup & Custom Compiling (Developers)

To customize visual elements or modify agent states:

```bash
# Double check you have Python installed, then inspect & install:
pip install -r requirements.txt

# Start sandbox
python agent.py

To generate standalone executable files for non-technical users to download, double-click, and play without Python setup, run `pyinstaller` on your target machines and attach the outputs:

1. Open your terminal or Command Prompt, and generate your build:

   pyinstaller --onefile --noconsole --name="GTA_AI_Agent_Sandbox" agent.py
