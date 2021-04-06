from datetime import date
from announcementStorage import AnnnouncementStorage
from announcement import Announcement


class AnnouncementSubmissionScreen:

    def display_form(self):
        print("Announcement Submission \n")
        project_id = int(input("Project ID? "))
        creator = str(input("Created by? "))
        date_created = str(date.today())
        title = str(input("Title of announcement? \n"))
        body = str(input("Body of announcement? \n"))
        confirm = str(
            input("Would you like to post this announcement? Yes or No \n"))

        if confirm == "Yes" or confirm == "yes" or confirm == "y":
            announcement_id = AnnnouncementStorage().get_announcementID()
            announcement = self.submit_announcement(
                announcement_id, project_id, creator, date_created, title, body)
            AnnnouncementStorage().save_announcement(
                project_id, announcement.announcement_dict)
            print("Announcement submitted! \n")

        else:
            new_confirm = str(input(
                "Announcement not submitted. Would you like to submit a new announcement? Yes or No \n"))
            if new_confirm == "Yes" or new_confirm == "yes" or new_confirm == "y":
                self.display_form()
            else:
                print("Thank you!")
                # take user back to announcement board

    def submit_announcement(self, announcement_id, project_id, creator, date_created, title, body):
        return Announcement(announcement_id, project_id,
                            creator, date_created, title, body)


AnnouncementSubmissionScreen().display_form()
# currently announcements are being submitted. need ability to increase project ID counter once submitted
