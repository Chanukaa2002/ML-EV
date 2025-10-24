from typing import Dict


def demo_driving_controller() -> Dict[str, str]:
    """Demo controller method for driving module.

    Returns a simple JSON-serializable dict indicating the controller is wired.
    """
    return {
        "module": "driving",
        "controller": "demo",
        "status": "ok",
        "message": "Driving controller demo is live",
    }
