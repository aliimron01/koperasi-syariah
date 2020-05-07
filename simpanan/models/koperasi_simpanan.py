from odoo import api, fields, models, _

class KoperasiPenyetoranSimpanan(models.Model):
    _name = "koperasi.penyetoran.simpanan"

    name = fields.Char(
        string='Kode',
        default='New',
        copy=False, required=True, readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('seq.anggota') or '/'
        return super(KoperasiPenyetoranSimpanan, self).create(vals)


    account_id = fields.Many2one(
        'koperasi.anggota', 
        required=True
    )

    jenis_simpanan_id = fields.Many2one(
        'koperasi.jenis.simpanan',
        string='Jenis Simpanan'
    )

    nilai_simpanan = fields.Integer('Nilai Simpanan')

    no_rek = fields.Char('No Rek Bank')

    bank_id = fields.Many2one(
        'res.bank', 'Bank')





class KoperasiPengambilanSimpanan(models.Model):
    _name = "koperasi.pengambilan.simpanan"

    name = fields.Char(
        string='Kode',
        default='New',
        copy=False, required=True, readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('seq.anggota') or '/'
        return super(KoperasiPengambilanSimpanan, self).create(vals)

    account_id = fields.Many2one(
        'koperasi.anggota', 
        required=True
    )

    jenis_simpanan_id = fields.Many2one(
        'koperasi.jenis.simpanan',
        string='Jenis Simpanan'
    )

    nilai_simpanan = fields.Integer('Nilai Simpanan')

    # No Anggota,
    # Nama Anggota,
    # Jenis Simpanan
    # Nilai Simpanan


class JenisSimpanan(models.Model):
    _name = "koperasi.jenis.simpanan"

    kode = fields.Char('Kode')

    name = fields.Char(
        string="Nama",
        required=True
    )

    keterangan = fields.Char(
        string="Keterangan"
    )