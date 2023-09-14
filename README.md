## cp_hec_api_python_sdk

## **Check Point Harmony Email and Collaboration SDK**

**This kit contains an API library covering all documented endpoints.**

## **Content**
*cphec* - The HEC SDK library.

*examples* - File containing examples of how to properly instantiate the class and call upon it for certain functions.



## **Installation**

Install the SDK by using the pip tool or by downloading the repository.



**Install with pip**

Install directly from console (NOT AVAILABLE YET):

`pip install cp-hec-api-sdk`

Install by pointing to the GitHub repo:

`pip install git+https://github.com/travislockman/cp_hec_api_python_sdk`

Note: you might be required to use "sudo" for this command.



**Download the repository**

Clone the repository with this command:

`git clone https://github.com/travislockman/cp_hec_api_python_sdk`

or by clicking on the ‘Download ZIP’ button and using unzip.

Navigate to .../cp_hec_api_python_sdk/ directory and run:

`pip install .`


## **Upgrading**

Upgrade the SDK by using pip tool:

`pip install --upgrade git+https://github.com/travislockman/cp_hec_api_python_sdk`

Note: you might be required to use "sudo" for this command.

## **Uninstalling**

Uninstall the SDK by using pip tool:

`pip uninstall cp-mgmt-api-sdk`

Note: you might be required to use "sudo" for this command.


## **How To Use This SDK**

Once installed, import the class and assign to a variable:

```python
from cp_hec_python_sdk import CPHEC
```

Create variables for your Client ID, Secret Key, and region.
You can get your Client ID and Secret Key from inside your Infinity Portal in Global Settings.
When you create the API Key, ensure to select Email and Collaboration.
Also please make sure to save your secret key somewhere secure.
The four regions available are (USA, Europe, Australia, India):

```python
ClientID = 'Your Client ID Here'  # Portal Client ID
SecretKey = 'Your Secret Key Here'  # Portal Secret Key
region = 'USA'

# Instantiate the class with your information and assign it to a variable.
cp = CPHEC(ClientID, SecretKey, region)
```



**Install with pip**

Install directly from console (NOT AVAILABLE YET):

`pip install cp-hec-api-sdk`

Install by pointing to the GitHub repo:

`pip install git+https://github.com/travislockman/cp_hec_api_python_sdk`

Note: you might be required to use "sudo" for this command.


## **Developed for Python 3.7 and later.**

## **Acknowledgements**

Freddy for pushing me to Python all those years ago.
Hec, Raf, Franky for always having my back, love you bros.
Alex, thanks for the burrito ;)