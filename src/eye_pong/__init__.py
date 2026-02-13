"""Eye Controlled Pong game using EyeTrax"""

__version__ = "0.1.0"

from .game import Pong
from .utils import DwellDetector
from .gaze_control import get_gaze_estimator, get_smoother

__all__ = [
    "Pong",
    "DwellDetector",
    "get_gaze_estimator",
    "get_smoother"
]