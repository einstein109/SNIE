from plyer import notification

# Function to send a desktop notification
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # You can add an icon here, set to None for now
        timeout=10  # Notification stays for 10 seconds
    )

# Example usage
if __name__ == "__main__":
    send_notification("Einstein", "This is your desktop notification!")

if __name__ == "__main__":
    send_notification("REMINDER", "This is your desktop notification!")


