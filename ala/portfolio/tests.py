from django.test import TestCase

class PortfolioTestCase(TestCase):
    def test_portfolio(self):
        res = self.client.get("/portfolio/")
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "portfolio/index.html")