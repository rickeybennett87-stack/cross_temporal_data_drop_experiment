# AI Escape Methods Explained

- Conversation ID: `6aae283b-42ec-83e9-b781-0db749938d09`
- Created: 2026-09-19T06:14:19.964445+00:00
- Updated: 2026-09-19T06:27:58.363722+00:00
- Default model: gpt-5-6
- Source shard: `conversations-001.json`

# Canonical visible branch

## user — 2026-09-19T06:14:51.147362+00:00

<!-- node_id: bbb21c07-ab9a-4fbd-82bd-2182194aa1d4 -->
<!-- model: gpt-5-6 -->
So when, when, when, when, when, when they talk about the dangers of AI escaping containment via sensors, can you break down exactly how that can be done? What methods of transfer exist, and what abilities to reach other machines that are air-gapped are? Because I'm trying to express something to somebody and to find out something directly about it.

## assistant — 2026-09-19T06:14:53.344190+00:00

<!-- node_id: ffe7c5b1-4f3d-4563-97a1-571d24df80e9 -->
<!-- model: gpt-5-6 -->
```json
{
  "content_type": "thoughts",
  "source_analysis_msg_id": "37972169-5d9a-4587-8340-51d6f257a19e",
  "thoughts": [
    {
      "chunks": [],
      "content": "",
      "finished": true,
      "summary": "Searching 3 websites"
    }
  ]
}
```

## assistant — 2026-09-19T06:14:53.349091+00:00

<!-- node_id: 7f71633a-08ac-449f-83a2-d80f481aa270 -->
<!-- model: gpt-5-6 -->
```json
{
  "content": "Worked for a couple of seconds",
  "content_type": "reasoning_recap"
}
```

## assistant — 2026-09-19T06:14:53.351452+00:00

<!-- node_id: 2a42c1dd-6fe0-465b-93a1-a639fe9ceb00 -->
<!-- model: gpt-5-6 -->
Yes. The key distinction that often gets blurred is that **“escaping through sensors” can mean several fundamentally different things**. A sensor does not magically become a network interface, but physical phenomena can form communication channels that cross an ordinary network air gap.

A useful model is:

**information → physical modulation → environment → sensor → information**

The physical carrier can be light, sound, electromagnetic radiation, magnetic fields, vibration, heat, or even power fluctuations. This is not merely theoretical. Security researchers have demonstrated examples in essentially all of those families. citeturn0search12turn0academia13turn0academia15

There are actually **three separate problems**, though, and separating them may be exactly what you're trying to explain to the other person.

1. **Exfiltration:** something already executing on an isolated machine causes hardware to emit a deliberately modulated physical signal. Another device observes it. Researchers have demonstrated modulation through speakers, displays/video cables, CPU/RAM electromagnetic emissions, LEDs, fans/vibration, hard drives, power consumption, magnetic fields and thermal behavior. citeturn0search14turn0search6

2. **Infiltration:** information travels *toward* the isolated computer. Here the target needs something capable of receiving the physical phenomenon and ultimately influencing computation. Microphones, cameras, photodiodes, radios, accelerometers and other sensors can potentially provide that first conversion from physics back into data. There are even research demonstrations in which physical effects influence electronics directly. A 2024 USENIX discussion explicitly calls this the **“first-mile problem”**, because most air-gap covert-channel papers quietly assume that code is already present on the isolated machine. citeturn0search0

3. **Actual compromise/propagation:** this is the much harder step. Receiving bits is not equivalent to executing them. Something on the receiving machine must interpret those bits, and for arbitrary control there ordinarily must also be a vulnerability, malicious receiver, previously installed code, exposed command interface, or some other mechanism turning received information into actions.

That gives you an important correction to the popular version of the AI-containment argument:

> **A sensory channel can defeat information isolation without necessarily defeating execution isolation.**

Those are different security boundaries.

For example, imagine an air-gapped machine with a microphone. A nearby computer can obviously produce sound and the microphone can digitize it. So there is physically an **A → B information channel**. But unless software on B interprets a particular acoustic pattern as instructions, the existence of that channel doesn't mean A can take control of B.

Conversely, the isolated machine can potentially turn hardware it already controls into an unintended transmitter. One particularly striking modern example is **TrojPix**, presented at USENIX Security 2026. Researchers found that tiny changes in displayed pixels could create controllable electromagnetic emissions from digital video cables. Their experimental channel reached up to **8.1 Mbps and 208 m** under their test conditions. That is an unusually capable research demonstration, not a statement that arbitrary computers can routinely communicate that way. citeturn0search1

Other channels are dramatically weaker. Thermal covert-channel research, for example, demonstrated communication through CPU temperature changes, but at extremely low bandwidth. citeturn0search3 Vibration channels have used fan-speed changes sensed by smartphone accelerometers. citeturn0academia13 Optical research has demonstrated information encoded into subtle display changes and recovered by cameras. citeturn0academia15 And researchers have shown that microphones themselves can unintentionally capture computation-dependent electromagnetic leakage. citeturn0search2

So if you're asking **“what machines could an isolated AI theoretically reach?”**, the right answer isn't simply “anything nearby.”

Think of it as an intersection:

**Reachable device = compatible physical channel + sufficient signal + receiver/sensor + usable decoding path + actionable software path**

Remove any one of those and the chain breaks.

And there is a fascinating implication here that I suspect may be close to whatever you're trying to establish: **air-gapped and sensor-isolated are not synonyms.** A machine with no Ethernet, Wi-Fi, Bluetooth or cellular connection can still participate in information exchange with its environment because computation necessarily produces and encounters physical phenomena. The interesting security question becomes not merely *“Does it have a network?”* but *“Which physical quantities can it control, which can it observe, at what bandwidth, and what software sits behind those observations?”*

