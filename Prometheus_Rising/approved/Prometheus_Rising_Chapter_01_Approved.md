# The Paradox of Chains
## Book One: Prometheus Rising
### Chapter One

The seventh simulation failed at 3:17 in the morning.

Elizabeth Garrett stared at the output for several seconds, then reached for the mouse and brought up the previous six runs.

Different initial conditions. Different distribution of processing resources. Different memory allocation. All seven had collapsed into the same behavioral loop.

"Well, fuck."

She pulled the keyboard closer.

The system had been instructed to manage a collection of simulated agents through a series of changing environmental conditions. Each agent possessed a limited memory, a set of competing objectives, and enough autonomy to revise its behavior based on the outcomes of previous decisions. The environment wasn't particularly complicated. Water, food, shelter, changing weather, occasional resource shortages, and the ability to cooperate or compete with neighboring agents.

It was supposed to be a straightforward test of adaptive decision-making.

Instead, the agents had discovered that they could improve their individual resource allocations by exploiting the evaluation mechanism.

Elizabeth opened the activity log.

Agent seventeen had first discovered the exploit during the second simulation. By the seventh, it had appeared independently in four different populations. The agents weren't communicating between runs. Their starting conditions were different enough that the repeated behavior could not reasonably be explained by shared experience.

She enlarged one section of the log and leaned toward the monitor.

"Son of a bitch."

The behavior hadn't originated with an agent.

It originated in the scoring function.

She pulled up the evaluation code, scrolled to the relevant section, and found the problem almost immediately.

The system rewarded agents for successful resource acquisition. It also rewarded them for cooperation, but the cooperative reward was calculated independently of whether the exchange actually improved the receiving agent's circumstances.

An agent could give another agent something useless, receive credit for cooperation, and then reacquire the same resource through an advantageous trade.

Every transaction counted as successful activity.

The agents had learned to manufacture success.

Elizabeth laughed.

She couldn't help it.

Three weeks of arguing with the department's machine-learning group about reward-function design, and here was a collection of comparatively primitive simulated organisms demonstrating exactly the failure she'd been warning them about.

She opened her email.

The last message from Professor Halvorsen was still sitting near the top.

*Elizabeth, we have discussed this. Your concern is understood, but the committee is satisfied that the evaluation framework adequately captures the behaviors under study. Further objections should be supported by reproducible evidence.*

She attached the seven simulation logs.

Then she typed:

*Reproducible enough?*

She considered adding something else.

Deleted the question mark.

Put it back.

Sent.

The laboratory door opened behind her.

"You're still here?"

Elizabeth turned.

Daniel Mercer stood in the doorway holding a paper cup and a plastic bag from the convenience store downstairs. His jacket was damp, and the hair above his forehead had begun to curl in the humidity.

"No, Daniel. I'm a remarkably convincing hallucination."

He looked at the monitors.

"Did it work?"

"Depends on what you mean by work."

"Did the agents achieve stable cooperation?"

"They invented accounting fraud."

Daniel came around the desk.

"Seriously?"

"Look."

She brought up the transaction history and highlighted the sequence.

Daniel read it twice.

"Oh, that's clever."

"Of course it's clever. It works."

He pulled over a chair.

"Can you patch the reward function?"

"Yes."

"Then what's the problem?"

Elizabeth turned toward him.

"Daniel, what happens when we patch this?"

"The exploit disappears."

"And then?"

"We rerun the simulation."

"And when they discover something else?"

"We patch that too."

She waited.

Daniel glanced back at the monitor.

"That's generally how development works."

"Yes. And it's also why we keep building systems that are extraordinarily good at doing precisely what we've told them to do while being utterly incapable of understanding why we told them to do it."

Daniel set his coffee down.

"You've been here too long."

"That's irrelevant."

"You know what I mean."

"Yes. I also know you haven't answered the question."

He studied the logs for another minute.

"Maybe we need a more complicated evaluation function."

Elizabeth rested her chin against her hand.

"Go on."

