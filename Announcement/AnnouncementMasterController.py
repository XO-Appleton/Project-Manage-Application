from AnnouncementStorage import AnnouncementStorage
from Announcement import Announcement
from AnnouncementBoard import AnnouncementBoard
from AnnouncementSubmissionScreen import AnnouncementSubmissionScreen
from User import User


class AnnouncementMasterController:
    def __init__(self, project_id, user):
        # Keeps track of the current project ID
        self.project_id = project_id
        # Keeps track of the current user
        self.user = user
        # Keeps track if user is in announcement branch - switches to false when they are done
        self.active = True

    # Takes user to screen to create announcement
    def create_announcement(self):
        # Looks for user input for if they want to go to announcement submission screen
        create_announcement = str(
            input("Would you like to create an announcement? Reply 'Yes' to create an announcement, 'No' to exit announcement screen. \n"))
        # If user would like to create an announcement, displays the announcement submission form for the project
        if create_announcement == "Yes" or create_announcement == "yes" or create_announcement == "y":
            AnnouncementSubmissionScreen(
                self.project_id, self.user).display_form(self.project_id)
        # If user does not want to make an announcement, program leaves the announcement branch
        else:
            self.exit_announcement()

    # Exits user out of announcement branch
    def exit_announcement(self):
        print("Exiting announcement branch")
        self.active = False

    # Main function of master controller runs the announcement branch
    def main(self):
        while(self.active):
            announcements_list = AnnouncementStorage().get_announcements(self.project_id)
            AnnouncementBoard().display_announcements(announcements_list)
            self.create_announcement()