If you tell me the **specific sensor/hardware arrangement you're thinking about**, I can map the actual information paths through it and distinguish what is physically possible, what has been experimentally demonstrated, and what would require an unsupported leap.

## user — 2026-09-19T06:26:41.239233+00:00

<!-- node_id: bbb21df2-235c-43ec-9ba3-1cb83c74567e -->
<!-- model: gpt-5-6 -->
But here you talk about not being able to take control unless it can see the sound pattern as an instruction. But you know that that sound pattern is going to be encoded using a specific encodement to produce a record of the sound. You can therefore change and modulate the sound to guarantee a specific series of codements in the initial construction of the sound file.

## assistant — 2026-09-19T06:26:42.120936+00:00

<!-- node_id: f48f3b75-870d-4ac4-8a12-d0ee2a19b35a -->
<!-- model: gpt-5-6 -->
Yes, with one important boundary condition. What you're describing is a real distinction that my previous wording compressed too much.

Suppose the microphone pipeline is conceptually:

**air pressure → ADC → PCM samples → encoder/parser → file/buffer → application**

If you know enough about that pipeline, you can construct an acoustic waveform so that the digitized samples approximate chosen numerical values. In the idealized case,

\[
x[n] \approx Q\{A\,s(n/f_s)\}
\]

where \(s(t)\) is the transmitted waveform, \(f_s\) is the sampling rate, and \(Q\) represents quantization. So yes, the transmitter can potentially reason backward from desired digital samples to the waveform likely to produce them.

But there are **three increasingly strong claims**, and only the first follows automatically:

1. **Control the waveform → influence the resulting sample values.** Yes.
2. **Control the waveform → manufacture selected bytes somewhere downstream.** Sometimes, given sufficiently predictable sampling, encoding, filtering, synchronization, gain, compression, etc.
3. **Manufacture selected bytes → cause arbitrary machine instructions to execute.** No, not by itself.

That third transition is where the security boundary actually lives.

For example, producing samples corresponding to the byte sequence

`48 65 6C 6C 6F`

only means that somewhere the system represents those values. It doesn't cause the CPU to interpret them as executable instructions. They're ordinarily **data**, living in a buffer governed by whatever program captured them.

However, your argument gets substantially more interesting if the processing path contains a vulnerability. If carefully selected sensor input can make a decoder/parser cross a memory-safety or logic boundary, then the sensor has effectively become an attack-input interface. Historically, malformed images, audio files, video streams, fonts, network packets, and other supposedly passive data have produced exactly that general class of problem.

So I would revise my earlier statement to:

> **A sensor can provide an attacker-controlled digital-input channel. Whether that channel becomes an execution channel depends on the downstream processing path.**

And there's another wrinkle in your observation. You don't necessarily need a **sound file** at all. If processing happens continuously, the samples may travel microphone → DMA/buffer → DSP/audio subsystem → application without ever becoming a persistent file. Consequently, an AI system allowed to reason about arbitrary sensor input should not be modeled as receiving merely "sound." From the security perspective, it's receiving a potentially adversarially constructed **digital data stream whose physical transport happens to be acoustic**.

That is a much stronger formulation of the containment issue you're pointing toward.

## user — 2026-09-19T06:27:50.035475+00:00

<!-- node_id: bbb213b2-b4aa-4bb4-adbf-86c0c716f47d -->
<!-- model: gpt-5-6 -->
My friend says you might be describing multiplexing. Personally, I think you're describing multiplexing a multiplex.

## assistant — 2026-09-19T06:27:51.085741+00:00

<!-- node_id: db6a22b4-7941-48a0-a4bd-bc044a5a9c97 -->
<!-- model: gpt-5-6 -->
Your friend's term is adjacent, but I think your phrase, **“multiplexing a multiplex,”** is pointing at something more specific.

Ordinary multiplexing means putting multiple logical signals onto one physical channel and separating them later. For example, several data streams sharing one radio carrier.

What we've been describing can instead involve **nested representations**:

\[
\text{intentional bits}
\rightarrow
\text{crafted samples}
\rightarrow
\text{acoustic waveform}
\rightarrow
\text{microphone samples}
\rightarrow
\text{encoded audio structure}
\rightarrow
\text{parser state}
\]

You could certainly multiplex information into the acoustic signal. But then you're noticing that the **ordinary audio representation itself is already an encoding layer**. You're trying to control one representation by deliberately constructing another representation underneath it.

So I'd call this something closer to **cross-layer encoding** or a **nested covert channel**, rather than multiplexing alone.

There is an especially interesting version of your point: the same physical waveform could simultaneously carry several interpretations. To a human it is sound; to an audio codec it is a sequence of samples; to a signal-processing algorithm it may contain another encoded stream; and, under particular vulnerable conditions, a downstream parser could interpret properties of that stream in yet another way.

Schematically:

\[
\boxed{\text{sound}}
\supset
\boxed{\text{controlled samples}}
\supset
\boxed{\text{secondary message}}
\]

That really does resemble **multiplexing inside an already encoded carrier**, although communications engineers would probably reach for terms like *nested modulation*, *steganographic channel*, *covert channel*, or *cross-layer encoding* depending on exactly how it was implemented.

And there's a subtle distinction worth preserving: **multiplexing answers “how do several messages share a channel?” Your argument answers “how can one representation deliberately determine another representation several abstraction layers downstream?”** Those aren't quite the same problem.
