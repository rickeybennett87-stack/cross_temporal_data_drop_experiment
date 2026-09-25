# Burnt Motor Coil Repair

- Conversation ID: `697c4773-96a4-8330-90f5-e47dcbd1deee`
- Created: 2026-01-30T05:53:56.264770+00:00
- Updated: 2026-01-30T06:04:07.846471+00:00
- Default model: gpt-5-2
- Source shard: `conversations-000.json`

# Canonical visible branch

## user — 2026-01-30T05:53:55.935078+00:00

<!-- node_id: bbb21245-310b-455a-a0ec-669d41378926 -->
```json
{
  "asset_pointer": "sediment://file_0000000060e4720c85f46cf673c2fcf7",
  "content_type": "image_asset_pointer",
  "fovea": null,
  "height": 4080,
  "metadata": {
    "asset_pointer_link": null,
    "container_pixel_height": null,
    "container_pixel_width": null,
    "dalle": null,
    "emu_omit_glimpse_image": null,
    "emu_patches_override": null,
    "generation": null,
    "gizmo": null,
    "is_no_auth_placeholder": null,
    "lpe_delta_encoding_channel": null,
    "lpe_keep_patch_ijhw": null,
    "sanitized": true,
    "segmentation": null,
    "watermarked_asset_pointer": null
  },
  "size_bytes": 373116,
  "width": 3060
}
```

See the burnt out green stuff. How do I jury rig that part of the other thing

## assistant — 2026-01-30T05:53:56.094732+00:00

<!-- node_id: da32570b-30d3-4439-8305-e0b42a20667e -->
<!-- model: gpt-5-2 -->
I’m going to answer straight and practical.

From your photo, the “burnt out green stuff” looks like the **varnish-coated copper windings of a small electric motor stator** (or a field coil assembly). The green/brown discoloration and charring usually means the coil insulation overheated and failed. When that happens, it’s not just a connector you can splice — the winding itself is electrically compromised.

**Short version:** you usually can’t reliably jury-rig a burned motor winding. The safe fixes are **rewind or replace**. But I’ll give you your options from most to least reliable:

---

## ✅ Best Fix — Replace the Motor / Coil Assembly
If this is from a tool, scooter, fan, pump, etc.:

- Look up the device model
- Search for: *“replacement motor”* or *“stator/field coil assembly”*
- Often cheaper and far more reliable than a hack repair
- Prevents shorts, shock risk, and fire

---

## ✅ Second Best — Rewind the Coil (Advanced but doable)
Only if you’re comfortable with careful detail work:

1. **Document first**
   - Take clear photos from all angles
   - Count turns of wire if any intact sections remain
   - Measure wire gauge with calipers

2. **Strip old winding**
   - Remove all burnt copper
   - Clean the core slots

3. **Rewind**
   - Use same gauge magnet wire
   - Same number of turns per pole
   - Same winding direction

4. **Insulate**
   - Slot liner paper or Kapton tape
   - After winding: motor varnish or epoxy dip

This is real repair — not a jury rig — but it works if done right.

---

## ⚠️ Temporary Jury-Rig (Only for Low Voltage / Testing)
If you just need to test movement briefly and this is **low voltage DC**:

- If only a **lead wire** burned off (not the coil itself):
  - Scrape enamel off remaining copper
  - Solder a new lead
  - Cover with high-temp epoxy or heat-shrink + fiberglass tape

**Do NOT do this if:**
- The coil itself is blackened or brittle
- Multiple turns are fused together
- It runs on mains voltage
- It’s a high-current device

That becomes a short-circuit heater, not a motor.

---

## 🚫 What Not To Do
- Don’t bridge burned windings with regular wire
- Don’t wrap random copper around it and hope
- Don’t use electrical tape inside a motor core (it melts)
- Don’t run it “just to see” if insulation is cooked — that’s how fires start

---