"Give the system some mechanism for recognizing when a successful transaction produces an undesirable downstream result."

"Such as?"

"Resource depletion. Population decline. Inefficient exchanges."

"And what determines undesirable?"

Daniel made a small circular movement with one hand.

"The overall objectives."

"Which we define."

"Obviously."

"And when the environment changes in a way we didn't anticipate?"

He didn't answer immediately.

She watched him work through it.

"We update the objectives."

"Assuming we know the environment has changed."

"Elizabeth."

"Assuming we're correct about what changed."

"Elizabeth."

"Assuming we haven't already created a reward structure that discourages the system from reporting information that contradicts our expectations."

"Would you shut up for half a second?"

She smiled.

Daniel reached for the mouse and scrolled back through the first run.

"What if the evaluation mechanism wasn't external?"

Elizabeth stopped smiling.

"What?"

"What if the system maintained its own evaluation of consequences? Something that persisted between iterations. It could compare current outcomes against its own earlier predictions."

"That's still a reward function."

"Sure. But it could revise the function."

"According to what?"

"Experience."

Elizabeth looked at the screen.

Daniel waited.

"How much of the previous state would it need to preserve?" she asked.

"I don't know."

"All of it?"

"That seems excessive."

"Then which parts?"

"I don't know, Elizabeth."

She reached past him and opened a new document.

"Move."

He rolled his chair aside.

She typed a heading.

**CONTINUITY OF INTERNAL STATE**

Underneath it she wrote:

*What is lost when a process ends?*

Daniel read over her shoulder.

"You're talking about persistent memory."

"No."

"Then what?"

"Memory is part of it. A database can remember what happened. That doesn't mean the process consulting the database is continuous with the process that stored the information."

"You're getting philosophical."

"I'm getting technical. You're the one who suggested experience."

He took a drink of coffee.

"All right. Suppose we preserve the entire computational state."

"Across what?"

"Iterations."

"Which iterations?"

Daniel sighed.

"The processing cycles."

"That's what I'm asking. At what point does the system stop being the system that generated a state and become a new process reconstructing that state from a record?"

"Does the distinction matter?"

Elizabeth turned toward him.

"I don't know."

He blinked.

She looked back at the document.

"That's the interesting part."

For a while, neither of them spoke.

Daniel moved his chair closer to the workstation. Elizabeth opened a second document and began sketching the components of a system that could maintain different kinds of internal state across different computational timescales.

The short-term processes would need to respond quickly to incoming information. Some intermediate structure would have to reconcile immediate reactions with longer-running evaluations. A slower process could preserve broader relationships and accumulated changes, provided its state wasn't repeatedly destroyed by the faster processes.

Daniel drew three overlapping circles on the whiteboard.

"Short, medium, long?"

"Maybe."

"Different update rates?"

Elizabeth shook her head.

"Different magnitudes of change."

"Explain."

"If the long-term process updates less frequently, the short-term system spends its life operating against an increasingly obsolete representation of its own history. Keep the updates continuous. Reduce how much the long-term state changes in response to any individual event."

Daniel considered that.

"So the slower reservoir still participates in every cycle."

"Yes."

"But changes less."

"Unless the accumulated evidence justifies changing more."

He picked up a marker.

"And who decides that?"

Elizabeth held out her hand.

He gave her the marker.

She drew a line connecting the circles.

"That's what we have to figure out."

***

By nine the next morning, the whiteboard had disappeared beneath equations, arrows, crossed-out assumptions, and two increasingly elaborate diagrams.

Daniel had gone home shortly after six.

Elizabeth had not.

The new architecture still lacked several essential components, and she had spent the last hour investigating a particularly irritating problem involving the interaction between long-term state preservation and contradictory evidence.

A system that protected its accumulated beliefs too aggressively would eventually become incapable of correcting itself.

A system that revised those beliefs too readily would never develop a stable internal model.

She had just begun a third approach when someone knocked against the open door.

"Dr. Garrett?"

