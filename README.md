cp_hec_api_python_sdk
Check Point Harmony Email and Collaboration SDK. The kit contains an API library covering all endpoints.

Content
cp_hec_api - the HEC library.

examples.py - file containing examples of how to properly instantiate the class and call upon it for certain functions.

SDK usage from a remote machine
Install the SDK by using the pip tool or by downloading the repository.

Install with pip
Run:

pip install cp-mgmt-api-sdk (NOT AVAILABLE YET)
Or:

pip install git+https://github.com/CheckPointSW/cp_mgmt_api_python_sdk
Note: you might be required to use "sudo" for this command.
Download the repository
Clone the repository with this command:

git clone https://github.com/CheckPointSW/cp_mgmt_api_python_sdk
or by clicking on the ‘Download ZIP’ button and using unzip.

Navigate to .../cp_mgmt_api_python_sdk/ directory and run:

pip install .


Upgrade
Upgrade the SDK by using pip tool:

pip install --upgrade git+https://github.com/CheckPointSW/cp_mgmt_api_python_sdk
Note: you might be required to use "sudo" for this command.
Uninstall
Uninstall the SDK by using pip tool:

pip uninstall cp-mgmt-api-sdk
Note: you might be required to use "sudo" for this command.

Developed for Python 3.7 and later.

Acknowledgements
Freddy for pushing me to Python all those years ago.
Hec, Raf, Franky for always having my back, love you bros.



Help Output
Below is the output of a python help command on the SDK.  It provides a comprehensive breakdown of all functions.

Help on class CPHEC in module __main__:

