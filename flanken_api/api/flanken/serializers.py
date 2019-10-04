from flask_restplus import fields
from flanken_api.api.restplus import api

status_result = api.model('server status', {'server_status': fields.Boolean(default=False, required=True)})

list = fields.String()
dropdownlist = api.model('Dropdown list for sample ids ',{'sidis': fields.List(list), 'status':fields.Boolean(required=True)})
dropdownlist_capture = api.model('Dropdown list for capture ids ',{'sample_capture': fields.List(list), 'status':fields.Boolean(required=True)})

ploturl_list = api.model('List the rul for static franken plots', {'image_url': fields.List(list), 'status':fields.Boolean(required=True)})

probio_ref_data = api.model('ProbioBloodReferral', {
    'crid': fields.String(description='referral id for reach record'),
    'pnr': fields.String(description='personal number of patient'),
    'rid': fields.String(description='referral id'),
    'datum': fields.String(description='date and of entry'),
    'tid': fields.String(description='tid of sample'),
    'sign': fields.String(description='binary stautus 1 or 0 '),
    'countyletter': fields.String(description='hospital code'),
    'new': fields.String(description='new'),
    'progression': fields.String(description='state of progression'),
    'follow_up': fields.String(description='status to follow_up'),
    'cf_dna1': fields.String(description='proof read 1'),
    'cf_dna2': fields.String(description='proof read 2'),
    'cf_dna3': fields.String(description='proof read 3'),
    'kommentar': fields.String(description='comments of each sample'),
    'filnamn': fields.String(description='path to sample report in pdf '),

})

psff_ref_data = api.model('PsffBloodReferral', {
    'crid': fields.String(description='referral id for reach record'),
    'rid': fields.String(description='referral id'),
    'datum': fields.String(description='date and of entry'),
    'tid': fields.String(description='tid of sample'),
    'sign': fields.String(description='binary stautus 1 or 0 '),
    'blood1': fields.String(description='proof read 1'),
    'blood2': fields.String(description='proof read 2'),
    'blood3': fields.String(description='proof read 3'),
    'blood4': fields.String(description='proof read 4'),
    'comment': fields.String(description='comments on case'),
    'filnamn': fields.String(description='path to sample report in pdf '),
    'cdk': fields.String(description='cdk id')
})

header = api.model('Probio header', {'key':fields.String(description='Column name') , 'title': fields.String(description='Column display name')})
#probio_ref_data_list = api.model('Referral DB Data', { 'status':fields.Boolean(required=True), 'data': fields.List(fields.Nested(probio_ref_data)), 'header': fields.List(fields.Nested(header)), 'error':fields.String() }
probio_ref_data_list = api.model('Referral DB Data', { 'status':fields.Boolean(required=True), 'data': fields.List(fields.Nested(probio_ref_data)), 'header': fields.List(fields.Nested(header)), 'error': fields.String()})


header_psff = api.model('Psff header', {'key':fields.String(description='Column name') , 'title': fields.String(description='Column display name')})
psff_ref_data_list = api.model('Referral DB Data', { 'status':fields.Boolean(required=True), 'data': fields.List(fields.Nested(psff_ref_data)), 'header': fields.List(fields.Nested(header_psff)), 'error': fields.String()})


referral_db_out =  api.model('Referral DB update', { 'status':fields.Boolean(required=True), 'error': fields.String()})