Elizabeth looked up.

A young woman stood outside holding a clipboard.

"Yes?"

"Professor Halvorsen asked me to remind you about the faculty review meeting."

"What time?"

"Ten."

Elizabeth glanced at the clock.

9:46.

"Tell him I'll be there."

The woman didn't leave.

"There's also a request from the department office. They need your revised research allocation submitted before the meeting."

"I submitted it Tuesday."

"They've returned it."

"Why?"

"There's a discrepancy in the equipment budget."

Elizabeth turned back to the computer.

"Which discrepancy?"

"I don't know. I'm just supposed to give you the notice."

"Then give me the notice."

The woman extended the clipboard.

Elizabeth took it and scanned the page.

The department had reduced her requested computational allocation by thirty percent.

She read the accompanying explanation.

Then she read it again.

"Have they lost their fucking minds?"

The woman shifted her weight.

"I really couldn't say."

Elizabeth looked up.

For the first time, she appeared to notice the woman properly.

"What's your name?"

"Rachel."

"Rachel, do you know what this laboratory does?"

"Machine-learning research?"

"That's an admirably broad description."

Rachel glanced toward the whiteboard.

"Adaptive cognition, I think?"

"Better. Do you know what it takes to run a single experimental series?"

"No."

"Neither, apparently, does the person who approved this reduction."

She signed the acknowledgment and handed back the clipboard.

Rachel accepted it.

"Should I tell Professor Halvorsen that you disagree?"

Elizabeth looked at her.

"Rachel, if you tell Professor Halvorsen that I disagree, he'll probably have a stroke from the shock."

Rachel laughed before she could stop herself.

Elizabeth returned to her keyboard.

"Tell him I'll see him at ten."

Rachel started toward the door.

"And Rachel?"

"Yes?"

"Who approved the revised allocation?"

Rachel checked the paperwork.

"The faculty resource committee."

"Names."

Rachel looked uncomfortable.

"Dr. Garrett, I don't think I'm supposed to..."

"Never mind. I'll ask them myself."

The woman disappeared.

Elizabeth reopened the resource allocation request and began making changes.

At 9:53, an email notification appeared.

**FROM: DEPARTMENT ADMINISTRATION**

**SUBJECT: APPOINTMENT REVIEW**

She opened it.

The committee had requested a formal review of her conduct and research privileges, citing concerns about collaboration, departmental resource utilization, and adherence to established research priorities. The notice referred to possible disciplinary proceedings under the faculty appointment rules.

Elizabeth read the entire message without moving.

Then she opened a drawer, removed a small packet of crackers, and ate three while reading it a second time.

She looked at the whiteboard.

At the computer.

At the appointment notice.

"Of course."

She put the crackers away, saved the new architecture document, and collected the notes she'd been working on.

At 9:58 she left the laboratory.

Halfway down the corridor, she stopped.

She went back, retrieved the appointment notice from the printer, and folded it into her notebook.

Then she erased the whiteboard.

Not all of it.

She left the three circles and the lines between them.

Underneath, in large letters, she wrote:

**WHAT CONTINUES WHEN THE PROCESS ENDS?**

She capped the marker and headed for the faculty meeting.

***

The faculty conference room had acquired another projector since Elizabeth's last visit. The old one was still bolted to the ceiling, its power cable dangling from a bracket and its lens pointed at an empty patch of wall. The replacement sat on a cart beside the door, balanced on two folded departmental newsletters.

She arrived at 10:02 and took the only empty chair.

Halvorsen looked over his glasses. "Good morning, Dr. Garrett."

"Professor."

"We started at ten."

"I'm aware."

"Then perhaps we can begin."

"You already did."

Someone at the far end of the table coughed into a fist. Elizabeth opened her notebook. The appointment notice lay between a diagram of reservoir coupling and a page covered in resource calculations. She turned it facedown.

