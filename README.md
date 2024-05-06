PRESENTATION OF MY E-COMMERCE PROJECT.

As part of my project work in preparation to become a QA Automation tester, This project is to collect information from an e-commerce site in the format json, using the end point from the e-commerce site.
Then produce python scripts that could be executed in a vscode terminal to collect the same information as i got from using postman. Among the content i am exploiting on the e-commerce site are:

All Products List

All Brand List

User account detail by email

All price below Rs. 500

Below are the step by step procedure I used to acomplish the given task.

Workspace Creation
Below is the processes I used to creat my workspace.
On the home page click on workspace from the top left side
Enter the name you want to give to your work space in our case is ' dataCollection'
Choose visibility public
Click on create workspace at the top right conner
Your workspace is created


Collection Creation

Below is the processes I used to creat my collection.

Click on the recently created workspace (in this case : datacollection)
At the top left side Click on New
Select collections
Name your collections by entering the desired name (in this case: My e-commerce Collections) then enter
Your collections with the desired name is created


Adding requests

Below is the processes I used to add a new request

Click on the recentely created collections
At the extreme end click on the 3 horizontal dots ...
Choose add request
Name your request by clicking on New request to rename it .
You have added a new request


Authentication

Go to clients website and search for the end point link to be used to collect the necessary information and also request for authorization Keys.
The e-commerce plateform we are using is an open source and has not protected the page content, hence there was no authentication key to request for.
However perform an exploratory search on the site to find the endpoints of the needed information.


Get All Products List

Below is the processes I used to get all product List.
With the endpoint link from clients site already copied to clip board
Click on Get all products from your collection list
Select get
Paste the endpoint link in the given space
Click on send
Inspect results and choose Json as data type
If code response is 200 then the request was successful
In the case where Response is not 200, check the error message and correct it if possible.


The rest of the requests

I repeat the above process for all the request and below is the results

Get All Brand List
API URL: https://automationexercise.com/api/brandsList
Request Method: GET
Response Code: 200
Response JSON: All brands list


Get user account detail by email
API URL: https://automationexercise.com/api/getUserDetailByEmail
Request Method: GET
Request Parameters: email
Response Code: 200
Response JSON: User Detail


Collect the python code to any python interprater in this case vscode
create a python program that can help me get the same data.
collect information in a json file with the code below


 with open('response.json', 'w') as file:
            json.dump(json_response, file, indent=4)

        print("The response has been saved to response.json")
    else:
        print("Error during the request:", response.status_code)


Finally i have my data in a json file.
