# factik
Steps to use this project :

1. The first step is to import chrome extensoin provided in this project to your chrome browser.As we have not yet published our extension so you can download it on your local machine and then import it in chrome manually (On its developer mode).
Go to <b> chrome://extensions > click on Load unpacked link > choose the extension folder which you have downloaded > Enable the extension<b>
2. Now you have to go to your social media site and select the post or news to check how much likely it is correct or fake. Select the content and right click on it. Now in order to verify the text, select Factik option from the right click options.
3. It will show a popup window with the percentage that how much likely it is fake or correct.


There is another folder in this project - 'flask' :
 - There are two files related to our ML model - feature.pkl and pickle_file_name.pkl and one file (RestApi.py) is used for making rest call for I/O.
 - Our api requests to ML with the fact/post/news to verify them and returns the resonse to the client that how much likely it is correct or fake.