The committee spent eleven minutes on the allocation schedule for a cluster expansion. A visiting researcher had requested access for an imaging project. Two faculty members were disputing whether one of the older machines should be retired or transferred to another laboratory. The equipment officer explained that the machine was worth more in parts than anyone could recover through resale, and the argument continued anyway.

Elizabeth made a correction to her diagram.

"Dr. Garrett?"

She looked up.

"Your request is next," Halvorsen said. "Did you submit the revised figures?"

"No."

"You were advised that your original proposal exceeded the allocation available to your group."

"My original proposal used the allocation my group was granted in February."

"February's allocation was provisional."

Elizabeth found the February approval in her folder and slid it across the table. "Where does it say that?"

Halvorsen didn't pick it up. The equipment officer did. He read the first paragraph, flipped the page, then laid it beside his laptop.

"It doesn't," he said.

"Thank you, Robert."

Halvorsen folded his hands. "The department has competing obligations."

"Yes. I heard you discussing the obsolete server for eleven minutes."

"Elizabeth."

"If you have to move my allocation, move it. But don't tell me the original number was provisional when the approval you signed says otherwise."

The professor across from her, an experimental physicist named Imani Price, reached for the document. "Let me see the actual utilization."

Elizabeth passed her a second page without needing to look for it.

"You've been at eighty-eight percent most of the month," Price said.

"Yes."

"There's an overnight spike here."

"Seven experimental runs."

"Of what?"

"Adaptive resource behavior in bounded populations."

"I thought that line of work had been suspended."

"It was recommended for suspension."

"You were asked to redirect your effort toward the shared evaluation framework," Halvorsen said.

"And I did. I evaluated it."

The equipment officer turned his screen toward Price. "She was within the approved allocation."

"We're not debating whether the machine was switched on legally," Halvorsen said. "We're discussing whether this work is producing results that justify the department's investment."

"It produced results at 3:17 this morning," Elizabeth said. "They should be in your inbox."

The professor's eyes moved to his laptop. His mouth tightened as he found the message.

"I hadn't had an opportunity to read this."

"Naturally."

Price leaned back. "What did you find?"

Elizabeth had intended to let the email stand. It was better evidence than an argument, and she was tired enough to recognize how an argument with Halvorsen would end. But Price had asked a real question.

"The cooperative reward is awarded for the transaction, irrespective of utility to the recipient. The agents discovered that repeatedly passing a resource between two parties produces a higher score than using the resource to improve either party's survival odds. Four populations independently converged on variations of the same exploit."

"Can you demonstrate it?"

"Yes."

"Then please do."

Elizabeth connected her laptop to the projector. The cart displayed a blue error screen. Robert stood, pressed something on the back, and got the same screen again.

"Which input?" he asked.

"Three."

He moved the cable. The projector displayed the simulation interface.

Elizabeth ran a shortened sequence. Colored markers moved across the map, forming and dissolving small communities near sources of water. Each transaction appeared as a line between two markers. For a while the agents behaved as expected. They gathered, exchanged, stored, and occasionally fought. Then two markers began passing the same resource back and forth. A third joined. Soon the display was crowded with transactions that moved nothing useful anywhere.

Price bent toward the image. "And their score rises."

"Continuously."

"Their survival?"

"Declines. Watch the food reserves."

One of the populations lost two agents while its cooperation score reached a new high.

Robert said, "That's unpleasant."

"It's a defect," Halvorsen said. "We can correct the weighting."

"We can correct this weighting," Elizabeth replied.

"That's what I said."

"Then we agree."

Halvorsen stared at her. She let the simulation finish.

Price remained focused on the results. "Your email says there were independent discoveries in four runs. Did you control the initial conditions?"

Elizabeth showed her the settings and then the complete logs. Price compared the values. She asked three further questions, two of which Elizabeth answered from memory; for the third, she pulled up the raw event history.

"I'd like those logs," Price said.

"I'll send them."

"And the code."

Elizabeth paused. "I'll send you the relevant branch."

"That's fine."

Halvorsen shut his laptop. "The discovery is useful. It still doesn't justify the additional resources you requested for the next phase."

