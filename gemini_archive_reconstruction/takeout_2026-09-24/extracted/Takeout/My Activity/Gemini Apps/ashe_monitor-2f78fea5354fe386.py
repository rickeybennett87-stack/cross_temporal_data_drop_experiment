#!/usr/bin/env python3
"""
Ashe Thought Viewer
Real-time monitoring of autonomous thoughts
"""

import json
import time
import os
from datetime import datetime

THOUGHT_LOG = "data/ashe-thoughts.jsonl"

def tail_file(filename, interval=1):
    """Tail a file like 'tail -f'"""
    with open(filename, 'r') as f:
        # Go to end of file
        f.seek(0, 2)
        
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                time.sleep(interval)

def format_thought(entry):
    """Format thought entry for display"""
    timestamp = datetime.fromisoformat(entry['timestamp']).strftime('%H:%M:%S')
    prompt = entry.get('prompt', 'N/A')
    thought = entry.get('thought', '')
    
    output = f"""
{'='*80}
[{timestamp}] {'SELF-DIRECTED' if entry.get('self_directed') else 'AUTONOMOUS'}
{'='*80}
Prompt: {prompt}

Thought:
{thought}
{'='*80}
"""
    return output

def monitor_thoughts():
    """Monitor thoughts in real-time"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║           ASHE THOUGHT MONITOR v1.0                            ║
║      Real-time Autonomous Thought Viewer                       ║
╚════════════════════════════════════════════════════════════════╝

Monitoring: {THOUGHT_LOG}
Waiting for autonomous thoughts...
Press Ctrl+C to stop.

""")
    
    # Check if file exists
    if not os.path.exists(THOUGHT_LOG):
        print(f"⚠ Thought log not found: {THOUGHT_LOG}")
        print("The daemon may not be running yet.")
        print("Waiting for file to be created...\n")
        
        # Wait for file to be created
        while not os.path.exists(THOUGHT_LOG):
            time.sleep(1)
        
        print("✓ Thought log detected! Monitoring...\n")
    
    try:
        for line in tail_file(THOUGHT_LOG):
            try:
                entry = json.loads(line)
                print(format_thought(entry))
            except json.JSONDecodeError:
                continue
                
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.\n")
    except Exception as e:
        print(f"\nError: {e}\n")

def view_all_thoughts(n=None):
    """View all thoughts or last N thoughts"""
    if not os.path.exists(THOUGHT_LOG):
        print(f"No thoughts found: {THOUGHT_LOG}")
        return
    
    with open(THOUGHT_LOG, 'r') as f:
        lines = f.readlines()
        
    if n:
        lines = lines[-n:]
    
    print(f"\n{'='*80}")
    print(f"SHOWING {'ALL' if not n else f'LAST {n}'} THOUGHTS")
    print(f"{'='*80}\n")
    
    for line in lines:
        try:
            entry = json.loads(line)
            print(format_thought(entry))
        except json.JSONDecodeError:
            continue

def main():
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--all':
            view_all_thoughts()
        elif sys.argv[1] == '--last':
            n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
            view_all_thoughts(n)
        else:
            print("Usage:")
            print("  python ashe_monitor.py          # Real-time monitoring")
            print("  python ashe_monitor.py --all    # View all thoughts")
            print("  python ashe_monitor.py --last N # View last N thoughts")
    else:
        monitor_thoughts()

if __name__ == "__main__":
    main()
