# **Session 1 - Working with Jupyter Files**

## **What are Jupyter Notebook Files?**

Jupyter Notebook files (`*.ipynb`) are documents that allow you to combine live code, visualizations, and explanatory text in a single interactive environment. 
These are widely used for data analysis, machine learning, and scientific research.
---

## **Prerequisites for Working with Jupyter Notebooks**

Before you start working with Jupyter Notebooks, you need to make sure your system is set up with the necessary tools:

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

### *3. Python Virtual Environment (venv)*

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

#### **4. Requirements**
Activate your virtual environment and install all dependencies listed in the requirements.txt file.

```bash
pip install -r requirements.txt
```


