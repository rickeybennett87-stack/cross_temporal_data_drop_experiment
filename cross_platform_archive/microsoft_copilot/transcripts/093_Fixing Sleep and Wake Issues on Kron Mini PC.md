# Fixing Sleep and Wake Issues on Kron Mini PC

- Source: `/home/jadedjade/Documents/copilot-activity-history.csv`
- Source CSV rows: 2356-2357
- Exported messages: 2
- Earliest timestamp: 2026-01-09T11:39:30
- Latest timestamp: 2026-01-09T11:39:30
- Reconstruction: contiguous title run; timestamps ascending; Human before AI for equal timestamps

## Human — 2026-01-09T11:39:30

<!-- source_csv_row: 2357 -->
Tell me every thing you can about this PC and then walk me through whatever I need to do to make it stop powering off or sleeping or whatever it is doing that keeps making the screen go black instead of running the screen saver and the system powering down enough that my Bluetooth mouse and keyboard can wake it up anymore

## AI — 2026-01-09T11:39:30

<!-- source_csv_row: 2356 -->
Here’s everything I’ve found about your **Kron Mini K1 Mini PC**, along with a full walkthrough to stop it from going dark or unresponsive when idle.

---

## 🧠 Full Specs and Capabilities

Your Mini PC is part of the **ACEMAGIC Kron Mini K1** series. Based on the product label and official documentation, here’s what it’s packing:

### Core Hardware
- **Processor**: AMD Ryzen 5 7430U (6 cores / 12 threads, up to 4.3GHz)
- **Graphics**: Integrated AMD Radeon RX Vega 7 (1800MHz GPU frequency)
- **RAM**: 16GB DDR4 (upgradeable to 64GB)
- **Storage**: 256GB M.2 NVMe SSD (upgradeable to 2TB)

### Connectivity
- **Wi-Fi**: WiFi 6
- **Bluetooth**: 5.2
- **Ports**: USB-C, USB-A, HDMI 2.0, DisplayPort 1.4, audio jack
- **Display Support**: Triple 4K output (HDMI + DP + USB-C)

### Power Input
- **DC 19V** barrel jack (not USB-C powered)

### Operating System
- Typically ships with **Windows 11 Home or Pro**, but Linux is also supported.

---

## 🛠️ Fixing the Sleep/Black Screen Issue

Your issue sounds like a combination of **aggressive sleep settings** and **Bluetooth power management**. Here’s how to fix it:

### 1. **Disable Sleep and Screen Timeout**
Go to:
- **Settings → System → Power & Battery → Screen and Sleep**
  - Set **“When plugged in”** and **“On battery”** to:
    - *Turn off my screen*: **Never**
    - *Put my device to sleep*: **Never**

### 2. **Enable Screen Saver Instead of Sleep**
- Press **Windows + R**, type `control desk.cpl,,@screensaver`, press Enter.
- Choose a screen saver (e.g., “Blank” or “Mystify”).
- Set **Wait time** (e.g., 10 minutes).
- **Uncheck** “On resume, display logon screen” if you don’t want to re-enter your password.

### 3. **Prevent Bluetooth Devices from Being Disabled**
- Open **Device Manager** (Windows + X → Device Manager).
- Expand **Bluetooth**, right-click your mouse and keyboard → **Properties**.
- Go to **Power Management tab**.
  - **Uncheck** “Allow the computer to turn off this device to save power”.

### 4. **Allow Bluetooth Devices to Wake the PC**
- In Device Manager, for each Bluetooth device:
  - Go to **Properties → Power Management**
  - **Check** “Allow this device to wake the computer”

### 5. **Disable USB Selective Suspend**
- Go to **Control Panel → Power Options → Change plan settings → Change advanced power settings**
- Expand **USB settings → USB selective suspend setting**
  - Set to **Disabled**

### 6. **Check BIOS Settings (Optional)**
If the issue persists:
- Reboot and enter BIOS (usually **Del** or **F2** during startup).
- Look for:
  - **Wake on USB** or **Wake on Bluetooth** → Enable
  - **Power Saving / S3 Sleep** → Disable or set to **S1/S0**

---

## 🧪 Final Test Sequence

Try this after applying all settings:
1. Leave the PC idle for 15–30 minutes.
2. Let the screen saver activate.
3. Move your Bluetooth mouse or press a key.
4. Confirm the system wakes without needing a hard power cycle.

If it still fails, I can walk you through creating a **custom power plan** or checking for **driver conflicts**. Just say the word.

Would you like me to help you verify the BIOS wake settings or build a diagnostic checklist for deeper troubleshooting?
