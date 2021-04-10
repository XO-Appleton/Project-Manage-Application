from datetime import date
from announcementStorage import AnnnouncementStorage
from announcement import Announcement
from User import User


class AnnouncementSubmissionScreen:
    def __init__(self, project_id, user):
        # Keeps track of the current project ID
        self.project_id = project_id
        # Keeps track of the current user
        self.user = user

    # Displays the announcement submission form
    def display_form(self, project_id):
        # Announcement submission form includes the title and the body.
        # The creator, date created, and which project are attached by the class to the
        # submitted announcement.
        print("\nANNOUNCEMENT SUBMISSION FORM: \n")
        creator = self.user.login_name
        date_created = str(date.today())
        title = str(input("Title of announcement? \n"))
        body = str(input("\nBody of announcement? \n"))

        # If user confirms they would like to post the announcement, it will be put in storage
        confirm = str(
            input("\nWould you like to post this announcement? Yes or No \n"))

        if confirm == "Yes" or confirm == "yes" or confirm == "y":
            announcement_id = AnnnouncementStorage().get_announcementID()
            announcement = self.submit_announcement(
                announcement_id, project_id, creator, date_created, title, body)
            AnnnouncementStorage().save_announcement(
                project_id, announcement.announcement_dict)
            print("\nAnnouncement submitted! \n")

        # If user does not wish to submit the announcement that they filled the form for,
        # they have the option to return to the form to submit a new announcement
        # or to the announcement display board.
        else:
            new_confirm = str(input(
                "\nAnnouncement not submitted. Would you like to submit a new announcement? Yes or No \n"))
            if new_confirm == "Yes" or new_confirm == "yes" or new_confirm == "y":
                self.display_form(self.project_id)
            else:
                print("\nThank you!\n")

    # Returns an announcement object with the details provided by the form and the SubmissionScreen object
    def submit_announcement(self, announcement_id, project_id, creator, date_created, title, body):
        return Announcement(announcement_id, project_id,
                            creator, date_created, title, body)
