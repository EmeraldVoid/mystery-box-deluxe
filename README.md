<p align="center"><img src="https://i.imgur.com/D2XfHia.png"></p>

[![Made with - Python](https://img.shields.io/badge/Made_with-Python-3776AB?logo=Python&logoColor=ffcc00)](https://)

---

# Mystery Box Deluxe

Mystery Box Deluxe is a randomizer that generates a randomized seed file for use with the [Goemon Randomizer](https://github.com/abyssonym/mn64rando) by [abyssonym](https://www.github.com/abyssonym).

This project got its name because it is a randomizer for a randomizer. Since seeds are unique per person (even with the same settings), it adds an extra layer of chaos. This tool was made purely for fun.

**Be sure to get the [latest release!](https://github.com/EmeraldVoid/mystery-box-deluxe/releases)**

---

## Features
- Automatically generates a randomized YAML seed file.
- Compatible with the Goemon Randomizer.
- Simple and lightweight Python script.

---

## Installation & Usage

### **Step 1: Download**
Head over to the [latest releases](www.google.com) to get the most up-to-date version. Place this file in a dedicated folder alongside the Goemon Randomizer.

### **Step 2: Set Up a Virtual Environment (Recommended)**
To keep dependencies isolated, create and activate a virtual environment:

#### **Windows**
```sh
python -m venv venv
venv\Scripts\activate
```

#### **Mac/Linux**
```sh
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install Dependencies**
Ensure `pyyaml` is installed by running:
```sh
pip install pyyaml
```

### **Step 4: Run the Script**
#### **Windows**
- Double-click the `.py` file if Python is installed.
- Alternatively, open a terminal (`cmd` or `PowerShell`) and run:
  ```sh
  python Mystery_Box_Deluxe.py
  ```

#### **Mac/Linux**
- Open a terminal and navigate to the script's directory:
  ```sh
  cd /path/to/script
  ```
- Run the script:
  ```sh
  python3 Mystery_Box_Deluxe.py
  ```

### **Step 5: Locate the Output File**
The script will automatically save the generated YAML file inside a folder named **`Random Seeds`** in the same directory as the script.

To find your file:
- Navigate to the folder where `Mystery_Box_Deluxe.py` is located.
- Open the **`Random Seeds`** folder.
- The newly generated YAML file will be inside, with a timestamped filename.

### **Step 6: Copy the Output to mn64_settings.yaml**
- Navigate to `mn64_settings.yaml`.
- Open it and replace the contents with the generated YAML file.
- Save the file (`Ctrl + S`).

### **Step 7: Run the Randomizer**
- Open `mn64rando.exe` and wait.
- The output will contain a playable ROM with the randomized settings.

### **Step 8: Enjoy!**
Have fun with your randomized experience!

---

## Contributing
Pull requests are welcome! Please ensure your contributions align with the project's goals and coding standards.

