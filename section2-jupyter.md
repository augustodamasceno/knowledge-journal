# **Section 2 - Working with Jupyter Files**

## **What are Jupyter Notebook Files?**

Jupyter Notebook files (`*.ipynb`) are documents that allow you to combine live code, visualizations, and explanatory text in a single interactive environment. 
These are widely used for data analysis, machine learning, and scientific research.
---

## **Prerequisites for Working with Jupyter Notebooks**

Before working with Jupyter Notebooks, you need Python and a way to manage packages and isolated environments. There are two main approaches to choose from:

- **Traditional approach (sections 1–3):** Use Python with `pip` for package installation and `venv` for virtual environment management. This is the most widely documented approach and works on all platforms.
- **Modern approach (section 4):** Use `uv`, a single fast tool written in Rust that replaces `pip`, `venv`, and more. Recommended for new projects due to its speed and simplicity.

Regardless of which approach you choose, section 5 explains how to install project dependencies from a `requirements.txt` file.

### **1. Python**  
Jupyter Notebooks are built on Python, so you will need to have Python installed on your system. 
You can download Python from [python.org](https://www.python.org/downloads/) or use a package manager (like `apt` on Linux or `brew` on macOS).

To check if Python is installed, run the following in your terminal or command prompt:

```bash
python3 --version
```

### **2. Pip**
Pip is Python's package installer, used to install external libraries that Jupyter Notebooks often rely on (e.g., numpy, pandas, matplotlib). Make sure pip is installed:

```bash
pip3 --version
```
If pip is not installed, you can install it using:

```bash
python3 -m ensurepip --upgrade
```

### **3. Python Virtual Environment (venv)**

A **Python virtual environment** creates isolated environments to manage Python packages and dependencies separately for each project, preventing conflicts between projects.

* Install 
```bash
# Debian/Ubuntu
sudo apt install python3-venv

# Fedora
sudo dnf install python3-venv

# Arch
sudo pacman -S python

# FreeBSD
pkg install py39-virtualenv  # or adjust version as needed

# Windows
# No installation needed, venv comes with Python ≥ 3.3
```

* Creating a Virtual Environment

In your terminal, navigate to your project's directory and run:

```bash
python3 -m venv myenv
```

This command creates a new virtual environment named `myenv`.

* Activating the Virtual Environment

**On FreeBSD/Linux/macOS:**

```bash
source myenv/bin/activate
```

**On Windows (CMD):**

```cmd
myenv\Scripts\activate
```

**On Windows (PowerShell):**

```powershell
myenv\Scripts\Activate.ps1
```

After activation, your terminal prompt will start with `(myenv)`.

* Installing Packages

Within your activated environment, install packages using:

```bash
pip install package_name
```

These packages will only exist inside this environment.

* Deactivating the Environment

To exit the virtual environment, run:

```bash
deactivate
```

Your terminal prompt returns to normal.

### **4. uv**

`uv` is an extremely fast Python package and project manager written in Rust. It can replace `pip`, `venv`, and more in a single tool.

* Installation

```bash
# Using pip
pip install uv

# Standalone installer (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

To verify the installation:

```bash
uv --version
```

* Creating a Virtual Environment

```bash
uv venv myenv
```

Activation and deactivation work the same as with `venv` (see section 3 above).

* Installing Packages

```bash
uv pip install package_name
```

* Installing from requirements.txt

```bash
uv pip install -r requirements.txt
```

* Running Jupyter directly without activating the environment

```bash
uv run jupyter notebook
```

---

### **5. Requirements**
Activate your virtual environment and install all dependencies listed in the requirements.txt file.

```bash
pip install -r requirements.txt
```


