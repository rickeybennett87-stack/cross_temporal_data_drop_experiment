# Exway battery compatibility

- Conversation ID: `6898723d-062c-832d-9446-1439498feb23`
- Created: 2025-08-10T10:20:14.860271+00:00
- Updated: 2025-08-10T10:20:26.648006+00:00
- Default model: gpt-5
- Source shard: `conversations-000.json`

# All exported message nodes

This includes alternate, superseded, and branched nodes.

<!-- parent_node_id: 2ecbff85-dfd6-4e89-b631-fc92a1fe4b10 -->
## user — 2025-08-10T10:20:14.215300+00:00

<!-- node_id: bbb21ba2-c3fa-43e6-a2c3-c3bd19dd1ea1 -->
Hey so I need to make a non-xway battery work on an Xway longboard how does the smart battery on an X-ray determine it's an x-way battery

<!-- parent_node_id: bbb21ba2-c3fa-43e6-a2c3-c3bd19dd1ea1 -->
## assistant — 2025-08-10T10:20:20.459968+00:00

<!-- node_id: c8da437c-512c-4cd7-91db-a054902976cf -->
<!-- model: gpt-5 -->
You're asking how an Exway board's *smart battery* system determines whether it's an authentic “X-way” (i.e., Exway) battery—so you can explore whether a non-Exway battery can be made to work. Here’s what I found:

---

###  How Exway Smart Batteries Are Identified

Most discussions suggest that Exway’s system relies on a **data connection**—not just power lines. In effect, the ESC (electronic speed controller) expects to receive data from the battery's internal management system (BMS) or a specific communication interface. Without that proper handshake, the board may not function properly. Essentially, the ESC is looking for firmware or signals that indicate it's talking to a genuine Exway battery. citeturn1search1

---

###  Community Insight on Compatibility Workarounds

On Reddit, one user outlined two potential methods when using a non-standard battery:

> **"You can attempt to reverse engineer the data protocol used between the ESC and the smart battery by using an oscilloscope to analyze the signals… Or, keep the original battery BMS as a ‘data battery’ and use a secondary battery just for power, as long as voltage/current match."** citeturn1search1

- **Method 1: Reverse Engineering the Data Protocol**  
  Quite technical—requires capturing and decoding communications and then emulating them with a microcontroller.

- **Method 2: Use the Original Battery as a "Data Pass-Through"**  
  Retain the original battery’s BMS solely for data communication, and connect an external battery to actually supply power. This bypasses the need to recreate that data handshake, though it demands careful handling to ensure voltages and currents align.

---

###  Summary & What You Can Do

- **Exway boards detect authenticity via the data handshake between ESC and battery.** Without it, the board won’t operate correctly.
- **Possible options include:**
  1. Reverse-engineering the communication (advanced and complex).
  2. Using the stock battery’s BMS as a data interface while powering the board from another battery (easier, but still requires matching specs).

---

Want a deeper dive into how that data link might be structured or tips on safely combining batteries? Let me know—I’ll gladly unpack it further.
