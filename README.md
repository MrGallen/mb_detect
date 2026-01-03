# Micro:bit Detector

A lightweight Python utility to automatically detect and select BBC micro:bit devices connected via USB.

It handles cross-platform port detection (Windows/Mac/Linux) and robustly manages scenarios where multiple micro:bits are connected simultaneously.

## Features

* **Auto-Detection:** Automatically finds the correct serial port (`COM3`, `/dev/ttyACM0`, etc.).
* **Multi-Device Support:** Can detect multiple connected micro:bits.
* **Smart Selection:**
    * If 1 device is found, it selects it automatically.
    * If multiple are found, it can prompt the user to choose one.
* **Metadata:** Retrieves Serial Numbers to distinguish between identical devices.

## Installation

```bash
pip install mb_detect
