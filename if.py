einkommen = 40000
if einkommen <10000:
    print ("Du zahlst 0 € Steuer")
elif einkommen >= 10000 and einkommen <=29999:
    print ("Du zahlst zwischen 1000 und 2999 € Steuern")
elif einkommen >= 30000 and einkommen <= 99999:
    print ("Du zahlst zwischen 2100 und 2997 € Steuern ")
else:
    print ("Du zahlst 42000 € Steuern")