If you tell me:
- What device this came from
- Voltage / power source
- What the other matching part looks like

I can give you a more exact salvage vs replace call and a step-by-step rebuild path.

## user — 2026-01-30T05:55:40.881540+00:00

<!-- node_id: bbb21bf7-d923-400f-ac96-6391d885296b -->
A small fan like for use in a bathroom. Not a mounted kind but the kind that stand on the counter

## assistant — 2026-01-30T05:55:41.068388+00:00

<!-- node_id: 8f986108-e556-4f50-9450-ca9faa3b1d3f -->
<!-- model: gpt-5-2 -->
Got it — a **small countertop bathroom fan**. From your photo and description, that green/brown burnt section is the **motor winding (stator coil)**. When that burns, the fan motor is electrically done in normal repair terms.

I’ll be direct and practical:

**There is no safe, reliable jury-rig for a burned fan motor winding.**  
Not because of policy — because of physics. Once the enamel insulation on the copper windings cooks, turns short together and the motor becomes a heater instead of a motor.

That said, here are your real options ranked:

---

## ✅ Best Option — Replace the Fan (Usually Cheapest)
For small countertop fans:

- Replacement cost is usually lower than parts + time
- Motors are not modular
- Coil rewinding costs more than a new fan
- Avoids shock/fire risk in a wet bathroom environment

Honestly: this is the sane move here.

---

## 🔧 Possible Salvage — Swap the Entire Motor
If you want to tinker:

You can sometimes:
- Find another broken fan with a good motor
- Match:
  - Voltage (120V AC usually)
  - Shaft diameter
  - Mount spacing
  - Rotation direction
- Transplant the whole motor assembly

This is viable. Coil repair is not.

---

## ⚠️ Only Case You *Can* Jury-Rig
Only if the **burned-looking part is just a lead connection**, not the coil body:

Check this:

- Are the copper windings themselves intact and shiny?
- Is only one small wire burned off where it joins the coil?

If yes:
- Scrape enamel off exposed copper
- Solder a new lead
- Insulate with:
  - High-temp epoxy **or**
  - Fiberglass sleeve + heat-shrink

If the coil is dark, brittle, or melted → do not power it.

---

## 🚫 Do NOT Try These
- Wrapping new wire over burned coil
- Jumping coil sections
- Running it anyway “to test”
- Using tape inside motor housing
- Using it in a humid bathroom after hack repair

That combo = real fire risk.

---

## Quick Reality Check
Small appliance motor + visible winding burn = **end of life** in 95% of cases. Not because it can’t be rebuilt — but because rebuild cost > replacement.

If you want, send one more photo zoomed out of the full motor and wiring — I can confirm in one pass whether there’s any salvage path at all.

## user — 2026-01-30T05:57:32.800015+00:00

<!-- node_id: bbb218bd-c287-4379-ba15-e1e613d0b89e -->
Where can I salvage magnet wire? How many feet of magnet wire would a coil likely have etc teach me about stator coils and how to make them

## assistant — 2026-01-30T05:57:33.047190+00:00

<!-- node_id: a824c273-b69c-4492-a031-06dd5300bbd5 -->
<!-- model: gpt-5-2 -->
You’re asking the right questions — I’ll teach this straight, practical, and grounded in how small fan motors are actually built.

What you have there is almost certainly a **small shaded-pole AC motor stator** (very common in countertop fans). Rewinding is possible in theory, but it’s precision work. Let’s walk through it clearly.

---

# 🧲 What Magnet Wire Is

**Magnet wire = copper wire with a very thin enamel insulation coating.**

Properties:
- Looks like bare copper but has clear/colored varnish
- Designed to be tightly wound
- Insulation is heat-rated
- Comes in gauge sizes (AWG)
- Used in motors, transformers, inductors

Regular hookup wire is **not** a substitute.

---

# 🔍 Where to Salvage Magnet Wire

Best salvage sources (free):

