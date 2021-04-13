class Announcement:
    def __init__(self, announcement_id, project_id, creator, date_created, title, body):
        self.announcement_id = announcement_id
        self.project_id = project_id
        self.creator = creator
        self.date_created = date_created
        self.title = title
        self.body = body
        self.announcement_dict = {
            "announcement_id": announcement_id, "project_id": project_id, "creator": creator, "date_created": date_created, "title": title, "body": body}
