from flanken_api.database import db
from flanken_api.database.models import ProbioBloodReferral as probio
from flanken_api.database.models import PSFFBloodReferral as psff
import os, io
#from flanken_api.settings import MOUNT_POINT
from flask import current_app
from flanken_api.util_notfound import Not_found
import json
import csv
import re
import ast
from flask import jsonify
import subprocess

def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')





def check_nfs_mount(file_path=None):
    "Check anchorage is mount to /nfs"


    if os.path.exists(file_path) and len(file_path) > 0:
        return  True, 200
    else :
        return False, 400



def get_sample_design_ids(project_path, sample_id):
    "get all sample design ids for given sample id"


    capture_dir = project_path + '/' + sample_id
    status, error =  check_nfs_mount(capture_dir)
    if not status:
        return {'sample_capture': [], 'status': False}, error

    sample_capture_list = list(filter(lambda x: (x.startswith('PB-') or x.startswith('LB-') or x.startswith('AL-') or x.startswith('OT-') or x.startswith('PSFF-')),
                os.listdir(capture_dir)))

    if len(sample_capture_list) < 1:
        return {'sample_capture': [], 'status': False}, 400

    return {'sample_capture': sample_capture_list, 'status': True}, 200


def get_sample_ids(project_path):
    "Get all probio samples"
    status, error = check_nfs_mount(project_path)

    if status:

        files = list(filter(lambda x: x.startswith('P-'), os.listdir(project_path)))
        files.sort(key=lambda x : os.path.getmtime(project_path + '/' + x), reverse=True)
        return {'sidis': files, 'status': True}, error

    return {'sidis': [], 'status': False}, error

def get_static_frankenplot(project_path, project_name, sample_id, capture_id):
    "return the static franken plots as image"

    file_path = project_path + '/' + sample_id + '/' + capture_id + '/qc/'
    temp_url_list = []
    ip_addr = run_cmd('hostname -I').split(' ')[0]
    status = True if os.path.exists(file_path) and len(os.listdir(file_path)) > 0 else False
    if status:
        for each_file in filter(lambda x: x.endswith('liqbio-cna.png') and not x.startswith('.'), os.listdir(file_path)):
            #temp_url_list.append('http://localhost:5000/api/flanken/staticimage?project_name=' + project_name + '&sdid=' + sample_id + '&capture_id=' + capture_id + '&imagename=' + each_file)
            temp_url_list.append('http://' + ip_addr + ':5000/api/flanken/staticimage?project_name=' + project_name + '&sdid=' + sample_id + '&capture_id=' + capture_id + '&imagename=' + each_file)

        if len(temp_url_list) > 0:
            return {'image_url': temp_url_list, 'status': True}, 200

    return {'image_url':[], 'status': False}, 400


def get_static_image(project_path, sample_id, capture_id, image_name):
    """retrun the franken static png image"""

    file_path = project_path + '/' + sample_id + '/' + capture_id + '/qc/' + image_name
    if os.path.exists(file_path):
        return file_path, 200

    return file_path, 400

def get_interactive_plot(project_path, sample_id, capture_id, plotname):
    'retrun the json files to plot interative frankenplots'
    file_path = project_path + '/' + sample_id + '/' + capture_id + '/qc/'
    print(file_path)
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
            'type' : 'text',
            'editable': False
        }

    return head_obj

def generate_headers_ngx_table(headers):
    columns= []
    for each_head in headers:
          columns.append({ 'key': each_head ,'title':each_head})
    return columns

def get_table_svs_header(project_path, sdid, capture_id, header='true'):
    "read structural variant file from sdid_annotate_combined_SV.txt and return as json"
    file_path = project_path + '/' + sdid + '/' + capture_id + '/svs/igv/' +  sdid + '_annotate_combined_SV.txt'
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            reader_ponter = csv.DictReader(f, delimiter ='\t')
            for each_row in reader_ponter:
                data.append(dict(each_row))

            #header = generate_headers_table_sv(data[0].keys())
            header = generate_headers_ngx_table(data[0].keys())
            return {'header': header, 'data': data, 'status': True}, 200

    else:
        return {'header': [], 'data': [], 'status': False}, 400

