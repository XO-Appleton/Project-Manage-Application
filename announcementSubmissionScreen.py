from datetime import date
from announcementStorage import AnnnouncementStorage
from announcement import Announcement
from User import User

#from announcementMasterController import AnnouncementMasterController


class AnnouncementSubmissionScreen:
    # convert code to work with submission init - creator and project id should be from constructor
    def __init__(self, project_id, user):
        self.project_id = project_id
        self.user = user

    def display_form(self, project_id):
        print("\nANNOUNCEMENT SUBMISSION FORM: \n")
        # str(input("Created by? "))  # switch to accepting user
        creator = self.user.login_name
        date_created = str(date.today())
        title = str(input("Title of announcement? \n"))
        body = str(input("\nBody of announcement? \n"))
        confirm = str(
            input("\nWould you like to post this announcement? Yes or No \n"))

        if confirm == "Yes" or confirm == "yes" or confirm == "y":
            announcement_id = AnnnouncementStorage().get_announcementID()
            announcement = self.submit_announcement(
                announcement_id, project_id, creator, date_created, title, body)
            AnnnouncementStorage().save_announcement(
                project_id, announcement.announcement_dict)
            print("\nAnnouncement submitted! \n")

        else:
            new_confirm = str(input(
                "\nAnnouncement not submitted. Would you like to submit a new announcement? Yes or No \n"))
            if new_confirm == "Yes" or new_confirm == "yes" or new_confirm == "y":
                self.display_form()
            else:
                print("\nThank you!\n")

    def submit_announcement(self, announcement_id, project_id, creator, date_created, title, body):
        return Announcement(announcement_id, project_id,
                            creator, date_created, title, body)
