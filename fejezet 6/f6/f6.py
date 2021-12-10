honap = input()

def honap_napszam(honap):
    if(honap == "Január"): return 30
    if(honap == "Február"): return 28
    if(honap == "Március"): return 31
    if(honap == "Április"): return 30
    if(honap == "Május"): return 31
    if(honap == "Június"): return 30
    if(honap == "Július"): return 31
    if(honap == "Augusztus"): return 31
    if(honap == "Szeptember"): return 30
    if(honap == "Október"): return 30
    if(honap == "November"): return 30
    if(honap == "December"): return 31
    
print(honap_napszam(honap))