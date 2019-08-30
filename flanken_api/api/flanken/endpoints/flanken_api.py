import logging

from flask import request, send_file, make_response, send_from_directory
from flask_restplus import Resource
#from flanken_api.api.flanken.serializers import search_result
from flanken_api.api.flanken.parsers import search_arguments, capture_arguments, ploturls_arguments, staticplot_arguments, igv_arguments
from flanken_api.api.restplus import api
from flask import jsonify
from flanken_api.api.flanken.business import check_nfs_mount, get_sample_ids, get_sample_design_ids, get_static_frankenplot, get_static_image, get_interactive_plot
from flanken_api.api.flanken.serializers import status_result, dropdownlist, dropdownlist_capture, ploturl_list
import io
#import  flanken_api.database.models 
log = logging.getLogger(__name__)
ns = api.namespace('flanken', description='Interactive Flanken Plots')

@ns.route('/')
@api.response(200, 'Status of API')
@api.response(400, '/nfs is not mount locally')
class FlankenStatus(Resource):
    @api.marshal_with(status_result)
    def get(self):
        """
        Returns status of the endpoint.
        ```
        {
            "server_status": true
        }

        ```
        """
        status, error_code = check_nfs_mount()
        result = {'server_status': True}

        if not status:
            return {'server_status': False}, error_code


        return result, error_code

@ns.route('/samples')
@api.response(200, 'All Samples for dropdown')
@api.response(400, '/nfs is not mount locally no data found')
class DropdownListSample(Resource):
    @api.marshal_with(dropdownlist)
    def get(self):
        """
        Returns List of sample ids for dropdown in UI.
        ```
        [sdid1, sdid2,......]
        ```
        """
        result, errorcode = get_sample_ids()
        return result, errorcode

@ns.route('/capture')
@api.response(200, 'All Samples for dropdown')
@api.response(400, '/nfs is not mount locally no data found')
class DropdownListCapture(Resource):
    @api.expect(capture_arguments, validate=True)
    @api.marshal_with(dropdownlist_capture)
    def get(self):
        """
        Returns List of capture ids for given sample ids which are used for dropdown in UI.
        ```
        [cpture_id1, capture2,......]
        ```
        """
        args = capture_arguments.parse_args()
        result, errorcode = get_sample_design_ids(args['sdid'])
        return result, errorcode


@ns.route('/ploturls')
@api.response(200, 'Franken plot urls')
@api.response(400, 'No franken plot images found in qc folder')
class FrankenUrls(Resource):
    @api.expect(ploturls_arguments, validate=True)
    @api.marshal_with(ploturl_list)
    def get(self):
        """
        Returns List of franken plot url.
        ```
        [url1, url2,......]
        ```
        """
        args = ploturls_arguments.parse_args()
        result, errorcode = get_static_frankenplot(args['sdid'], args['capture_id'])
        return result, errorcode


@ns.route('/staticimage')
@api.response(200, 'Franken Static plot')
@api.response(400, 'No Static plots found')
class FrankenStaticImages(Resource):
    @api.representation('image/png')
    @api.expect(staticplot_arguments, validate=True)
    def get(self):
        """
        Returns static franken plot.
        ```
        base64 of png
        ```
        """
        args = staticplot_arguments.parse_args()
        result, errorcode = get_static_image(args['sdid'], args['capture_id'], args['imagename'])
        return send_file(result,
                      attachment_filename='frankenplot.png',
                      mimetype='image/png')

@ns.route('/plot')
@api.response(200, 'Json file to plot')
@api.response(400, 'sample or json file not found')
class FlankenPlot(Resource):
    @api.expect(search_arguments, validate=True)
    def get(self):
        """
        Returns Json file to plot.
        ```
        Json data to plot the flanken plots
        ```
        """
        args = search_arguments.parse_args()
        result , errocode = get_interactive_plot( args['sdid'], args['capture_id'], args['pname'])
        return result, errocode




@ns.route('/igvfiles')
@api.response(200, 'Files to load in igv tracks')
@api.response(400, 'No file found')
class IGVTracksFiles(Resource):
    @api.expect(igv_arguments, validate=True)
    def get(self):
        """
        Returns Files Required To Load in IGV Tracks
        ```
        bam, vcf etc.
        ```
        """
        args = igv_arguments.parse_args()
        if args['filename'] == '1':
            return send_from_directory('/nfs/PROBIO/autoseq-output/P-00356971/PB-P-00356971-CFDNA-03589573-KH20190515-C220190515_PB-P-00356971-N-03589575-KH20190515-C220190515/bams/C2',
                             'PB-P-00356971-CFDNA-03589573-KH-C2-nodups.bam' )

        return send_from_directory('/nfs/PROBIO/autoseq-output/P-00356971/PB-P-00356971-CFDNA-03589573-KH20190515-C220190515_PB-P-00356971-N-03589575-KH20190515-C220190515/bams/C2',
                         'PB-P-00356971-CFDNA-03589573-KH-C2-nodups.bam.bai')
        #return send_from_directory('/nfs/PROBIO/autoseq-output/P-00356971/PB-P-00356971-CFDNA-03589573-KH20190515-C220190515_PB-P-00356971-N-03589575-KH20190515-C220190515/bams/C2/', 'PB-P-00356971-CFDNA-03589573-KH-C2-nodups.bam.bai')
