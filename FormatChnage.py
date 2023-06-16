import re
def new_key_name(key):
    if 'fiserv/dfm/' in key and key.split('/')[-1][0:2]=='CL':
        return f"encrypt/fiserv/north/ps/{key.split('/')[-1]}" 
    
    if 'fiserv/dfm/' in key and key.split('/')[-1][0:2]=='FS':
        return f"encrypt/fiserv/north/ep/{key.split('/')[-1]}" 
    
    if 'fis/emaf/' in key:
        return f"encrypt/fis/core/{key.split('/')[-1]}"

    elif 'fis/litle/' in key:
        return f"encrypt/fis/ecom/{key.split('/')[-1]}"

    elif 'fis/deposits/' in key:
        return f"encrypt/settlement/{key.split('/')[-1]}"
    
    elif 'fis/ach/' in key:
        return f"encrypt/settlement/{key.split('/')[-1]}"
    
    elif 'billing_data/' in key:
        return f"encrypt/billing/'{key.split('/')[-1]}"
        
print(list(map(new_key_name,['billing_data/FILE1.csv','fis/deposits/FILE2.csv','fis/ach/FILE3.csv','fis/emaf/FILE4.csv','fiserv/dfm/FS_Qualification_Expense_<yyyymmdd>_38175.txt','fiserv/dfm/CL9DFMDE.34806.NAGW-OPJMB001.497960027884.d.20201015.dfm.20220415.gz'])))
