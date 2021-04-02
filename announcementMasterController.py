from announcementStorage import AnnnouncementStorage
from announcement import Announcement


class AnnouncementMasterController:
    announcement_branch_active = False

    def create_announcement(self):
        self.announcement_branch_active = True

    def exit_announcement_branch(self):
        self.announcement_branch_active = False


announcementMaster = AnnouncementMasterController()
announcementMaster.create_announcement()
