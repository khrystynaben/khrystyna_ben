import unittest
from datetime import *
from pr import*
from copy import deepcopy
from collect import Collection
from shutil import copyfile
from caretaker import CareTaker


class PaymentRequestTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.payments = Collection()
        cls.paym_for_insert = PaymentRequest(880000000000, 'aaaaaaaaaaaaa@gmail.com', 9999.9, 'uah', '2000-01-01', '2021-09-29', '89023894-90')

    def setUp(self):
        self.payments_for_test = deepcopy(PaymentRequestTest.payments)
        copyfile(self.payments_for_test.file_name, 'copy_data.txt')
        self.payments_for_test.file_name = 'copy_data.txt'
        self.handler = CareTaker(self.payments_for_test, 5)
        self.sorted_emails = ['bilochka@gmail.com','khrystyna.ben@gmail.com','oryslava.kalyniak@ukr.net','ustia.ben@gmail.com','vika.gavlo@ukr.net']
        #self.serched = PaymentRequest(8695066767, 'vika.gavlo@ukr.net', 8900.0, 'uah', '2020-02-15', '2020-03-07', '14536700-23')
        self.sorted_ids = [1445566767,3489022751,4695066767, 6930238767, 9403367679]
        self.sorted_currency = ['euro','uah','uah','usd', 'usd']
        self.sorted_amount = [3000.0,4600.45,5500.0,8900.0,33678.9]
        self.sorted_pr_date = ['2002-01-18','2007-08-13', '2018-12-05', '2019-08-20','2020-02-15']
        self.sorted_pd_date = ['2002-02-07', '2007-09-03', '2018-12-26', '2019-09-11', '2020-03-07']
        self.sorted_transact_id = ['14536700-23', '24511767-29', '34566709-23', '71556792-14', '73569712-45']
        

    def test_search(self):
        self.assertTrue(self.payments_for_test.search2('vika'))
        self.assertFalse(self.payments_for_test.search2('mikki'))

    def test_insert(self):
        self.payments_for_test.insert(PaymentRequestTest.paym_for_insert)
        self.assertTrue(self.payments_for_test.search2('aaaaaaaaaaaa'))

    def test_sort_ids(self):
        self.payments_for_test.sort('_ID')
        for payment, id_ in zip(self.payments_for_test.payments,self.sorted_ids):
            self.assertEqual(payment._ID,id_ )

    def test_sort_emails(self):
        self.payments_for_test.sort('_payer_email')
        for payment, email in zip(self.payments_for_test.payments, self.sorted_emails):
            self.assertEqual(payment._payer_email, email)
    
    def test_sort_amount(self):
        self.payments_for_test.sort('_amount')
        for payment, amnt in zip(self.payments_for_test.payments, self.sorted_amount):
            self.assertEqual(payment._amount, amnt)

    def test_sort_currency(self):
        self.payments_for_test.sort('_currency')
        for payment, curren in zip(self.payments_for_test.payments, self.sorted_currency):
            self.assertEqual(payment._currency, curren)
        
    def test_sort_pr_date(self):
        self.payments_for_test.sort('_payment_request_date')
        for payment, pr_date in zip(self.payments_for_test.payments, self.sorted_pr_date):
            self.assertEqual(payment._payment_request_date.strftime('%Y-%m-%d'), pr_date)

    def test_sort_pd_date(self):
        self.payments_for_test.sort('_payment_due_to_date')
        for payment, pd_date in zip(self.payments_for_test.payments, self.sorted_pd_date):
            self.assertEqual(payment._payment_due_to_date.strftime('%Y-%m-%d'), pd_date)
    
    def test_sort_transact_id(self):
        self.payments_for_test.sort('_transaction_id')
        for payment, transact in zip(self.payments_for_test.payments, self.sorted_transact_id):
            self.assertEqual(payment._transaction_id, transact)

    def test_erase(self):
        self.payments_for_test.erase(3445566767)
        self.assertFalse(self.payments_for_test.search2('3445566767'))

    def test_replace(self):
        self.payments_for_test.edit(4695066767)
        self.assertTrue(self.payments_for_test.search2('bbbbbbbbbb'))
        self.assertFalse(self.payments_for_test.search2('4695066767'))

    def test_backup(self):
        self.handler.backup()
        self.assertEqual(len(self.handler.states),1)

    def test_backup2(self):
        self.handler.backup()
        self.payments_for_test.insert(PaymentRequestTest.paym_for_insert)
        self.handler.backup()
        self.payments_for_test.insert(PaymentRequestTest.paym_for_insert)
        self.handler.backup()
        self.payments_for_test.sort('_ID')
        self.handler.backup()
        self.payments_for_test.sort('_payer_email')
        self.handler.backup()
        self.payments_for_test.erase(3445566767)
        self.handler.backup()
        self.assertEqual(len(self.handler.states),5)

    def test_undo(self):
        self.handler.backup()
        self.payments_for_test.insert(PaymentRequestTest.paym_for_insert)
        self.handler.undo()
        self.assertFalse(self.payments_for_test.search2('aaaaaaaaaaaa'))

    def test_redo(self):
        self.handler.backup()
        self.payments_for_test.insert(PaymentRequestTest.paym_for_insert)
        self.handler.backup()
        self.payments_for_test.sort('_ID')
        self.handler.undo()
        self.handler.undo()
        self.handler.redo()
        self.assertTrue(self.payments_for_test.search2('aaaaaaaaaaaa'))


if __name__ == "__main__":
    unittest.main()