"""
Unified Perception Module for Ashe
===================================

Modular addition to Ashe autonomous AI system.
Provides dual-mode perception: symbolic (tokenized) and continuous (embeddings).

This module is OPTIONAL - Ashe works without it.
When installed, Ashe can perceive images and audio in both traditional
and biological-style modes, comparing them to develop understanding.

Author: Rickey Jay Bennett II
Version: 1.0.0
License: MIT (or whatever Ashe uses)
"""

from .unified_perception import UnifiedPerceptionEngine
from .perception_plugin import PerceptionPlugin

__all__ = ['UnifiedPerceptionEngine', 'PerceptionPlugin']
__version__ = '1.0.0'
__author__ = 'Rickey Jay Bennett II'

# Module metadata
PERCEPTION_MODE_SYMBOLIC = "symbolic"
PERCEPTION_MODE_CONTINUOUS = "continuous"
PERCEPTION_MODE_UNIFIED = "unified"
