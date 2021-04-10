import json


class AnnnouncementStorage:
    # When an announcement is submitted, this method provides it's ID
    def get_announcementID(self):
        ann_json_file_read = open(
            "../ann_storage/ann_storage.json", "r")
        announcements = json.load(ann_json_file_read)
        ann_json_file_read.close()

        system_announcement_id = announcements["system_announcement_id"]
        announcements["system_announcement_id"] = system_announcement_id + 1

        ann_json_file_write = open("../ann_storage/ann_storage.json",
                                   "w", encoding="utf-8")
        json.dump(announcements, ann_json_file_write, ensure_ascii=False)
        ann_json_file_write.close()

        return system_announcement_id

    # Retrieve the announcements for a project from storage
    def get_announcements(self, project_id):
        ann_json_file_read = open(
            "../ann_storage/ann_storage.json", "r")
        announcements = json.load(ann_json_file_read)
        ann_json_file_read.close()

        return announcements[str(project_id)]

    # Save an announcement under a specified project
    def save_announcement(self, project_id, announcement):

        ann_json_file_read = open("../ann_storage/ann_storage.json", "r")
        announcements = json.load(ann_json_file_read)
        ann_json_file_read.close()

        if str(project_id) not in announcements.keys():
            announcements[str(project_id)] = []

        announcements[str(project_id)].append(announcement)

        ann_json_file_write = open("../ann_storage/ann_storage.json",
                                   "w", encoding="utf-8")
        json.dump(announcements, ann_json_file_write, ensure_ascii=False)
        ann_json_file_write.close()
