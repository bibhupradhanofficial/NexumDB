"""
NexumDB AI Engine
Handles embedding generation, semantic caching, NL translation, and query optimization
"""

__version__ = "0.3.0"

from .optimizer import SemanticCache, QueryOptimizer
from .translator import NLTranslator
from .rl_agent import QLearningAgent

__all__ = ["SemanticCache", "QueryOptimizer", "NLTranslator", "QLearningAgent"]
