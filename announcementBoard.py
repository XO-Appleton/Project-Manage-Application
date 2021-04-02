from announcementStorage import AnnnouncementStorage


class AnnouncementBoard:

    def display_announcements(self, announcements):
        announcement_number = 1
        print("Announcements for project: \n")
        # takes the list of announcements and displays them
        for announcement in announcements:
            print(str(announcement_number) + ") Announcement posted by " + announcement["creator"] +
                  " on " + announcement["date_created"] + ":")
            print("Title: \n" + announcement["title"] + "\n")
            print("Body: \n" + announcement["body"] + "\n")
            announcement_number += 1


x = AnnnouncementStorage()
y = x.get_announcements(2)
AnnouncementBoard().display_announcements(y)
