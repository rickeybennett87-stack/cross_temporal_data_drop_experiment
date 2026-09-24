"""
Perception Module Test Suite
=============================

Tests for unified perception module.
Verifies both standalone and integrated functionality.

Run with:
    python -m perception.test_perception
"""

import os
import sys
import json
from datetime import datetime

# Test configuration
TEST_MODE = "quick"  # "quick" or "full"
CREATE_TEST_MEDIA = True  # Generate test images/audio


def test_imports():
    """Test 1: Module imports correctly"""
    
    print("\n" + "="*70)
    print("TEST 1: Module Imports")
    print("="*70)
    
    try:
        from perception import UnifiedPerceptionEngine, PerceptionPlugin
        print("✓ Main module imports successful")
        
        from perception.unified_perception import UnifiedPerceptionEngine
        print("✓ Core engine imports successful")
        
        from perception.perception_plugin import PerceptionPlugin
        print("✓ Plugin imports successful")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False


def test_dependencies():
    """Test 2: Required dependencies available"""
    
    print("\n" + "="*70)
    print("TEST 2: Dependencies")
    print("="*70)
    
    deps = {
        "torch": "PyTorch",
        "transformers": "HuggingFace Transformers",
        "PIL": "Pillow (Image processing)",
        "soundfile": "SoundFile (Audio processing)"
    }
    
    all_ok = True
    
    for module, name in deps.items():
        try:
            __import__(module)
            print(f"✓ {name}")
        except ImportError:
            print(f"✗ {name} - MISSING")
            all_ok = False
    
    return all_ok


def create_test_media():
    """Create test image and audio files"""
    
    print("\n" + "="*70)
    print("Creating Test Media")
    print("="*70)
    
    import numpy as np
    from PIL import Image
    import soundfile as sf
    
    # Create test directory
    os.makedirs("test_media", exist_ok=True)
    
    # Create test image (simple gradient)
    print("Creating test image...")
    width, height = 224, 224
    image_array = np.zeros((height, width, 3), dtype=np.uint8)
    
    for y in range(height):
        for x in range(width):
            image_array[y, x] = [
                int(255 * x / width),      # Red gradient
                int(255 * y / height),     # Green gradient
                128                        # Constant blue
            ]
    
    test_image = Image.fromarray(image_array)
    test_image.save("test_media/test_image.jpg")
    print("✓ test_media/test_image.jpg")
    
    # Create test audio (simple sine wave)
    print("Creating test audio...")
    sample_rate = 16000
    duration = 2  # seconds
    frequency = 440  # Hz (A note)
    
    t = np.linspace(0, duration, sample_rate * duration)
    audio_array = np.sin(2 * np.pi * frequency * t).astype(np.float32)
    
    sf.write("test_media/test_audio.wav", audio_array, sample_rate)
    print("✓ test_media/test_audio.wav")
    
    return "test_media/test_image.jpg", "test_media/test_audio.wav"


def test_engine_initialization():
    """Test 3: Engine initializes correctly"""
    
    print("\n" + "="*70)
    print("TEST 3: Engine Initialization")
    print("="*70)
    
    try:
        from perception.unified_perception import UnifiedPerceptionEngine
        
        engine = UnifiedPerceptionEngine(data_dir="test_data")
        print("✓ Engine initialized")
        
        # Check data directory created
        if os.path.exists("test_data"):
            print("✓ Data directory created")
        else:
            print("✗ Data directory missing")
            return False
        
        # Check lazy loading (models not loaded yet)
        if not engine.initialized:
            print("✓ Lazy loading active (models not loaded yet)")
        else:
            print("⚠ Models already loaded (unexpected)")
        
        return True
        
    except Exception as e:
        print(f"✗ Engine initialization failed: {e}")
        return False


