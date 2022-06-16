from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
import os


#WORK IN PROGRESS
#Designer Deck integrated order sheets that update automatically
#DD has the most retarded excel order sheets ever
class OrdersDD():

    def __init__(self):
        self.gauth = GoogleAuth()
        self.drive = GoogleDrive(self.gauth)


    def getDDOrders(self, allProfiles, allColours, machineNum):

        # Drive Sheets files as MS Excel files.
        mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

        id='1R5opeAnOVvjW9HbD9IRU8-HC0uNUr14WlhPx15TiEho'

        #Depending on what machine the orders for change the google sheet id
        if machineNum == 1:
            id = '1DxwxjARN_GWzkq5XB7sLikTis74AElFnXmkczX6SVmo'
        elif machineNum == 2:
            id = '1R5opeAnOVvjW9HbD9IRU8-HC0uNUr14WlhPx15TiEho'
        elif machineNum == 3:
            id= '1W2HNurjM2WmsohwmC1j7M-IZY-eAl5tQ1gjnJp_EM9M'

        file = self.drive.CreateFile({'id': id, 'mimetype':mimetype})
        file.GetContentFile('DDOrders.xlsx', mimetype=mimetype)

        df = pd.read_excel(r'./DDOrders.xlsx')

        #Fill in profile value based on value above
        df['Profile'].fillna(method='ffill', inplace=True)

        #Only keep the columns we need
        df = df[['Colour', 'Tot.Units(4ft)', 'Filled Units(4ft)', 'Profile']]

        OrdersDict = {}

        for index, row in df.iterrows():
            for profile in allProfiles:
                for colour in allColours:

                    if (row['Profile'] == profile.productname and row['Colour'] == colour.colour):

                        #Fill empty values with 0
                        if pd.isna(row['Filled Units(4ft)']):
                            row['Filled Units(4ft)'] = 0
                        if pd.isna(row['Tot.Units(4ft)']):
                            row['Tot.Units(4ft)'] = 0

                        if str(""+profile.productname+"_"+colour.colour) in OrdersDict:
                            OrdersDict[str(""+profile.productname+"_"+colour.colour)][0] += row['Tot.Units(4ft)']
                            OrdersDict[str(""+profile.productname+"_"+colour.colour)][1] += row['Filled Units(4ft)']
                        else:

                            list = [row['Tot.Units(4ft)'], row['Filled Units(4ft)']]
                            OrdersDict[str(""+profile.productname+"_"+colour.colour)] = list

        #Remove Created Orderexcel sheet
        os.remove(r'./DDOrders.xlsx')
        print(OrdersDict)
        return OrdersDict
