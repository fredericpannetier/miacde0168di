# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MIADI_EtiquetteParameter(models.Model):
    _name = "miadi_etiquette.parameter"
    _description = "Parameters"
    _order = "name"
    
    name = fields.Char(string="Name", required=True)
    value = fields.Char(string="Value", required=True)
    
    