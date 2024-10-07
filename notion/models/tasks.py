import reflex as rx
from notion.constant import Icons

class Tasks(rx.Base):
    title: str
    description: str
    status: bool
    icon: Icons

    def dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "icon": self.icon,
        }

