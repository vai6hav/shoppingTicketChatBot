from datetime import datetime
from datetime import date
import pytz
import json
import random


def greetAsPerTime():
    time=pytz.timezone('Asia/Kolkata')
    hour=int(str(datetime.now(time))[11:13])
    if hour>=0 and hour<=11 :
        return "Morning"
    elif hour>=12 and hour<=16:
        return "After Noon"
    else:
        return "Evening"
def inputIssue():
    issue=int(input("\nChoose Any: "))
    return issue
def updateTicketStatus(ticketNumber):
    jsonFile = open("tickets.json", "r")
    prevData = json.load(jsonFile)
    jsonFile.close()
    prevData[str(ticketNumber)]['ticket_status']=False


    jsonFile = open("tickets.json", "w+")
    jsonFile.write(json.dumps(prevData))
    jsonFile.close()

def CreatedTicket(ticketNumber,details):
    jsonFile = open("tickets.json", "r")
    prevData = json.load(jsonFile)
    jsonFile.close()
    prevData[str(ticketNumber)]=details

    jsonFile = open("tickets.json", "w+")
    jsonFile.write(json.dumps(prevData))
    jsonFile.close()


def alreadyHaveTicket():
    ticketNumber=input("\nPlease enter your Ticket number: ")
    f = open('tickets.json',)
    data = json.load(f)
    f.close()
    status=data[ticketNumber]['ticket_status']
    if status:
        resolved=input("Is Your Problem resolved? (Y/N) : ").lower()
        if resolved=="y":
            updateTicketStatus(ticketNumber)
            print("\nWe are very Happy that your problem is resolved. Good bye. ")
        else:
            details=data[ticketNumber]
            print("\nName: ",details['name'])
            print("Product Name: ",details['product_name'])
            print("Ticket Created on: ",details['ticket_Date'])
            print("Issue Type: ",details['issue_type'])
            print("Issue: ",details['issue_discription'])
            print("\nR E M A R K S ===== >>> ")
            print("\nDear "+ details['name'] +", Your product ( "+ details['product_name'] +" ) will be delivered by Tomorrow.")
            print("Sorry ! for the inconvenience, We are always there to help you.")

            inp=input("\n\nDo you want to close this ticket? (Y/N): ").lower()
            if inp=="y":
                updateTicketStatus(ticketNumber)
            
                print("\nWe are very Happy that your problem is resolved. Good bye. ")
                print("Thankyou.")
            else:
                print("Track you Ticket status for further reference. Good Bye.")

            print("\n\n******* End **********")
            
    else:
        print("\nYour Ticket Has been closed. Thankyou")
def createNewTicket(name):
    print("\n\n******************** Create your Ticket Here *******************************")

    print("\nDear ",name," Choose Your Product : ")
    with open("customerProducts.json", "r") as outfile:
        products=json.load(outfile)
        dic={}
        c=1
        for i in dict(products[name]).keys():
            print(c,"=> ",i)
            dic[c]=i
            c+=1
    issue=inputIssue()  

    print("\nProduct: ",dic[issue])
    print("Purchase Date: ",products[name][dic[issue]]['purchase_date'])
    print("Price: ",products[name][dic[issue]]['price'])
    print("Description: ",products[name][dic[issue]]['description'])
    print("\nFor ",dic[issue]," Please Select following option")
    commonQ={
        1:"Delayed Shipping",
        2:"Damage Product Dilivered",
        3:"Return/Replacement"
    }
    print("\n1. Delayed Shipping\n2. Damage Product Dilivered\n3. Return/Replacement")
    issue2=inputIssue()
    issueType=commonQ[issue2]
    briefDesc=input("\nPlease breif us about your Issue: ")

    product_name=dic[issue]
    ticket_Date=str(date.today())

    ticketNumber=random.randint(1000,1000000000000)
    details={
        'name':name,
        'product_name':product_name,
        'ticket_Date':ticket_Date,
        'issue_discription':briefDesc,
        'issue_type':issueType,
        'ticket_status': True
    }

    CreatedTicket(ticketNumber,details)

    print("\n\n****** Kindly Note the following Ticket Number for your future reference ***********")
    print("\nTICKET NUMBER :  ",ticketNumber)
    print("\n************************************************************************************")

def ticketoption(issue,name):
    if issue==1:
        alreadyHaveTicket()
    elif issue==2:
        createNewTicket(name)
    else:
        ticketoption(inputIssue(),name)

print("************************** ONLINE SHOPPING - CHATBOT ***********************************")

print("\nGood "+ greetAsPerTime())
name= input("\nPlease type Your Name : ").lower()
print("\nHi "+name+", I hope you're doing well.")
print("\n\n++++++++++++++++++ Select following option +++++++++++++++++++")
print("\nI have Issue in : \n\n1. Do You Have ticket Number? \n2. Do you want to create a new ticket? ")
ticketoption(inputIssue(),name)
print("\nThankyou for Connecting with Us, We insure you to help you anytime, anywhere ")
print("Good Bye")



