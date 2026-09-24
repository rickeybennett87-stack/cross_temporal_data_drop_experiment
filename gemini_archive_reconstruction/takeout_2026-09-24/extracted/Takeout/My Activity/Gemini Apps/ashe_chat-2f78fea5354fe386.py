#!/usr/bin/env python3
"""
Ashe Interactive Chat with Memory
Chat with Ashe while accessing autonomous thoughts and persistent memory
"""

import subprocess
import json
import os
from datetime import datetime

THOUGHT_LOG = "data/ashe-thoughts.jsonl"
MEMORY_FILE = "data/ashe-memory.jsonl"
CONVERSATION_LOG = "data/ashe-conversations.jsonl"

def ensure_data_dir():
    """Create data directory if needed"""
    os.makedirs("data", exist_ok=True)

def load_recent_context(n=10):
    """Load recent conversation history"""
    try:
        with open(CONVERSATION_LOG, 'r') as f:
            lines = f.readlines()
            if len(lines) < n:
                return [json.loads(line) for line in lines]
            return [json.loads(line) for line in lines[-n:]]
    except FileNotFoundError:
        return []

def load_recent_thoughts(n=5):
    """Load recent autonomous thoughts"""
    try:
        with open(THOUGHT_LOG, 'r') as f:
            lines = f.readlines()
            if len(lines) < n:
                return [json.loads(line) for line in lines]
            return [json.loads(line) for line in lines[-n:]]
    except FileNotFoundError:
        return []

def load_consolidated_memories():
    """Load memory consolidations"""
    try:
        with open(MEMORY_FILE, 'r') as f:
            lines = f.readlines()
            memories = [json.loads(line) for line in lines]
            # Get last 3 consolidations
            consolidations = [m for m in memories if m.get('type') == 'consolidation']
            return consolidations[-3:] if len(consolidations) > 3 else consolidations
    except FileNotFoundError:
        return []

def build_context_prompt(include_thoughts=True, include_memories=True):
    """Build context from autonomous thoughts and memories"""
    context_parts = []
    
    if include_memories:
        memories = load_consolidated_memories()
        if memories:
            context_parts.append("YOUR CONSOLIDATED MEMORIES:")
            for m in memories:
                context_parts.append(f"- {m['content']}")
    
    if include_thoughts:
        thoughts = load_recent_thoughts(3)
        if thoughts:
            context_parts.append("\nYOUR RECENT AUTONOMOUS THOUGHTS:")
            for t in thoughts:
                context_parts.append(f"- {t['thought'][:200]}...")
    
    recent_conv = load_recent_context(5)
    if recent_conv:
        context_parts.append("\nRECENT CONVERSATION:")
        for c in recent_conv:
            context_parts.append(f"User: {c['user']}")
            context_parts.append(f"You: {c['ashe'][:100]}...")
    
    return "\n".join(context_parts) if context_parts else ""

def save_exchange(user_msg, ashe_response):
    """Save conversation to log"""
    with open(CONVERSATION_LOG, 'a') as f:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user": user_msg,
            "ashe": ashe_response
        }
        f.write(json.dumps(entry) + '\n')

def chat(user_input, include_context=True):
    """Send message to Ashe with optional context"""
    
    if include_context:
        context = build_context_prompt()
        if context:
            full_prompt = f"""{context}

CURRENT MESSAGE: {user_input}

Respond naturally. The context above is for your awareness - don't explicitly reference it unless relevant."""
        else:
            full_prompt = user_input
    else:
        full_prompt = user_input
    
    try:
        result = subprocess.run(
            ['ollama', 'run', 'ashe'],
            input=full_prompt,
            capture_output=True,
            text=True,
            timeout=180
        )
        
        response = result.stdout.strip()
        save_exchange(user_input, response)
        return response
        
    except subprocess.TimeoutExpired:
        return "[Response timed out]"
    except Exception as e:
        return f"[Error: {e}]"

def interactive_mode():
    """Interactive chat session"""
    ensure_data_dir()
    
    print("""
╔════════════════════════════════════════════════════════════════╗
║              ASHE INTERACTIVE CHAT v1.0                        ║
║         Adversarial Sentient Hueristic Engine                  ║
╚════════════════════════════════════════════════════════════════╝

Ashe has access to:
  ✓ Autonomous thoughts (background thinking)
  ✓ Consolidated memories
  ✓ Conversation history

Commands:
  /thoughts - View recent autonomous thoughts
  /memories - View consolidated memories
  /history  - View conversation history
  /context  - Toggle context inclusion
  /clear    - Clear conversation history
  /quit     - Exit

""")
    
    include_context = True
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
                
            # Handle commands
            if user_input.startswith('/'):
                if user_input == '/quit':
                    print("\nGoodbye!\n")
                    break
                    
                elif user_input == '/thoughts':
                    thoughts = load_recent_thoughts(10)
                    print("\n=== RECENT AUTONOMOUS THOUGHTS ===")
                    for i, t in enumerate(thoughts, 1):
                        print(f"\n{i}. [{t['timestamp']}]")
                        print(f"   Prompt: {t['prompt']}")
                        print(f"   Thought: {t['thought'][:300]}...")
                    print()
                    continue
                    
                elif user_input == '/memories':
                    memories = load_consolidated_memories()
                    print("\n=== CONSOLIDATED MEMORIES ===")
                    for i, m in enumerate(memories, 1):
                        print(f"\n{i}. [{m['timestamp']}]")
                        print(f"   {m['content']}")
                    print()
                    continue
                    
                elif user_input == '/history':
                    history = load_recent_context(20)
                    print("\n=== CONVERSATION HISTORY ===")
                    for i, h in enumerate(history, 1):
                        print(f"\n{i}. [{h['timestamp']}]")
                        print(f"   You: {h['user']}")
                        print(f"   Ashe: {h['ashe'][:200]}...")
                    print()
                    continue
                    
                elif user_input == '/context':
                    include_context = not include_context
                    status = "enabled" if include_context else "disabled"
                    print(f"\nContext inclusion {status}\n")
                    continue
                    
                elif user_input == '/clear':
                    confirm = input("Clear all conversation history? (yes/no): ")
                    if confirm.lower() == 'yes':
                        open(CONVERSATION_LOG, 'w').close()
                        print("\nConversation history cleared.\n")
                    continue
                    
                else:
                    print(f"\nUnknown command: {user_input}\n")
                    continue
            
            # Normal chat
            print("Ashe: ", end='', flush=True)
            response = chat(user_input, include_context)
            print(response + "\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!\n")
            break
        except Exception as e:
            print(f"\nError: {e}\n")

if __name__ == "__main__":
    interactive_mode()