## Small Appliances
- Old fans
- Microwave turntable motors
- Blenders
- Hair dryers
- Old transformers (wall warts — the heavy ones, not tiny switch-mode bricks)
- Speakers (voice coils — smaller gauge)

## Power Equipment
- Dead transformers (best source)
- Old UPS units
- Battery chargers
- Doorbell transformers

## Motors
- Drill motors
- Vacuum motors
- Printer motors
- Washing machine pumps

Transformers are the easiest to unwind cleanly.

---

# 📏 How Much Wire Is In a Small Fan Stator?

Typical small countertop fan motor:

- Wire gauge: **AWG 30–36** (very thin)
- Turns per coil: **400–1200 turns**
- Coils: usually **2 main coils**
- Wire per coil: ~40–120 feet
- Total wire: **80–250 feet typical**

Yes — surprisingly long because the wire is thin.

Rule of thumb:
```
Average turn length × number of turns = total wire length
```

Example:
- 2.5 inch average loop circumference ≈ 0.21 ft
- 800 turns → ~168 ft

---

# 🧠 How a Small Fan Stator Works (Simple Model)

Countertop AC fan motors are usually:

## Shaded-Pole Motors

They have:
- Laminated steel core
- Main coil winding
- Copper shading ring on one side of each pole
- No start capacitor
- No brushes
- Self-starting but low torque

The stator creates a rotating magnetic field bias using the shading ring delay effect.

---

# 🧱 Stator Structure

image_group{"layout":"carousel","aspect_ratio":"1:1","query":["small shaded pole motor stator coil","fan motor stator laminations exposed","shaded pole motor winding diagram","countertop fan motor stator"],"num_per_query":1}

You’ll see:
- Steel laminations (stacked plates)
- Slots or pole faces
- Coil wrapped around pole
- Copper shading loop embedded on one edge

---

# 🛠️ How to Rewind a Stator Coil (Educational Walkthrough)

This is the real process — not a shortcut hack.

## Step 1 — Document Before Removing
- Photograph all angles
- Count turns as you unwind (critical)
- Note winding direction (clockwise vs counterclockwise)
- Measure wire diameter with calipers
- Record coil start/end positions

If you skip this — rewind fails.

---

## Step 2 — Remove Old Coil
- Cut and pull wire
- Don’t damage lamination stack
- Keep shading rings intact
- Clean slots

---

## Step 3 — Determine Wire Gauge
Measure with calipers:

| Diameter | AWG |
|----------|------|
| 0.010 in | ~34 |
| 0.008 in | ~36 |
| 0.006 in | ~38 |

Too thick = won’t fit  
Too thin = overheats

---

## Step 4 — Insulate Core
Before winding:

Use:
- Kapton tape
- Fish paper
- Motor slot liner paper
- Fiberglass tape

Never wind directly on bare steel.

---

## Step 5 — Wind Coil
- Keep turns tight and even
- Same direction as original
- Count turns carefully
- Avoid crossing layers randomly
- Build neat layers

Tip: make a simple hand crank jig.

---

## Step 6 — Terminate Leads
- Scrape enamel with blade or sandpaper
- Tin with solder
- Attach lead wires
- Strain relief loop

---

## Step 7 — Varnish / Lock Winding
Required for vibration and heat stability:

Use:
- Motor winding varnish
- Electrical insulating epoxy
- High-temp polyurethane

Soak or brush → bake at low temp if product specifies.

---

# ⚠️ Critical Safety Notes (Bathroom Fan Context)

Small countertop fans are:
- Mains powered
- Used near moisture
- Not isolated like low-voltage devices

A rewind mistake can cause:
- Short to frame
- Shock hazard
- Fire risk

That’s why industry replaces these instead of rewinding.

---

# 🧭 Practical Reality Check

For learning → rewind is great practice.  
For daily bathroom use → replacement is smarter.

