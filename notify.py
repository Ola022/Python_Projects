from win10toast import ToastNotifier
import datetime

""" [ pip install win10toast ]"""
data = datetime.datetime.now()
data = str(data)
#toaster = ToastNotifier()
#toaster.show_toast("Hello World!!!", "Python is 10 seconds awsm!", duration=10)
#toaster.show_toast("Example two", "Once you start coding in Python you'll hate other languages")


from winotify import Notification, audio

# Create a notification instance
toast = Notification(app_id="Python Notification",
                     title="Test Notification",
                     msg="This is a test notification from winotify",
                     duration="long")

# Optionally, set an icon for the notification
# toast.set_icon("path_to_icon.ico")

# Optionally, add sound to the notification
toast.set_audio(audio.Default, loop=False)
# Send the notification
toast.show()


from plyer import notification

# Show a notification
notification.notify(
    title="Test Notification",
    message="This is a test notification from plyer",
    timeout=20
)




