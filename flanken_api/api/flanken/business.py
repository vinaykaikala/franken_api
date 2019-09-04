from flanken_api.database import db
import os, io
from flanken_api.settings import MOUNT_POINT
from flanken_api.util_notfound import Not_found
import json
import csv



def check_nfs_mount(file_path=None):
    "Check anchorage is mount to /nfs"

    if os.path.exists(MOUNT_POINT) and len(os.listdir(MOUNT_POINT)) > 0:
        return  True, 200
    else :
        return False, 400



def get_sample_design_ids(sample_id):
    "get all sample design ids for given sample id"


    capture_dir = MOUNT_POINT + '/' + sample_id
    sample_capture_list = list(filter(lambda x: (x.startswith('PB-') or x.startswith('LB-') or x.startswith('AL-')),
                os.listdir(capture_dir)))

    if len(sample_capture_list) < 1:
        return {'sample_capture': [], 'status': False}, 400

    return {'sample_capture': sample_capture_list, 'status': True}, 200


def get_sample_ids():
    "Get all probio samples"
    status, error = check_nfs_mount()

    if status:
        return {'sidis': list(filter(lambda x: x.startswith('P-'), os.listdir(MOUNT_POINT))), 'status': True}, error

    return {'sidis': [], 'status': False}, error

def get_static_frankenplot(sample_id, capture_id):
    "return the static franken plots as image"

    file_path = MOUNT_POINT + '/' + sample_id + '/' + capture_id + '/qc/'
    temp_url_list = []
    status = True if os.path.exists(file_path) and len(os.listdir(file_path)) > 0 else False
    if status:
        for each_file in filter(lambda x: x.endswith('liqbio-cna.png') and not x.startswith('.'), os.listdir(file_path)):
            temp_url_list.append('http://localhost:5000/api/flanken/staticimage?sdid=' + sample_id + '&capture_id=' + capture_id + '&imagename=' + each_file)

        if len(temp_url_list) > 0:
            return {'image_url': temp_url_list, 'status': True}, 200

    return {'image_url':[], 'status': False}, 400


def get_static_image(sample_id, capture_id, image_name):
    """retrun the franken static png image"""

    file_path = MOUNT_POINT + '/' + sample_id + '/' + capture_id + '/qc/' + image_name
    if os.path.exists(file_path):
        return file_path, 200

    return file_path, 400

def get_interactive_plot(sample_id, capture_id, plotname):
    'retrun the json files to plot interative frankenplots'
    file_path = MOUNT_POINT + '/' + sample_id + '/' + capture_id + '/qc/'
    status = True if os.path.exists(file_path) and len(os.listdir(file_path)) > 0 else False
    if status:
        for each_file in filter(lambda x: x.endswith('_' + plotname + '.json'),
                                os.listdir(file_path)):
            with open(file_path + each_file, 'r') as f:
                return {'plot_data': json.load(f), 'status': True}, 200

    return {'plot_data': {}, 'status': False}, 400

def generate_headers_table_sv(headers):
    head_obj = {}
    for each_head in headers:
        head_obj[each_head] = {
            'title':each_head,
            'type' : 'string',
            'editable': False
        }

    return head_obj

def get_table_svs_header(sdid, capture_id, header='true'):
    "read structural variant file from sdid_annotate_combined_SV.txt and return as json"
    file_path = MOUNT_POINT + '/' + sdid + '/' + capture_id + '/svs/igv/' +  sdid + '_annotate_combined_SV.txt'
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            reader_ponter = csv.DictReader(f, delimiter ='\t')
            for each_row in reader_ponter:
                data.append(dict(each_row))

            header = generate_headers_table_sv(data[0].keys())
            return {'header': header, 'data': data, 'status': True}, 200

    else:
        return {'header': {}, 'data': [], 'status': False}, 400


