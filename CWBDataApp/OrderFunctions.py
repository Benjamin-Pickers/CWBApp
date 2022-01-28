from .models import Ordersheetmachine1, Ordersheetmachine2, Ordersheetmachine3, Productprofiles
from datetime import date, timedelta
import math

class OrderFunctions():

    def __init__(self):
        pass

    #Add a given number of business days to a date, we ignore weekends
    def addDate(self, startDate, numDays):
        currentDate = startDate

        while numDays > 0:
            currentDate += timedelta(days=1)
            weekday=currentDate.weekday()
            if weekday >= 5:
                continue
            else:
                numDays -= 1
        return currentDate

    #Helper method to rearrange the priority and dates of orders
    def deprioritize(self, priority, endDate, querySet):

        #Hold the enddate for the order with one higher priority
        prevEndDate = endDate

        for entry in querySet:
            if entry.priorityrank == priority:
                entry.projectedstartdate = endDate
                prevEndDate = self.addDate(endDate, math.ceil(entry.lengthofrunindays))
                entry.projectedenddate = prevEndDate
            else:

                entry.projectedstartdate = prevEndDate
                prevEndDate =  self.addDate(prevEndDate, math.ceil(entry.lengthofrunindays))
                entry.projectedenddate = prevEndDate
            entry.priorityrank += 1
            entry.save()


    #Helper method to update orders when product is shipped
    def updateOrderSent(self, order, numSkids, orderSheet):

        try:
            prod = Productprofiles.objects.get(pk=order.boardprofile)
            pcsSent = int(Decimal(prod.pcsperskid) * numSkids)

            order.pcssent += pcsSent
            order.pcsinventorized -= pcsSent
            order.save()


            if order.pcssent >= order.pcs:
                self.deletedOrder(order, orderSheet)
                order.delete()
            return ""
        except:
            return "Could not Update Order"


    #Given a Product and colour, find the Ordersheet that and order that needs that product
    #Return the specific order and ordersheet for that product
    def FindOrder(self, product, colour):
        dict = {}
        if Ordersheetmachine1.objects.filter(boardprofile=product, colour=colour).exists():
            dict['order'] = Ordersheetmachine1.objects.filter(boardprofile=product, colour=colour).order_by('priorityrank').first()
            dict['orderSheet'] = Ordersheetmachine1.objects.all()
        elif Ordersheetmachine2.objects.filter(boardprofile=product, colour=colour).exists():
            dict['order'] = Ordersheetmachine2.objects.filter(boardprofile=product, colour=colour).order_by('priorityrank').first()
            dict['orderSheet'] = Ordersheetmachine2.objects.all()
        elif Ordersheetmachine3.objects.filter(boardprofile=product, colour=colour).exists():
            dict['order'] = Ordersheetmachine3.objects.filter(boardprofile=product, colour=colour).order_by('priorityrank').first()
            dict['orderSheet'] = Ordersheetmachine3.objects.all()
        return dict

    #Update an orders inventorized pieces
    def UpdateOrderInventory(self, order, pcsinventorized, orderSheet):
        order.pcsinventorized += pcsinventorized
        order.pcsremaining -= pcsinventorized
        order.save()
        if order.pcs <= 0:
            self.deletedOrder(order, orderSheet)
            order.delete()

    #Reorder orders when an order needs to be deleted
    def deletedOrder(self, order, orderSheet):
        endDate = date.today()
        if order.priorityrank != 1:
            higherOrder = orderSheet.filter(priorityrank=(order.priorityrank -1)).first()
            endDate = higherOrder.projectedenddate
        lowerOrder = orderSheet.filter(priorityrank__gt=order.priorityrank)

        #Change projected start and end dates based on which order was removed, update priority by 1
        for item in lowerOrder:
                item.projectedstartdate = endDate
                item.projectedenddate = self.addDate(endDate, math.ceil(item.lengthofrunindays))
                item.priorityrank -= 1
                item.save()
                endDate = item.projectedenddate
