from utils.file_handler import FileHandler

f_handler = FileHandler()

input_readme = f_handler.read_file("utils/samples/sample_input_readme.md")
example_readme = f_handler.read_file("utils/samples/sample_example_project.md")
example_output = {
    "id": "attendance-tracker-001",
    "projectHeroImg": "https://example.com/hero-image.png",
    "projectTitle": "Smart Attendance Tracker",
    "readTimeInMins": 10,
    "overview": {
        "textContents": [
            {
                "content": "The Smart Attendance Tracker helps automate attendance using Bluetooth beacons and geofencing. It provides real-time dashboards and notifications for attendance management. The following is the timeline for the project",
                "imgUrl": "https://storage.googleapis.com/gdg-fisk-assets/images/7faca2a38b3f44a9970c099bdf6df0b5.png",
            }
        ]
    },
    "problemStatement": "Manual attendance tracking is time-consuming and prone to errors. This system automates attendance and provides analytics.",
    "features": {
        "textContents": [
            {
                "content": "User Management, Beacon Detection, Geofencing, Attendance Recording, Analytics, Notifications, Admin Module."
            }
        ]
    },
    "demo": {
        "title": "Smart Attendance Demo",
        "imgUrl": "https://example.com/demo-thumbnail.png",
        "videoUrl": "https://example.com/demo-video.mp4",
        "genres": ["Educational", "Technology"]
    },
    "relevantLinks": [
        "https://example.com/docs",
        "https://example.com/tutorials"
    ],
    "author": "Anonymous"
}


