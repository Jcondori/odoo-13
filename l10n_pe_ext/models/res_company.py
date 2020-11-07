# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = "res.company"

    def _localization_use_documents(self):
        """ Peruvian localization use documents """
        self.ensure_one()
        return True if self.country_id == self.env.ref('base.pe') else super()._localization_use_documents()