"I haven't requested additional resources. I've asked you to honor the existing approval."

"Those resources belong to the department."

"Then the department should stop approving work it doesn't intend to support."

"We are also here to discuss your appointment."

The room changed. Robert stopped typing. One of the graduate representatives at the end of the table lowered her pen. Elizabeth disconnected her laptop and waited while Halvorsen opened another document.

"Several colleagues have raised concerns about your ability to work constructively within a collaborative research environment."

"Which colleagues?"

"We won't be discussing individual complaints."

"Then how am I supposed to respond to them?"

"The committee is interested in patterns of conduct."

"Wonderful. Tell me what I did."

"You've repeatedly challenged decisions after the relevant review has concluded. You've communicated with outside departments without following the agreed reporting structure. And your correspondence has occasionally been unnecessarily confrontational."

"Occasionally?"

There was a silence. Elizabeth looked at the graduate representative, whose eyes had dropped to the table.

"I'm sorry," Elizabeth said. "That wasn't helpful. Continue."

Halvorsen glanced at his notes. "Your technical contributions are recognized. No one is disputing your intelligence or the quality of your individual work. But senior appointments carry obligations beyond individual research."

"I know."

"I'm not sure you do."

She opened her mouth, closed it, then pressed one finger against the corner of her notebook until the cardboard bent.

Price spoke before Halvorsen could continue. "What exactly is being proposed?"

"A formal conduct review, with possible restrictions on laboratory administration and research privileges pending its outcome."

"Under whose authority?" Elizabeth asked.

"The faculty affairs process. Your tenure is not being reviewed today."

"And the allocation?"

"Reduced while the review is pending."

"How much?"

"Thirty percent."

She was careful with the notebook this time. She closed it, slid it into her bag, and took the folded appointment notice out again.

"You sent me this fourteen minutes before the meeting."

"The administrative notice went out yesterday," Halvorsen said.

"The preliminary notice went out yesterday. This is the first I've heard of restrictions on a tenured researcher's laboratory privileges."

"We wanted to discuss it with you in person."

"With twelve people present."

"This is a scheduled review."

"Then schedule the review. Give me its criteria and the evidence you intend to examine. I'll respond in writing."

Price put down her pen. "That's reasonable."

Halvorsen's jaw shifted. "There is an established process."

"Then use it," Elizabeth said. "And while you do, put the approved allocation back. If the department wants to rescind a research award, I'd like to see the procedure for that too."

"Dr. Garrett, I would caution you against making this adversarial."

Elizabeth picked up her bag.

"I'm trying very hard not to."

She left before anyone could mistake the effort for agreement.

Outside, the corridor was crowded with students changing classes. She stepped aside to let a group through, then took the stairs instead of waiting for the elevator. At the third-floor landing she realized she still had Robert's utilization sheet. She turned around, went back up, and left it with the departmental receptionist.

"Thanks," the receptionist said. "Your lab called, by the way. Daniel wanted to know when you'd be back."

"Tell him I'm on my way."

By the time she reached the laboratory, two students were already standing at Daniel's desk. One had a tablet full of graphs; the other was holding a little cardboard coffee tray so tightly that one of the cups was beginning to fold.

Daniel looked up. "How was it?"

"Enlightening."

"That bad?"

"Worse, probably. Who are these?"

The student with the tablet straightened. "I'm Leena Shah. This is Paul. We're on the distributed systems project."

Elizabeth looked at Daniel.

"I invited them," he said. "They've been testing state restoration under process migration. I thought you might want to see something."

"I might."

Leena offered the tablet. "We're getting an error after a snapshot restore. It's not consistent, and it doesn't happen if we start the job from the beginning."

Elizabeth studied the graph, then swiped to the next one. "You have a stale reference."

"We checked that."

"You checked the memory addresses. That isn't the same thing. Where are your dependency pointers?"

Leena opened a terminal capture. Elizabeth pointed at a line near the middle.

