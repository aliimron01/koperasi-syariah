from odoo import api, fields, models, _

class KoperasiAnggota(models.Model):
    _name = "koperasi.anggota"
    
    no_anggota = fields.Char(
    string='No Anggota', default='New',
    copy=False, required=True, readonly=True)

    name = fields.Char('Nama', required=True)
    alamat = fields.Text(string="Alamat", required=True)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ],default="male",string="Jenis Kelamin")

    birthday = fields.Date('Tanggal Lahir', required=True)

    place_of_birth = fields.Char('Tempat Lahir', required=True)

    umur = fields.Integer(string="Umur", compute="_hitung_umur", default=0)

    ibu_kandung = fields.Char(
        string="Nama Ibu Kandung",
        required=True
    )

    kontak_darurat = fields.Char(
        string="Kontak Darurat",
        required=True
    )

    telepon = fields.Char(
        string="Telepon",
        required=True
    )

    hubungan = fields.Char(
        string="Hubungan",
        required=True
    )

    tanggal_daftar = fields.Date(
        string="Tanggal Pendaftaran",
        required=True
    )

    email = fields.Char(
        string="Email",
        required=True
    )

    mobile_no = fields.Char(
        string="Phone/Mobile No",
        required=True
    )

    bank_id = fields.Many2one(
        'res.bank', 'Bank')

    no_rek = fields.Char(
        string="No Rekening"
    )

    def _hitung_umur(self):
        umur_saat_ini = 0
        for i in self:
            if i.birthday == False:
                continue
            else:
                from datetime import date
                selisih = date.today() - i.birthday
                umur_saat_ini = int(selisih.days / 365 //1)
        self.umur = umur_saat_ini

    @api.model
    def create(self, vals):
        if vals.get('no_anggota', '/') == '/':
            vals['no_anggota'] = self.env['ir.sequence'].next_by_code('seq.anggota') or '/'
        return super(KoperasiAnggota, self).create(vals)