class CPHEC(builtins.object)
 |  CPHEC(client_id, secret_key, region)
 |  
 |  A class to interact with the Check Point Harmony Email and Collaboration Platform.
 |  
 |  ---Please see the Official Harmony Email and Collaboration API documentation here---
 |  https://sc1.checkpoint.com/documents/Harmony_Email_and_Collaboration_API_Reference/Topics-HEC-Avanan-API-Reference-Guide/Overview/API-Overview.htm
 |  
 |  Methods defined here:
 |  
 |  __init__(self, client_id, secret_key, region)
 |      Initializing class and user variables
 |      :param client_id: string: Portal client_id, from global settings
 |      :param secret_key: string: Given at time client ID is created in Infinity Portal Global Settings.
 |      :param region: string: 'USA', 'Europe', 'Australia', 'India'
 |  
 |  build_headers(self)
 |      Build the proper headers to send with the HTTP request. Retrieves and/or checks token.
 |      --Can be called, but is designed to work internally to the class
 |      :return: string: Full headers,
 |                       e.g. (headers={'Accept': 'application/json',
 |                       'x-av-req-id': csrf,'Authorization': f'Bearer {token}'}
 |  
 |  build_url_path(self, api_endpoint, token_request=False)
 |      Build the proper path to the desired HEC API endpoint
 |      --Can be called, but is designed to work internally to the class
 |      :param api_endpoint: string: Desired endpoint, e.g. (/event or /exceptions), variables above
 |      :param token_request: boolean: Is this a token request? Default is False, an app request
 |      :return: string: Full path to desired endpoint, e.g.
 |              (https://cloudinfra-gw-us.portal.checkpoint.com/app/hec-api/v1.0/event/)
 |  
 |  entity_by_id(self, entityId)
 |      Retrieve entity data by ID.
 |      :param entityId: string: Required. ID of the entity you want to see.
 |      :return: json: JSON object containing all information about the entity.
 |  
 |  entity_query(self, saas, startDate, endDate, saasEntity=None, extendedfilter=None, scrollId=None)
 |      Entity query utilizing various parameters.  See API guide for full documentation.
 |      The optional parameters must be passed as key=value, e.g. (description="Incident 88484")
 |      Example:
 |          entitysearch = CPHEC.entity_query(saas, entitysearchdate_start,
 |                                            entitysearchdate_stop, saasEntity, extendedfilter)
 |      :param saas: string: Required. Desired SaaS types, e.g. ('office365_emails')
 |      :param startDate: string: Required.  Start date of query, e.g. ('2022-08-29T09:12:33.001Z')
 |      :param endDate: string: Required.  End date of query, e.g. ('2022-08-29T09:12:33.001Z')
 |      :param saasEntity: string: Optional. Name of SaaS entity. Possible values: office365_emails_email
 |      :param extendedfilter: list of dictionary: Optional. The optional parameters must be passed as a list of dictionary,
 |      due to the possibility of unknown amount of args.  Please see API guide for full documentation on the
 |      extended filter.
 |      Example:
 |          saas = 'office365_emails'
 |          entitysearchdate_start = '2022-08-29T09:12:33.001Z'
 |          entitysearchdate_stop = '2022-09-15T09:12:33.001Z'
 |          saasEntity = 'office365_emails_email'
 |          extendedfilter = [
 |              {
 |                  "saasAttrName": "entityPayload.fromEmail",
 |                  "saasAttrOp": "is",
 |                  "saasAttrValue": "developer@checkpoint.com"
 |              },
 |              {
 |                  "saasAttrName": "entityPayload.attachmentCount",
 |                  "saasAttrOp": "greaterThan",
 |                  "saasAttrValue": "0"
 |              }
 |                          ]
 |      :param scrollId: string: Required if paging. This parameter is used to retrieve large sets of results.
 |                                  The first response includes this parameter and partial result.
 |                                  Use this parameter to retrieve the rest of the results.
 |      :return: json: Json object with query results from server, available for further parsing.
 |  
 |  entity_take_action(self, entityIds, entityType, entityActionName, entityActionParam=None)
 |      Take action on a list of entities, for example mass quarantine a list of entities.
 |      The optional parameters must be passed as key=value, e.g. (description="Incident 88484")
 |      :param entityIds: list of string: Required.  List of entities to take action on,
 |                    e.g. ['9b0004c09cbb4701ae9bc3592bc310ef', '8f4004c09cbb4701ae9bc3592bc31ydh']
 |      :param entityType: string: Required.  Unclear in API documentation.  The one that was successful
 |                      for me was 'office365_emails_email', however you can view all entity types
 |                      in your backend by using the entity_query method above and searching for 'entityType'
 |      :param entityActionName: string: Required. 'quarantine' or 'restore'
 |      :param entityActionParam: list of string: Optional. Unclear in API documentation, I'm sorry.
 |      :return: json: JSON containing information about the request, including the taskid for the request.
 |  
 |  event_by_id(self, eventId)
 |      Retrieve an event by its ID
 |      :param eventId: string: ID number of the corresponding event
 |      :return: json: JSON object containing all related event ID fields
 |  
 |  event_query(self, startDate, endDate=None, eventTypes=None, eventStates=None, severities=None, saas=None, eventIds=None, confidenceIndicator=None, description=None, scrollId=None)
 |      Security event query utilizing various parameters.  See API guide for full documentation.
 |      The optional parameters must be passed as key=value, e.g. (description="Incident 88484")
 |      Example:
 |          eventsearchdate = '2022-08-29T09:12:33.001Z'
 |          eventtypes = ['phishing', 'malware']
 |          eventsearch = CPHEC.event_search(eventsearchdate, eventTypes=eventtypes)
 |      :param startDate: string: Required.  Start date of query, e.g. ('2022-08-29T09:12:33.001Z')
 |      :param endDate: string: Optional.  End date of query, e.g. ('2022-08-29T09:12:33.001Z')
 |      :param eventTypes: list of string: Optional. A list of desired event types, e.g. (['phishing', 'malware'])
 |      :param eventStates: list of string: Optional. A list of desired event states, e.g. (['new', 'pending'])
 |      :param severities: list of string: Optional. A list of possible severities, e.g. (['high', 'critical'])
 |      :param saas: list of string: Optional. Desired SaaS types, e.g. (['office365_emails', 'sharefile'])
 |      :param eventIds: list of string: Optional. A list of event IDs to retrieve.
 |      :param confidenceIndicator: string: Optional. Desired confidence indicators to search for, e.g. ('malicious')
 |      :param description: string: Optional. Search the descriptions of events.
 |      :param scrollId: string: Required if paging. This parameter is used to retrieve large sets of results.
 |                                  The first response includes this parameter and partial result.
 |                                  Use this parameter to retrieve the rest of the results.
 |      :return: json: Json object with query results from server, available for further parsing.
 |  
 |  event_take_action(self, eventIds, eventActionName, eventActionParam=None)
 |      Take action on a list of security events, for example mass quarantine a list of event IDs.
 |      The optional parameters must be passed as key=value, e.g. (description="Incident 88484")
 |      :param eventIds: list of string: Required.  List of events to take action on,
 |                    e.g. ('9b0004c09cbb4701ae9bc3592bc310ef', '8f4004c09cbb4701ae9bc3592bc31ydh'
 |      :param eventActionName: string: Required.  'quarantine' or 'restore'
 |      :param eventActionParam: string: Optional. Unclear in API documentation, I'm sorry.
 |      :return: json: JSON containing information about the request, including the taskid for the request.
 |  
 |  exception_by_id(self, excType, excId)
 |      Retrieve an exception by its ID.
 |      :param excType: string: Required. Type of exception, 'whitelist' or 'blacklist'
 |      :param excId: string: Required. Exception ID
 |      :return: json: JSON object containing your requested exception.
 |  
 |  exception_create(self, excType, attachmentMd5=None, senderEmail=None, senderName=None, recipient=None, senderClientIp=None, senderDomain=None, senderIp=None, linkDomains=None, subject=None, comment=None, actionNeeded=None, subjectMatching=None, linkDomainMatching=None, senderNameMatching=None, senderDomainMatching=None, recipientMatching=None)
 |      Create an exception, such as a block or allow rule.
 |      The optional parameters must be passed as key=value, e.g. (description="Incident 88484")
 |      :param excType: string: Required.  Type of exception, 'whitelist' or 'blacklist'.
 |      :param attachmentMd5: string: Optional.  MD5 checksum of attachment.
 |      :param senderEmail: string: Optional. Sender's email address, such as 'frank@badguy.com'.
 |      :param senderName: string: Optional. Sender's name.
 |      :param recipient: string: Optional. Recipient's email address.
 |      :param senderClientIp: string: Optional. IP address of sender's client.
 |      :param senderDomain: string: Optional. Domain of sender such as 'badguy.com'.
 |      :param senderIp: string: Optional. IP of sender.
 |      :param linkDomains: string: Optional. Link domains.
 |      :param subject: string: Optional. Subject of email you want to take action on.
 |      :param comment: string: Optional. Comment for the rule you create.
 |      :param actionNeeded: string: Optional. e.g. 'phishing'
 |      :param subjectMatching: string: Optional. contains
 |      :param linkDomainMatching: string: Optional. contains
 |      :param senderNameMatching: string: Optional. contains
 |      :param senderDomainMatching: string: Optional. endswith
 |      :param recipientMatching: string: Optional. match
 |      :return: json: Json object with task completion information, including task ID.
 |  
 |  exception_delete(self, excType, excId)
 |      Delete an exception by ID.
 |      :param excType: string: Required.  Type of exception you want to delete, 'whitelist' or 'blacklist'.
 |      :param excId: string: Required.  Exception ID you wish to change.
 |      :return: json: Json object with task completion information, including task ID.
 |  
 |  exception_get_all(self, excType)
 |      Retrieve all exceptions of a particular type.
 |      :param excType: string: Required. Type of exception, 'whitelist' or 'blacklist'
 |      :return: json: JSON object containing all exceptions.
 |  
 |  exception_modify(self, excType, excId, attachmentMd5=None, senderEmail=None, senderName=None, recipient=None, senderClientIp=None, senderDomain=None, senderIp=None, linkDomains=None, subject=None, comment=None, actionNeeded=None, subjectMatching=None, linkDomainMatching=None, senderNameMatching=None, senderDomainMatching=None, recipientMatching=None)
 |      Modify an exception, such as a block or allow rule.
 |      The optional parameters must be passed as key=value, e.g. (description="Incident 88484")
 |      :param excType: string: Required.  Type of exception, 'whitelist' or 'blacklist'.
 |      :param excId: string: Required.  Exception ID you wish to change.
 |      :param attachmentMd5: string: Optional.  MD5 checksum of attachment.
 |      :param senderEmail: string: Optional. Sender's email address, such as 'frank@badguy.com'.
 |      :param senderName: string: Optional. Sender's name.
 |      :param recipient: string: Optional. Recipient's email address.
 |      :param senderClientIp: string: Optional. IP address of sender's client.
 |      :param senderDomain: string: Optional. Domain of sender such as 'badguy.com'.
 |      :param senderIp: string: Optional. IP of sender.
 |      :param linkDomains: string: Optional. Link domains.
 |      :param subject: string: Optional. Subject of email you want to take action on.
 |      :param comment: string: Optional. Comment for the rule you create.
 |      :param actionNeeded: string: Optional. e.g. 'phishing'
 |      :param subjectMatching: string: Optional. contains
 |      :param linkDomainMatching: string: Optional. contains
 |      :param senderNameMatching: string: Optional. contains
 |      :param senderDomainMatching: string: Optional. endswith
 |      :param recipientMatching: string: Optional. match
 |      :return: json: Json object with task completion information, including task ID.
 |  
 |  get_full_request(self, url_path, headers, verify=False)
 |      Build and send a full get request to the server, and return the response.
 |      --Can be called, but is designed to work internally to the class
 |      :param url_path: string: The full path of the URL
 |      :param headers: dictionary: Header dictionary, e.g. (headers={'Content-Type': 'application/json'})
 |      :param verify: boolean: Default is to not verify the cert
 |      :return: json: Json object returned from the server, available for further parsing
 |  
 |  get_token(self)
 |      Retrieve a token and uuid for further calls to the server
 |      --Can be called, but is designed to work internally to the class
 |      :return: json: Token JSON response
 |  
 |  post_full_request(self, url_path, headers, verify=False, **kwargs)
 |      Build and send a full post request to the server, and return the response
 |      --Can be called, but is designed to work internally to the class
 |      :param url_path: string: The full path of the URL
 |      :param headers: dictionary: Header dictionary, e.g. (headers={'Content-Type': 'application/json'})
 |      :param verify: boolean: Default is to not verify the cert
 |      :param kwargs: dictionary: Fully formatted JSON dictionary to pass to the server,
 |                                  e.g. { "requestData":{"eventTypes": [eventtype]}}
 |      :return: json: Json object returned from the server, available for further parsing
 |  
 |  put_full_request(self, url_path, headers, verify=False, **kwargs)
 |      Build and send a full post request to the server, and return the response
 |      --Can be called, but is designed to work internally to the class
 |      :param url_path: string: The full path of the URL
 |      :param headers: dictionary: Header dictionary, e.g. (headers={'Content-Type': 'application/json'})
 |      :param verify: boolean: Default is to not verify the cert
 |      :param kwargs: dictionary: Fully formatted JSON dictionary to pass to the server,
 |                                  e.g. { "requestData":{"eventTypes": [eventtype]}}
 |      :return: json: Json object returned from the server, available for further parsing
 |  
 |  task_status(self, taskId)
 |      Check the status of a any task with an ID given to the server.
 |      :param taskId: string: Required. ID of the task you want to see.
 |      :return: json: Json object with task completion information, including task ID.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  exception_handler(http_response, exception) from builtins.type
 |      Non-user facing, custom exception handler.
 |  
 |  response_handler(http_response, json_response) from builtins.type
 |      Non-user facing, parses responses received from server to detect errors.
 |  
 |  token_expiry(datestamp) from builtins.type
 |      Non-user facing, determines if token is expired.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  format_json(params)
 |      Static utility to format our request data according to the API specifications.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

