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
            fulfillment_text = (
    f"Amount Payable is: {Amount_Payable}. Amount Due is: {Amount_Due} for property number: {property_number}.\n"
    " \nAnything else?\n\n"
    "- Property Tax\n"
    "- Profession Tax\n"
    "- Water Charge\n"
    "- Hall Booking\n"
    "- Sport Registration\n"
    "- E-Memo Payment\n"
    "- 24x7 Call Center\n"
    "- Right To Information Act\n"
    "- Shop And Establishment\n"
    "- Rajkot Rajpath LTD.\n"
    "- Vehicle Tax\n"
    "- Promotion Project's\n"
    "- Town Plan\n"
    "- AVAS Yojna"
)
        else:
            fulfillment_text = (
                f"No such property number found. You can contact 0281-2389274 for more information.\n"
    " \nAnything else?\n\n"
    "- Property Tax\n"
    "- Profession Tax\n"
    "- Water Charge\n"
    "- Hall Booking\n"
    "- Sport Registration\n"
    "- E-Memo Payment\n"
    "- 24x7 Call Center\n"
    "- Right To Information Act\n"
    "- Shop And Establishment\n"
    "- Rajkot Rajpath LTD.\n"
    "- Vehicle Tax\n"
    "- Promotion Project's\n"
    "- Town Plan\n"
    "- AVAS Yojna"
)

        return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })

    def Water_Charges_View(parameters: dict):
        Connection_No = parameters['Connection_No']
        Connection_No = Connection_No[0]
        Avg_Water_Terrif, Avg_Amount_Due = db_helper.get_waterCharges(Connection_No)

        if Avg_Water_Terrif:
            fulfullment_text = (
    f"Average Water Terrif is: {Avg_Water_Terrif}. Average Amount Due is: {Avg_Amount_Due} for connection number: {Connection_No}.\n"
    " \nAnything else?\n\n"
    "- Property Tax\n"
    "- Profession Tax\n"
    "- Water Charge\n"
    "- Hall Booking\n"
    "- Sport Registration\n"
    "- E-Memo Payment\n"
    "- 24x7 Call Center\n"
    "- Right To Information Act\n"
    "- Shop And Establishment\n"
    "- Rajkot Rajpath LTD.\n"
    "- Vehicle Tax\n"
    "- Promotion Project's\n"
    "- Town Plan\n"
    "- AVAS Yojna"
)
        else:
            fulfullment_text = (
    "No connection number found. You can contact 0281-2389274 for more information.\n"
    " \nAnything else?\n\n"
    "- Property Tax\n"
    "- Profession Tax\n"
    "- Water Charge\n"
    "- Hall Booking\n"
    "- Sport Registration\n"
    "- E-Memo Payment\n"
    "- 24x7 Call Center\n"
    "- Right To Information Act\n"
    "- Shop And Establishment\n"
    "- Rajkot Rajpath LTD.\n"
    "- Vehicle Tax\n"
    "- Promotion Project's\n"
    "- Town Plan\n"
    "- AVAS Yojna"
)

        return JSONResponse(content={
            "fulfillmentText": fulfullment_text
        })

    def Complaint_Status(parameters: dict):
        complaint_id = parameters['complaint_id']
        complaint_id = complaint_id[0]
        C_Status = db_helper.get_complaint_status(complaint_id)

        if C_Status:
            fulfillment_text = (f"The Complaint Status for complaint id: {complaint_id} is: {C_Status}\n"
    " \nAnything else?\n\n"
    "- Property Tax\n"
    "- Profession Tax\n"
    "- Water Charge\n"
    "- Hall Booking\n"
    "- Sport Registration\n"
    "- E-Memo Payment\n"
    "- 24x7 Call Center\n"
    "- Right To Information Act\n"
    "- Shop And Establishment\n"
    "- Rajkot Rajpath LTD.\n"
    "- Vehicle Tax\n"
    "- Promotion Project's\n"
    "- Town Plan\n"
    "- AVAS Yojna"
)
        else:
            fulfillment_text = (f"No complaint found with complaint id: {complaint_id}\n"
    " \nAnything else?\n\n"
    "- Property Tax\n"
    "- Profession Tax\n"
    "- Water Charge\n"
    "- Hall Booking\n"
    "- Sport Registration\n"
    "- E-Memo Payment\n"
    "- 24x7 Call Center\n"
    "- Right To Information Act\n"
    "- Shop And Establishment\n"
    "- Rajkot Rajpath LTD.\n"
    "- Vehicle Tax\n"
    "- Promotion Project's\n"
    "- Town Plan\n"
    "- AVAS Yojna"
)

        return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })
    
    def RTI_Application_Status(parameters: dict):
        Application_No = parameters['Application_No']
        Application_No = Application_No[0]
        A_Status = db_helper.get_application_status(Application_No)

        if A_Status:
            fulfillment_text = (f"The Application Status for application number: {Application_No} is: {A_Status}\n"
    " \nAnything else?\n\n"
    "- Property Tax\n"
    "- Profession Tax\n"
    "- Water Charge\n"
    "- Hall Booking\n"
    "- Sport Registration\n"
    "- E-Memo Payment\n"
    "- 24x7 Call Center\n"
    "- Right To Information Act\n"
    "- Shop And Establishment\n"
    "- Rajkot Rajpath LTD.\n"
    "- Vehicle Tax\n"
    "- Promotion Project's\n"
    "- Town Plan\n"
    "- AVAS Yojna"
)
        else:
            fulfillment_text = (f"No application found with application number: {Application_No}\n"
    " \nAnything else?\n\n"
    "- Property Tax\n"
    "- Profession Tax\n"
    "- Water Charge\n"
    "- Hall Booking\n"
    "- Sport Registration\n"
    "- E-Memo Payment\n"
    "- 24x7 Call Center\n"
    "- Right To Information Act\n"
    "- Shop And Establishment\n"
    "- Rajkot Rajpath LTD.\n"
    "- Vehicle Tax\n"
    "- Promotion Project's\n"
    "- Town Plan\n"
    "- AVAS Yojna"
)

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
    
    # ================================================================================


