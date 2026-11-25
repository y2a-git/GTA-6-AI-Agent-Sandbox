# 🤖 Vice City 3D GTA-6 AI Agent (Autonomous 3D Open-World Sandbox)

A **100% free, cross-platform 3D Autonomous AI Agent** set in a neon-lit Vice City open-world sandbox powered by **Three.js (WebGL)**. Unlike a standard passive game or app, the AI Agent runs a continuous **Sense → Decide → Act** neural loop with 3D lidar obstacle avoidance—navigating 3D city streets, hijacking sports cars, evading police cruisers, and completing missions completely on its own.

Zero coding, zero engine installs, and zero API keys required—just download the executable for your operating system and double-click to launch.

---

## 🚀 Download & Play (No Coding Required)

1. Open the **(https://github.com/y2a-git/GTA-6-AI-Agent-Sandbox/releases/tag/v1.0.0)** page (or click **Releases** on the right-hand sidebar of this repository).
2. Under **Assets**, download the executable for your operating system:

| Operating System | File to Download | How to Launch |
| :--- | :--- | :--- |
| **💻 Windows** | `ViceCity_AI_Agent.exe` | Double-click the `.exe` file to launch in 3D immediately. |
| **🍏 macOS** | `ViceCity_AI_Agent-macOS.zip` | Double-click the `.zip` to extract, then open `ViceCity_AI_Agent.app`. |
| **🐧 Linux** | `ViceCity_AI_Agent-Linux` | Right-click → **Properties** → enable **Allow executing file as program**, then run it. |

> **First-Launch Security Prompts:** Because open-source executables are unsigned, Windows SmartScreen may show *"Windows protected your PC"* (click **More info → Run anyway**), and macOS may show an *"unidentified developer"* alert (right-click the app → click **Open**).

---

## 🧠 Why It’s an AI Agent (Not Just an App)

* **3D Lidar Environmental Perception:** Casts forward and peripheral obstacle feelers to detect skyscrapers, traffic, mission beacons, and pursuing police units in real time.
* **Autonomous Tactical Decision Tree:** Evaluates distance-to-beacon vs. distance-to-vehicle to decide whether to sprint on foot, hijack the nearest sports car, or switch to high-speed evasion when Wanted stars rise.
* **Natural Language Directive Bar:** Type commands directly into the 3D HUD (`steal car`, `evade`, `patrol`, `mission`, `night`, `day`) to steer the agent's high-level goals while it handles low-level 3D driving and navigation autonomously.
* **Live Sense → Decide → Act HUD & Radar:** Displays real-time internal reasoning alongside a live 2D lidar minimap.

---

## 🎮 Controls

| Key | Action |
| :--- | :--- |
| **`TAB`** or **`P`** | **Toggle Autonomous AI Autopilot Mode (On / Off)** |
| **`W` `A` `S` `D`** or **Arrow Keys** | Walk on foot or steer, accelerate, and brake in Manual Mode |
| **`F`** | Hijack / enter the nearest vehicle, or exit your current vehicle |
| **`C`** | Cycle 3D Camera Angles (Chase Cam / Wide Action Cam / Tactical Overhead) |
| **`R`** | Respawn and redeploy the agent if **BUSTED** by police |
