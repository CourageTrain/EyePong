"""Utility function for gaze-controlled Pong"""

import time

class DwellDetector:
    """
    Detects when a condition stays True for a threshold duration
    Useful for detecting sustained gaze
    :return
        True : once threshold ( edge trigger ) is crossed
    """
    def __init__(self, threshold:float = 0.5):
        self.threshold = threshold
        self._start_time = None
        self._triggered = False

    def update(self, condition: bool)-> bool:
        now = time.time()
        if condition:
            # Start or continue tracking
            if self._start_time is None:
                self._start_time = now
                return False
            elapsed = now - self._start_time
            if not self._triggered and elapsed >= self.threshold:
                self._triggered = True
                return True
            return False
        else:
            self._start_time = None
            self._triggered = False
            return False


    def reset(self):
        """Reset detector state"""
        self._start_time = None
        self._triggered = False