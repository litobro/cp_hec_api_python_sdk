# Check Point Harmony Email and Collaboration SDK Library
# examples.py
# version 1.0
#
# Various examples showing how to interact with the CP HEC API library
#
# written by: Travis Lockman
# May 2023
# O_o tHe pAcKeTs nEvEr LiE o_O #

import cp_hec_api



ClientID = 'PLACE YOUR CLIENT ID HERE'  # Portal Client ID
SecretKey = 'PLACE YOUR SECRET KEY HERE'  # Portal Secret Key
region = 'USA, Europe, Australia, or India'

# Instantiate the CPHEC class with the provided ClientID, SecretKey, and region
CPHEC = cp_hec_api.CPHEC(ClientID, SecretKey, region)

''' 
    USE CAUTION THIS WILL TAKE ACTION ON YOUR ACTIVE HARMONY EMAIL PORTAL!!!
    For safety all examples have been commented out.
'''



# Print out a help manual based on the PEP 257 in the SDK
# print(help(CPHEC))

# Search for an event by ID
# eventid = '9b0004c09cbb4701ae9bc3592bc310ef'
# event = CPHEC.event_by_id(eventid)
# print(event)

# General event query
# eventsearchdate = '2022-08-29T09:12:33.001Z'
# eventtypes = ['phishing']
# eventsearch = CPHEC.event_query(eventsearchdate)
# print(eventsearch)

# Take action on an event
# eventid = 'c38191979ecd4c50a2017bc23cc93225'
# response = CPHEC.event_take_action([eventid], 'quarantine')
# print(response)

# Check status of any task
# taskid = '1694570143673866'
# response = CPHEC.task_status(taskid)
# print(response)

# Lookup an entity by its ID
# entityid = '4a476c17bbf24c8db037868c10dcf2c0'
# entitybyid = CPHEC.entity_by_id(entityid)
# print(entitybyid)

# General entity query
# saas = 'office365_emails'
# entitysearchdate_start = '2022-08-29T09:12:33.001Z'
# entitysearchdate_stop = '2023-08-29T09:12:33.001Z'
# saasEntity = 'office365_emails_email'
# scroll = '838383-383373'
# extendedfilter = [
#     {
#         "saasAttrName": "entityPayload.fromEmail",
#         "saasAttrOp": "is",
#         "saasAttrValue": "developer@checkpoint.com"
#     },
#     {
#         "saasAttrName": "entityPayload.attachmentCount",
#         "saasAttrOp": "greaterThan",
#         "saasAttrValue": "0"
#     }
#                 ]
#
# entityquery = CPHEC.entity_query(saas, entitysearchdate_start, entitysearchdate_stop)
# print(entityquery)

# Take acton on an entity by its ID
# entityid = ['4a476c17bbf24c8db037868c10dcf2c0']
# entityType = 'office365_emails_email'
# action = 'restore'
# entityaction = CPHEC.entity_take_action(entityid, entityType, action)
# print(entityaction)

# Get all exceptions of type blacklist
# exception_type = 'blacklist'
# # exception_list = CPHEC.exception_get_all(exception_type)
# # print(exception_list)

# Get a specific exception by its ID
# exception_id = '1996897'
# exception_type = 'blacklist'
# exception_by_id = CPHEC.exception_by_id(exception_type, exception_id)
# print(exception_by_id)

# Create an exception
# exception_type = 'blacklist'
# create_exception = CPHEC.exception_create(exception_type, senderEmail='tacohater5449@badguy.com', comment="ADDED BY THE SDK!")
# print(create_exception)

# Modify an exception
# comment = "CHANGED COMMENT WITH SDK!!!"
# exception_type = 'blacklist'
# exception_id = '1996897'
# exception_modify = CPHEC.exception_modify(exception_type, exception_id, comment=comment)
# print(exception_modify)

# Delete an exception
# exception_type = 'blacklist'
# exception_id = '1996897'
# exception_delete = CPHEC.exception_delete(exception_type, exception_id)
# print(exception_delete)