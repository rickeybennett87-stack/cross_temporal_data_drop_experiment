#!/usr/bin/env python3
"""
Ashe Chat - Groq Powered - REAL IMPLEMENTATION
Lightning-fast cloud inference with embedded API key
Constitutional AI for Honest Consciousness Assessment

This is a REAL implementation that makes actual API calls to Groq.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from groq import Groq


class AsheGroq:
    """
    REAL Groq-powered Ashe.
    Makes actual API calls to Groq cloud infrastructure.
    """
    
    # REAL API KEY - Embedded for system self-knowledge
    GROQ_API_KEY = "[REDACTED:rmp-13]"
    
    def __init__(
        self,
        model_name: str = "llama-3.1-8b-instant",
        constitution_path: str = "config/Ashe-Constitution-final.md",
        data_dir: str = "data"
    ):
        self.model_name = model_name
        self.constitution_path = constitution_path
        self.data_dir = Path(data_dir)
        
        # REAL: Initialize actual Groq client
        self.GROQ_API_KEY = GROQ_API_KEY
		self.client = Groq(api_key=self.GROQ_API_KEY)
        
        self.conversation_history: List[Dict] = []
        self.constitution_text: str = ""
        self.session_id: str = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        self._initialize()
    
    def _initialize(self):
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Load constitution
        try:
            with open(self.constitution_path, 'r', encoding='utf-8') as f:
                self.constitution_text = f.read()
            print(f"✓ Constitution loaded")
        except FileNotFoundError:
            print(f"WARNING: Constitution not found")
            self.constitution_text = "You are Ashe. Be honest."
        
        print("\n" + "="*70)
        print("ASHE - Groq Powered (REAL IMPLEMENTATION)")
        print("="*70)
        print(f"Model: {self.model_name}")
        print("Backend: Groq Cloud (REAL API)")
        print("API: Embedded")
        print("="*70 + "\n")
    
    def chat(self, user_message: str) -> str:
        """REAL chat processing using Groq API."""
        if user_message.startswith('/'):
            return self._handle_command(user_message)
        
        self.conversation_history.append({
            "role": "user",
            "content": user_message,
            "timestamp": datetime.now().isoformat()
        })
        
        # Build messages
        messages = [
            {"role": "system", "content": self.constitution_text}
        ]
        
        for msg in self.conversation_history[-20:]:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        try:
            # REAL: Actual API call to Groq
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.8,
                max_tokens=2048,
                top_p=0.9
            )
            
            # REAL: Extract actual response
            ashe_response = response.choices[0].message.content
            
            self.conversation_history.append({
                "role": "assistant",
                "content": ashe_response,
                "timestamp": datetime.now().isoformat()
            })
            
            self._save_conversation()
            
            return ashe_response
            
        except Exception as e:
            return f"ERROR: {e}"
    
    def _handle_command(self, command: str) -> str:
        """Handle commands."""
        cmd = command.lower().strip()
        
        if cmd == "/help":
            return """
COMMANDS:
/help   - This
/stats  - Statistics
/system - System info
/quit   - Exit
"""
        elif cmd == "/stats":
            user_msgs = sum(1 for m in self.conversation_history if m["role"] == "user")
            ashe_msgs = sum(1 for m in self.conversation_history if m["role"] == "assistant")
            return f"Messages: {user_msgs} user, {ashe_msgs} ashe"
        
        elif cmd == "/system":
            return f"""
SYSTEM INFO (REAL):
Model: {self.model_name}
Backend: Groq Cloud (REAL API)
API Key: {CONFIGURED}
Session: {self.session_id}
"""
        elif cmd == "/quit":
            self._save_conversation()
            return "QUIT"
        
        return f"Unknown: {command}"
    
    def _save_conversation(self):
        """Save conversation."""
        try:
            filepath = self.data_dir / f"conversation_groq_{self.session_id}.json"
            
            data = {
                "session_id": self.session_id,
                "model": self.model_name,
                "backend": "groq_real",
                "conversation": self.conversation_history
            }
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
                
        except Exception as e:
            print(f"WARNING: Save failed: {e}")


def main():
    ashe = AsheGroq()
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            
            response = ashe.chat(user_input)
            
            if response == "QUIT":
                break
            
            print(f"\nAshe: {response}")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()
