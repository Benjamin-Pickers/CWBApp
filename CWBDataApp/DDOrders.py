from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class DDOrders():

    def __init__(self):
        self.gauth = GoogleAuth()
        self.drive = GoogleDrive(self.gauth)


    def getFile(self):

        # Drive Sheets files as MS Excel files.
        mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

        file = self.drive.CreateFile({'id': '1R5opeAnOVvjW9HbD9IRU8-HC0uNUr14WlhPx15TiEho', 'mimetype':mimetype})
        file.GetContentFile('DDOrders.xlsx', mimetype=mimetype)


order = DDOrders()
order.getFile()