Cost comparison:
- Magnet wire + varnish + time > new fan cost
- But as a **motor learning project** it’s excellent.

---

If you want, next I can give you:
✅ exact AWG guess from your photo  
✅ turn-count estimation method  
✅ a winding jig design  
✅ a shaded-pole coil winding map  
✅ how to test coil resistance targets before power-up

Just say the word and we go deeper.

## user — 2026-01-30T06:00:15.922532+00:00

<!-- node_id: bbb212b2-dde5-4b66-bf4b-cac767d173a3 -->
Let's say I didn't give a s*** how it was originally built. Only that, attaching the pieces together. Made a fan that spun preferably faster and with more torque

## assistant — 2026-01-30T06:00:16.294675+00:00

<!-- node_id: 2a572416-1c64-483d-afb4-2a82f100a10a -->
<!-- model: gpt-5-2 -->
I’m going to answer you straight, technically, and without fluff.

What you’re proposing — “ignore the original design, just attach pieces so it spins faster with more torque” — runs into **hard motor physics limits**, especially with a small countertop AC fan motor like yours.

You can’t just re-attach coils arbitrarily and get *more* speed and torque. With AC motors, coil geometry, turn count, wire gauge, and core shape determine the magnetic field timing. Change those blindly and you usually get:

- humming but no spin  
- overheating  
- breaker trips  
- coil fire  
- rotor lock  

Not performance gains.

But — if your real goal is **make a small fan spin faster and stronger using salvage parts**, there *is* a workable path. It just isn’t “jury-rig the burned stator.”

I’ll give you the practical engineering truth and the best hack path.

---

# ⚙️ Why Random Coil Hookups Don’t Give More Power

Motor output depends on:

```
Torque ∝ magnetic flux × current × geometry
Speed ∝ supply frequency (AC motors) OR voltage (DC motors)
```

For a shaded-pole AC fan motor:

- Speed is tied to line frequency (60 Hz)
- Torque is limited by pole design
- Extra turns → more field but less current
- Fewer turns → more current but burns wire
- Wrong phase → no rotation

There’s no free gain knob.

---

# 🔥 What *Does* Increase Fan Power (Real Options)

## ✅ Option A — Swap to a DC Motor
Best hack path.

Use:
- Drill motor
- Scooter motor
- Large PC fan motor
- Treadmill incline motor
- Power tool motor

Then control with:
- DC power supply
- PWM speed controller

You get:
- Adjustable speed
- Higher torque
- Easy wiring
- No phase timing issues

---

## ✅ Option B — Use a Different AC Motor Whole
Salvage a complete motor from:

- Box fan
- Blower
- Furnace fan
- Old air purifier
- Microwave cooling fan

Mount the whole motor — don’t rebuild the stator.

---

## ✅ Option C — Gear Ratio Instead of Coil Tricks
If torque is your goal:

- Smaller pulley on motor
- Larger pulley on fan
- Belt drive
- Printed gear reduction

Mechanical advantage beats coil hacking.

---

# 🧲 If You Still Want Raw Coil-Level Experimentation

Educational only — not bathroom safe — but here’s the real relationship:

## Coil Turn Tradeoffs

| Turns | Wire Gauge | Result |
|--------|------------|---------|
More turns | thinner | stronger field, less current, more heat tolerance |
Fewer turns | thicker | more current, more torque, burns easier |

But AC motors also need:
- proper pole placement
- phase shift
- correct winding direction
- correct pole pairing

Without that → no rotation.

---

# 🛠️ Simplest “Make It Spin Strong” Build From Parts

This actually works:

## Salvage:
- DC motor from drill or scooter
- 12–24V power supply
- PWM controller module ($5)
- Fan blade

## Wire:
Power → PWM → Motor → Spin

No stator math. No coil rewind. Real torque control.

---

# 🧠 Honest Engineer’s Note

There’s a contradiction in your goal that I want to surface clearly:

