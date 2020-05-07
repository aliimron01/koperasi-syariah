from odoo import api, fields, models, _

class PinjamanAnggota(models.Model):
    _name = "pinjaman.anggota"
    
    name = fields.Char(
        string='Kode',
        default='New',
        copy=False, required=True, readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('seq.anggota') or '/'
        return super(KoperasiPengambilanSimpanan, self).create(vals)