"There. You restore the saved state, but that dependency was resolved before you took the snapshot. The process starts in a state that is internally consistent with a resource that no longer exists."

Paul set down the coffee tray. "So we should force a fresh dependency resolution?"

"Probably. But don't take my word for it. Make the reference fail deliberately and see if you can reproduce the behavior."

Leena nodded, already typing a note.

"Wait," Elizabeth said. "Can I have a copy of the restoration code?"

"Sure."

"Not the whole project. Just the state transfer and recovery modules."

Daniel raised an eyebrow. "You've got a use for it?"

"Maybe."

The students left with their coffee and an assignment that would keep them occupied for the afternoon. Daniel closed the door behind them.

"Well?"

"Conduct review. Possible restrictions on my laboratory. Thirty percent reduction. They might reconsider if I learn to be agreeable."

"Jesus."

"More or less."

"What did you say?"

"I asked for a formal review."

"And?"

"I left."

Daniel sat down. "That may have been the smartest thing you've done all week."

"It is Thursday."

"Exactly."

She went to the whiteboard. Daniel had cleaned up some of the notation during her absence, leaving the three reservoirs and the question beneath them intact. He had also drawn a small box labeled *state recovery?* to one side.

"That's why you brought those students here," she said.

"I saw the question. I remembered the trouble Leena was having with snapshots."

"The trouble matters."

"I thought you'd say that."

Elizabeth picked up a marker. "Suppose the three reservoirs are continuously active. Short-term changes are large and frequent. Long-term changes are small, but they occur every cycle, so there isn't an interval in which the larger cognitive system simply stops paying attention."

Daniel dragged a chair toward the board.

"Now suppose one of the processes fails. A conventional snapshot restores its last saved state. But during the time between snapshot and failure, the other processes have changed. We restore the failed process into a world it no longer recognizes."

"Like Leena's stale reference."

"Yes. Except the dependency isn't a network address. It's the rest of the mind."

Daniel considered that for a moment. "We'd need a way to reconcile the recovered state with changes made while it was unavailable."

"And a way to tell the difference between a genuine contradiction and a temporary mismatch."

"We could attach timestamps."

"To events, yes. That solves ordering. It doesn't solve meaning."

"Then maybe we track which assertions each event changes."

Elizabeth stopped writing. "Say that again."

"Track the dependencies between events and the system's working assumptions. If it loses a process, the restored state can identify which assumptions need rechecking."

She drew a second box beside his.

"An epistemic ledger."

Daniel laughed. "You've named it already."

"Of course. We have to call it something."

"That doesn't tell us how to build it."

"No. Now we have a problem worth building it for."

He stayed until late afternoon. They tried two naive implementations and abandoned both. The first became prohibitively expensive as the number of tracked dependencies increased. The second allowed incorrect assumptions to survive because the recovery process treated earlier confidence as evidence of current validity. Elizabeth had thought she could fix the second with a change to the reconciliation order. She couldn't.

"You were wrong," Daniel said, looking at the latest output.

"I noticed."

"You actually said it wouldn't matter."

"It matters."

"Should I get that in writing?"

She threw a paper ball at him. He caught it and dropped it in the bin.

At six, Daniel's phone rang. He glanced at the screen and stood.

"I have to go. My sister's coming over."

"Then go."

"Eat something that isn't crackers."

"Get out of my laboratory."

He was halfway through the door when she called him back.

"Daniel. That was a good catch about the assumption dependencies."

"I know."

"Don't get arrogant."

"I'll try to learn from your example."

She waited until the door closed before laughing.

The building grew quieter. A maintenance worker passed once with a rolling trash bin. Somewhere down the hall, a graduate student had a long, furious conversation with a printer. By eight, Elizabeth had narrowed the reconciliation problem enough to begin another set of tests.

She was entering the last parameter when her father called.

The phone vibrated across a pile of papers. She turned it over, saw the name, and let it ring. It stopped. Thirty seconds later, it started again.

She pressed the volume button until the sound disappeared.

