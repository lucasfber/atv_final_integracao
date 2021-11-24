import unittest
import requests
import os
import sys
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, 'features/steps/json_scenarios')
sys.path.append(path_dir)

from json_utils import  *

class FinancialStrategy(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_financial_strategy(self):
        company_id = get_company_id()
        auth = get_token()
        header = {'authorization': auth}

        response = requests.get(f'{self.url}/financial-strategy/{company_id}', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        financial_strategy = json_data

        self.assertIn('verifySalesGoalAndBreakevenPoint', financial_strategy)
        self.assertEqual(type(financial_strategy['verifySalesGoalAndBreakevenPoint']), bool)

        self.assertIn('hasActionsPermission', financial_strategy)
        self.assertEqual(type(financial_strategy['hasActionsPermission']), bool)

        # SALE PRICE
        sale_price = financial_strategy['salePrice']
        self.assertIn('salePrice', financial_strategy)
        self.assertEqual(type(sale_price), dict)

        self.assertIn('id', sale_price)
        self.assertEqual(type(sale_price['id']), int)

        #SALE PRICE['COMPANY']

        self.assertIn('company', sale_price)
        self.assertEqual(type(sale_price['company']), dict)

        self.assertIn('id', sale_price['company'])
        self.assertEqual(type(sale_price['company']['id']), int)

        # FIXED COST
        fixed_cost = financial_strategy['fixedCost']
        self.assertIn('fixedCost', financial_strategy)
        self.assertEqual(type(fixed_cost), dict)

        self.assertIn('office_supplies', fixed_cost)
        self.assertEqual(type(fixed_cost['office_supplies']), float)

        #FORMULAS
        formulas = financial_strategy['formulas']
        self.assertIn('formulas', financial_strategy)
        self.assertEqual(type(formulas), dict)

        self.assertIn('sumOfRentFixedCosts', formulas)
        self.assertEqual(type(formulas['sumOfRentFixedCosts']), float)

        self.assertIn('sumSalaryFixedCosts', formulas)
        self.assertEqual(type(formulas['sumSalaryFixedCosts']), float)

        self.assertIn('sumOfSocialChargesFixedCosts', formulas)
        self.assertEqual(type(formulas['sumOfSocialChargesFixedCosts']), float)

        self.assertIn('otherFixedCosts', formulas)
        self.assertEqual(type(formulas['otherFixedCosts']), float)

        self.assertIn('sumCommission', formulas)
        self.assertEqual(type(formulas['sumCommission']), float)

        self.assertIn('sumCommissionCharges', formulas)
        self.assertEqual(type(formulas['sumCommissionCharges']), float)

        self.assertIn('sumTaxForSale', formulas)
        self.assertEqual(type(formulas['sumTaxForSale']), float)

        self.assertIn('otherVariableCosts', formulas)
        self.assertEqual(type(formulas['otherVariableCosts']), float)

        self.assertIn('contribution', formulas)
        self.assertEqual(type(formulas['contribution']), float)

        self.assertIn('balance', formulas)
        self.assertEqual(type(formulas['balance']), float)

        self.assertIn('balanceNetProfit', formulas)
        self.assertEqual(type(formulas['balanceNetProfit']), float)

        self.assertIn('profit', formulas)
        self.assertEqual(type(formulas['profit']), float)

        self.assertIn('unitsToProduce', formulas)
        self.assertEqual(type(formulas['unitsToProduce']), float)

        print()