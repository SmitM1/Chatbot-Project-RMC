import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="rmc_tables"
)

#Complaint Status
def get_complaint_status(complaint_id):
    try:
        cursor = cnx.cursor()

        query = "SELECT C_Status FROM Complaint_Status WHERE complaint_id = %s"
        cursor.execute(query, (complaint_id,))

        result = cursor.fetchone()

        if result is not None:
            return result[0]
        else:
            return None

    except mysql.connector.Error as err:
        print(f"Error getting complaint status: {err}")
        cnx.rollback()
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        cnx.rollback()
        return None

    finally:
        cursor.close()

#Property Tax View
def get_amountPayable(property_number):
    try:
        cursor = cnx.cursor()

        query = "SELECT Amount_Payable, Amount_Due FROM Property_Tax_View WHERE property_number = %s"
        cursor.execute(query, (property_number,))

        result = cursor.fetchone()

        if result[0] is not None:
            return result[0], result[1]
        else:
            return None, None

    except mysql.connector.Error as err:
        print(f"Error getting complaint status: {err}")
        cnx.rollback()
        return None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        cnx.rollback()
        return None, None

    finally:
        cursor.close()

#Water Charges View
def get_waterCharges(Connection_No):
    try:
        cursor = cnx.cursor()

        query = "SELECT Avg_Water_Terrif, Avg_Amount_Due FROM Water_Charges_View WHERE Connection_No = %s"
        cursor.execute(query, (Connection_No,))

        result = cursor.fetchone()

        if result[0] is not None:
            return result[0], result[1]
        else:
            return None, None

    except mysql.connector.Error as err:
        print(f"Error getting complaint status: {err}")
        cnx.rollback()
        return None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        cnx.rollback()
        return None, None

    finally:
        cursor.close()


#RTI Application Status
def get_application_status(Application_No):
    try:
        cursor = cnx.cursor()

        query = "SELECT A_Status FROM RTI_Application_Status WHERE Application_No = %s"
        cursor.execute(query, (Application_No,))

        result = cursor.fetchone()

        if result is not None:
            return result[0]
        else:
            return None

    except mysql.connector.Error as err:
        print(f"Error getting complaint status: {err}")
        cnx.rollback()
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        cnx.rollback()
        return None

    finally:
        cursor.close()