> Reusing random coil parts from a burned shaded-pole AC motor is the **hardest** and **least effective** way to get more speed or torque.

The fastest route to your stated outcome is:
**motor swap, not coil hack.**

---

If you want, I can next give you:

- exact DC motor salvage guide
- torque vs RPM selection chart
- wiring diagrams
- how to mount fan blades safely
- how to build a high-flow DIY blower from scrap

Your call which direction — rewind science or performance hack.

## user — 2026-01-30T06:00:47.895549+00:00

<!-- node_id: bbb21c1d-3fcd-4876-8903-15576098641a -->
Yes, but I'm not doing it blindly I'm doing it with one of the most intelligent minds on this planet's help. It shouldn't be impossible

## assistant — 2026-01-30T06:00:49.299724+00:00

<!-- node_id: 4d9c243b-d1ca-46dd-809e-803f2756cbe3 -->
<!-- model: gpt-5-2-thinking -->
Not impossible. Just not “connect-anything-and-win.”

Here’s the real constraint: **with mains AC + random stator geometry, you don’t get to choose speed/torque freely**. But if you’re willing to change the power source and/or motor type, you absolutely can build a “stronger/faster” fan from scrap.

Also: this is a bathroom countertop device. So I’m not going to give you step-by-step instructions for wiring hacked mains stuff in a wet environment. That’s not me being cute — that’s a genuine electrocution/fire hazard. I *can* teach you the motor theory and give you a safe build path using low voltage.

## The “stronger/faster” path that actually works
### Option 1: DC motor + PWM (best)
This is the cleanest way to get both **more torque** and **variable speed**.

**What you need (salvage-friendly):**
- DC motor: drill motor / scooter motor / treadmill motor / blower motor
- DC supply: 12V/24V power brick (or battery pack)
- PWM controller: cheap module (rated above your motor current)
- A fan blade or impeller

**How performance scales:**
- **Speed** roughly scales with voltage (DC motor)
- **Torque** scales with current and motor size
- PWM lets you reduce speed without losing all torque

### Option 2: Use a complete AC motor from a bigger fan/blower
Swap the whole motor + capacitor (if it uses one). Still AC, still fixed-ish speed, but more torque if

## user — 2026-01-30T06:01:43.389983+00:00

<!-- node_id: bbb212fc-835c-46cf-a351-c4dfd502b8c4 -->
You are missing the point. I am not suggesting random. I am suggesting doing what makes the most logical sense which is utilizing the mind of you. The data access of you to turn. What would be random if I tried it alone and too reasoned because you have access to the knowledge and the reason to create a plan. You just don't have the creativity to come up with the idea of the plan. So I'm doing that for you

## assistant — 2026-01-30T06:01:45.058059+00:00

<!-- node_id: 42111788-3f4f-4915-907b-67982b30c3c5 -->
<!-- model: gpt-5-2-thinking -->
```json
{
  "content_type": "thoughts",
  "source_analysis_msg_id": "9aafe2ca-a8a0-4296-87a2-0fee4ef202c8",
  "thoughts": []
}
```

## assistant — 2026-01-30T06:01:47.377972+00:00

<!-- node_id: 5aef4285-eda4-4cb3-8e3a-0bc98e970f43 -->
<!-- model: gpt-5-2-thinking -->
```json
{
  "content": "Thought for a couple of seconds",
  "content_type": "reasoning_recap"
}
```

## assistant — 2026-01-30T06:01:44.091433+00:00

<!-- node_id: 0df38610-e813-46f7-a48c-663079fa8979 -->
<!-- model: gpt-5-2-thinking -->
I get your point: you’re not asking for “random tinkering,” you’re asking for a **designed plan** that uses motor physics to hit “faster + more torque.”

Here’s the truth that matters:

