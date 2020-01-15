"""Generate sales report showing total melons each salesperson sold."""


salespeople = []  
melons_sold = []

#define a functio that accepts a file.txt as an argument 
 #and Generate sales report showing total melons each salesperson sold.

# f = open('sales-report.txt') #opens the file report/// Suggestion: 
#                              # give a better name to the variable
# for line in f: # it loops through each line of te file
#     line = line.rstrip() #remove extra blanc spaces
#     entries = line.split('|')#convert each line/string into a list named entries

#     salesperson = entries[0] # captures the name of the the salesperson
#                              # index 0 in list intries
#     melons = int(entries[2]) # captures how many mellons each salesperson sold

#     if salesperson in salespeople:                  # SUGESTION: 
#                                                     #make a dicionary which
#         position = salespeople.index(salesperson)   #salespeople is the key and
#                                                     #the number of melons sold
#         melons_sold[position] += melons             #is the value
#     else:
#         salespeople.append(salesperson)   
#         melons_sold.append(melons)  


# for i in range(len(salespeople)): #loop throug salespeople list by index
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')  


#######################################################################


def generate_sales_report(filename):
    """Generate sales report showing total melons each salesperson sold."""

    file = open(filename)

    sales_report = {}

    for line in file:
        line = line.rstrip()
        entries = line.split("|")

        sales_report[entries[0]] = entries[2]

    for person, melons_sold in sales_report.items():
        print(f"{person} sold {melons_sold} melons.")

generate_sales_report("sales-report.txt")

