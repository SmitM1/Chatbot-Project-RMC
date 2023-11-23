from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import db_helper
import generic_helper

app = FastAPI()

@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    session_id = generic_helper.extract_session_id(output_contexts[0]['name'])

    def property_tax_view(parameters: dict):
        property_number = parameters['property_number']
        property_number = int(property_number[0])
        Amount_Payable, Amount_Due = db_helper.get_amountPayable(property_number)
        
        if Amount_Payable:
            fulfillment_text = f"Amount Payable is: {Amount_Payable}. Amount Due is: {Amount_Due} for property number: {property_number}."
        else:
            fulfillment_text = f"No such property number found. You can contact 0281-2389274 for more information."

        return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })

    def Water_Charges_View(parameters: dict):
        Connection_No = parameters['Connection_No']
        Connection_No = Connection_No[0]
        Avg_Water_Terrif, Avg_Amount_Due = db_helper.get_waterCharges(Connection_No)

        if Avg_Water_Terrif:
            fulfullment_text = f"Average Water Terrif is: {Avg_Water_Terrif}. Average Amount Due is: {Avg_Amount_Due} for connection number: {Connection_No}."
        else:
            fulfullment_text = f"No connection number found. You can contact 0281-2389274 for more information."

        return JSONResponse(content={
            "fulfillmentText": fulfullment_text
        })

    def Complaint_Status(parameters: dict):
        complaint_id = parameters['complaint_id']
        complaint_id = complaint_id[0]
        C_Status = db_helper.get_complaint_status(complaint_id)

        if C_Status:
            fulfillment_text = f"The Complaint Status for complaint id: {complaint_id} is: {C_Status}"
        else:
            fulfillment_text = f"No complaint found with complaint id: {complaint_id}"

        return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })
    
    def RTI_Application_Status(parameters: dict):
        Application_No = parameters['Application_No']
        Application_No = Application_No[0]
        A_Status = db_helper.get_application_status(Application_No)

        if A_Status:
            fulfillment_text = f"The Application Status for application number: {Application_No} is: {A_Status}"
        else:
            fulfillment_text = f"No application found with application number: {Application_No}"

        return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })

    


    if intent == "property_tax_view:property_no":
        return property_tax_view(parameters)

    if intent == "Complaint_Status:complaint_id":
        return Complaint_Status(parameters)
    
    if intent == "RTI_Application_Status:application_number":
        return RTI_Application_Status(parameters)
    
    if intent == "Water_Charges_View:connection_number":
        return Water_Charges_View(parameters)
    
    
    

    