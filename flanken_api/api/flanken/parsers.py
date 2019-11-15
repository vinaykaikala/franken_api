from flask_restplus import reqparse

project_arguments = reqparse.RequestParser()
project_arguments.add_argument('project_name', choices=('PROBIO', 'PSFF'), required=True,
                              help="valid Project names: 'PROBIO', 'PSFF")

capture_arguments = reqparse.RequestParser()
capture_arguments.add_argument('project_name', choices=('PROBIO', 'PSFF'), required=True,
                              help="valid Project names: 'PROBIO', 'PSFF")
capture_arguments.add_argument('sdid', type=str, required=True,  help='sdid example : P-00360714')


common_arguments = reqparse.RequestParser()
common_arguments.add_argument('project_name', choices=('PROBIO', 'PSFF'), required=True,
                              help="valid Project names: 'PROBIO', 'PSFF")
common_arguments.add_argument('sdid', type=str, required=True,  help='sdid example : P-00360714')
common_arguments.add_argument('capture_id', type=str, required=True,  help='capture id')


search_arguments = common_arguments.copy()
search_arguments.add_argument('pname', choices=('normal', 'variant_allelic', 'plot_AR', 'snpratio', 'scatter_plot', 'snpratio_density', 'scatter_density_plot' ), required=True,
                              help="valid plot names: 'normal', 'variant_allelic', 'plot_AR', 'snpratio', 'scatter_plot','scatter_density_plot', 'snpratio_density.json'")


ploturls_arguments = common_arguments.copy()


staticplot_arguments = common_arguments.copy()
staticplot_arguments.add_argument('imagename', type=str, required=True,  help='static franken plot name')


igv_arguments =  common_arguments.copy()
igv_arguments.add_argument('filename', type=str, required=True,  help='file required for igv track creation')


table_svs_arguments =  common_arguments.copy()
table_svs_arguments.add_argument('header', choices=('true', 'false'), default='true', required=True,  help='Boolen True or False : True returns only column header')


table_igvnav_arguments = table_svs_arguments.copy()

table_qc_arguments = table_svs_arguments.copy()

igv_save_file_arguments = reqparse.RequestParser()
igv_save_file_arguments.add_argument('file_name',  required=True, help="igvnav-input.txt as File Name  ")
igv_save_file_arguments.add_argument('data',  type=str, required=True, help="Jsondata")


referral_update_arguments  = reqparse.RequestParser()
referral_update_arguments.add_argument('db_name', choices=('probio', 'psff'), required=True,
                              help="provide db name to updae the referral db for probio / psff")










