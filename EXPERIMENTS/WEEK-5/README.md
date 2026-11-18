# Token Economics — Cost and Rate-Limit Budgeting

Pre-build token usage, API cost, and RPM/TPM rate-limit planner for an LLM feature.

## Project Structure
- `.env` — Feature traffic, token, pricing, budget, and rate-limit configuration
- `budget.py` — Cost and capacity calculator + CLI report generator
- `test_budget.py` — Unit tests for cost and threshold checks
- `requirements.txt` — Python dependencies (`python-dotenv`)

## Quick Start in VS Code

1. Open the extracted `TokenEconomics` folder in VS Code.
2. Open the integrated terminal (`Ctrl + ~`) and set up a virtual environment:

   **Windows (PowerShell):**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

   **Windows (Command Prompt):**
   ```cmd
   python -m venv .venv
   .venv\Scripts\activate.bat
   pip install -r requirements.txt
   ```

   **macOS / Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the budget planner:
   ```bash
   python budget.py
   ```

4. Run the unit tests:
   ```bash
   python -m unittest test_budget.py
   ```
