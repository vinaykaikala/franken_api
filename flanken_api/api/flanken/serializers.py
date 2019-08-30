from flask_restplus import fields
from flanken_api.api.restplus import api

status_result = api.model('server status', {'server_status': fields.Boolean(default=False, required=True)})

list = fields.String()
dropdownlist = api.model('Dropdown list for sample ids ',{'sidis': fields.List(list), 'status':fields.Boolean(required=True)})
dropdownlist_capture = api.model('Dropdown list for capture ids ',{'sample_capture': fields.List(list), 'status':fields.Boolean(required=True)})

ploturl_list = api.model('List the rul for static franken plots', {'image_url': fields.List(list), 'status':fields.Boolean(required=True)})

