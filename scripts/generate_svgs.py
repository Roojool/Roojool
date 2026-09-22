"""
SVG Generator & Validator for Rujul Talekar's GitHub Profile
Generates 8 high-aesthetic dark and light SVGs:
- banner-dark.svg & banner-light.svg
- identity-dark.svg & identity-light.svg
- research-dark.svg & research-light.svg
- stack-dark.svg & stack-light.svg
"""

import os
import xml.etree.ElementTree as ET

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. BANNER SVGs (960 x 230)
# -------------------------------------------------------------
def build_banner(is_dark=True):
    bg = "#0d1117" if is_dark else "#f6f8fa"
    card_bg = "#161b22" if is_dark else "#ffffff"
    border = "#30363d" if is_dark else "#d0d7de"
    grid_stroke = "#21262d" if is_dark else "#e5e8ec"
    accent = "#58a6ff" if is_dark else "#0969da"
    accent_green = "#3fb950" if is_dark else "#1a7f37"
    text_primary = "#f0f6fc" if is_dark else "#1f2328"
    text_secondary = "#8b949e" if is_dark else "#57606a"
    pill_bg = "#21262d" if is_dark else "#f0f2f5"
    pill_border = "#30363d" if is_dark else "#d8dee4"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 230" width="100%" height="230" style="background:transparent;">
  <defs>
    <pattern id="grid_{'dark' if is_dark else 'light'}" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="{grid_stroke}" stroke-width="0.8" opacity="0.6"/>
    </pattern>
    <linearGradient id="headerGrad_{'dark' if is_dark else 'light'}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="{accent_green}" stop-opacity="0.8"/>
    </linearGradient>
  </defs>

  <rect width="958" height="228" x="1" y="1" rx="8" fill="{bg}" stroke="{border}" stroke-width="1"/>
  <rect width="958" height="228" x="1" y="1" rx="8" fill="url(#grid_{'dark' if is_dark else 'light'})"/>

  <!-- Corner Brackets -->
  <path d="M 12 24 L 12 12 L 24 12" fill="none" stroke="{accent}" stroke-width="2"/>
  <path d="M 948 24 L 948 12 L 936 12" fill="none" stroke="{accent}" stroke-width="2"/>
  <path d="M 12 206 L 12 218 L 24 218" fill="none" stroke="{accent}" stroke-width="2"/>
  <path d="M 948 206 L 948 218 L 936 218" fill="none" stroke="{accent}" stroke-width="2"/>

  <!-- Top Metadata Bar -->
  <g transform="translate(30, 36)">
    <text font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" fill="{accent}" font-weight="600" letter-spacing="1.5">DOSSIER // RESEARCH &amp; SYSTEMS SPECIFICATION</text>
  </g>
  <g transform="translate(680, 36)">
    <circle cx="6" cy="-4" r="4" fill="{accent_green}">
      <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="16" y="0" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" fill="{accent_green}" font-weight="600" letter-spacing="1">STATUS: ACTIVE_RESEARCH</text>
  </g>

  <!-- Horizontal Divider Line -->
  <line x1="30" y1="48" x2="930" y2="48" stroke="{border}" stroke-width="1"/>

  <!-- Main Identity Content -->
  <g transform="translate(30, 102)">
    <text font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="36" font-weight="800" fill="{text_primary}" letter-spacing="-0.5">RUJUL TALEKAR</text>
  </g>
  <g transform="translate(30, 134)">
    <text font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="16" font-weight="600" fill="{accent}" letter-spacing="2">AI RESEARCHER × SYSTEMS BUILDER</text>
    <text x="365" y="0" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="12" fill="{text_secondary}">// COMPUTER ENGINEERING @ VIT PUNE</text>
  </g>

  <!-- Bottom Core Vectors Pills -->
  <g transform="translate(30, 168)">
    <!-- Pill 1: Human-Centered AI -->
    <rect x="0" y="0" width="168" height="28" rx="5" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1"/>
    <text x="14" y="18" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="500" fill="{text_primary}">HUMAN-CENTERED AI</text>

    <!-- Pill 2: Video Analytics -->
    <rect x="178" y="0" width="145" height="28" rx="5" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1"/>
    <text x="192" y="18" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="500" fill="{text_primary}">VIDEO ANALYTICS</text>

    <!-- Pill 3: Computer Vision -->
    <rect x="333" y="0" width="148" height="28" rx="5" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1"/>
    <text x="347" y="18" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="500" fill="{text_primary}">COMPUTER VISION</text>

    <!-- Pill 4: Network Systems -->
    <rect x="491" y="0" width="150" height="28" rx="5" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1"/>
    <text x="505" y="18" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="500" fill="{text_primary}">NETWORK SYSTEMS</text>

    <!-- Pill 5: Edge AI -->
    <rect x="651" y="0" width="86" height="28" rx="5" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1"/>
    <text x="665" y="18" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="500" fill="{text_primary}">EDGE AI</text>

    <!-- Location Tag -->
    <text x="795" y="18" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" fill="{text_secondary}">PUNE, MAHARASHTRA, IN</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 2. IDENTITY TERMINAL SVGs (960 x 280)
