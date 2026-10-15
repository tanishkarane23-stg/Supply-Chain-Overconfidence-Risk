# Supply-Chain-Overconfidence-Risk

Welcome to the Hawkins Lab Supply Chain Risk Portal. This Flask-based web application analyzes supply chain metrics to determine if a network is stable, or if critical overconfidence has left it vulnerable to a gateway breach (The Upside Down). 

##  Features

*   **Immersive Stranger Things UI:** A dynamic, multi-page Tailwind CSS interface featuring floating spores, portal transitions, CRT scanlines, and reactive ambient audio.
*   **Risk Analysis Engine:** Calculates a 0-100% risk score based on three core supply chain pillars:
    *   **Performance:** Historical Fill Rate and Average Lead Time.
    *   **Buffer:** Inventory Buffer and Recovery Time.
    *   **Network:** Supplier Count and Concentration Ratio.
*   **Dynamic Dashboard State:** If the risk score exceeds 75%, the system triggers a "DANGER" state, altering the UI to reflect an Upside Down breach (complete with visual distortions, red neon aesthetics, and alarm audio).

##  Repository Structure

```text
hawkins-supply-risk/
â”œâ”€â”€ app.py                  # Core Flask application and risk logic
â”œâ”€â”€ requirements.txt        # Python dependencies
â”œâ”€â”€ static/                 # Assets
â”‚   â”œâ”€â”€ style.css           # Retro thematic styling
â”‚   â””â”€â”€ clock.mp3           # Ambient Upside Down audio
â”œâ”€â”€ templates/              # HTML views
â”‚   â”œâ”€â”€ landing.html        # Initial market alert screen
â”‚   â”œâ”€â”€ portal.html         # Gateway transition animation
â”‚   â”œâ”€â”€ input.html          # Data upload interface
â”‚   â””â”€â”€ dashboard.html      # Reactive results dashboard
â””â”€â”€ *.xlsx                  # Sample standard & 'overconfident' datasets
