import logging
from flask import current_app
from flask import request, send_file, make_response, send_from_directory
from flask_restplus import Resource
from flanken_api.api.flanken.parsers import curation_germline_arguments, curation_somatic_arguments, curation_svs_arguments
from flanken_api.api.restplus import api
from flanken_api.api.flanken.business import  get_curation_igv_germline, get_curation_igv_somatic, get_curation_svs
from flanken_api.api.flanken.serializers import curation_germline, germline_data_list, somatic_data_list, svs_data_list

log = logging.getLogger(__name__)
ns3 = api.namespace('curation DB', description='Curation Database API')

@ns3.route('/')
@api.response(200, 'Check API status')
@api.response(400, '/nfs is not mount locally no data found')
class CurationStatus(Resource):
    def get(self):
        """
        Referral API status check
        ```

        ```
        """
        return 'Working', 200


@ns3.route('/curation/igv/germline')
@api.response(200, 'Success')
@api.response(400, '/nfs is not mount locally no data found')
class CurationIgvGermline(Resource):
    @api.marshal_with(germline_data_list)
    def get(self):
        """
        Fetch all Germline
        ```

        ```
        """
        result, error = get_curation_igv_germline()
        return result, error

    @api.expect(curation_germline_arguments, validate=True)
    def post(self):
        """
        Fetch all Germline
        ```

        ```
        """
        result, errorcode = get_curation_igv_germline()
        return result, errorcode

@ns3.route('/curation/igv/somatic')
@api.response(200, 'Success')
@api.response(400, '/nfs is not mount locally no data found')
class CurationIgvSomatic(Resource):
    @api.marshal_with(somatic_data_list)
    def get(self):
        """
        Fetch all Somatic
        ```

        ```
        """
        result, error = get_curation_igv_somatic()
        return result, error

    @api.expect(curation_somatic_arguments, validate=True)
    def post(self):
        """
        Fetch all Germline
        ```

        ```
        """

        return '', 200

@ns3.route('/curation/svs')
@api.response(200, 'Success')
@api.response(400, '/nfs is not mount locally no data found')
class CurationSVS(Resource):
    @api.marshal_with(svs_data_list)
    def get(self):
        """
        Fetch all Somatic
        ```

        ```
        """
        result, error = get_curation_svs()
        return result, error

    @api.expect(curation_svs_arguments, validate=True)
    def post(self):
        """
        Fetch all Germline
        ```

        ```
        """

        return '', 200





