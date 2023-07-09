data_to_send1={}
data_to_send2={}
data_to_send3={}
data_to_send={}
data_to_sendzs={}
data_to_sendzb={}
def formatting_response1(success=False,data=[],error=''):
    data_to_send1['success']=success
    data_to_send1['data']=data
    data_to_send1['error']=error
    return data_to_send1
    
def formatting_response2(success=False,data=[],error=''):
    data_to_send2['success']=success
    data_to_send2['data']=data
    data_to_send2['error']=error
    return data_to_send2
    
def formatting_response3(success=False,data=[],error=''):
    data_to_send3['success']=success
    data_to_send3['data']=data
    data_to_send3['error']=error
    return data_to_send3
    
def formatting_response(success=False,data=[],error=''):
    data_to_send['success']=success
    data_to_send['data']=data
    data_to_send['error']=error
    return data_to_send
    

def formatting_responsezs(success=False,data=[],error=''):
    data_to_sendzs['success']=success
    data_to_sendzs['data']=data
    data_to_sendzs['error']=error
    return data_to_sendzs
    

def formatting_responsezb(success=False,data=[],error=''):
    data_to_sendzb['success']=success
    data_to_sendzb['data']=data
    data_to_sendzb['error']=error
    return data_to_sendzb
    