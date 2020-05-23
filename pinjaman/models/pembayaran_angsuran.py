from odoo import api, fields, models, _

class PembayaranAngsuran(models.Model):
    _name = "pembayaran.angsuran"

    name = fields.Char(
        string='Kode',
        default='New',
        copy=False, required=True, readonly=True)

    anggota_id = fields.Many2one(
        'koperasi.anggota', 
        required=True
    )

    nominal_angsuran = fields.Integer('Nominal Angsuran')

    no_rek = fields.Char('No Rek Bank')

    bank_id = fields.Many2one(
        'res.bank', 'Bank')


    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('seq.pembayaran.angsuran') or '/'
        return super(PembayaranAngsuran, self).create(vals)