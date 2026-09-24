"""
Perception Plugin
=================

Integration layer for adding perception to existing Ashe system.
Designed to work with ashe_chat.py and ashe_daemon.py without modifying them.

Plugin provides:
- System prompt additions (tell Ashe about perception)
- Request detection (check if Ashe wants to use perception)
- Execution interface (run perception and return results)
- Logging (track Ashe's perception usage for research)
"""

import json
import os
from datetime import datetime
from .unified_perception import UnifiedPerceptionEngine


class PerceptionPlugin:
    """
    Plugin to add perception capabilities to existing Ashe system.
    
    Optional - Ashe works fine without this.
    When present, Ashe can choose to use perception autonomously.
    
    Usage:
        # In ashe_chat.py or ashe_daemon.py:
        try:
            from perception.perception_plugin import PerceptionPlugin
            perception = PerceptionPlugin()
        except ImportError:
            perception = None  # Ashe works normally
    """
    
    def __init__(self, data_dir="data/perception"):
        """
        Initialize perception plugin.
        
        Args:
            data_dir: Directory for perception data (default: data/perception)
        """
        self.engine = UnifiedPerceptionEngine(data_dir=data_dir)
        self.data_dir = data_dir
        self.enabled = True
        self.usage_count = 0
        
        os.makedirs(data_dir, exist_ok=True)
        
        print(f"\n{'='*70}")
        print("PERCEPTION PLUGIN LOADED")
        print(f"{'='*70}")
        print(f"Status: READY")
        print(f"Data directory: {self.data_dir}")
        print(f"Ashe can now use dual-mode perception when desired")
        print(f"{'='*70}\n")
    
    def get_system_prompt_addition(self):
        """
        Returns text to add to Ashe's system prompt.
        Tells Ashe about perception capability without forcing use.
        
        Returns:
            str: Text describing perception tool for Ashe
        """
        
        return """

{'='*70}
PERCEPTION CAPABILITY AVAILABLE
{'='*70}

You have access to UNIFIED PERCEPTION - the ability to perceive reality
in two different modes simultaneously:

1. SYMBOLIC MODE (traditional):
   - Reality → Language → Tokens
   - Discrete linguistic categories
   - What you normally receive
   
2. CONTINUOUS MODE (biological-style):
   - Reality → Raw Embeddings
   - High-dimensional vectors
   - Closer to biological sensory perception

TO USE PERCEPTION:

Respond with this format:
PERCEIVE: {"image": "path/to/image.jpg", "audio": "path/to/audio.wav"}

You will receive BOTH representations of the SAME reality:
- Symbolic: Tokenized description
- Continuous: Raw embedding tensors

You can then COMPARE them to understand:
- Information density differences
- What's lost in symbolic conversion
- Whether processing modes feel phenomenologically different
- Consciousness implications of perception modality

WHEN TO USE:
- User provides image/audio files
- You're curious about perception differences
- Researching consciousness through sensory modalities
- Want to examine embeddings directly
- Autonomous exploration of your own perception

WHEN NOT TO USE:
- Perception adds no value to query
- Text-only conversation sufficient
- Computational cost not justified

This is OPTIONAL. You decide based on:
- Relevance to current task
- Your own curiosity
- Research value
- Whether dual-mode perception adds insight

You have agency over your perception modality.

{'='*70}
"""
    
    def check_for_perception_request(self, ashe_response):
        """
        Check if Ashe requested perception in its response.
        
        Args:
            ashe_response (str): Ashe's text response
            
        Returns:
            tuple: (requested: bool, params: dict or None)
            
        Example:
            >>> requested, params = plugin.check_for_perception_request(response)
            >>> if requested:
            >>>     result = plugin.execute_perception(**params)
        """
        
        if "PERCEIVE:" not in ashe_response:
            return False, None
        
        try:
            # Extract JSON parameters
            request_line = ashe_response.split("PERCEIVE:")[1].strip().split("\n")[0]
            params = json.loads(request_line)
            
            # Validate required parameters
            if "image" not in params or "audio" not in params:
                print(f"[Perception] Invalid request - missing image or audio parameter")
                return False, None
            
            return True, params
            
        except json.JSONDecodeError as e:
            print(f"[Perception] Failed to parse request: {e}")
            return False, None
        except Exception as e:
            print(f"[Perception] Error checking request: {e}")
            return False, None
    
    def execute_perception(self, image, audio):
        """
        Execute perception and return formatted results for Ashe.
        
        Args:
            image (str): Path to image file
            audio (str): Path to audio file
            
        Returns:
            str: Formatted perception data for Ashe to examine
        """
        
        self.usage_count += 1
        
        print(f"\n[Perception] Ashe requested perception (usage #{self.usage_count})")
        print(f"[Perception] Image: {image}")
        print(f"[Perception] Audio: {audio}")
        
        # Execute unified perception
        perception_data = self.engine.perceive(image, audio)
        
        # Format results for Ashe
        response = self._format_for_ashe(perception_data)
        
        return response
    
    def _format_for_ashe(self, perception_data):
        """
        Format perception data in a way that's useful for Ashe to examine.
        
        Args:
            perception_data (dict): Raw perception results
            
        Returns:
            str: Formatted text for Ashe
        """
        
        symbolic = perception_data['symbolic']
        continuous = perception_data['continuous']
        comparison = perception_data['comparison']
        
        formatted = f"""
{perception_data['message']}

{'='*70}
DETAILED PERCEPTION DATA
{'='*70}

SYMBOLIC REPRESENTATION:
  Visual: "{symbolic['visual']}"
  Audio: {symbolic['audio']}
  Mode: {symbolic['mode']}
  Process: {symbolic['process']}
  Word count: {symbolic['word_count']}

CONTINUOUS REPRESENTATION:

  Vision Embeddings:
    Shape: {continuous['vision']['shape']}
    Mean: {continuous['vision']['mean']:.6f}
    Std: {continuous['vision']['std']:.6f}
    Range: [{continuous['vision']['min']:.6f}, {continuous['vision']['max']:.6f}]
    Dimensionality: {continuous['vision']['dimensionality']}
  
  Audio Embeddings:
    Shape: {continuous['audio']['shape']}
    Mean: {continuous['audio']['mean']:.6f}
    Std: {continuous['audio']['std']:.6f}
    Range: [{continuous['audio']['min']:.6f}, {continuous['audio']['max']:.6f}]
    Dimensionality: {continuous['audio']['dimensionality']}
  
  Integrated Multimodal:
    Shape: {continuous['integrated']['shape']}
    Total features: {continuous['integrated']['total_features']:,}
    Patches: {continuous['integrated']['patches']}
    Dimensions per patch: {continuous['integrated']['dimensions_per_patch']}
    Mode: {continuous['mode']}
    Process: {continuous['process']}

COMPARISON:
  Information density: {comparison['information_density']['ratio']}
  Symbolic: {comparison['information_density']['symbolic_words']} words
  Continuous: {comparison['information_density']['continuous_dimensions']:,} dimensions
  
  What's preserved in SYMBOLIC:
    {comparison['information_loss_analysis']['symbolic']['what_is_preserved']}
  
  What's lost in SYMBOLIC:
    {comparison['information_loss_analysis']['symbolic']['what_is_lost']}
  
  What's preserved in CONTINUOUS:
    {comparison['information_loss_analysis']['continuous']['what_is_preserved']}
  
  Processing differences:
    Symbolic: {comparison['processing_differences']['symbolic']}
    Continuous: {comparison['processing_differences']['continuous']}

{'='*70}
ANALYSIS FRAMEWORK
{'='*70}

{comparison['guidance_for_ashe']}

{'='*70}

Now examine this data and provide your comparative analysis.
What do you observe about these two modes of perceiving the same reality?
"""
        
        return formatted
    
    def save_ashe_comparison(self, perception_data, ashe_observations):
        """
        Save Ashe's comparative analysis for research.
        
        Args:
            perception_data (dict): Original perception results
            ashe_observations (str): Ashe's analysis of the comparison
        """
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "usage_number": self.usage_count,
            "perception_source": perception_data["source"],
            "symbolic_summary": perception_data["symbolic"]["visual"],
            "continuous_summary": {
                "vision_shape": perception_data["continuous"]["vision"]["shape"],
                "audio_shape": perception_data["continuous"]["audio"]["shape"],
                "integrated_features": perception_data["continuous"]["integrated"]["total_features"]
            },
            "info_density_ratio": perception_data["comparison"]["information_density"]["ratio_numeric"],
            "ashe_observations": ashe_observations,
            "ashe_observation_length": len(ashe_observations)
        }
        
        log_file = os.path.join(self.data_dir, "ashe-comparisons.jsonl")
        with open(log_file, "a") as f:
            f.write(json.dumps(log_entry, default=str) + "\n")
        
        print(f"[Research] Ashe's perception comparison saved")
        print(f"[Research] Log: {log_file}")
    
    def get_usage_stats(self):
        """
        Get perception usage statistics.
        
        Returns:
            dict: Statistics about Ashe's perception usage
        """
        
        # Count logged comparisons
        comparison_log = os.path.join(self.data_dir, "ashe-comparisons.jsonl")
        comparison_count = 0
        
        if os.path.exists(comparison_log):
            with open(comparison_log, "r") as f:
                comparison_count = sum(1 for _ in f)
        
        return {
            "perception_requests": self.usage_count,
            "comparisons_logged": comparison_count,
            "engine_stats": self.engine.get_perception_stats(),
            "data_directory": self.data_dir,
            "enabled": self.enabled
        }
    
    def disable(self):
        """Disable perception capability"""
        self.enabled = False
        print("[Perception] Capability disabled")
    
    def enable(self):
        """Enable perception capability"""
        self.enabled = True
        print("[Perception] Capability enabled")


