# 🎮 Python Games Collection

A collection of Python games and applications built with popular Python libraries like Pygame and DearPyGui.

## 📁 Project Contents

- **`calculator.py`** - A GUI calculator application built with DearPyGui
- **`jump_example_02.py`** - A jumping ball game built with Pygame
- **`tictactoe.py`** - Classic Tic-Tac-Toe game
- **`wordrescue.py`** - Word rescue game
- **`jumpingGame.py`** - Another jumping game variant

## 🖥️ Cross-Platform Compatibility

✅ **All games work on Windows, macOS, and Linux!**

The games use cross-platform Python libraries:
- **DearPyGui** - Modern GUI framework
- **Pygame** - Game development library

## 🚀 Setup Instructions

### Prerequisites
Make sure you have Python 3.8 or higher installed on your system.

---

## 🪟 Windows Setup

### Method 1: Using Command Prompt (Recommended for beginners)

```cmd
# 1. Navigate to the project directory
cd path\to\py_games

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
venv\Scripts\activate

# 4. Install dependencies
pip install dearpygui pygame

# 5. Run a game
python calculator.py
python jump_example_02.py
```

### Method 2: Using PowerShell (Multiple options)

**Option A: Use batch file (Works with any execution policy)**
```powershell
# 1. Navigate to project directory
cd path\to\py_games

# 2. Create virtual environment
python -m venv venv

# 3. Activate using batch file (avoids execution policy issues)
venv\Scripts\activate.bat

# 4. Install dependencies
pip install dearpygui pygame

# 5. Run games
python calculator.py
```

**Option B: Enable PowerShell scripts (One-time setup)**
```powershell
# Allow scripts for current user (run once):
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then you can use the PowerShell script:
.\venv\Scripts\Activate.ps1
```

**Option C: Bypass execution policy temporarily**
```powershell
# Bypass policy for one session:
PowerShell -ExecutionPolicy Bypass -File "venv\Scripts\Activate.ps1"
```

### Deactivating the environment:
```cmd
deactivate
```

---

## 🍎 macOS Setup

### Using Terminal

```bash
# 1. Navigate to the project directory
cd path/to/py_games

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Upgrade pip (recommended)
pip install --upgrade pip

# 5. Install dependencies
pip install dearpygui pygame

# 6. Run a game
python calculator.py
python jump_example_02.py
```

### If you don't have Python installed:
```bash
# Install using Homebrew (recommended):
brew install python

# Or download from python.org
```

### Deactivating the environment:
```bash
deactivate
```

---

## 🐧 Linux Setup (Ubuntu/Debian)

### Using Terminal

```bash
# 1. Update package list and install Python (if needed)
sudo apt update
sudo apt install python3 python3-pip python3-venv

# 2. Navigate to the project directory
cd path/to/py_games

# 3. Create virtual environment
python3 -m venv venv

# 4. Activate virtual environment
source venv/bin/activate

# 5. Upgrade pip (recommended)
pip install --upgrade pip

# 6. Install dependencies
pip install dearpygui pygame

# 7. Run a game
python calculator.py
python jump_example_02.py
```

### For other Linux distributions:

**CentOS/RHEL/Fedora:**
```bash
# Install Python
sudo yum install python3 python3-pip  # CentOS/RHEL
sudo dnf install python3 python3-pip  # Fedora

# Then follow the same steps as Ubuntu
```

**Arch Linux:**
```bash
# Install Python
sudo pacman -S python python-pip

# Then follow the same steps as Ubuntu
```

### Deactivating the environment:
```bash
deactivate
```

---

## 🎯 Quick Start Guide

After setting up your virtual environment:

1. **Test the Calculator:**
   ```bash
   python calculator.py
   ```
   - Click number buttons to enter numbers
   - Use +, -, ×, ÷ for operations
   - Press = to calculate
   - Use C to clear, ⌫ to delete

2. **Test the Jumping Game:**
   ```bash
   python jump_example_02.py
   ```
   - Use SPACE to jump
   - Use LEFT/RIGHT arrows to move
   - Ball wraps around screen edges

---

## 📦 Dependencies

The project uses these Python packages:

- **dearpygui** - Modern GUI framework for the calculator
- **pygame** - Game development library for the games

### Installing individual packages:
```bash
# Activate your virtual environment first, then:
pip install dearpygui  # For calculator app
pip install pygame     # For games
```

---

## 🛠️ Troubleshooting

### Common Issues:

**"Python not found" error:**
- Make sure Python is installed and added to your PATH
- On Windows, try `py` instead of `python`
- On macOS/Linux, try `python3` instead of `python`

**Virtual environment activation fails:**
- **Windows PowerShell "execution policy" error:**
  - Use batch file: `venv\Scripts\activate.bat` (easiest solution)
  - Or enable scripts: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
  - Or use Command Prompt instead of PowerShell
- Make sure you're in the correct directory
- Check that the virtual environment was created successfully

**Package installation fails:**
- Make sure your virtual environment is activated
- Try upgrading pip: `pip install --upgrade pip`
- Check your internet connection

**Games don't run:**
- Ensure all dependencies are installed: `pip list`
- Check that you're running from the correct directory
- Make sure your virtual environment is activated

### Getting Help:
If you encounter issues:
1. Check that Python 3.8+ is installed: `python --version`
2. Verify virtual environment is activated (should see `(venv)` in prompt)
3. List installed packages: `pip list`
4. Try reinstalling packages: `pip install --force-reinstall dearpygui pygame`

---

## 🎮 How to Play

### Calculator
- Standard calculator with +, -, ×, ÷ operations
- Supports decimal numbers
- Clear button (C) resets everything
- Backspace button (⌫) deletes last character

### Jumping Ball Game
- **SPACE**: Make the ball jump
- **LEFT/RIGHT arrows**: Move the ball horizontally
- **Goal**: Keep the ball bouncing and moving!
- The ball wraps around screen edges

---

## 🚀 Next Steps

Want to expand the project? Try:
- Adding new games
- Improving the calculator with memory functions
- Creating multiplayer features
- Adding sound effects
- Building a game launcher menu

## 📄 License

This project is open source. Feel free to modify and distribute!

---

**Happy Gaming! 🎮**