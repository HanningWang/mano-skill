BASE_URL = "http://127.0.0.1:8000"
# Keep existing window/animation/text configurations unchanged
WINDOW_CONFIG = {
    "WIDTH": 320,
    "MIN_HEIGHT": 240,
    "MAX_HEIGHT": 400,
    "MARGIN": 18,
    "ALPHA": 0.92,
    "BG_COLOR": "#1e1e1e",
    "LOG_BG_COLOR": "#000000",
    "TEXT_COLOR": "#eaeaea",
    "TITLE_FONT_SIZE": 12,
    "LOG_FONT_SIZE": 11,
    "CORNER_RADIUS": 14,
    "BUTTON_RADIUS": 10,
    "BUTTON_HEIGHT": 32,
    "STOP_BTN_COLOR": "#ff5050",
    "STOP_BTN_HOVER": "#ff7070"
}

ANIMATION_CONFIG = {
    "BLINK_INTERVAL": 500,
    "POLL_INTERVAL": 200,
    "STOP_DELAY": 1000,
    "HEIGHT_ADJUST_DELAY": 10
}

TEXT_CONSTANTS = {
    "WINDOW_TITLE": "VLA Task Monitor",
    "RUNNING_TEXT": "Running",
    "DONE_TEXT": "Done ✅",
    "STOPPED_TEXT": "Stopped ⏹",
    "ERROR_TEXT": "Error ❌",
    "STEP_PREFIX": "Step: ",
    "TASK_PREFIX": "Task: ",
    "STOP_BUTTON_TEXT": "Stop",
    "STOPPING_BUTTON_TEXT": "Stopping…",
    "CLOSE_BUTTON_TEXT": "Close",
    "ACTION_PREFIX": "Action: ",
    "REASONING_PREFIX": "Reasoning: "
}

TASK_STATUS = {
    "RUNNING": "running",
    "COMPLETED": "completed",
    "STOPPED": "stopped",
    "ERROR": "error",
    "CALL_USER": "call_user"  # New: requires user intervention status
}

# ========== New: Automation Business Configuration ==========
AUTOMATION_CONFIG = {
    "BASE_URL": "http://127.0.0.1:8000",
    "DEVICE_FILE": "~/.myapp_device_id",
    "SCREEN_SCALE_WIDTH": 1280,   # Server screenshot width
    "SCREEN_SCALE_HEIGHT": 720,  # Server screenshot height
    "SCROLL_MULTIPLIER": 5,      # Scroll multiplier
    "ACTION_DELAY": 2,           # Delay after action (seconds)
    "APP_START_DELAY": 1,        # App start delay (seconds)
    "MOUSE_MOVE_STEPS_PER_SEC": 30,  # Mouse movement smooth steps
    "MOUSE_CLICK_DELAY": 0.1,    # Delay before click
    "HOTKEY_DELAY": 0.08,        # Hotkey delay
    "SESSION_TIMEOUT": 60,       # Session request timeout (seconds)
    "STEP_TIMEOUT": 600,         # Step request timeout (seconds)
    "CLOSE_SESSION_TIMEOUT": 30  # Close session timeout (seconds)
}