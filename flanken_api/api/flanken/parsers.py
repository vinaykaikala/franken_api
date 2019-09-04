from flask_restplus import reqparse

search_arguments = reqparse.RequestParser()
search_arguments.add_argument('sdid', type=str, required=True,  help='sdid example : P-00360714')
search_arguments.add_argument('capture_id', type=str, required=True,  help='capture id')
search_arguments.add_argument('pname', choices=('normal', 'variant_allelic', 'plot_AR', 'snpratio', 'scatter_plot', 'snpratio_density', 'scatter_density_plot' ), required=True,
                              help="valid plot names: 'normal', 'variant_allelic', 'plot_AR', 'snpratio', 'scatter_plot','scatter_density_plot', 'snpratio_density.json'")


capture_arguments = reqparse.RequestParser()
capture_arguments.add_argument('sdid', type=str, required=True,  help='sdid example : P-00360714')


ploturls_arguments = reqparse.RequestParser()
ploturls_arguments.add_argument('sdid', type=str, required=True,  help='sdid example : P-00360714')
ploturls_arguments.add_argument('capture_id', type=str, required=True,  help='capture id')

staticplot_arguments = reqparse.RequestParser()
staticplot_arguments.add_argument('sdid', type=str, required=True,  help='sdid example : P-00360714')
staticplot_arguments.add_argument('capture_id', type=str, required=True,  help='capture id')
staticplot_arguments.add_argument('imagename', type=str, required=True,  help='static franken plot name')


igv_arguments = reqparse.RequestParser()
igv_arguments.add_argument('sdid', type=str, required=True,  help='sdid example : P-00360714')
igv_arguments.add_argument('capture_id', type=str, required=True,  help='capture id')
igv_arguments.add_argument('filename', type=str, required=True,  help='file required for igv track creation')


table_svs_arguments = reqparse.RequestParser()
table_svs_arguments.add_argument('sdid', type=str, required=True,  help='sdid example : P-00360714')
table_svs_arguments.add_argument('capture_id', type=str, required=True,  help='capture id')
table_svs_arguments.add_argument('header', choices=('true', 'false'), default='true', required=True,  help='Boolen True or False : True returns only column header')










