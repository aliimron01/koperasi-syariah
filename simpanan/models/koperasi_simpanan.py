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

    jumlah_pengambilan = fields.Integer('Jumlah Pengambilan')

    jenis_simpanan_id = fields.Many2one(
        'koperasi.jenis.simpanan',
        string='Jenis Simpanan'
    )

    @api.onchange('account_id')
    def _compute_total_simpanan(self):
        total_penyetoran = sum(self.account_id.penyetoran_simpanan_ids.mapped('nilai_simpanan'))
        total_pengambilan = sum(self.account_id.pengambilan_simpanan_ids.mapped('jumlah_pengambilan'))
        self.total_simpanan = total_penyetoran - total_pengambilan




    # total_simpanan = fields.Integer('Total Simpanan', compute='_compute_total_simpanan')
    total_simpanan = fields.Integer('Total Simpanan')

    # @api.depends('code')
    # def _compute_account_root(self):
    #     # this computes the first 2 digits of the account.
    #     # This field should have been a char, but the aim is to use it in a side panel view with hierarchy, and it's only supported by many2one fields so far.
    #     # So instead, we make it a many2one to a psql view with what we need as records.
    #     for record in self:
    #         record.root_id = record.code and (ord(record.code[0]) * 1000 + ord(record.code[1])) or False

    # def _compute_number_entries(self):
    #     data = self.env['account.move.line'].read_group([('reconcile_model_id', 'in', self.ids)], ['reconcile_model_id'], 'reconcile_model_id')
    #     mapped_data = dict([(d['reconcile_model_id'][0], d['reconcile_model_id_count']) for d in data])
    #     for model in self:
    #         model.number_entries = mapped_data.get(model.id, 0)

    # number_entries = fields.Integer(string='Number of entries related to this model', compute='_compute_number_entries')


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