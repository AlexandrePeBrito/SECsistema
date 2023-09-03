from django.test import TestCase
from sistemaSec.nte.models import NTE

class NTETestCase(TestCase):
    
    def setUp(self):
        NTE.objects.create(
            nome_direitor_NTE = "Alexandre Pereira Brito",
            telefone_NTE = "(71)99966-3589",
            email_NTE = "teste@gmail.com"
        )
        NTE.objects.create(
            nome_direitor_NTE = "Maiure Pereira Brito",
            telefone_NTE = "(71)99966-3589",
            email_NTE = "teste@gmail.com"
        )

    def test_returna_str(self):
        nte1 = NTE.objects.get(nome_direitor_NTE = "Alexandre Pereira Brito")
        nte2 = NTE.objects.get(nome_direitor_NTE = "Maiure Pereira Brito")

        self.assertEqual(nte1.__str__(),'1')
        self.assertEqual(nte2.__str__(),'2')