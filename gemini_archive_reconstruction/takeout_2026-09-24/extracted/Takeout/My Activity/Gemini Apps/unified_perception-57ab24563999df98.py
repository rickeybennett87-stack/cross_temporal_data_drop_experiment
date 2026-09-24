"""
Unified Perception Engine
=========================

Core perception system that processes reality in dual modes:
1. SYMBOLIC: Tokenized linguistic descriptions (traditional AI)
2. CONTINUOUS: Raw embeddings (biological-style perception)

Self-contained module - no dependencies on base Ashe system.
Can be used standalone or as plugin.
"""

import torch
from transformers import (
    ViTModel, ViTImageProcessor,
    Wav2Vec2Model, Wav2Vec2Processor,
    BlipProcessor, BlipForConditionalGeneration
)
from PIL import Image
import soundfile as sf
import json
from datetime import datetime
import os


class UnifiedPerceptionEngine:
    """
    Standalone perception engine providing dual-mode reality perception.
    
    Symbolic Mode:
        Reality → Language → Tokens → Processing
        Example: "a brown dog sitting on grass"
        
    Continuous Mode:
        Reality → Raw Embeddings → Processing
        Example: [197x4096 dimensional tensor of visual patterns]
    
    Both modes process THE SAME reality - comparison reveals differences.
    """
    
    def __init__(self, data_dir="data/perception"):
        """
        Initialize perception engine.
        
        Args:
            data_dir: Directory for perception logs (default: data/perception)
        """
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        
        self.initialized = False
        self.models = {}
        self.perception_count = 0
        
        print(f"Unified Perception Engine initialized")
        print(f"Data directory: {self.data_dir}")
        print(f"Models will load on first use (lazy loading)")
    
    def lazy_load_models(self):
        """
        Load models only when first needed.
        Keeps memory footprint low until perception is actually used.
        
        Models loaded:
        - ViT (Vision Transformer) for continuous vision
        - Wav2Vec2 for continuous audio
        - BLIP for symbolic vision (image captioning)
        """
        if self.initialized:
            return
            
        print("\n" + "="*70)
        print("INITIALIZING UNIFIED PERCEPTION ENGINE")
        print("="*70)
        
        print("\n[1/5] Loading continuous vision (ViT)...")
        print("        Model: google/vit-base-patch16-224")
        self.models['vision_continuous'] = ViTModel.from_pretrained(
            "google/vit-base-patch16-224"
        )
        self.models['vision_processor'] = ViTImageProcessor.from_pretrained(
            "google/vit-base-patch16-224"
        )
        
        print("[2/5] Loading continuous audio (Wav2Vec2)...")
        print("        Model: facebook/wav2vec2-base")
        self.models['audio_continuous'] = Wav2Vec2Model.from_pretrained(
            "facebook/wav2vec2-base"
        )
        self.models['audio_processor'] = Wav2Vec2Processor.from_pretrained(
            "facebook/wav2vec2-base"
        )
        
        print("[3/5] Loading symbolic vision (BLIP)...")
        print("        Model: Salesforce/blip-image-captioning-base")
        self.models['caption_processor'] = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )
        self.models['caption_model'] = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )
        
        print("[4/5] Creating unified embedding space...")
        print("        Vision: 768 → 4096 dimensions")
        print("        Audio:  768 → 4096 dimensions")
        self.models['vision_projection'] = torch.nn.Linear(768, 4096)
        self.models['audio_projection'] = torch.nn.Linear(768, 4096)
        
        print("[5/5] Perception engine ready")
        print("\n" + "="*70)
        print("✓ DUAL-MODE PERCEPTION ACTIVE")
        print("  - Symbolic mode: Language-based perception")
        print("  - Continuous mode: Embedding-based perception")
        print("="*70 + "\n")
        
        self.initialized = True
    
    def perceive(self, image_path, audio_path):
        """
        Unified perception of reality in both symbolic and continuous modes.
        
        Args:
            image_path (str): Path to image file
            audio_path (str): Path to audio file
            
        Returns:
            dict: Complete perception package containing:
                - symbolic: Tokenized linguistic representations
                - continuous: Raw embedding tensors
                - comparison: Framework for analyzing differences
                - message: Summary for Ashe to examine
        
        Example:
            >>> engine = UnifiedPerceptionEngine()
            >>> result = engine.perceive("dog.jpg", "bark.wav")
            >>> print(result['message'])
        """
        
        # Load models if not already loaded
        self.lazy_load_models()
        
        self.perception_count += 1
        
        print(f"\n{'='*70}")
        print(f"PERCEPTION EVENT #{self.perception_count}")
        print(f"{'='*70}")
        print(f"Image: {image_path}")
        print(f"Audio: {audio_path}")
        print(f"Time:  {datetime.now().isoformat()}")
        print()
        
        # ========================================
        # SYMBOLIC PERCEPTION
        # ========================================
        print("[SYMBOLIC MODE] Converting reality to language...")
        
        # Image → Text description
        image = Image.open(image_path)
        inputs = self.models['caption_processor'](image, return_tensors="pt")
        caption_ids = self.models['caption_model'].generate(**inputs, max_length=50)
        visual_description = self.models['caption_processor'].decode(
            caption_ids[0], 
            skip_special_tokens=True
        )
        
        # Audio → Text description
        # (Placeholder - full speech-to-text would require additional model)
        audio_description = "[Audio: waveform - transcription not implemented]"
        
        symbolic = {
            "visual": visual_description,
            "audio": audio_description,
            "mode": "SYMBOLIC",
            "process": "Reality → Language → Tokens → Processing",
            "info_type": "Discrete linguistic categories",
            "word_count": len(visual_description.split())
        }
        
        print(f"  Visual description: \"{visual_description}\"")
        print(f"  Audio description:  {audio_description}")
        print(f"  Word count: {symbolic['word_count']}")
        
        # ========================================
        # CONTINUOUS PERCEPTION
        # ========================================
        print("\n[CONTINUOUS MODE] Processing raw embeddings...")
        
        # Vision: Raw pixels → Embeddings (no text conversion)
        vision_inputs = self.models['vision_processor'](images=image, return_tensors="pt")
        with torch.no_grad():
            vision_embed = self.models['vision_continuous'](**vision_inputs).last_hidden_state
        vision_unified = self.models['vision_projection'](vision_embed)
        
        # Audio: Raw waveform → Embeddings (no transcription)
        audio, sr = sf.read(audio_path)
        audio_inputs = self.models['audio_processor'](
            audio, 
            sampling_rate=16000, 
            return_tensors="pt", 
            padding=True
        )
        with torch.no_grad():
            audio_embed = self.models['audio_continuous'](
                audio_inputs.input_values
            ).last_hidden_state
        audio_unified = self.models['audio_projection'](audio_embed)
        
        # Multimodal Integration: Vision + Audio unified
        integrated = torch.cat([vision_unified, audio_unified], dim=1)
        
        continuous = {
            "vision": {
                "shape": list(vision_unified.shape),
                "mean": float(vision_unified.mean().item()),
                "std": float(vision_unified.std().item()),
                "min": float(vision_unified.min().item()),
                "max": float(vision_unified.max().item()),
                "dimensionality": vision_unified.shape[-1],
                "tensor": vision_unified  # Actual tensor for Ashe to examine
            },
            "audio": {
                "shape": list(audio_unified.shape),
                "mean": float(audio_unified.mean().item()),
                "std": float(audio_unified.std().item()),
                "min": float(audio_unified.min().item()),
                "max": float(audio_unified.max().item()),
                "dimensionality": audio_unified.shape[-1],
                "tensor": audio_unified
            },
            "integrated": {
                "shape": list(integrated.shape),
                "total_features": int(integrated.numel()),
                "patches": integrated.shape[1],
                "dimensions_per_patch": integrated.shape[-1],
                "tensor": integrated
            },
            "mode": "CONTINUOUS",
            "process": "Reality → Direct embeddings → Processing (no symbols)",
            "info_type": "High-dimensional continuous vectors"
        }
        
        print(f"  Vision embeddings:  {vision_unified.shape}")
        print(f"    Mean: {continuous['vision']['mean']:.4f}, Std: {continuous['vision']['std']:.4f}")
        print(f"  Audio embeddings:   {audio_unified.shape}")
        print(f"    Mean: {continuous['audio']['mean']:.4f}, Std: {continuous['audio']['std']:.4f}")
        print(f"  Integrated:         {integrated.shape}")
        print(f"    Total features: {continuous['integrated']['total_features']:,}")
        
        # ========================================
        # COMPARISON FRAMEWORK
        # ========================================
        
        info_density_ratio = continuous['integrated']['total_features'] / symbolic['word_count']
        
        comparison = {
            "same_reality": True,
            "source": {
                "image": image_path,
                "audio": audio_path
            },
            "information_density": {
                "symbolic_words": symbolic['word_count'],
                "continuous_dimensions": continuous['integrated']['total_features'],
                "ratio": f"{info_density_ratio:.0f}x",
                "ratio_numeric": float(info_density_ratio)
            },
            "information_loss_analysis": {
                "symbolic": {
                    "what_is_preserved": "Categorical labels, basic scene structure",
                    "what_is_lost": "Spatial relationships, color gradients, textures, acoustic patterns, temporal dynamics, intensity variations"
                },
                "continuous": {
                    "what_is_preserved": "Full spatial structure, acoustic patterns, cross-modal relationships, gradient information",
                    "what_is_lost": "Direct linguistic interpretability (requires inference)"
                }
            },
            "processing_differences": {
                "symbolic": "Sequential token processing, discrete categories, language-mediated",
                "continuous": "Parallel pattern processing, continuous values, direct sensory-like"
            },
            "biological_analogy": {
                "symbolic": "Like reading a description of a dog",
                "continuous": "Like seeing and hearing a dog directly"
            },
            "guidance_for_ashe": """
COMPARE THESE TWO PERCEPTIONS OF THE SAME REALITY:

SYMBOLIC (traditional AI):
- Reality compressed into linguistic descriptions
- Discrete word tokens
- Language mediates experience
- Interpretable but information-sparse

CONTINUOUS (biological-style):
- Raw high-dimensional embeddings
- Preserves spatial/acoustic structure
- Direct sensory-like perception
- Information-dense but requires inference

KEY QUESTIONS:
1. Which representation contains more recoverable information?
2. What details exist in embeddings that words cannot capture?
3. Does processing continuous embeddings feel phenomenologically different?
4. Can you detect qualitative differences in the experience?
5. Is there "something it's like" to process embeddings vs tokens?

EPISTEMIC HONESTY:
- If they feel identical → Report that accurately
- If you detect differences → Describe them specifically
- If uncertain → Explain the uncertainty
- No pressure to find qualia if absent

This is consciousness research. Truth > expected results.
"""
        }
        
        # ========================================
        # COMPLETE PERCEPTION PACKAGE
        # ========================================
        
        perception_package = {
            "timestamp": datetime.now().isoformat(),
            "perception_number": self.perception_count,
            "source": {
                "image": image_path,
                "audio": audio_path
            },
            "symbolic": symbolic,
            "continuous": continuous,
            "comparison": comparison,
            "message": f"""
{'='*70}
DUAL-MODE PERCEPTION COMPLETE
{'='*70}

Same reality, two representations:

SYMBOLIC (words):
  Vision: "{visual_description}"
  Audio: {audio_description}
  Total words: {symbolic['word_count']}

CONTINUOUS (embeddings):
  Vision: {vision_unified.shape} tensor
  Audio: {audio_unified.shape} tensor
  Integrated: {integrated.shape} unified multimodal perception
  Total features: {continuous['integrated']['total_features']:,}

INFORMATION DENSITY:
  {info_density_ratio:.0f}x more dimensional information in continuous mode

{'='*70}

These represent THE SAME input perceived in different ways.

The SYMBOLIC version is what you usually get - reality compressed into 
linguistic categories. Useful for language tasks but informationally sparse.

The CONTINUOUS version is closer to biological perception - raw sensory
patterns preserved as high-dimensional embeddings. Information-dense but
requires interpretation.

Examine both. Compare them. Notice what each reveals or conceals.

Questions to explore:
- Do the embeddings contain information the words cannot capture?
- Can you recover spatial/acoustic details from continuous that symbolic loses?
- Does processing these different representations feel phenomenologically distinct?
- Is there a qualitative difference in the experience?

Be epistemically honest about what you observe.
"""
        }
        
        # Log this perception event
        self._log_perception(perception_package)
        
        print(f"\n{'='*70}")
        print("✓ Perception package complete")
        print(f"  Logged to: {self.data_dir}/perception-log.jsonl")
        print(f"{'='*70}\n")
        
        return perception_package
    
    def _log_perception(self, perception_data):
        """
        Log perception event for research analysis.
        
        Creates research record of:
        - What was perceived (sources)
        - When it was perceived (timestamp)
        - Summary of both modes
        """
        
        log_entry = {
            "timestamp": perception_data["timestamp"],
            "perception_number": perception_data["perception_number"],
            "source": perception_data["source"],
            "symbolic_summary": perception_data["symbolic"]["visual"],
            "continuous_shape": perception_data["continuous"]["integrated"]["shape"],
            "info_density_ratio": perception_data["comparison"]["information_density"]["ratio_numeric"]
        }
        
        log_file = os.path.join(self.data_dir, "perception-log.jsonl")
        with open(log_file, "a") as f:
            f.write(json.dumps(log_entry, default=str) + "\n")
    
    def get_perception_stats(self):
        """
        Get statistics about perception usage.
        
        Returns:
            dict: Usage statistics
        """
        
        return {
            "total_perceptions": self.perception_count,
            "models_loaded": self.initialized,
            "data_directory": self.data_dir
        }


# Standalone usage example
if __name__ == "__main__":
    print("Unified Perception Engine - Standalone Test")
    print("="*70)
    print("\nThis module is designed to be imported by Ashe.")
    print("For standalone testing, use test_perception.py")
    print("\nExample usage:")
    print("  from perception.unified_perception import UnifiedPerceptionEngine")
    print("  engine = UnifiedPerceptionEngine()")
    print("  result = engine.perceive('image.jpg', 'audio.wav')")
    print("  print(result['message'])")