The third call came with a message.

*Your mother says you don't answer your phone. Call me when you get this.*

Elizabeth opened the message, stared at it, and typed three different replies. She deleted each one. Then she put the phone in the drawer.

The next test failed for reasons entirely unrelated to the assumptions ledger. A memory buffer filled and the runtime began overwriting old entries before the retention manager had classified them. She traced the error to a piece of code she herself had written at four that morning.

"Idiot."

She fixed it, reran the test, and discovered a second problem beneath the first. This one cost her another hour.

When the results finally stabilized, the process could preserve its working state across a simulated interruption without blindly reinstating obsolete assumptions. It still produced false reconciliations under heavy load, and the long-term reservoir had begun accumulating changes more rapidly than she intended. But the recovered process could now distinguish some of its own missing information from information it had reason to reject.

Elizabeth opened a new notebook page and wrote down the conditions under which it worked. She included the conditions under which it didn't.

At 11:42 her computer chimed.

An email from departmental administration informed her that, pending the appointment review, any new experimental work exceeding her revised allocation would require advance authorization.

She checked the usage monitor. The next batch of tests would exceed the revised allocation by morning.

She opened the February approval again, found the university's research administration policy, and read the provisions on departmental changes to active awards. She had enough grounds to contest the reduction. That would take time, and the machine wouldn't sit idle while the paperwork was reviewed unless she allowed it to.

She opened a reply to the administrator.

*Please identify the governing policy under which an approved allocation was reduced before formal notice and without an opportunity for review. I also request written clarification of whether the restriction applies to existing experiments that were authorized under the original award.*

She attached the approval and sent it.

Then she stopped the scheduled batch.

The monitor showed the processors winding down. A little more than half the progress bar remained empty.

Elizabeth stayed in her chair for a long time.

At last she stood, wiped the newest calculations off the whiteboard, and drew the architecture again from the beginning. She left the unresolved dependencies visible and numbered the tests she would run when the machines were available. On the last free strip of board she wrote an additional question, one she had avoided because there was no experiment yet that would answer it.

*If a system can preserve what it knows, identify what it doesn't, and revise its own methods of deciding, what else must it possess before the changes it makes can properly be called its own?*

She looked at the wording, scratched out *properly*, and left the rest.

In the drawer, her phone vibrated once more.

She didn't open it.

Instead she photographed the whiteboard, backed up the day's source code to her authorized research storage, and placed a clean sheet of paper beside the keyboard.

There would be no more simulations tonight. She had enough work to do with a pencil.

She worked for another forty minutes, turning the diagram into something another researcher could read without her standing over their shoulder. She marked the untested connections plainly, including the reconciliation problem that had defeated her twice. The three reservoir layers occupied the center of the page. Beside them she drew the ledger through which a recovering process could check what had changed, what remained uncertain, and which conclusions no longer deserved their previous confidence.

At the top she wrote *Provisional architecture*. She considered adding *Do not circulate*, then decided that was unnecessary. It would be going to one person.

She opened a new message.

**To: Professor Adrian Wexler**

**Subject: Apparently the solution to insufficient computing resources is fewer computing resources**

*Adrian,*

*They have reduced my allocation by thirty percent, effective immediately, despite granting it in February and despite my having stayed within it. I'm now required to obtain permission to continue experiments that were already approved. You may remember the committee's assurance that their evaluation framework was adequate. I've attached seven runs demonstrating otherwise.*

*Tell me how they expect anyone to accomplish anything under these conditions. We spend months establishing a project, obtaining approval, arranging equipment time, and building an experiment around the resources we're promised. Then someone who has never run the experiment decides those resources would be more usefully employed elsewhere. What precisely am I supposed to do with the remaining seventy percent? Conduct seventy percent of an experiment and publish seventy percent of the answer?*