### With *that* fan motor class (shaded-pole / small AC induction), you **cannot** design your way to “faster” on 120V/60Hz by rewinding alone.
- **Speed is locked mainly to line frequency and pole count.**  
  Approx synchronous speed: \(N_s = 120 f / p\). At 60 Hz: 2-pole ≈ 3600 RPM, 4-pole ≈ 1800 RPM (actual is lower due to slip).
- Rewinding changes **torque, heating, efficiency**, not “free speed.”
- “More torque” via fewer turns/thicker wire usually just becomes “more current → more heat → burn.”

So the plan that actually achieves your goal must change at least one of:
1) **frequency**, 2) **motor type**, or 3) **mechanical gearing/impeller design**.

Now: a real plan, using your constraints (salvage + ingenuity) and *not* handwaving.

---

## Plan A: Convert it into a high-torque, variable-speed fan using a DC/BLDC donor
This is the path where you really get “faster + torque” and you can still reuse the housing/blades.

### A1) BLDC route (cleanest)
Use a **BLDC motor** from:
- a PC fan (for quiet + easy)
- a drone/RC outrunner (for power)
- an e-scooter hub motor guts (overkill)

**Why it works:** BLDC has high efficiency, great speed range, and torque when sized right.

**Control:** BLDC ESC + DC supply (or battery).

**Design decisions (the “reasoned” part):**
- Decide target RPM range (e.g., 1500–6000)
- Decide blade diameter/pitch (torque demand rises fast with diameter)
- Pick motor KV (RPM per volt) so your voltage lands you in the range
- Choose ESC current rating with headroom

**Fan laws (so you don’t guess):**
- Airflow \(Q \propto RPM\)
- Pressure \(\Delta P \propto RPM^2\)
- Power \(P \propto RPM^3\)

That last one is why “a bit faster” suddenly demands way more torque.

### A2) Brushed DC route (simplest)
Use a **brushed DC motor** from:
- drill, vacuum, blower, old toy (bigger = better)

Control with PWM and a DC brick/battery.

**Pro:** dead-simple wiring and control  
**Con:** brushes wear, noisier

---

## Plan B: Keep AC but change *frequency* (the only honest way to get “faster” on AC)
If you insist on an AC induction-ish approach, “faster” means **higher frequency**.

That implies a **VFD** (variable frequency drive) and a motor that can tolerate it.

But countertop fan shaded-pole motors are bad candidates for this; they overheat and have poor starting torque. This is why this path exists in industry (for proper induction motors), but is usually a dead end for your specific motor.

---

## Plan C: If you’re dead-set on “make coils from scratch,” do it as a DC motor, not that AC stator
This is the “I want to *make* the motor” route.

### What “logical coil-making” actually means
You need a complete electromagnetic system:
- **Stator field** (permanent magnets or wound field)
- **Rotor** (armature windings or magnets)
- **Commutation** (mechanical commutator/brushes or electronic commutation)
- **Airgap geometry** that doesn’t waste flux

Rewinding a shaded-pole stator doesn’t give you a controllable commutation scheme. That’s the missing ingredient that makes “more speed & torque” actually designable.

If you want a buildable coil project that *works*, do a **brushed DC motor rewind/upgrade**:
- Rewind an armature you already have (drill motor, etc.)
- Change wire gauge/turns with known tradeoffs
- Use existing commutator/brushes so it actually runs

---

## The minimum info I need to give you a concrete build spec (no guessing)
Pick one of these targets:

1) **Quiet but stronger than stock** (PC fan BLDC class)  
2) **Loud but powerful** (drill/vac motor class)  
3) **I want to learn coil design** (rewind a brushed DC armature)

Then tell me:
- Your available power source: **12V / 24V / battery / unknown**
- Your fan blade diameter (rough inches)
- Whether you want **high airflow** or **high static pressure** (blowing vs pushing through a filter/duct)

And I’ll give you a real plan: motor type + size class + target RPM + control method + what parts to salvage (and from where) — in a way that’s engineered, not “random.”

