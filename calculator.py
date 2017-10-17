#!/usr/bin/env python3i

import sys

def op():
    if len(sys.argv)>=2:
        base=3500
        salary=int(sys.argv[1])
        tax_Base=salary-base
        if tax_Base<=1500:
            tax_Paid=tax_Base*0.03
        elif tax_Base<=4500:
            tax_Paid=tax_Base*0.1-105
        elif tax_Base<=9000:
            tax_Paid=tax_Base*0.2-555
        elif tax_Base<=35000:
            tax_Paid=tax_Base*0.25-1005
        elif tax_Base<=55000:
            tax_Paid=tax_Base*0.3-2755
        elif tax_Base<=80000:
            tax_Paid=tax_Base*0.35-5505
        else:
            tax_Paid=tax_Base*0.45-13505
    else:
        print("Parameter Error")
    print("{:.2f}".format(tax_Paid))

if __name__=='__main__':
    op()
