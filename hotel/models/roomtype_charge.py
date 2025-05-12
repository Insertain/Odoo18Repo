from odoo import models, fields

class RoomTypeCharge(models.Model):
    _name = 'hotel.roomtype.charge'
    _description = 'Room Type Daily Charge'

    roomtype_id = fields.Many2one('hotel.roomtypes', string='Room Type', ondelete='cascade')
    charge_name = fields.Char('Charge Name')
    amount = fields.Float('Amount')
    description = fields.Char('Description')
