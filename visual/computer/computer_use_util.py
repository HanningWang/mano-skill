import base64
import os
import uuid
from typing import Any, Dict, Optional

import mss
import mss.tools
from pynput import mouse

from visual.config.visual_config import AUTOMATION_CONFIG

def screenshot_to_bytes():
    """Capture primary screen and return PNG bytes"""
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        return mss.tools.to_png(screenshot.rgb, screenshot.size)

def b64_png(png_bytes: bytes) -> str:
    """Encode PNG bytes to base64 string"""
    return base64.b64encode(png_bytes).decode("utf-8")

def make_tool_result(tool_use_id: str, ok: bool, message: str,
                     include_screenshot: bool, screenshot_bytes: Optional[bytes],
                     meta: Optional[Dict[str, Any]]=None):
    """Build tool result"""
    tr: Dict[str, Any] = {
        "tool_use_id": tool_use_id,
        "status": "success" if ok else "error",
        "output": message,
        "error": None if ok else message,
        "include_screenshot": bool(include_screenshot),
        "meta": meta or {},
    }
    if include_screenshot and screenshot_bytes:
        tr["screenshot_b64"] = b64_png(screenshot_bytes)
    return tr

def focus_on_primary_screen():
    """Focus mouse on primary screen center"""
    with mss.mss() as sct:
        primary = sct.monitors[1]
        mouse_controller = mouse.Controller()
        mouse_controller.position = (
            primary["left"] + primary["width"] // 2,
            primary["top"] + primary["height"] // 2
        )

def get_or_create_device_id():
    """Get or create device ID"""
    device_file = os.path.expanduser(AUTOMATION_CONFIG["DEVICE_FILE"])
    if os.path.exists(device_file):
        with open(device_file, "r") as f:
            return f.read().strip()

    device_id = str(uuid.uuid4())
    with open(device_file, "w") as f:
        f.write(device_id)
    return device_id