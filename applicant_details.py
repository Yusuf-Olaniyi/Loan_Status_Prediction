# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:20:43 2024

@author: YUSUF
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class applicant_detail(BaseModel):
    dependent: int
    income: float
    co_app_income: float
    loan_amt: float
    loan_term: int
    cred_hist: int
    prop_area: str
    gender: str
    grad: str
    marr: str
    self_emp: str