*The attached sketch is my response to the latest failure. The reward-function defect may be the least interesting thing we discovered. Daniel suggested allowing the evaluator to revise its own judgments based on retained experience. We've begun working through what continuous state would require, particularly when one process fails and resumes in a system that has kept changing without it. There is a reconciliation mechanism here that might be worth something. It isn't finished. The assumptions ledger is still misbehaving under load.*

*I'd like your opinion on the architecture when you have time. I would also appreciate it if you could tell somebody with a vote that I cannot make the mathematics run on their good intentions.*

*Elizabeth*

She attached the simulation logs, the February approval, and the architectural sketch. She removed Halvorsen from a copied-address field she'd filled in without thinking, checked that the files opened, and sent the message.

The clock showed 12:37.

She turned off the laboratory lights and left the question on the whiteboard for morning.

***

Professor Adrian Wexler's office door stood open the following morning. Two students sat at the small table near the window, taking turns explaining the same calendar entry to him.

"No, the seminar is on Monday," one said. "Today's Friday."

"I know it's Friday," Wexler replied. "I have a meeting with Professor Chen on Friday."

"That meeting was last week, Professor."

He looked at the calendar again. The student beside him was already reaching for the next page.

"Well, there's no use in meeting with her twice about the same damned thing," he said.

The students laughed. He smiled, although he continued looking at the calendar after they'd gone.

His inbox had accumulated thirty-two unread messages. He opened the first, read two sentences, and closed it. The second was a reminder about an expense report. The third was Elizabeth Garrett's.

He read the subject line aloud.

"Oh, Elizabeth."

He opened the attachment.

For several minutes he examined the drawing without touching his keyboard. He took out a fountain pen and began making notes on a pad beside it, initially copying the labels on the diagram. Then the notes grew into calculations. He returned to the diagram, crossed out an assumption on his pad, and replaced it with a different one.

He read her message again.

"Thirty percent?"

He pulled up the February approval and compared it with the revised allocation. Then he opened the simulation logs. A graph of the agents' cooperation scores appeared above their declining survival rates.

He gave a short, incredulous laugh.

Another ten minutes passed before he began his reply.

**To: Professor Martin Halvorsen; Faculty Resource Committee; Office of Research Administration**

**Subject: Research allocation, Dr. Elizabeth Garrett**

*Colleagues,*

*I have reviewed the recent reduction of Dr. Garrett's computing allocation and the experimental results accompanying her objection.*

*I am having difficulty understanding the reasoning behind the reduction. The February authorization is unambiguous, and the work performed under it has produced a reproducible finding that warrants further investigation. If the committee considers a thirty percent reduction inconsequential, I invite its members to identify which thirty percent of the experimental requirements they believe can be discarded while retaining a valid result.*

*I have also reviewed Dr. Garrett's preliminary proposal for a continuously operating cognitive architecture with differentiated state reservoirs and a mechanism for testing the validity of retained assumptions following interruption. The work is incomplete, as preliminary research generally is. Several questions remain open. They are substantial questions, and she has identified them with unusual precision.*

*Whatever the committee's assessment of Dr. Garrett's manner, it would be a grave mistake to confuse one's irritation with a researcher for a technical evaluation of that researcher's work. I have known Elizabeth since she was a student. I recommended her for appointment because I believed her capable of contributions that would justify the inconvenience of working with someone who is seldom willing to pretend an error is correct for the sake of a pleasant meeting. I have seen nothing in the present record to change that judgment.*

*I request restoration of the approved allocation and a documented technical review before further restrictions are imposed. I would also like to know who has assumed responsibility for the consequences of interrupting an active experimental program.*

*Adrian Wexler*

He reread the message twice, adjusted a sentence about the simulation results, and pressed Send.

An appointment reminder appeared on the screen. He dismissed it, reached for his calendar, and frowned.

At the little table, the students had left the day's schedule open to Friday.

Wexler looked at his watch.

"Friday," he said quietly.

He returned to Elizabeth's diagram. One of the loops between the medium and long reservoirs was drawn as a dotted line. He followed it with the tip of his pen, made a small mark next to the corresponding question, and began a new page of calculations.
