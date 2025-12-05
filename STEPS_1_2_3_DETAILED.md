# Steps 1-3: Install Git & Configure - Detailed Guide

## 📌 STEP 1: Install Git on Windows

### What is Git?
Git is a tool that tracks changes to your code and helps you upload projects to GitHub.

### How to Install Git:

#### **Method 1: Automatic (Recommended)**

1. Open your web browser (Chrome, Firefox, Edge, Safari)

2. Go to: https://git-scm.com/download/win
   - Click the blue "Click here to download" button
   - Or it may auto-download

3. Find the downloaded file:
   - Look in your Downloads folder
   - File name: `Git-2.x.x-64-bit.exe` (version number may be different)

4. **Double-click the file to run the installer**

5. **Installation Window appears**
   ```
   ┌─────────────────────────────────────────┐
   │ Git Setup Wizard                        │
   │                                         │
   │ [Next >] [Cancel]                       │
   └─────────────────────────────────────────┘
   ```
   - Click **Next >** button

6. **License Agreement**
   ```
   ┌─────────────────────────────────────────┐
   │ GNU GENERAL PUBLIC LICENSE              │
   │                                         │
   │ [Read through this]                     │
   │                                         │
   │ [Next >] [Cancel]                       │
   └─────────────────────────────────────────┘
   ```
   - Click **Next >** button (don't worry about reading the license)

7. **Choose Installation Folder**
   ```
   ┌─────────────────────────────────────────┐
   │ Select Destination Location             │
   │                                         │
   │ C:\Program Files\Git\                   │
   │                                         │
   │ [Next >] [Cancel]                       │
   └─────────────────────────────────────────┘
   ```
   - Keep default path
   - Click **Next >** button

8. **Select Components**
   ```
   ┌─────────────────────────────────────────┐
   │ Select Components                       │
   │ ☑ Git Bash Here                         │
   │ ☑ Git GUI Here                          │
   │ ☑ Git LFS (Large File Support)          │
   │ ☑ Associate .git* configuration files   │
   │ ☑ Associate .sh files to be run with Bash
   │                                         │
   │ [Next >] [Cancel]                       │
   └─────────────────────────────────────────┘
   ```
   - Keep all defaults (all checked ☑)
   - Click **Next >** button

9. **Start Menu Folder**
   ```
   ┌─────────────────────────────────────────┐
   │ Start Menu Folder                       │
   │ Git                                     │
   │                                         │
   │ [Next >] [Cancel]                       │
   └─────────────────────────────────────────┘
   ```
   - Keep default
   - Click **Next >** button

10. **Choose Default Editor**
    ```
    ┌─────────────────────────────────────────┐
    │ Choose the default editor for Git       │
    │                                         │
    │ ○ Vim                                   │
    │ ○ Nano                                  │
    │ ○ Notepad                               │
    │ ○ Visual Studio Code                    │
    │ ● Use Notepad++ as Git's default editor│
    │                                         │
    │ [Next >] [Cancel]                       │
    └─────────────────────────────────────────┘
    ```
    - Any option is fine
    - Click **Next >** button

11. **Adjust the name of the initial branch**
    ```
    ┌─────────────────────────────────────────┐
    │ Adjust the name of the initial branch   │
    │                                         │
    │ ○ Let Git decide                        │
    │ ● Override the default branch name      │
    │   (for new repositories)                │
    │   [main]                                │
    │                                         │
    │ [Next >] [Cancel]                       │
    └─────────────────────────────────────────┘
    ```
    - Select **"Override the default branch name"**
    - Keep it as "main"
    - Click **Next >** button

12. **Adjust your PATH environment**
    ```
    ┌─────────────────────────────────────────┐
    │ Adjust your PATH environment            │
    │                                         │
    │ ● Use Git from the Windows Command      │
    │   Prompt (recommended)                  │
    │ ○ Use Git from Git Bash only            │
    │ ○ Use Git and optional Unix tools       │
    │                                         │
    │ [Next >] [Cancel]                       │
    └─────────────────────────────────────────┘
    ```
    - Select **"Use Git from the Windows Command Prompt"**
    - Click **Next >** button

13. **Choose HTTPS transport backend**
    ```
    ┌─────────────────────────────────────────┐
    │ Choose HTTPS transport backend          │
    │                                         │
    │ ● Use the native Windows Secure Channel │
    │   library (recommended)                 │
    │ ○ Use OpenSSL library                   │
    │                                         │
    │ [Next >] [Cancel]                       │
    └─────────────────────────────────────────┘
    ```
    - Keep default selected
    - Click **Next >** button

14. **Configure the line ending conversions**
    ```
    ┌─────────────────────────────────────────┐
    │ Configure the line ending conversions   │
    │                                         │
    │ ● Checkout Windows-style, commit Unix   │
    │   -style line endings (recommended)     │
    │ ○ Checkout as-is, commit Unix-style     │
    │ ○ Checkout as-is, commit as-is          │
    │                                         │
    │ [Next >] [Cancel]                       │
    └─────────────────────────────────────────┘
    ```
    - Keep default selected
    - Click **Next >** button

15. **Configure the terminal emulator**
    ```
    ┌─────────────────────────────────────────┐
    │ Configure the terminal emulator to use  │
    │ with Git Bash                           │
    │                                         │
    │ ● Use MinTTY (the default terminal of   │
    │   MSYS2) - recommended                  │
    │ ○ Use Windows' default console window   │
    │                                         │
    │ [Next >] [Cancel]                       │
    └─────────────────────────────────────────┘
    ```
    - Keep default selected
    - Click **Next >** button

16. **Choose the default behavior of `git pull`**
    ```
    ┌─────────────────────────────────────────┐
    │ Choose the default behavior of git pull │
    │                                         │
    │ ● Default (fast-forward or merge)       │
    │ ○ Rebase                                │
    │ ○ Only ever fast-forward                │
    │                                         │
    │ [Next >] [Cancel]                       │
    └─────────────────────────────────────────┘
    ```
    - Keep default selected
    - Click **Next >** button

17. **Choose a credential helper**
    ```
    ┌─────────────────────────────────────────┐
    │ Choose a credential helper              │
    │                                         │
    │ ● Git Credential Manager (recommended)  │
    │ ○ Git Credential Manager Core           │
    │ ○ None                                  │
    │                                         │
    │ [Next >] [Cancel]                       │
    └─────────────────────────────────────────┘
    ```
    - Keep default selected
    - Click **Next >** button

18. **Extra options**
    ```
    ┌─────────────────────────────────────────┐
    │ Extra options                           │
    │                                         │
    │ ☑ Enable file system caching            │
    │ ☐ Enable symbolic links (requires admin)
    │                                         │
    │ [Next >] [Cancel] [Install]             │
    └─────────────────────────────────────────┘
    ```
    - Click **[Install]** button

19. **Installation Progress**
    ```
    ┌─────────────────────────────────────────┐
    │ Installing...                           │
    │ ████████████████░░░░░░░░ 60%            │
    │                                         │
    │ [Cancel]                                │
    └─────────────────────────────────────────┘
    ```
    - Wait for installation to complete (1-2 minutes)

20. **Installation Complete**
    ```
    ┌─────────────────────────────────────────┐
    │ Completing the Git Setup Wizard         │
    │                                         │
    │ ☐ View Release Notes                    │
    │ ☑ Launch Git Bash                       │
    │                                         │
    │ [Finish]                                │
    └─────────────────────────────────────────┘
    ```
    - Click **[Finish]** button
    - ✅ **Git is now installed!**

---

## 📌 STEP 2: Verify Git Installation

After installation, verify that Git was installed correctly.

### Open PowerShell:

1. **Press the Windows key** (bottom left of keyboard)
2. **Type: `PowerShell`**
3. **Click on "Windows PowerShell"** (or "Windows PowerShell ISE")

   ```
   ┌─────────────────────────────────────────┐
   │ Search Results                          │
   │ ┌─────────────────────────────────────┐ │
   │ │ Windows PowerShell                  │ │ ← Click here
   │ │ Windows PowerShell ISE              │ │
   │ └─────────────────────────────────────┘ │
   └─────────────────────────────────────────┘
   ```

### PowerShell Window Opens:

```
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\SRIJA>
```

### Type the command to check Git version:

```powershell
git --version
```

### Press Enter

You should see:
```
git version 2.42.0.windows.2
```

(The version number might be different, that's OK!)

✅ **If you see this, Git is installed correctly!**

If you get an error like `git is not recognized`, Git wasn't installed correctly. Try installing again.

---

## 📌 STEP 3: Configure Git with Your Name and Email

This tells Git who you are (needed for commits).

### In the PowerShell window, type:

```powershell
git config --global user.name "Your Full Name"
```

**Replace "Your Full Name" with your actual name:**
- Example: `git config --global user.name "Srija Patel"`
- Don't include the quotes around your name in the actual command

### Press Enter

(No response means it worked)

### Now configure your email:

```powershell
git config --global user.email "your.email@gmail.com"
```

**Replace "your.email@gmail.com" with your actual email:**
- Example: `git config --global user.email "srija.patel@gmail.com"`
- Use the same email you'll use for GitHub

### Press Enter

(No response means it worked)

---

## 📌 STEP 3: Verify Git Configuration

To confirm the configuration is correct:

### Type:

```powershell
git config --global --list
```

### Press Enter

You should see output like:

```
user.name=Srija Patel
user.email=srija.patel@gmail.com
credential.helper=wincred
core.autocrlf=true
...
```

✅ **If you see your name and email, configuration is complete!**

---

## Complete Step-by-Step Summary

### Step 1: Install Git
- Download from https://git-scm.com/download/win
- Run the installer
- Click Next through all screens
- Use default options for everything

### Step 2: Verify Installation
- Open PowerShell
- Type: `git --version`
- You should see a version number

### Step 3: Configure Git
- Type: `git config --global user.name "Your Name"`
- Type: `git config --global user.email "your.email@gmail.com"`
- Verify with: `git config --global --list`

---

## ✅ Verification Checklist

```
☐ Downloaded Git installer from https://git-scm.com/download/win
☐ Ran the installer
☐ Clicked through all setup screens
☐ Opened PowerShell
☐ Ran: git --version
☐ Saw version number (e.g., git version 2.42.0)
☐ Ran: git config --global user.name "Your Name"
☐ Ran: git config --global user.email "your.email@gmail.com"
☐ Ran: git config --global --list
☐ Saw name and email in output
```

---

## 🎯 What's Next?

Once you complete steps 1-3, you're ready for:
- **Step 4**: Create a repository on GitHub
- **Step 5-9**: Initialize Git in your project folder
- **Step 10-11**: Push your code to GitHub

**You've successfully completed the hardest part! 🎉**

The rest is much easier - just copy-paste commands from the GITHUB_GUIDE.md file.

---

## Troubleshooting

### **Git command not found**
```
Error: 'git' is not recognized as an internal or external command
```

**Solution:**
- Git didn't install properly
- Try reinstalling from https://git-scm.com/download/win
- Make sure to select "Use Git from the Windows Command Prompt"

### **PowerShell is not opening**
- Press Windows Key + R
- Type `powershell` and press Enter
- Or search "PowerShell" from Start menu

### **Can't find the installer**
- Check your Downloads folder
- Or go directly to https://git-scm.com/download/win
- Click "Click here to download manually"

---

**When you complete steps 1-3, come back and do steps 4-11 from the GITHUB_GUIDE.md file! ✅**
