# Week 4 – Tokenizer Lab (BPE, WordPiece, SentencePiece)

Comparison of **BPE (`gpt2`)**, **WordPiece (`bert-base-multilingual-cased`)**, and **SentencePiece (`xlm-roberta-base`)** across **English**, **Telugu**, and **Hindi**.

## How to Run in VS Code

1. Extract this ZIP archive and open the `Week4` folder in **VS Code** (`File -> Open Folder...`).
2. Open the integrated terminal in VS Code (`Ctrl + ~`).
3. Create and activate a virtual environment (or activate your existing `.MyEnv`):
   - **Windows (PowerShell):**
     ```powershell
     python -m venv .MyEnv
     .\.MyEnv\Scripts\Activate.ps1
     ```
     *(If using an existing `.MyEnv` in the parent folder: `..\.MyEnv\Scripts\Activate.ps1`)*
   - **macOS / Linux:**
     ```bash
     python3 -m venv .MyEnv
     source .MyEnv/bin/activate
     ```
4. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the program:
   ```bash
   python tokenizer_comparison.py
   ```
   *(Note: Internet access is required on the first run to download the pretrained tokenizer files.)*
