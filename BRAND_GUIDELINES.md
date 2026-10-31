### PG Mana - Brand Identity & UI Asset Guidelines

### Corporate Visual Identity System (CVIS) for Odynex Axis Logistics LLC

This document establishes the official visual rules, user interface constraints, and asset paths for the **PG Mana** platform. All front-end dashboards, command tablets, mobile applications, and investor collateral must strictly align with these parameters under internal brand consistency protocols. 

### 🎨 1. Core Color System (Cybernetic Botanics)

The palette balances deep enterprise computing security with electric biological efficiency. Hex codes must be maintained across all digital assets. 

ElementToken NameHex CodeRGBPrimary Use Case
** **Mana Core Emerald****
color-brand-primary#00E6760, 230, 118Interactive accents, logo mark strokes, positive telemetry indicators.
** **Deep Slate Blue****
color-bg-dark#1A237E26, 35, 126Deep UI background fills, dark-mode panels, primary branding screens.
** **Cybernetic Jet Black****
color-bg-darker#0D111713, 17, 23Terminal interfaces, code blocks, main app workspace backgrounds.
** **Vortex Stark White****
color-text-light#FFFFFF255, 255, 255Dominant typography, high-contrast visual layers, clean layout highlights.

### 📐 2. Logo Architecture & Layout Rule

The logo is a geometric monogram blending the letters **P** and **M** via an integrated fluid dynamics gradient curve. 

                  [P-M Intersecting Monogram Vector]
                         /               \
              (Fluid Core Accent)    (Micro-Vortex Rings)
                         \               /
                    [ PG Mana Custom Typography ]

### Visual Constraints

* **Minimum Clear Space:** The logo must be surrounded by a buffer zone equal to 25% of the total logo height on all four sides. No other UI assets or lines may enter this perimeter.
* **Aspect Ratio:** Fixed 16:9 bounding presentation layout.
* **Prohibited Layouts:** Never convert the **Mana Core Emerald** mark to pastel greens, and never stretch the vector lines horizontally or vertically under any viewport size constraints.

### 🔤 3. Typography & Interface Typefaces

To reinforce a crisp, industrial, aerospace-grade aesthetic across the software, use the following web font stacks: 

* **Primary Headers & Display Titles:** Rajdhani, sans-serif (Square geometric font profiles with clean, technical corner angles).
* **Application UI & Interactive Fields:** Inter, system-ui, -apple-system, sans-serif (Highly scannable, clean, universal font rendering optimized for fast mobile or dashboard readout).
* **Terminal Data, JSON Renders, & Code Fields:** JetBrains Mono, monospace (Fixed-width typeface emphasizing structural numerical values and spatial coordinate streams).

### 💻 4. Tailwind CSS Component Token Specifications

For rapid web application and dashboard deployment, copy these custom utility themes into your front-end tailwind.config.js framework: 

javascript

module.exports = {
  theme: {
    extend: {
      colors: {
        mana: {
          emerald: '#00E676',
          slate: '#1A237E',
          jet: '#0D1117',
        }
      },
      fontFamily: {
        technical: ['Rajdhani', 'sans-serif'],
        interface: ['Inter', 'sans-serif'],
        code: ['JetBrains Mono', 'monospace'],
      },
      boxShadow: {
        'glow-emerald': '0 0 15px rgba(0, 230, 118, 0.45)',
      }
    },
  },
}

Use code with caution.

### Quick UI Design Reference (HTML/Tailwind Copy-Paste Component)

Use this specific markup blueprint to render an enterprise UI button that matches the visual language of the PG Mana app: 

html

<button class="bg-mana-jet border border-mana-emerald text-mana-emerald font-technical tracking-wider px-6 py-3 rounded-none shadow-glow-emerald transition-all hover:bg-mana-emerald hover:text-mana-jet duration-300">
  INITIALIZE PINN INFERENCE LOOP
</button>

Use code with caution.

### 📂 5. Repository File Asset Paths

Store all finalized design resources exactly at these root directory targets: 

* /assets/brand/logo_master_rgb.svg (The master vector outline configuration)
* /assets/brand/logo_monochrome_white.svg (For solid jet-black app workspaces)
* /assets/ui/dashboard_mockup_v1.png (Reference guide for developer workspace layouts)
* /assets/ui/favicon.ico (Browser tab system application icon)
