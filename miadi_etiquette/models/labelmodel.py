# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MIADI_EtiquetteLabelModel(models.Model):
    _name = "miadi_etiquette.labelmodel"
    _description = "Label model"
    _order = "name"
    
    code = fields.Char(string="Code", required=True)
    name = fields.Char(string="Name", required=True)
    file = fields.Char(sting="File", required=True,help="Path of the label file")
    commentary = fields.Text(string="Commentary")
    
    _sql_constraints = [("uniq_id","unique(code)","A label already exists with this code. It must be unique !"),]