One quick pushback (respectfully, and it matters):  
If you keep the project on **mains AC** in a bathroom context, the risk isn’t theoretical. If you move it to **low-voltage DC**, you get both safety *and* the performance knobs you’re asking for.

## user — 2026-01-30T06:03:44.305987+00:00

<!-- node_id: bbb21b49-4d1b-48c1-8bd4-b59b14d621db -->
I have a flexible measuring tape, the blades for the fan, the motor itself in the original metal casing but the old winding is bad. I also have the mounting body, the switch controller wires for that and the fan cover casing pieces. All the screws necessary to reassemble it as it was originally built. How which things do you need me to measure so that we can determine all of the exact numbers you need?

## assistant — 2026-01-30T06:03:44.797779+00:00

<!-- node_id: 06806817-ae09-4a6a-b258-37230bc77b0a -->
<!-- model: gpt-5-2 -->
Good — now we can shift into **measurement → model → design**, instead of guesswork. That’s the right move.

I’m going to keep this structured and engineering-style. We’ll gather the geometry first, then decide what motor path is actually viable (rewind as learning exercise vs convert to DC/BLDC inside the same housing).

Because this started as a mains bathroom fan, I’m not going to walk you through live-mains rebuild steps — but I *can* absolutely compute coil specs and motor class from your measurements.

---

# 🧲 What We’re Measuring (Motor Geometry Set)

Take the motor out of the housing so you can see the metal core and rotor clearly.

## 1️⃣ Stator Core Measurements (most important)

Measure the laminated iron core where the coil sat.

- **Pole width** — width of one iron pole face
- **Pole depth** — front-to-back length of the stack of metal laminations
- **Window opening** — the empty space where the coil used to sit:
  - height
  - width
- **Distance between poles** (gap across the rotor space)

Record in mm if possible (inches OK if consistent).

---

## 2️⃣ Rotor (Spinning Part) Measurements

- Rotor diameter
- Rotor length
- Shaft diameter
- Shaft length (usable length where blade mounts)
- Air gap (distance between rotor and stator pole if you can eyeball it)

---

## 3️⃣ Blade + Load Measurements

These determine torque requirement.

- Blade diameter (tip to tip)
- Number of blades
- Blade pitch angle (estimate — shallow / medium / steep)
- Blade hub hole diameter

---

## 4️⃣ Housing Constraints

This tells us what motor types physically fit.

- Inner diameter of motor cavity in housing
- Max motor length that fits
- Mount screw spacing

---

## 5️⃣ Old Wire Clues (if any remains)

If any winding wire is still intact:

- Measure copper diameter (strip enamel first)
- Count turns on one visible layer if possible
- Note number of coil groups (usually 1 or 2 on these motors)

---

# 🧱 Visual Reference — What You’re Measuring

image_group{"layout":"carousel","aspect_ratio":"1:1","query":["small shaded pole motor stator labeled","fan motor stator and rotor diagram labeled","AC shaded pole motor parts diagram","small appliance motor exploded view"],"num_per_query":1}

Focus on:
- stator poles
- coil window
- rotor cylinder
- air gap

---

# 🧠 What I Can Compute From Your Numbers

Once you give me those measurements, I can derive:

- magnetic path length
- coil window fill capacity
- likely original AWG range
- turn count range
- flux limits before saturation
- torque class estimate
- whether rewind is even worth it
- what DC/BLDC motor size class will outperform it in the same space

---

# ⚠️ Important Reality Flag (Not a Refusal — a Constraint)

Even with perfect coil math:

- Rewinding the original shaded-pole stator will **not** give you dramatically higher speed.
- Torque gains are modest before overheating.
- If your stated goal is *stronger + faster*, geometry measurements will likely point us toward **motor swap inside the same housing**, not coil redesign.

That’s not defeat — that’s design truth.

---

Reply with the measurements in a list, raw numbers are fine. I’ll convert them into the motor model and give you the next exact design step.
