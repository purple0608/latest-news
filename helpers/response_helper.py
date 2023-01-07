data_to_send={}
def formatting_response(success=False,data=[],error=''):
    data_to_send['success']=success
    data_to_send['data']=data
    data_to_send['error']=error
    return data_to_send
    
    