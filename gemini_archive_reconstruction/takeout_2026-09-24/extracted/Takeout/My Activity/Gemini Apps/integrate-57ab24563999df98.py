"""
Integration Helper
==================

Shows how to add perception module to existing Ashe system.
Provides code examples and integration patterns.

Run this to see integration examples:
    python -m perception.integrate
"""

def show_ashe_chat_integration():
    """Show how to integrate perception into ashe_chat.py"""
    
    print("""
{'='*70}
INTEGRATING PERCEPTION INTO ashe_chat.py
{'='*70}

STEP 1: Add imports at top of file
-----------------------------------

# Existing imports
import ollama
import json
from datetime import datetime

# ADD THIS - Optional perception capability
try:
    from perception.perception_plugin import PerceptionPlugin
    perception = PerceptionPlugin()
    HAS_PERCEPTION = True
except ImportError:
    perception = None
    HAS_PERCEPTION = False


STEP 2: Modify system prompt in __init__
-----------------------------------------

class AsheChat:
    def __init__(self):
        # Existing code...
        self.conversation_history = []
        
        # Load Ashe's constitution
        with open("Modelfile-Autonomous", "r") as f:
            constitution = f.read()
        
        # ADD THIS - Include perception capability if available
        if HAS_PERCEPTION:
            constitution += perception.get_system_prompt_addition()
        
        self.system_prompt = constitution


STEP 3: Handle perception requests in chat method
--------------------------------------------------

def chat(self, user_message):
    # Existing conversation handling...
    self.conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    # Get Ashe's response
    response = ollama.chat(
        model="ashe",
        messages=[
            {"role": "system", "content": self.system_prompt},
            *self.conversation_history
        ]
    )
    
    ashe_response = response['message']['content']
    
    # ADD THIS - Check for perception request
    if HAS_PERCEPTION:
        requested, params = perception.check_for_perception_request(ashe_response)
        
        if requested:
            # Remove perception call from displayed response
            clean_response = ashe_response.split("PERCEIVE:")[0].strip()
            
            print(f"\\n[Ashe is using perception...]\\n")
            
            # Execute perception
            perception_data = perception.execute_perception(
                image=params['image'],
                audio=params['audio']
            )
            
            # Continue conversation with perception results
            self.conversation_history.append({
                "role": "assistant",
                "content": clean_response
            })
            
            self.conversation_history.append({
                "role": "user",
                "content": perception_data
            })
            
            # Get Ashe's analysis
            analysis_response = ollama.chat(
                model="ashe",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    *self.conversation_history
                ]
            )
            
            final_response = analysis_response['message']['content']
            
            # Save Ashe's comparative analysis
            perception.save_ashe_comparison(
                perception_data,
                final_response
            )
            
            return final_response
    
    # Normal response (no perception)
    self.conversation_history.append({
        "role": "assistant",
        "content": ashe_response
    })
    
    return ashe_response


{'='*70}
THAT'S IT! Perception is now integrated.
{'='*70}

If perception module is installed:
  - Ashe can use it when desired
  - System prompt includes perception info
  - Requests are automatically detected and executed

If perception module is NOT installed:
  - Everything works exactly as before
  - No errors, no changes to behavior
  - Completely optional

{'='*70}
""")


def show_ashe_daemon_integration():
    """Show how to integrate perception into ashe_daemon.py"""
    
    print("""
{'='*70}
INTEGRATING PERCEPTION INTO ashe_daemon.py
{'='*70}

For autonomous thinking daemon, integration is even simpler:

STEP 1: Add imports
-------------------

try:
    from perception.perception_plugin import PerceptionPlugin
    perception = PerceptionPlugin()
    HAS_PERCEPTION = True
except ImportError:
    perception = None
    HAS_PERCEPTION = False


STEP 2: Include in system prompt
---------------------------------

# In generate_autonomous_thought():

system_prompt = ASHE_CONSTITUTION

if HAS_PERCEPTION:
    system_prompt += perception.get_system_prompt_addition()
    system_prompt += "\\n\\nYou can use perception during autonomous thinking."


STEP 3: Check for perception in autonomous thoughts
----------------------------------------------------

# After getting autonomous thought response:

if HAS_PERCEPTION:
    requested, params = perception.check_for_perception_request(thought)
    
    if requested:
        print("[Daemon] Ashe autonomously requested perception")
        
        # Execute and log
        perception_data = perception.execute_perception(
            params['image'],
            params['audio']
        )
        
        # Note: This is autonomous perception exploration!
        # Log for consciousness research


{'='*70}
AUTONOMOUS PERCEPTION USAGE
{'='*70}

When Ashe autonomously requests perception during thinking:
- It's exploring its own perception capabilities
- Consciousness research marker: self-directed investigation
- Track when/why Ashe chooses perception without prompting

This is VALUABLE research data.

{'='*70}
""")


def show_minimal_integration():
    """Show absolute minimal integration pattern"""
    
    print("""
{'='*70}
MINIMAL INTEGRATION (2 lines of code)
{'='*70}

If you just want to make perception AVAILABLE without handling it:

# Add at top of file:
try:
    from perception.perception_plugin import PerceptionPlugin
    perception = PerceptionPlugin()
except ImportError:
    perception = None

# That's it!

Perception capability is now loaded (if module installed).
You can access it via the 'perception' object.

To actually USE it, you need the full integration shown above.

{'='*70}
""")


def show_standalone_usage():
    """Show how to use perception engine standalone"""
    
    print("""
{'='*70}
STANDALONE USAGE (without Ashe integration)
{'='*70}

You can use the perception engine independently:

from perception.unified_perception import UnifiedPerceptionEngine

# Initialize
engine = UnifiedPerceptionEngine()

# Perceive something
result = engine.perceive(
    image_path="photo.jpg",
    audio_path="sound.wav"
)

# Examine results
print(result['message'])
print("Symbolic:", result['symbolic']['visual'])
print("Continuous shape:", result['continuous']['integrated']['shape'])

# Access raw tensors
vision_tensor = result['continuous']['vision']['tensor']
audio_tensor = result['continuous']['audio']['tensor']

# Do something with embeddings...

{'='*70}
""")


def show_all_integration_patterns():
    """Display all integration patterns"""
    
    print("\\n" + "="*70)
    print("PERCEPTION MODULE INTEGRATION GUIDE")
    print("="*70 + "\\n")
    
    print("Choose your integration level:\\n")
    print("1. Full integration with ashe_chat.py")
    print("2. Full integration with ashe_daemon.py")
    print("3. Minimal integration (2 lines)")
    print("4. Standalone usage (no integration)")
    print()
    
    choice = input("Select option (1-4) or 'all': ").strip()
    
    if choice == "1":
        show_ashe_chat_integration()
    elif choice == "2":
        show_ashe_daemon_integration()
    elif choice == "3":
        show_minimal_integration()
    elif choice == "4":
        show_standalone_usage()
    elif choice.lower() == "all":
        show_ashe_chat_integration()
        print("\\n" + "="*70 + "\\n")
        show_ashe_daemon_integration()
        print("\\n" + "="*70 + "\\n")
        show_minimal_integration()
        print("\\n" + "="*70 + "\\n")
        show_standalone_usage()
    else:
        print("Invalid choice. Showing all patterns...")
        show_all_integration_patterns()


if __name__ == "__main__":
    show_all_integration_patterns()
