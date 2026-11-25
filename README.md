# 🤖 Vice City GTA-6 AI Agent (Autonomous Open-World Sandbox)

A **100% free, cross-platform Autonomous AI Agent** set in a procedural open-world action sandbox inspired by GTA-6. Unlike a standard passive game or app, you can press **`A`** at any time to hand full control over to a self-navigating **AI Agent** that perceives its environment, makes tactical decisions, hijacks vehicles, evades police pursuits, and completes missions completely on its own.

Zero coding, zero Python setup, and zero API keys required—just download the executable for your operating system and run it.

---

## 🚀 Download & Play (No Coding Required)

1. Open the **[Releases](releases/latest)** page (or click **Releases** on the right-hand sidebar of this repository).
2. Under **Assets** (`v1.0.0`), download the file for your operating system:

| Operating System | File to Download | How to Launch |
| :--- | :--- | :--- |
| **💻 Windows** | `ViceCity_AI_Agent.exe` | Double-click the `.exe` file to launch immediately. |
| **🍏 macOS** | `ViceCity_AI_Agent-macOS.zip` | Double-click the `.zip` to extract, then open `ViceCity_AI_Agent.app`. |
| **🐧 Linux** | `ViceCity_AI_Agent-Linux` | Right-click → **Properties** → enable **Allow executing file as program** (or run `chmod +x ViceCity_AI_Agent-Linux`), then run it. |

> **First-Launch Security Prompts:** Because these free open-source executables are unsigned, Windows SmartScreen may show *"Windows protected your PC"* (click **More info → Run anyway**), and macOS may show an *"unidentified developer"* alert (right-click the app → click **Open**).

---

## 🧠 Why It’s an AI Agent (Not Just an App)

When **Autonomous Mode (`[A]`)** is activated, the agent runs a continuous **Sense → Decide → Act** loop in real time:
* **Environmental Perception:** Continuously scans the 3000×3000 city grid for nearby vehicles, active mission checkpoints, and police pursuit proximity.
* **Tactical Decision Tree:** Evaluates distance-to-target vs. distance-to-vehicle to decide autonomously whether to sprint on foot or hijack the nearest car for faster transit.
* **Autonomous Navigation & Driving:** Calculates steering angles, acceleration, and braking physics dynamically to reach targets without human input.
* **Live Intelligence Logs HUD:** Displays the agent's real-time internal reasoning and active mission state directly on screen.

---

## ✨ Key Features

* **Autonomous Autopilot (`[A]`):** Watch the AI Agent play, drive, steal cars, and complete objectives independently.
* **Dynamic Wanted & Pursuit System:** Stealing vehicles and completing missions raises your Wanted level (up to 5 stars), triggering active police NPC chases.
* **Procedural City & Day/Night Cycle:** Generates roads, buildings, traffic, pedestrians, exhaust particles, and smooth day-to-night lighting shifts on the fly with zero external asset downloads.
* **100% Free & Offline Ready:** Runs locally on Windows, macOS, and Linux with no subscriptions or accounts.

---

## 🎮 Controls

| Key | Action |
| :--- | :--- |
| **`A`** | **Toggle Autonomous AI Agent Mode (On / Off)** |
| **`W` `A` `S` `D`** or **Arrow Keys** | Walk on foot or steer, accelerate, and brake in Manual Mode |
| **`F`** | Enter / hijack the nearest vehicle, or exit your current vehicle |
| **`R`** | Respawn and redeploy the agent if **BUSTED** by police |

---

## 🛠️ Run from Source (For Developers)

If you prefer to inspect or modify the Python source code:

```bash
pip install -r requirements.txt
python gta_agent.py
