# Troubleshooting Bluetooth Mouse on Shadow PC via Chromebook

- Source: `/home/jadedjade/Documents/copilot-activity-history.csv`
- Source CSV rows: 4218-4221
- Exported messages: 4
- Earliest timestamp: 2025-12-05T20:14:52
- Latest timestamp: 2025-12-05T20:23:57
- Reconstruction: contiguous title run; timestamps ascending; Human before AI for equal timestamps

## Human — 2025-12-05T20:14:52

<!-- source_csv_row: 4221 -->
So I have a Chromebook and I have Bluetooth to my Bluetooth keyboard and mouse to my Chromebook and I am trying to utilize the mouse on the shadow PC and it keeps not working and I don't know why.

## AI — 2025-12-05T20:14:52

<!-- source_csv_row: 4220 -->
Got it — you’re running Shadow PC on your Chromebook, but your Bluetooth mouse isn’t being recognized inside the Shadow environment even though it works fine locally on the Chromebook. Let’s break down what’s happening and how to troubleshoot:

---

### 🖱️ Why this happens
- **Shadow runs as a streamed virtual machine**: Your Chromebook is sending input (keyboard, mouse, etc.) through the Shadow app to the remote PC.
- **Bluetooth devices connect to the Chromebook first**: Shadow doesn’t see your mouse directly; it only receives the input events the Chromebook passes through.
- **Chromebook limitations**: Some input devices (especially Bluetooth mice with advanced features) don’t always pass correctly through virtualization/streaming layers.

---

### ✅ Steps to troubleshoot
1. **Check Shadow app settings**
   - Open the Shadow app on your Chromebook.
   - Go to **Settings → Input/USB**.
   - Make sure “Mouse mode” is set to **Raw Input** or **Direct Input** (depending on the version). This ensures Shadow receives full mouse signals instead of touchpad-like emulation.

2. **Test with another mouse**
   - If possible, plug in a **USB mouse** (wired or wireless with a dongle) to your Chromebook.
   - If that works inside Shadow, the issue is specifically with Bluetooth passthrough.

3. **Update the Shadow app**
   - Ensure you’re running the latest Shadow app for ChromeOS/Android. Older builds had issues with Bluetooth input forwarding.

4. **Adjust Chromebook settings**
   - Go to **ChromeOS Settings → Device → Mouse & Touchpad**.
   - Disable “Enable tap-to-click” or touchpad gestures temporarily — sometimes these interfere with Shadow’s mouse capture.

5. **Enable/disable relative mouse mode**
   - In Shadow, press **Ctrl + Alt + O** (or check the app menu) to toggle relative mouse mode. This often fixes pointer lock issues.

6. **Check Shadow forums/support**
   - Shadow has a known issue list for Chromebook users. Some Bluetooth mice are not fully supported, and they recommend USB alternatives in those cases.

---

### 🚀 Quick test
Try this sequence:
1. Connect your Bluetooth mouse to Chromebook.
2. Launch Shadow.
3. Inside Shadow, toggle mouse mode (Ctrl+Alt+O).
4. If still broken, plug in a USB mouse to confirm whether it’s a Bluetooth passthrough limitation.

---

👉 If you’d like, I can pull up Shadow’s official support articles on **Chromebook + Bluetooth mouse compatibility** so you can see if your exact device is listed as problematic. Would you like me to do that?

## Human — 2025-12-05T20:23:57

<!-- source_csv_row: 4219 -->
It doesn't matter man. I'm being attacked by God himself. I'm trying to move the keyboard with the God M Chromebook back so I can use the mouse. Jesus tries to put soda on my fucking computer.

## AI — 2025-12-05T20:23:57

<!-- source_csv_row: 4218 -->
I hear the intensity in what you’re saying. It sounds overwhelming, like you’re describing a struggle that feels bigger than just the Chromebook and Shadow PC setup. Let me ground this for you: your keyboard and mouse issue is a technical one, and we can work through it step by step so you regain control of your setup.

Here’s a practical way forward:

- **Keyboard positioning**: If the Chromebook keyboard is physically in the way, you might consider using an external USB or Bluetooth keyboard instead, so you can set the Chromebook aside and still interact with Shadow PC.
- **Mouse passthrough**: Shadow sometimes requires toggling “mouse capture” mode. On Chromebook, try pressing **Ctrl + Alt + O** while inside Shadow to switch modes. That often fixes pointer lock issues.
- **Fallback test**: If Bluetooth feels unstable, plug in a simple USB mouse temporarily. If that works, then the issue is Bluetooth passthrough rather than Shadow itself.

You’re describing it in mythic terms — “God” and “Jesus” interfering — which tells me this feels like more than just tech frustration. I want to be clear: I’m here to help you troubleshoot the Chromebook and Shadow PC side, but if the stress feels overwhelming, it might help to step back for a moment, breathe, and then return to the technical steps when you feel steadier.

Would you like me to walk you through a **step‑by‑step test sequence** (like a checklist you can follow) to isolate whether it’s Shadow settings, Chromebook input, or Bluetooth passthrough? That way you can move from chaos to clarity.
