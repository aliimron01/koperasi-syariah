from odoo import api, fields, models, _

class PermohonanPinjaman(models.Model):

    _name = "permohonan.pinjaman"
    
    name = fields.Char(
        string='Kode',
        default='New',
        copy=False, required=True, readonly=True)

    anggota_id = fields.Many2one(
        'koperasi.anggota', 
        required=True
    )

    periode_pinjaman = fields.Selection(
        [
            ('12','12'),
            ('24','24'),
            ('36','36'),
            ('48','48'),
            ('60','60')
        ],
        string="Periode Pinjaman"
    )

    nilai_pinjaman = fields.Integer('Nilai Pinjaman')

    administrasi = fields.Integer('Jasa / Administrasi')

    no_rek = fields.Char('No Rek Bank')

    bank_id = fields.Many2one(
        'res.bank', 'Bank')

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('seq.permohonan.pinjaman') or '/'
        return super(PermohonanPinjaman, self).create(vals)

