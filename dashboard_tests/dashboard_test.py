import unittest
import requests
import os
import sys
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, 'features/steps/json_scenarios')
sys.path.append(path_dir)

from json_utils import  *


class Dashboard(unittest.TestCase):
    def setUp(self):
        self.url = get_url()


    def test_1_get_dashboard(self):
        company_id = get_company_id()
        auth = get_token()
        header = {'authorization': auth}

        response = requests.get(f'{self.url}/dashboard/{company_id}', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        self.assertIn('totalProductsSelled', json_data)
        self.assertEqual(type(json_data['totalProductsSelled']), float)

        self.assertIn('percentAveragePresence', json_data)
        self.assertEqual(type(json_data['percentAveragePresence']), float)

        # JOURNEYS
        journeys = json_data['journeys']
        self.assertIn('journeys', json_data)
        self.assertEqual(type(journeys), list)

        for journey in journeys:
            self.assertIn('id', journey)
            self.assertEqual(type(journey['id']), int)

            self.assertIn('sort_order', journey)
            self.assertEqual(type(journey['sort_order']), int)

            self.assertIn('current', journey)
            self.assertEqual(type(journey['current']), bool)

            self.assertIn('open', journey)
            self.assertEqual(type(journey['open']), bool)

        # GOALS
        goals = json_data['goals']

        self.assertIn('goals', json_data)
        self.assertEqual(type(goals), dict)

        self.assertIn('breakevenPoint', goals)
        self.assertEqual(type(goals['breakevenPoint']), float)

        self.assertIn('salesGoal', goals)
        self.assertEqual(type(goals['salesGoal']), float)

        self.assertIn('totalTaxForSale', goals)
        self.assertEqual(type(goals['totalTaxForSale']), float)

        self.assertIn('unitBP', goals)
        self.assertEqual(type(goals['unitBP']), float)

        self.assertIn('unitSG', goals)
        self.assertEqual(type(goals['unitSG']), float)

        # PROGRESS
        progress = json_data['progress']

        self.assertIn('progress', json_data)
        self.assertEqual(type(progress), dict)

        self.assertIn('progressPlaning', progress)
        self.assertEqual(type(progress['progressPlaning']), float)

        self.assertIn('progressRH', progress)
        self.assertEqual(type(progress['progressRH']), float)

        self.assertIn('progressProduction', progress)
        self.assertEqual(type(progress['progressProduction']), int)

        self.assertIn('progressMarketing', progress)
        self.assertEqual(type(progress['progressMarketing']), int)

        self.assertIn('progressFinancial', progress)
        self.assertEqual(type(progress['progressFinancial']), float)


        # SALE DEVOLUTION INFO
        sale_devolution_info = json_data['saleDevolutionInfo']

        self.assertIn('saleDevolutionInfo', json_data)
        self.assertEqual(type(sale_devolution_info), dict)

        self.assertIn('retired', sale_devolution_info)
        self.assertEqual(type(sale_devolution_info['retired']), int)

        self.assertIn('stock', sale_devolution_info)
        self.assertEqual(type(sale_devolution_info['stock']), int)


        # FORMULAS
        formulas = json_data['formulas']

        self.assertIn('formulas', json_data)
        self.assertEqual(type(formulas), dict)

        self.assertIn('actionsProfitability', formulas)
        self.assertEqual(type(formulas['actionsProfitability']), float)

        self.assertIn('totalShareCapital', formulas)
        self.assertEqual(type(formulas['totalShareCapital']), float)

        self.assertIn('productionGoal', formulas)
        self.assertEqual(type(formulas['productionGoal']), float)

        self.assertIn('saleGoal', formulas)
        self.assertEqual(type(formulas['saleGoal']), float)

        # DRE1
        dre1 = json_data['dre1']

        self.assertIn('dre1', json_data)
        self.assertEqual(type(dre1), dict)

        self.assertIn('provider', dre1)
        self.assertEqual(type(dre1['provider']), float)

        self.assertIn('income', dre1)
        self.assertEqual(type(dre1['income']), float)

        self.assertIn('sales', dre1)
        self.assertEqual(type(dre1['sales']), float)

        self.assertIn('rent', dre1)
        self.assertEqual(type(dre1['rent']), float)

        self.assertIn('taxForSales', dre1)
        self.assertEqual(type(dre1['taxForSales']), float)

        self.assertIn('socialCompanyCharges', dre1)
        self.assertEqual(type(dre1['socialCompanyCharges']), float)

        self.assertIn('socialEmployeeCharges', dre1)
        self.assertEqual(type(dre1['socialEmployeeCharges']), float)

        self.assertIn('comissions', dre1)
        self.assertEqual(type(dre1['comissions']), float)

        self.assertIn('netProfit', dre1)
        self.assertEqual(type(dre1['netProfit']), float)

        self.assertIn('taxes', dre1)
        self.assertEqual(type(dre1['taxes']), float)

        self.assertIn('finalProfit', dre1)
        self.assertEqual(type(dre1['finalProfit']), float)

        # DRE2
        dre2 = json_data['dre2']

        self.assertIn('dre2', json_data)
        self.assertEqual(type(dre2), dict)

        self.assertIn('provider', dre2)
        self.assertEqual(type(dre2['provider']), float)

        self.assertIn('income', dre2)
        self.assertEqual(type(dre2['income']), float)

        self.assertIn('sales', dre2)
        self.assertEqual(type(dre2['sales']), float)

        self.assertIn('rent', dre2)
        self.assertEqual(type(dre2['rent']), float)

        self.assertIn('taxForSales', dre2)
        self.assertEqual(type(dre2['taxForSales']), float)

        self.assertIn('socialCompanyCharges', dre2)
        self.assertEqual(type(dre2['socialCompanyCharges']), float)

        self.assertIn('socialEmployeeCharges', dre2)
        self.assertEqual(type(dre2['socialEmployeeCharges']), float)

        self.assertIn('comissions', dre2)
        self.assertEqual(type(dre2['comissions']), float)

        self.assertIn('netProfit', dre2)
        self.assertEqual(type(dre2['netProfit']), float)

        self.assertIn('taxes', dre2)
        self.assertEqual(type(dre2['taxes']), float)

        self.assertIn('finalProfit', dre2)
        self.assertEqual(type(dre2['finalProfit']), float)
        print()


    def test_2_get_dashboard_goals(self):
        company_id = get_company_id()
        auth = get_token()
        header = {'authorization': auth}

        response = requests.get(f'{self.url}/dashboard/goals/{company_id}', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        self.assertEqual(type(json_data), dict)

        goals = json_data

        self.assertIn('breakevenPoint', goals)
        self.assertEqual(type(goals['breakevenPoint']), float)

        self.assertIn('salesGoal', goals)
        self.assertEqual(type(goals['salesGoal']), float)

        self.assertIn('totalTaxForSale', goals)
        self.assertEqual(type(goals['totalTaxForSale']), float)

        self.assertIn('unitBP', goals)
        self.assertEqual(type(goals['unitBP']), float)

        self.assertIn('unitSG', goals)
        self.assertEqual(type(goals['unitSG']), float)
        print()