# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:18:00 2020

@author: ThanaphatJ
"""

def validate_pin(otp):
    if otp.isdecimal() and (len(otp) == 4 || len(otp) == 6):
        return True
    return False
    