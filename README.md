# Live Barcode Reader MongoDB Integration
This should serve as a tutorial for a simple working live barcode scanner with mongodb integration. Simply scan bar codes and have the corresponding data imported to your mongodb collection.

Credits:
- How to make a live barcode scanner: https://www.thepythoncode.com/code/making-a-barcode-scanner-in-python
- Code: https://github.com/x4nth055/pythoncode-tutorials/blob/5101b00b5143983db2b8fe29be8068f03e2f86d5/general/barcode-reader/live_barcode_reader.py

Assumptions:
- You can and have already setup MongoDB account 
- You have a MongoDB database name, collection name if not you have set them up.

# What to do?

## Step 1
Get your mongodb connection string (assuming you have already setup an account and database), you can get this from Databse > Connect > Connect your application. For this project we will select the python 3.4 or later from the version dropdown menu.

![Alt text](/3.png)

## Step 2
Find the mongo_connect.py file and open it. We will configure this to work with our database.

![Alt text](/1.png)

## Step 3
Copy connection string from step one. And paste it here. Remember it has to go in as a string, make sure to include the ' " '.

![Alt text](/2.png)

## Step 4
Type in the database name as a string (within the inverted commas).

![Alt text](/4.png)

## Step 5
Type the collection name where you want the data to be stored.

![Alt text](/5.png)

# That's all!
Just run the live_barcode_mongodb_integration.py and watch scan your barcode to see your database get populated.
I have included a 10 second timeout as default. You can adjust or remove it as you like.

![Alt text](/6.png)