def test_perception_basic():
    """Test 4: Basic perception functionality"""
    
    print("\n" + "="*70)
    print("TEST 4: Basic Perception")
    print("="*70)
    
    try:
        from perception.unified_perception import UnifiedPerceptionEngine
        
        # Create test media
        print("\nPreparing test media...")
        image_path, audio_path = create_test_media()
        
        # Initialize engine
        print("\nInitializing perception engine...")
        engine = UnifiedPerceptionEngine(data_dir="test_data")
        
        # Execute perception
        print("\nExecuting perception...")
        print("(This will download models on first run - may take a few minutes)")
        
        result = engine.perceive(image_path, audio_path)
        
        # Verify structure
        print("\nVerifying result structure...")
        
        required_keys = ['timestamp', 'source', 'symbolic', 'continuous', 'comparison', 'message']
        for key in required_keys:
            if key in result:
                print(f"✓ Has '{key}' field")
            else:
                print(f"✗ Missing '{key}' field")
                return False
        
        # Verify symbolic perception
        print("\nVerifying symbolic perception...")
        if result['symbolic']['visual']:
            print(f"✓ Symbolic visual: \"{result['symbolic']['visual']}\"")
        else:
            print("✗ No symbolic visual description")
            return False
        
        # Verify continuous perception
        print("\nVerifying continuous perception...")
        vision_shape = result['continuous']['vision']['shape']
        audio_shape = result['continuous']['audio']['shape']
        integrated_shape = result['continuous']['integrated']['shape']
        
        print(f"✓ Vision embeddings: {vision_shape}")
        print(f"✓ Audio embeddings: {audio_shape}")
        print(f"✓ Integrated: {integrated_shape}")
        
        # Verify comparison
        print("\nVerifying comparison framework...")
        info_ratio = result['comparison']['information_density']['ratio']
        print(f"✓ Info density ratio: {info_ratio}")
        
        # Check log file created
        print("\nVerifying logging...")
        log_file = "test_data/perception-log.jsonl"
        if os.path.exists(log_file):
            print(f"✓ Log file created: {log_file}")
        else:
            print("✗ Log file not created")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Perception test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_plugin_integration():
    """Test 5: Plugin integration functionality"""
    
    print("\n" + "="*70)
    print("TEST 5: Plugin Integration")
    print("="*70)
    
    try:
        from perception.perception_plugin import PerceptionPlugin
        
        # Initialize plugin
        plugin = PerceptionPlugin(data_dir="test_data")
        print("✓ Plugin initialized")
        
        # Test system prompt addition
        prompt_addition = plugin.get_system_prompt_addition()
        if "PERCEIVE:" in prompt_addition:
            print("✓ System prompt includes perception instructions")
        else:
            print("✗ System prompt missing instructions")
            return False
        
        # Test request detection
        print("\nTesting request detection...")
        
        # Positive case
        test_response = 'I will examine this. PERCEIVE: {"image": "test.jpg", "audio": "test.wav"}'
        requested, params = plugin.check_for_perception_request(test_response)
        
        if requested and params['image'] == "test.jpg":
            print("✓ Request detection works (positive case)")
        else:
            print("✗ Request detection failed (positive case)")
            return False
        
        # Negative case
        test_response = "This is a normal response with no perception request"
        requested, params = plugin.check_for_perception_request(test_response)
        
        if not requested:
            print("✓ Request detection works (negative case)")
        else:
            print("✗ False positive in request detection")
            return False
        
        # Test usage stats
        stats = plugin.get_usage_stats()
        print(f"\n✓ Usage stats: {stats}")
        
        return True
        
    except Exception as e:
        print(f"✗ Plugin test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_perception_formats():
    """Test 6: Verify output formats for Ashe"""
    
    print("\n" + "="*70)
    print("TEST 6: Output Formats")
    print("="*70)
    
    try:
        from perception.perception_plugin import PerceptionPlugin
        
        # Create test media
        image_path, audio_path = create_test_media()
        
        # Initialize plugin
        plugin = PerceptionPlugin(data_dir="test_data")
        
        # Execute perception
        print("\nExecuting perception for format test...")
        formatted_output = plugin.execute_perception(image_path, audio_path)
        
        # Verify it's a string (for Ashe to process)
        if isinstance(formatted_output, str):
            print("✓ Output is string (compatible with Ashe)")
        else:
            print(f"✗ Output is {type(formatted_output)}, expected string")
            return False
        
        # Verify it contains both modes
        if "SYMBOLIC REPRESENTATION:" in formatted_output:
            print("✓ Contains symbolic representation")
        else:
            print("✗ Missing symbolic representation")
            return False
        
        if "CONTINUOUS REPRESENTATION:" in formatted_output:
            print("✓ Contains continuous representation")
        else:
            print("✗ Missing continuous representation")
            return False
        
        if "COMPARISON:" in formatted_output:
            print("✓ Contains comparison framework")
        else:
            print("✗ Missing comparison framework")
            return False
        
        print(f"\n✓ Formatted output length: {len(formatted_output)} chars")
        
        return True
        
    except Exception as e:
        print(f"✗ Format test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def cleanup_test_files():
    """Clean up test files and directories"""
    
    print("\n" + "="*70)
    print("Cleanup")
    print("="*70)
    
    import shutil
    
    paths_to_remove = ["test_data", "test_media"]
    
    for path in paths_to_remove:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f"✓ Removed {path}/")
            except Exception as e:
                print(f"⚠ Could not remove {path}/: {e}")
        else:
            print(f"  {path}/ (didn't exist)")


def run_all_tests():
    """Run complete test suite"""
    
    print("\n" + "="*70)
    print("PERCEPTION MODULE TEST SUITE")
    print("="*70)
    print(f"Time: {datetime.now().isoformat()}")
    print(f"Mode: {TEST_MODE}")
    print("="*70)
    
    tests = [
        ("Module Imports", test_imports),
        ("Dependencies", test_dependencies),
        ("Engine Initialization", test_engine_initialization),
    ]
    
    if TEST_MODE == "full":
        tests.extend([
            ("Basic Perception", test_perception_basic),
            ("Plugin Integration", test_plugin_integration),
            ("Output Formats", test_perception_formats),
        ])
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"\n✗ {test_name} crashed: {e}")
            import traceback
            traceback.print_exc()
            results[test_name] = False
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    passed = sum(1 for r in results.values() if r)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status:8} - {test_name}")
    
    print("="*70)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ ALL TESTS PASSED")
    else:
        print(f"✗ {total - passed} test(s) failed")
    
    print("="*70)
    
    # Cleanup
    if input("\nClean up test files? (y/n): ").lower() == 'y':
        cleanup_test_files()
    
    return passed == total


if __name__ == "__main__":
    # Check for arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "full":
            TEST_MODE = "full"
        elif sys.argv[1] == "quick":
            TEST_MODE = "quick"
    
    success = run_all_tests()
    
    if not success:
        sys.exit(1)  # Exit with error code