def get_table_igv(variant_type, project_path, sdid, capture_id, header='true'):
    "read  variant file for given sdid and return as json"

    file_path = project_path + '/' + sdid + '/' + capture_id
    data = []
    missing_header = []


    if variant_type == 'germline':
        regex = '^(?:(?!CFDNA).)*igvnav-input.txt$'
    elif variant_type == 'somatic':
        missing_header = ['GENE', 'IMPACT', 'CONSEQUENCE', 'HGVSp', 'T_DP', 'T_ALT', 'T_VAF', 'N_DP', 'N_ALT', 'N_VAF', 'CLIN_SIG', 'gnomAD', 'BRCAEx', 'OncoKB']
        regex = '.*-CFDNA-.*igvnav-input.txt$'
    else:
        missing_header = ['GENE', 'IMPACT', 'CONSEQUENCE', 'HGVSp', 'N_DP', 'N_ALT', 'N_VAF', 'CLIN_SIG', 'gnomAD', 'BRCAEx', 'OncoKB']
        return {'header': {}, 'data': [], 'status': False, 'error': 'unknown variant type: ' + variant_type}, 400

    try:
        igv_nav_file = list(filter(lambda x: re.match(regex, x) and not x.startswith('.') and not x.endswith('.out'), os.listdir(file_path)))[0]
        igv_nav_file = file_path + '/' + igv_nav_file
        with open(igv_nav_file, 'r') as f:
            reader_pointer = csv.DictReader(f, delimiter='\t')
            for each_row in reader_pointer:
                each_row = dict(each_row)
                print(each_row)
                if None in each_row:
                    if isinstance(each_row[None], list):
                        for i, each_none in enumerate(each_row[None]):
                            each_row[missing_header[i]] = each_none
                        #each_row['Notes'] = " ".join( each_row[None])
                        del each_row[None]

                data.append(dict(each_row))

        #header = generate_headers_table_sv(data[0].keys())
        header = generate_headers_ngx_table(data[0].keys())
        return {'header': header, 'data': data, 'filename' : igv_nav_file, 'status': True}, 200

    except Exception as e:
        return {'header': [], 'data': [], 'status': False, 'error': str(e)}, 400


def save_igvnav_input_file(filename, data):
    "save the igvnav input file with updated calls and tags column"
    try:
        with open(filename, 'w') as fpw:
            headers = data[0].keys()
            writer = csv.DictWriter(fpw, fieldnames=headers, delimiter='\t' )
            writer.writeheader()
            for each_row in data:
                writer.writerow(each_row)

        return str("written to file"), 200

    except Exception as e:
        return str(e), 400

def get_probio_blood_referrals():
    "Fetch the all the records from probio referral database"
    header = ['crid','pnr','rid','datum','tid','sign','countyletter','new','progression','follow_up','cf_dna1','cf_dna2','cf_dna3','kommentar','filnamn']
    try:
        return {'status': True, 'data': probio.query.filter().all(), 'header': generate_headers_ngx_table(header), 'error': '' }, 200
    except Exception as e:
        return {'status': True, 'data': [], 'header': header, 'error': str(e) }, 400

def get_psff_blood_referrals():
    "Fetch the all the records from probio referral database"
    header = ['crid','rid','datum','tid','sign','blood1','blood2','blood3','blood4','comment', 'filnamn', 'cdk']
    try:
        return {'status': True, 'data': psff.query.filter().all(), 'header': generate_headers_ngx_table(header), 'error': '' }, 200
    except Exception as e:
        return {'status': True, 'data': [], 'header': header, 'error': str(e) }, 400


def update_referrals(db_name):
    "Update the referrals data from ftp into postgres db using referral-manager tool"
    referral_conf = {
        'fetch': {
            'common': 'refman --sentry-login /nfs/PROBIO/referraldb/.sentrylogin fetch --referrals-login /nfs/PROBIO/referraldb/referral-manager_conf_files/login.json',
            'probio': ' --local-data-dir /nfs/PROBIO/referraldb/remote_files --remote-data-dir /ProBio2/Scannade_remisser',
            'psff': ' --local-data-dir /nfs/CLINSEQ/PSFF/referraldb/remote_files --remote-data-dir /PSFF/Scannade_remisser',
            'psff_log': '/nfs/CLINSEQ/PSFF/referraldb/referral_db_fetch.log',
            'probio_log': '/nfs/PROBIO/referraldb/referral_db_fetch.log'
        },
        'db_import':{
            'common' : 'refman --sentry-login /nfs/PROBIO/referraldb/.sentrylogin dbimport --dbcred /nfs/PROBIO/referraldb/referral-manager_conf_files/config.json',
            'probio': ' --local-data-dir /nfs/PROBIO/referraldb/remote_files/csv --referral-type ProbioBloodReferral',
            'psff': '--local-data-dir /nfs/CLINSEQ/PSFF/referraldb/remote_files/csv --referral-type PsffBloodReferral',
            'psff_log': '/nfs/CLINSEQ/PSFF/referraldb/referral_db_dbimport.log',
            'probio_log': '/nfs/PROBIO/referraldb/referral_db_dbimport.log'

        }
    }
    try:
        logfile_fetch = open(referral_conf['fetch'][db_name+'_log'], 'w')
        logfile_dbimport = open(referral_conf['db_import'][db_name+'_log'], 'w')
        cmd_fetch = referral_conf['fetch']['common'] + referral_conf['fetch'][db_name]
        cmd_dbimport = referral_conf['db_import']['common'] + referral_conf['db_import'][db_name]
        proc = subprocess.check_call(cmd_fetch, stdout=logfile_fetch, stderr=logfile_fetch)
        proc = subprocess.check_call(cmd_dbimport, stdout=logfile_dbimport, stderr=logfile_dbimport)
        logfile_fetch.close()
        logfile_dbimport.close()
        return {'status': True, 'error': ''}, 200
    except subprocess.CalledProcessError as err:
        logfile_fetch.close()
        logfile_dbimport.close()
        return {'status': False, 'error': err}, 400



