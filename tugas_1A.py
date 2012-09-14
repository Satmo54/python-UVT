#!/usr/bin/env python2

def kabisat(tahun):
    if tahun % 4 == 0:
        if tahun % 100 == 0:
            if tahun % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
check_tahun = int ( raw_input ( "Input tahun : "))

print kabisat(check_tahun)