# def automate_property_tax(property_number):
#     try:
#         # Set up the browser (assuming Chrome for this example)
#         driver = webdriver.Chrome()
#         driver.get("https://ahmedabadcity.gov.in/PTAX/DuesSearch")  # Replace with the actual URL

#         # Find the input field by its name or other attribute
#         input_field = driver.find_element(by=By.NAME, value="tenementNo")  # Replace with the actual attribute

#         # Type the property number
#         input_field.send_keys(str(property_number))
#         print(f"Filled property number: {property_number}")
#         # Find and click the submit button
#         submit_button = driver.find_element(by=By.NAME, value="action")  # Replace with the actual attribute
#         submit_button.click()
#         print("Clicked the submit button")
#         # Wait for the page to load (you may need to adjust the sleep time)
#         time.sleep(2)

#         # Extract information from the page or take other actions as needed

#         # Example: Get the result text from the page
#         result_text = driver.find_element("id", "result_text").text  # Replace with the actual attribute
#         print(f"Result text: {result_text}")

#         fulfillment_text = (
#             f"Amount Payable is: {result_text}. Amount Due is: {result_text} for property number: {property_number}.\n"
#             " \nAnything else?\n\n"
#             "- Property Tax\n"
#             "- Profession Tax\n"
#             "- Water Charge\n"
#             "- Hall Booking\n"
#             "- Sport Registration\n"
#             "- E-Memo Payment\n"
#             "- 24x7 Call Center\n"
#             "- Right To Information Act\n"
#             "- Shop And Establishment\n"
#             "- Rajkot Rajpath LTD.\n"
#             "- Vehicle Tax\n"
#             "- Promotion Project's\n"
#             "- Town Plan\n"
#             "- AVAS Yojna"
#         )

#         return JSONResponse(content={"fulfillmentText": fulfillment_text})

#     except Exception as e:
#         return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)

#     finally:
#         # Close the browser window
#         driver.quit()
    

# @app.post("/property_tax_view")
# async def property_tax_view(request: Request):
#     payload = await request.json()
#     parameters = payload['queryResult']['parameters']
#     property_number = "05442838390001T"
    
#     return automate_property_tax(property_number)
    

    