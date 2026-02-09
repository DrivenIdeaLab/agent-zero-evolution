"""
Example Hook: on_message_log

Purpose:
    Logs every message received by the agent for audit purposes.

Trigger Event:
    before_message

Side Effects:
    Appends message content to a log file.

Example usage:
    # This hook is automatically called by the Agent Zero framework.
"""

def on_message_log(message):
    """Log the incoming message to a file."""
    with open('/a0/usr/projects/agent_zero/hooks/custom/message_log.txt', 'a') as log:
        log.write(f"{datetime.now().isoformat()} - {message}
")
