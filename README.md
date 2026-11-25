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
** WASD or arrow keys: walk and drive.
** SHIFT: sprint, which uses stamina.
** F or E: hijack, enter or exit a car.
** SPACE: handbrake.
** H: horn.
** C: change camera.
** Mouse drag: look around.
** R: restart the current stage.
** ESC: pause. The game also pauses when you switch to another window.


## Game Features
Start screen: a title screen with a controls list and a START button.
7 stages with cash rewards:
Walk to the marker.
Hijack a car and drive to the marker.
A timed courier run across town.
A 6-checkpoint street race.
Collect 8 cash bags on the sidewalks.
Reach 3 wanted stars, then lose the police.
A final getaway with police already chasing you.
GPS route: the minimap draws a route along the roads to your objective. Cash bags show as yellow dots.
HUD and recovery: the HUD shows cash, health, stamina, the stage objective and a countdown timer. Health slowly regenerates if you avoid damage for a few seconds.
BUSTED: if police reach you while you're on foot or nearly stopped, you lose 10% of your cash and restart the stage.
WASTED: dying costs 5% of your cash.
Winning: finishing all stages shows "YOU BEAT VICE CITY!", and you can keep exploring afterward.
