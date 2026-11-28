# Neon Coast — Original Open-World Sandbox

Neon Coast is an original neon-lit 3D open-world sandbox experience built with Three.js and a lightweight Python launcher.

## Originality and rebranding

This project does not reproduce or depend on proprietary game assets or branding. It uses procedurally generated characters, original fictional locations, original presentation, and generic open-world systems. The title, HUD, locations, and character names have been changed to be distinct from third-party franchises.

## Character presentation

The game includes a procedural anatomical character system with:

- sculpted facial geometry
- skin-tone-matched procedural portrait textures
- bump and roughness detail
- anatomically placed eyes and brows
- procedural hair shells and facial hair
- blinking, speech, expressions, and interaction poses

## New presentation module

`neon-coast.js` provides copyright-safe runtime rebranding and presentation polish. `gta_agent.py` serves the enhancement module locally when launching the desktop application.

## Controls

| Key | Action |
| :--- | :--- |
| `W` `A` `S` `D` / Arrow Keys | Move or steer |
| `Shift` | Sprint |
| `F` / `E` | Enter or exit vehicles |
| `Space` | Handbrake |
| `H` | Horn |
| `C` | Change camera |
| `Mouse drag` | Look around |
| `R` | Restart stage |
| `Esc` | Pause |
| `X` | Interact |
| `Q` | Melee action |
| `Z` | Emote |
| `B` | Sunglasses |
| `U` | Character close-up |

## Running locally

```bash
python3 -m pip install -r requirements.txt
python3 gta_agent.py
```

## Disclaimer

Neon Coast is an independently developed inspired sandbox and is not affiliated with, endorsed by, or a copy of any commercial game or franchise.