# -------------------------------------------------------------
def build_identity(is_dark=True):
    bg = "#0d1117" if is_dark else "#f6f8fa"
    card_bg = "#161b22" if is_dark else "#ffffff"
    border = "#30363d" if is_dark else "#d0d7de"
    header_bar = "#1c2128" if is_dark else "#eef1f4"
    accent = "#58a6ff" if is_dark else "#0969da"
    accent_green = "#3fb950" if is_dark else "#1a7f37"
    text_primary = "#f0f6fc" if is_dark else "#1f2328"
    text_secondary = "#8b949e" if is_dark else "#57606a"
    key_color = "#79c0ff" if is_dark else "#0550ae"
    val_highlight = "#7ee787" if is_dark else "#116329"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 280" width="100%" height="280" style="background:transparent;">
  <!-- Terminal Window Outer Container -->
  <rect width="958" height="278" x="1" y="1" rx="8" fill="{card_bg}" stroke="{border}" stroke-width="1"/>

  <!-- Terminal Window Chrome / Header Bar -->
  <rect width="958" height="38" x="1" y="1" rx="8" fill="{header_bar}"/>
  <rect width="958" height="12" x="1" y="27" fill="{header_bar}"/>
  <line x1="1" y1="39" x2="959" y2="39" stroke="{border}" stroke-width="1"/>

  <!-- Window Control Dots -->
  <circle cx="20" cy="20" r="6" fill="#ff5f56"/>
  <circle cx="38" cy="20" r="6" fill="#ffbd2e"/>
  <circle cx="56" cy="20" r="6" fill="#27c93f"/>

  <!-- Window Title -->
  <text x="80" y="24" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="12" fill="{text_secondary}">rujul@lab-workstation: ~/identity.sh --dossier</text>
  <text x="820" y="24" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" fill="{accent_green}">● SYSTEM_ACTIVE</text>

  <!-- Prompt Command Line -->
  <g transform="translate(24, 66)">
    <text font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="13" font-weight="600" fill="{accent_green}">rujul@research</text>
    <text x="110" y="0" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="13" fill="{text_secondary}">:</text>
    <text x="120" y="0" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="13" font-weight="600" fill="{accent}">~</text>
    <text x="130" y="0" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="13" fill="{text_secondary}">$ sysinfo --target=rujul-talekar --spec=full</text>
  </g>

  <!-- Horizontal Rule inside Terminal -->
  <line x1="24" y1="80" x2="936" y2="80" stroke="{border}" stroke-width="0.8" stroke-dasharray="4 4"/>

  <!-- Key-Value Telemetry Block -->
  <g transform="translate(24, 108)" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="12" xml:space="preserve">
    <!-- Row 1 -->
    <text x="0" y="0" fill="{key_color}" font-weight="600">ROLE</text>
    <text x="120" y="0" fill="{text_secondary}">::</text>
    <text x="145" y="0" fill="{text_primary}" font-weight="600">AI Researcher × Systems Builder</text>

    <!-- Row 2 -->
    <text x="0" y="24" fill="{key_color}" font-weight="600">AFFILIATION</text>
    <text x="120" y="24" fill="{text_secondary}">::</text>
    <text x="145" y="24" fill="{text_primary}">B.Tech Computer Engineering, Vishwakarma Institute of Technology (VIT Pune)</text>

    <!-- Row 3 -->
    <text x="0" y="48" fill="{key_color}" font-weight="600">LAB GROUP</text>
    <text x="120" y="48" fill="{text_secondary}">::</text>
    <text x="145" y="48" fill="{text_primary}">Research Intern under Prof. Ganesh Bhutkar — Usability of AI ICT Applications</text>

    <!-- Row 4 -->
    <text x="0" y="72" fill="{key_color}" font-weight="600">CORE FOCUS</text>
    <text x="120" y="72" fill="{text_secondary}">::</text>
    <text x="145" y="72" fill="{text_primary}">Human-Centered AI · Video Management Systems · Computer Vision · Network Systems</text>

    <!-- Row 5 -->
    <text x="0" y="96" fill="{key_color}" font-weight="600">PATENT PUB</text>
    <text x="120" y="96" fill="{text_secondary}">::</text>
    <text x="145" y="96" fill="{val_highlight}">Personalized Voice Control Car [Electronics // Filed Dec 2025 // Pub Jan 2026]</text>

    <!-- Row 6 -->
    <text x="0" y="120" fill="{key_color}" font-weight="600">ENG PRINCIPLE</text>
    <text x="120" y="120" fill="{text_secondary}">::</text>
    <text x="145" y="120" fill="{text_primary}">Measure before claiming · Characterize queues &amp; pipelines · Defensible evidence</text>

    <!-- Row 7 -->
    <text x="0" y="144" fill="{key_color}" font-weight="600">LOCATION</text>
    <text x="120" y="144" fill="{text_secondary}">::</text>
    <text x="145" y="144" fill="{text_secondary}">Pune, Maharashtra, India [UTC+05:30 IST]  |  Scheduled CHIuXD '26 Presentation</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 3. RESEARCH METHODOLOGY PIPELINE SVGs (960 x 180)
# -------------------------------------------------------------
def build_research(is_dark=True):
    bg = "#0d1117" if is_dark else "#f6f8fa"
    card_bg = "#161b22" if is_dark else "#ffffff"
    box_bg = "#21262d" if is_dark else "#f6f8fa"
    border = "#30363d" if is_dark else "#d0d7de"
    accent = "#58a6ff" if is_dark else "#0969da"
    accent_green = "#3fb950" if is_dark else "#1a7f37"
    text_primary = "#f0f6fc" if is_dark else "#1f2328"
    text_secondary = "#8b949e" if is_dark else "#57606a"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 180" width="100%" height="180" style="background:transparent;">
  <!-- Container Card -->
  <rect width="958" height="178" x="1" y="1" rx="8" fill="{card_bg}" stroke="{border}" stroke-width="1"/>

  <!-- Header -->
  <g transform="translate(24, 28)">
    <text font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="600" fill="{accent}" letter-spacing="1.5">RESEARCH METHODOLOGY &amp; EXPERIMENTAL PIPELINE</text>
    <text x="560" y="0" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" fill="{text_secondary}">DISCIPLINE: RIGOROUS SYSTEMATIC VERIFICATION</text>
  </g>
  <line x1="24" y1="38" x2="936" y2="38" stroke="{border}" stroke-width="0.8"/>

  <!-- 4 Pipeline Stages -->
  <!-- Stage 1 -->
  <g transform="translate(24, 56)">
    <rect width="206" height="96" rx="6" fill="{box_bg}" stroke="{border}" stroke-width="1"/>
    <text x="14" y="22" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="10" font-weight="700" fill="{accent}">01 // SETUP</text>
    <text x="14" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="13" font-weight="700" fill="{text_primary}">Configured State</text>
    <text x="14" y="66" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="11" fill="{text_secondary}">Controlled baselines,</text>
    <text x="14" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="11" fill="{text_secondary}">environment parameters</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 238 104 L 254 104 M 250 99 L 255 104 L 250 109" stroke="{accent}" stroke-width="1.8" fill="none"/>

  <!-- Stage 2 -->
  <g transform="translate(262, 56)">
    <rect width="206" height="96" rx="6" fill="{box_bg}" stroke="{border}" stroke-width="1"/>
    <text x="14" y="22" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="10" font-weight="700" fill="{accent}">02 // INSTRUMENT</text>
    <text x="14" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="13" font-weight="700" fill="{text_primary}">Observed State</text>
    <text x="14" y="66" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="11" fill="{text_secondary}">Telemetry streams, video</text>
    <text x="14" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="11" fill="{text_secondary}">frames &amp; packet logs</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 476 104 L 492 104 M 488 99 L 493 104 L 488 109" stroke="{accent}" stroke-width="1.8" fill="none"/>

  <!-- Stage 3 -->
  <g transform="translate(500, 56)">
    <rect width="206" height="96" rx="6" fill="{box_bg}" stroke="{border}" stroke-width="1"/>
    <text x="14" y="22" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="10" font-weight="700" fill="{accent}">03 // QUANTIFY</text>
    <text x="14" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="13" font-weight="700" fill="{text_primary}">Measured Behavior</text>
    <text x="14" y="66" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="11" fill="{text_secondary}">Latency, queue depth,</text>
    <text x="14" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="11" fill="{text_secondary}">and usability metrics</text>
  </g>

  <!-- Arrow 3 -->
  <path d="M 714 104 L 730 104 M 726 99 L 731 104 L 726 109" stroke="{accent_green}" stroke-width="1.8" fill="none"/>

  <!-- Stage 4 -->
  <g transform="translate(738, 56)">
    <rect width="198" height="96" rx="6" fill="{box_bg}" stroke="{accent_green}" stroke-width="1.2"/>
    <text x="14" y="22" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="10" font-weight="700" fill="{accent_green}">04 // SYNTHESIZE</text>
    <text x="14" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="13" font-weight="700" fill="{text_primary}">Defensible Claim</text>
    <text x="14" y="66" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="11" fill="{text_secondary}">Reproducible conclusions,</text>
    <text x="14" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="11" fill="{text_secondary}">explicit bounds &amp; limits</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 4. TECH STACK MATRIX SVGs (960 x 270)
# -------------------------------------------------------------
def build_stack(is_dark=True):
    bg = "#0d1117" if is_dark else "#f6f8fa"
    card_bg = "#161b22" if is_dark else "#ffffff"
    col_bg = "#21262d" if is_dark else "#f6f8fa"
    chip_bg = "#161b22" if is_dark else "#ffffff"
    border = "#30363d" if is_dark else "#d0d7de"
    accent = "#58a6ff" if is_dark else "#0969da"
    text_primary = "#f0f6fc" if is_dark else "#1f2328"
    text_secondary = "#8b949e" if is_dark else "#57606a"
    accent_green = "#3fb950" if is_dark else "#1a7f37"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 270" width="100%" height="270" style="background:transparent;">
  <!-- Container Card -->
  <rect width="958" height="268" x="1" y="1" rx="8" fill="{card_bg}" stroke="{border}" stroke-width="1"/>

  <!-- Header -->
  <g transform="translate(24, 28)">
    <text font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="600" fill="{accent}" letter-spacing="1.5">BUILD &amp; RESEARCH TOOLING MATRIX</text>
    <text x="640" y="0" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" fill="{text_secondary}">VERIFIED TECHNICAL SURFACE</text>
  </g>
  <line x1="24" y1="38" x2="936" y2="38" stroke="{border}" stroke-width="0.8"/>

  <!-- 4 Columns Grid -->
  <!-- Col 1: Core Languages -->
  <g transform="translate(24, 52)">
    <rect width="216" height="198" rx="6" fill="{col_bg}" stroke="{border}" stroke-width="1"/>
    <text x="14" y="24" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="700" fill="{accent}">CORE LANGUAGES</text>
    <line x1="14" y1="34" x2="202" y2="34" stroke="{border}" stroke-width="0.8"/>

    <g transform="translate(14, 50)" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" fill="{text_primary}">
      <text x="0" y="0">▸ Python</text>
      <text x="100" y="0">▸ C / C++</text>
      <text x="0" y="26">▸ Java</text>
      <text x="100" y="26">▸ Kotlin</text>
      <text x="0" y="52">▸ TypeScript</text>
      <text x="100" y="52">▸ JavaScript</text>
      <text x="0" y="78">▸ SQL</text>
      <text x="100" y="78">▸ Shell / Bash</text>
    </g>
    <text x="14" y="180" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="10" fill="{text_secondary}">Systems &amp; algorithmic tooling</text>
  </g>

  <!-- Col 2: AI & Vision -->
  <g transform="translate(254, 52)">
    <rect width="216" height="198" rx="6" fill="{col_bg}" stroke="{border}" stroke-width="1"/>
    <text x="14" y="24" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="700" fill="{accent}">AI &amp; VISION</text>
    <line x1="14" y1="34" x2="202" y2="34" stroke="{border}" stroke-width="0.8"/>

    <g transform="translate(14, 50)" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" fill="{text_primary}">
      <text x="0" y="0">▸ Computer Vision</text>
      <text x="0" y="26">▸ OpenCV Pipelines</text>
      <text x="0" y="52">▸ Video Analytics</text>
      <text x="0" y="78">▸ LLM Architectures</text>
      <text x="0" y="104">▸ RAG / Agent Systems</text>
      <text x="0" y="130">▸ LangChain / APIs</text>
    </g>
    <text x="14" y="180" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="10" fill="{text_secondary}">Inference &amp; perceptual systems</text>
  </g>

  <!-- Col 3: Systems & Runtime -->
  <g transform="translate(484, 52)">
    <rect width="216" height="198" rx="6" fill="{col_bg}" stroke="{border}" stroke-width="1"/>
    <text x="14" y="24" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="700" fill="{accent}">SYSTEMS &amp; RUNTIME</text>
    <line x1="14" y1="34" x2="202" y2="34" stroke="{border}" stroke-width="0.8"/>

    <g transform="translate(14, 50)" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" fill="{text_primary}">
      <text x="0" y="0">▸ Android SDK / NDK</text>
      <text x="0" y="26">▸ JNI Interfacing</text>
      <text x="0" y="52">▸ Linux Environments</text>
      <text x="0" y="78">▸ Docker Containers</text>
      <text x="0" y="104">▸ CMake Build Systems</text>
      <text x="0" y="130">▸ Git &amp; GitHub Actions</text>
    </g>
    <text x="14" y="180" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="10" fill="{text_secondary}">Low-overhead execution runtimes</text>
  </g>

  <!-- Col 4: Web & Backend -->
  <g transform="translate(714, 52)">
    <rect width="222" height="198" rx="6" fill="{col_bg}" stroke="{border}" stroke-width="1"/>
    <text x="14" y="24" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="700" fill="{accent}">WEB &amp; BACKEND</text>
    <line x1="14" y1="34" x2="208" y2="34" stroke="{border}" stroke-width="0.8"/>

    <g transform="translate(14, 50)" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" fill="{text_primary}">
      <text x="0" y="0">▸ React / Next.js</text>
      <text x="0" y="26">▸ Node.js / Express</text>
      <text x="0" y="52">▸ FastAPI Services</text>
      <text x="0" y="78">▸ REST / WebSocket APIs</text>
      <text x="0" y="104">▸ MongoDB</text>
      <text x="0" y="130">▸ MySQL / PostgreSQL</text>
    </g>
    <text x="14" y="180" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif" font-size="10" fill="{text_secondary}">HCI dashboards &amp; telemetry sinks</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# Generate and Validate All 8 Assets
# -------------------------------------------------------------
svg_map = {
    "banner-dark.svg": build_banner(True),
    "banner-light.svg": build_banner(False),
    "identity-dark.svg": build_identity(True),
    "identity-light.svg": build_identity(False),
    "research-dark.svg": build_research(True),
    "research-light.svg": build_research(False),
    "stack-dark.svg": build_stack(True),
    "stack-light.svg": build_stack(False),
}

for filename, content in svg_map.items():
    filepath = os.path.join(ASSETS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    # XML Validation
    try:
        ET.fromstring(content)
        print(f"VALID XML: {filename}")
    except ET.ParseError as e:
        print(f"ERROR in {filename}: {e}")
        raise e

print("All 8 SVGs generated and validated successfully.")
