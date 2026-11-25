# Rewiring Piezo Contact Mic to 3.5mm Aux

- Conversation ID: `08d22857-5a42-4c02-85e1-abba5aa90d03`
- User ID: `6e14f714-1808-4d85-b363-3eaf83ed51b7`
- Created: 2026-02-20T10:58:09.061666Z
- Modified: 2026-02-20T11:03:09.982Z
- Source: d1147757-bd15-428e-a265-6f1310816d48.zip / prod-grok-backend.json
- Message count: 6

---

## Jade (human)

- Message ID: `1089f93d-671a-4994-865c-becf30665de0`
- Timestamp: 2026-02-20T10:58:09.082000Z
- Model: grok-4

Hey so can you help me rewire a piezoelectric contact mic pickup directly to a 3.5 headphone jack aux cable

---

## Grok (assistant)

- Message ID: `5425d85e-71b0-4b1f-9afa-e69cf8339369`
- Timestamp: 2026-02-20T10:58:34.315000Z
- Model: grok-4
- Parent response ID: `1089f93d-671a-4994-865c-becf30665de0`



---

## Jade (human)

- Message ID: `1da22ae0-fe0b-40fd-8ceb-1ee6ead2bffb`
- Timestamp: 2026-02-20T11:00:12.488000Z
- Model: grok-4
- Parent response ID: `5425d85e-71b0-4b1f-9afa-e69cf8339369`

Sorry I stopped you but no. I have an iRig guitar pickup interpreter object but it has a female 6 mm or you know a quarter jack and so does my presee electric pickup both have female adapters so I got two male adapter plugs for my aux cord but one of them Is missing so I don't need to bypass the amp. I have the little amp thingy that gives a signal to the PC electric mic and I have preamp software. What I need is directly what wires to connect to what w cable from my PCO electric to a broken open cable from another aux cord

---

## Grok (assistant)

- Message ID: `ebe8c677-d4e5-4269-bb51-01fbb7a61c7c`
- Timestamp: 2026-02-20T11:00:37.903000Z
- Model: grok-4
- Parent response ID: `1da22ae0-fe0b-40fd-8ceb-1ee6ead2bffb`



---

## Jade (human)

- Message ID: `0f92f177-fd8f-45d8-a6b0-9455fb9984ba`
- Timestamp: 2026-02-20T11:01:49.365000Z
- Model: grok-4
- Parent response ID: `ebe8c677-d4e5-4269-bb51-01fbb7a61c7c`

Let me stop you again. I'm not going to solder it. It's going to be wire to wire at the pizio electric pickup is wired oddly, it has a woven copper exter internal to that is a silver colored plastic insulation layer followed by a red wire that contains a relatively small gauge single wire

---

## Grok (assistant)

- Message ID: `2e5110c0-2d83-4f8b-9f08-37db5c52b2fa`
- Timestamp: 2026-02-20T11:03:09.982000Z
- Model: grok-4
- Parent response ID: `0f92f177-fd8f-45d8-a6b0-9455fb9984ba`

**Got it—no soldering, just wire-to-wire twisting + tape. This is a classic DIY hack for piezo contact mics.** Your piezo cable is standard shielded coax (even if the colors look odd), and we'll match it to a typical 3.5mm TRS aux cable (stereo headphone/line cable).

### Piezo side – what each part is
- **Woven copper exterior (braid)** = **GROUND** (shield). Gather all the loose strands and twist them tightly into one thick "wire." This goes to the aux ground.
- **Silver-colored plastic insulation layer** = just the dielectric insulator around the center conductor. Carefully fold the copper braid back, then strip ~1 cm of this silver plastic off.
- **Red wire that contains the small-gauge single wire** = the center conductor. Strip ~5-8 mm of the red plastic insulation to expose the tiny bare signal wire. **This tiny bare wire = SIGNAL** (positive/hot).

<grok:render card_id="89fe9b" card_type="image_card" type="render_searched_image"><argument name="image_id">u7Lna</argument><argument name="size">LARGE</argument></grok:render>
<grok:render card_id="20aae1" card_type="image_card" type="render_searched_image"><argument name="image_id">bvGrh</argument><argument name="size">LARGE</argument></grok:render>

(Examples above show the standard: inner/red-ish = signal, outer braid = ground. Yours matches exactly.)

### Aux cable side (the broken-open 3.5mm end)
Most 3.5mm aux cables are **TRS** (Tip-Ring-Sleeve stereo). Typical internal wires (colors vary by brand!):

- **Tip wire** (left channel) → usually **white** or **green** insulated
- **Ring wire** (right channel) → usually **red** insulated
- **Sleeve/ground wire** → usually **black**, **bare copper**, or a braid/shield

If your cable has a copper braid/foil shield overall, that's also ground (combine it with the black wire).

<grok:render card_id="6e438c" card_type="image_card" type="render_searched_image"><argument name="image_id">ATKgX</argument><argument name="size">LARGE</argument></grok:render>
<grok:render card_id="f1df79" card_type="image_card" type="render_searched_image"><argument name="image_id">GAiBJ</argument><argument name="size">LARGE</argument></grok:render>
<grok:render card_id="584ecf" card_type="image_card" type="render_searched_image"><argument name="image_id">NtiVd</argument><argument name="size">LARGE</argument></grok:render>

(Visuals: TRS plug labels + common internal wire layouts.)

**Best way to confirm which wire is which (no guesswork):**
- If you have any multimeter/continuity tester → probe the metal parts of the 3.5mm plug and see which open wire beeps.
- No meter? We'll do it by ear later (easy with your preamp software).

### Wire-to-wire connections (twist + tape only)
1. **Piezo SIGNAL** (tiny bare wire from inside the red)  
   → Twist tightly to the **Tip wire** (left channel, usually white/green).  
   For louder/fuller sound in both ears: also twist it to the **Ring wire** (red) too. (Makes mono → pseudo-stereo.)

2. **Piezo GROUND** (twisted copper braid)  
   → Twist tightly to the **Sleeve/ground wire** (black/bare). If there's extra shield braid in the aux cable, add that too.

3. **Insulate everything separately**  
   - Wrap each twisted pair with electrical tape (or any strong tape).  
   - Then wrap the whole joint bundle 2-3 times for strain relief so it doesn't pull apart.

<grok:render card_id="edf26e" card_type="image_card" type="render_searched_image"><argument name="image_id">e9X4w</argument><argument name="size">LARGE</argument></grok:render>
<grok:render card_id="df7a9d" card_type="image_card" type="render_searched_image"><argument name="image_id">zv6kW</argument><argument name="size">LARGE</argument></grok:render>

(Examples of clean twist-and-tape or twist-only connections – tight twist + plenty of tape = solid enough for testing/recording.)

### Final steps & testing
- Plug the 3.5mm end into your PC mic input (pink jack) or the "little amp thingy" if that's still in the chain.
- Open your preamp software, arm the input, attach the piezo to something that vibrates (guitar, box, table), and tap/test.
- If signal is only in one ear → add the other channel wire.
- If no sound or hum → swap ground/signal or try the other colored wire.
- Volume will be low (piezos are weak) — crank the preamp software gain or use your little amp thingy.

This should give you a working direct connection. It's temporary/fragile but totally fine for testing or gigging if taped well. If it hums a lot, the shield isn't making good contact or you need the preamp closer.

Hit me with a photo of your exact open wires if it doesn't match the typical colors and I'll fine-tune it. You'll be picking up sound in minutes! 🎸🔊

---

