import logging
from flask import current_app
from flask import request, send_file, make_response, send_from_directory
from flask_restplus import Resource
from flanken_api.api.flanken.parsers import referral_update_arguments
from flanken_api.api.restplus import api
from flanken_api.api.flanken.business import  get_probio_blood_referrals, get_psff_blood_referrals, update_referrals
from flanken_api.api.flanken.serializers import probio_ref_data_list, psff_ref_data_list

log = logging.getLogger(__name__)
ns2 = api.namespace('referral', description='Referral Database API')

@ns2.route('/')
@api.response(200, 'Check API status')
@api.response(400, '/nfs is not mount locally no data found')
class ReferralStatus(Resource):
    def get(self):
        """
        Referral API status check
        ```

        ```
        """
        return 'Working', 200


@ns2.route('/probio')
@api.response(200, 'Fetched all probio referals')
@api.response(400, '/nfs is not mount locally no data found')
class ProbioReferral(Resource):
    @api.marshal_with(probio_ref_data_list)
    def get(self):
        """
        Fetch all probio referrals records
        ```

        ```
        """
        result, errorcode = get_probio_blood_referrals()
        return result, errorcode


@ns2.route('/psff')
@api.response(200, 'Fetched all psff referals')
@api.response(400, '/nfs is not mount locally no data found')
class PsffReferral(Resource):
    @api.marshal_with(psff_ref_data_list)
    def get(self):
        """
        Fetch all psff referrals records
        ```

        ```
        """
        result, errorcode = get_psff_blood_referrals()
        return result, errorcode


@ns2.route('/update')
@api.response(200, 'Fetched all psff referals')
@api.response(400, '/nfs is not mount locally no data found')
class ReferralUpdate(Resource):
    @api.expect(referral_update_arguments, validate=True)
    def get(self):
        """
        Fetch all psff referrals records
        ```

        ```
        """
        args = referral_update_arguments.parse_args()
        result, errorcode = update_referrals(args['db_name'])
        return result, errorcode








