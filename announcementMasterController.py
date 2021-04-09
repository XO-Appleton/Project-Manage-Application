from announcementStorage import AnnnouncementStorage
from announcement import Announcement
from announcementBoard import AnnouncementBoard
from announcementSubmissionScreen import AnnouncementSubmissionScreen
from User import User


class AnnouncementMasterController:
    def __init__(self, project_id, user):
        self.project_id = project_id
        self.user = user
        self.active = True

    def create_announcement(self):
        # looks for user input for if they want to go to announcement submission screen
        create_announcement = str(
            input("Would you like to create an announcement? Reply 'Yes' to create an announcement, 'No' to exit announcement screen. \n"))

        if create_announcement == "Yes" or create_announcement == "yes" or create_announcement == "y":
            AnnouncementSubmissionScreen(
                self.project_id, self.user).display_form(self.project_id)
        else:
            self.exit_announcement()

    def exit_announcement(self):
        print("Exiting announcement branch")
        self.active = False

    def main(self):

        while(self.active):
            announcements_list = AnnnouncementStorage().get_announcements(self.project_id)
            AnnouncementBoard().display_announcements(announcements_list)
            self.create_announcement()