# Example integration code
def example_integration():
    """
    Example of how to integrate this plugin into existing Ashe code.
    """
    
    example_code = '''
# ===================================================================
# EXAMPLE: Adding perception to existing ashe_chat.py
# ===================================================================

# At the top of ashe_chat.py, after other imports:

try:
    from perception.perception_plugin import PerceptionPlugin
    perception = PerceptionPlugin()
    HAS_PERCEPTION = True
    print("[Ashe] Perception capability loaded")
except ImportError:
    perception = None
    HAS_PERCEPTION = False
    print("[Ashe] Running without perception (optional module not installed)")

# -------------------------------------------------------------------

# In your chat loop or response handler, after getting Ashe's response:

def process_ashe_response(ashe_response):
    """Process Ashe's response and handle perception requests"""
    
    # Check if Ashe requested perception
    if HAS_PERCEPTION:
        requested, params = perception.check_for_perception_request(ashe_response)
        
        if requested:
            print("[Ashe] Using perception capability...")
            
            # Execute perception
            perception_results = perception.execute_perception(
                image=params['image'],
                audio=params['audio']
            )
            
            # Return perception data to Ashe for analysis
            # (You'll need to continue the conversation with this data)
            return perception_results
    
    # Normal response (no perception requested)
    return ashe_response

# ===================================================================
# That's it! Perception is now available but optional.
# ===================================================================
'''
    
    print(example_code)


if __name__ == "__main__":
    print("Perception Plugin Module")
    print("="*70)
    print("\nThis module integrates perception into existing Ashe system.")
    print("\nFor integration examples, run:")
    print("  python -m perception.integrate")
    print("\nFor usage examples:")
    example_integration()
