#!/usr/bin/env python

# Import modules for CGI handling 
import cgi, cgitb
import matlab.engine


print "Content-type: text/html\n"

# Create instance of FieldStorage 
form = cgi.FieldStorage()

# Get data from fields
file_input = form.getvalue('file_input')
preprocessing_method = form.getvalue('preprocessing_method')
classification_method = form.getvalue('classification_method')

function_path = 'D:/TUGAS AKHIR/Progress/SIDANG/Source Code/Classification'
file_input = 'D:/TUGAS AKHIR/Progress/SIDANG/DEMO/' + file_input

# Create matlab file
eng = matlab.engine.start_matlab()

# Call matlab function
eng.eval("cd '"+function_path+"';",nargout=0)
eng.eval("[valence,arousal] = getPrediction('"+file_input+"','"+preprocessing_method+"','"+classification_method+"');",nargout=0)
valence = eng.workspace["valence"]
arousal = eng.workspace["arousal"]

if valence==3.0:
    strValence = '''<img src="../img/class/hv.png" width="100%"> 
                                                <h4 class="text-center">High Valence</h4>'''
else:
    strValence = '''<img src="../img/class/lv.png" width="100%"> 
                                                <h4 class="text-center">Low Valence</h4>'''

if arousal==3.0:
    strArousal = '''<img src="../img/class/ha.png" width="100%"> 
                                                <h4 class="text-center">High Arousal</h4>'''
else:
    strArousal = '''<img src="../img/class/la.png" width="100%"> 
                                                <h4 class="text-center">Low Arousal</h4>'''

if valence==1.0 and arousal==3.0:
    strClass = '''<img src="../img/class/halv.png" width="100%">
                                                <h4 class="text-center">Class 1</h4>'''

elif valence==3.0 and arousal==3.0:
    strClass = '''<img src="../img/class/hahv.png" width="100%">
                                                <h4 class="text-center">Class 2</h4>'''

elif valence==3.0 and arousal==1.0:
    strClass = '''<img src="../img/class/lahv.png" width="100%">
                                                <h4 class="text-center">Class 3</h4>'''

elif valence==1.0 and arousal==1.0:
    strClass = '''<img src="../img/class/lalv.png" width="100%">
                                                <h4 class="text-center">Class 4</h4>'''

if preprocessing_method=='fft':
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
                    <div class="col-lg-12">
                        <div class="panel panel-info">
                            <div class="panel-body">
                                <!-- Nav tabs -->
                                <ul class="nav nav-tabs">
                                    <li class="active"><a href="#emotiv-channels" data-toggle="tab">Emotiv Channels</a>
                                    </li>
                                    <li><a href="#raw-data" data-toggle="tab">Raw Data</a>
                                    </li>
                                    <li><a href="#fast-fourier-transformation" data-toggle="tab">Fast Fourier Transformation</a>
                                    </li>
                                    <li><a href="#prediction-result" data-toggle="tab">Prediction Result</a>
                                    </li>
                                </ul>

                                <!-- Tab panes -->
                                <div class="tab-content">
                                    <div class="tab-pane fade in active" id="emotiv-channels">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-4"></div>
                                            <div class="col-lg-4">
                                                <img src="../img/emotiv_channel.png" width="100%">
                                                <h4 class="text-center">Emotiv Channels</h4>
                                            </div>
                                            <div class="col-lg-4"></div>
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="raw-data">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/1.png" width="100%">
                                                <h4 class="text-center">AF3</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/2.png" width="100%">
                                                <h4 class="text-center">F7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/3.png" width="100%">
                                                <h4 class="text-center">F3</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/4.png" width="100%">
                                                <h4 class="text-center">FC5</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/5.png" width="100%">
                                                <h4 class="text-center">T7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/6.png" width="100%">
                                                <h4 class="text-center">P7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/7.png" width="100%">
                                                <h4 class="text-center">O1</h4>
                                            </div>
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/8.png" width="100%">
                                                <h4 class="text-center">O2</h4>
                                            </div>
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/9.png" width="100%">
                                                <h4 class="text-center">P8</h4>
                                            </div>
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/10.png" width="100%">
                                                <h4 class="text-center">T8</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/11.png" width="100%">
                                                <h4 class="text-center">FC6</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/12.png" width="100%">
                                                <h4 class="text-center">F4</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/13.png" width="100%">
                                                <h4 class="text-center">F8</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4"></div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/14.png" width="100%">
                                                <h4 class="text-center">AF4</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="fast-fourier-transformation">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/fft/delta.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Delta</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/fft/theta.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Theta</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/fft/alpha.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Alpha</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/fft/beta.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Beta</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/fft/gamma.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Gamma</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="prediction-result">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-2"></div>
                                            <div class="col-lg-2">'''+strValence+'''</div>
                                            <div class="col-lg-4"></div>
                                            <div class="col-lg-2">'''+strArousal+'''</div>
                                            <div class="col-lg-2"></div>
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-4"></div>
                                            <div class="col-lg-4">'''+strClass+'''</div>
                                            <div class="col-lg-4"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /.panel-body -->
                        </div>
                        <!-- /.panel -->
                    </div>
                    <!-- /.col-lg-12 -->
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

if preprocessing_method=='ica_fft':
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
                    <div class="col-lg-12">
                        <div class="panel panel-info">
                            <div class="panel-body">
                                <!-- Nav tabs -->
                                <ul class="nav nav-tabs">
                                    <li class="active"><a href="#emotiv-channels" data-toggle="tab">Emotiv Channels</a>
                                    </li>
                                    <li><a href="#raw-data" data-toggle="tab">Raw Data</a>
                                    </li>
                                    <li><a href="#independent-component-analysis" data-toggle="tab">Independent Component Analysis</a>
                                    </li>
                                    <li><a href="#fast-fourier-transformation" data-toggle="tab">Fast Fourier Transformation</a>
                                    </li>
                                    <li><a href="#prediction-result" data-toggle="tab">Prediction Result</a>
                                    </li>
                                </ul>

                                <!-- Tab panes -->
                                <div class="tab-content">
                                    <div class="tab-pane fade in active" id="emotiv-channels">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-4"></div>
                                            <div class="col-lg-4">
                                                <img src="../img/emotiv_channel.png" width="100%">
                                                <h4 class="text-center">Emotiv Channels</h4>
                                            </div>
                                            <div class="col-lg-4"></div>
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="raw-data">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/1.png" width="100%">
                                                <h4 class="text-center">AF3</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/2.png" width="100%">
                                                <h4 class="text-center">F7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/3.png" width="100%">
                                                <h4 class="text-center">F3</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/4.png" width="100%">
                                                <h4 class="text-center">FC5</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/5.png" width="100%">
                                                <h4 class="text-center">T7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/6.png" width="100%">
                                                <h4 class="text-center">P7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/7.png" width="100%">
                                                <h4 class="text-center">O1</h4>
                                            </div>
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/8.png" width="100%">
                                                <h4 class="text-center">O2</h4>
                                            </div>
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/9.png" width="100%">
                                                <h4 class="text-center">P8</h4>
                                            </div>
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/10.png" width="100%">
                                                <h4 class="text-center">T8</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/11.png" width="100%">
                                                <h4 class="text-center">FC6</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/12.png" width="100%">
                                                <h4 class="text-center">F4</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/13.png" width="100%">
                                                <h4 class="text-center">F8</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4"></div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/14.png" width="100%">
                                                <h4 class="text-center">AF4</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="independent-component-analysis">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/ica/1.png" width="100%">
                                                <h4 class="text-center">AF3</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/2.png" width="100%">
                                                <h4 class="text-center">F7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/3.png" width="100%">
                                                <h4 class="text-center">F3</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/ica/4.png" width="100%">
                                                <h4 class="text-center">FC5</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/5.png" width="100%">
                                                <h4 class="text-center">T7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/6.png" width="100%">
                                                <h4 class="text-center">P7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/ica/7.png" width="100%">
                                                <h4 class="text-center">O1</h4>
                                            </div>
                                            <div class="col-lg-4">
                                                <img src="../img/ica/8.png" width="100%">
                                                <h4 class="text-center">O2</h4>
                                            </div>
                                            <div class="col-lg-4">
                                                <img src="../img/ica/9.png" width="100%">
                                                <h4 class="text-center">P8</h4>
                                            </div>
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/ica/10.png" width="100%">
                                                <h4 class="text-center">T8</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/11.png" width="100%">
                                                <h4 class="text-center">FC6</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/12.png" width="100%">
                                                <h4 class="text-center">F4</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/ica/13.png" width="100%">
                                                <h4 class="text-center">F8</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4"></div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/14.png" width="100%">
                                                <h4 class="text-center">AF4</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="fast-fourier-transformation">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/fft/delta.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Delta</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/fft/theta.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Theta</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/fft/alpha.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Alpha</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/fft/beta.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Beta</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/fft/gamma.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Gamma</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="prediction-result">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-2"></div>
                                            <div class="col-lg-2">'''+strValence+'''</div>
                                            <div class="col-lg-4"></div>
                                            <div class="col-lg-2">'''+strArousal+'''</div>
                                            <div class="col-lg-2"></div>
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-4"></div>
                                            <div class="col-lg-4">'''+strClass+'''</div>
                                            <div class="col-lg-4"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /.panel-body -->
                        </div>
                        <!-- /.panel -->
                    </div>
                    <!-- /.col-lg-12 -->
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

if preprocessing_method=='swt':
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
                    <div class="col-lg-12">
                        <div class="panel panel-info">
                            <div class="panel-body">
                                <!-- Nav tabs -->
                                <ul class="nav nav-tabs">
                                    <li class="active"><a href="#emotiv-channels" data-toggle="tab">Emotiv Channels</a>
                                    </li>
                                    <li><a href="#raw-data" data-toggle="tab">Raw Data</a>
                                    </li>
                                    <li><a href="#stationery-wavelet-transform" data-toggle="tab">Stationery Wavelet Transform</a>
                                    </li>
                                    <li><a href="#prediction-result" data-toggle="tab">Prediction Result</a>
                                    </li>
                                </ul>

                                <!-- Tab panes -->
                                <div class="tab-content">
                                    <div class="tab-pane fade in active" id="emotiv-channels">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-4"></div>
                                            <div class="col-lg-4">
                                                <img src="../img/emotiv_channel.png" width="100%">
                                                <h4 class="text-center">Emotiv Channels</h4>
                                            </div>
                                            <div class="col-lg-4"></div>
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="raw-data">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/1.png" width="100%">
                                                <h4 class="text-center">AF3</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/2.png" width="100%">
                                                <h4 class="text-center">F7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/3.png" width="100%">
                                                <h4 class="text-center">F3</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/4.png" width="100%">
                                                <h4 class="text-center">FC5</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/5.png" width="100%">
                                                <h4 class="text-center">T7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/6.png" width="100%">
                                                <h4 class="text-center">P7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/7.png" width="100%">
                                                <h4 class="text-center">O1</h4>
                                            </div>
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/8.png" width="100%">
                                                <h4 class="text-center">O2</h4>
                                            </div>
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/9.png" width="100%">
                                                <h4 class="text-center">P8</h4>
                                            </div>
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/10.png" width="100%">
                                                <h4 class="text-center">T8</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/11.png" width="100%">
                                                <h4 class="text-center">FC6</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/12.png" width="100%">
                                                <h4 class="text-center">F4</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/13.png" width="100%">
                                                <h4 class="text-center">F8</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4"></div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/14.png" width="100%">
                                                <h4 class="text-center">AF4</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="stationery-wavelet-transform">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/swt/a5.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Approximation 5</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/swt/d5.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Detail 5</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/swt/d4.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Detail 4</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/swt/d3.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Detail 3</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/swt/d2.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Detail 2</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="prediction-result">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-2"></div>
                                            <div class="col-lg-2">'''+strValence+'''</div>
                                            <div class="col-lg-4"></div>
                                            <div class="col-lg-2">'''+strArousal+'''</div>
                                            <div class="col-lg-2"></div>
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-4"></div>
                                            <div class="col-lg-4">'''+strClass+'''</div>
                                            <div class="col-lg-4"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /.panel-body -->
                        </div>
                        <!-- /.panel -->
                    </div>
                    <!-- /.col-lg-12 -->
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

if preprocessing_method=='ica_swt':
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
                    <div class="col-lg-12">
                        <div class="panel panel-info">
                            <div class="panel-body">
                                <!-- Nav tabs -->
                                <ul class="nav nav-tabs">
                                    <li class="active"><a href="#emotiv-channels" data-toggle="tab">Emotiv Channels</a>
                                    </li>
                                    <li><a href="#raw-data" data-toggle="tab">Raw Data</a>
                                    </li>
                                    <li><a href="#independent-component-analysis" data-toggle="tab">Independent Component Analysis</a>
                                    </li>
                                    <li><a href="#stationery-wavelet-transform" data-toggle="tab">Stationery Wavelet Transform</a>
                                    </li>
                                    <li><a href="#prediction-result" data-toggle="tab">Prediction Result</a>
                                    </li>
                                </ul>

                                <!-- Tab panes -->
                                <div class="tab-content">
                                    <div class="tab-pane fade in active" id="emotiv-channels">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-4"></div>
                                            <div class="col-lg-4">
                                                <img src="../img/emotiv_channel.png" width="100%">
                                                <h4 class="text-center">Emotiv Channels</h4>
                                            </div>
                                            <div class="col-lg-4"></div>
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="raw-data">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/1.png" width="100%">
                                                <h4 class="text-center">AF3</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/2.png" width="100%">
                                                <h4 class="text-center">F7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/3.png" width="100%">
                                                <h4 class="text-center">F3</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/4.png" width="100%">
                                                <h4 class="text-center">FC5</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/5.png" width="100%">
                                                <h4 class="text-center">T7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/6.png" width="100%">
                                                <h4 class="text-center">P7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/7.png" width="100%">
                                                <h4 class="text-center">O1</h4>
                                            </div>
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/8.png" width="100%">
                                                <h4 class="text-center">O2</h4>
                                            </div>
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/9.png" width="100%">
                                                <h4 class="text-center">P8</h4>
                                            </div>
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/10.png" width="100%">
                                                <h4 class="text-center">T8</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/11.png" width="100%">
                                                <h4 class="text-center">FC6</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/12.png" width="100%">
                                                <h4 class="text-center">F4</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/13.png" width="100%">
                                                <h4 class="text-center">F8</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4"></div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/raw_data/14.png" width="100%">
                                                <h4 class="text-center">AF4</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="independent-component-analysis">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/ica/1.png" width="100%">
                                                <h4 class="text-center">AF3</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/2.png" width="100%">
                                                <h4 class="text-center">F7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/3.png" width="100%">
                                                <h4 class="text-center">F3</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/ica/4.png" width="100%">
                                                <h4 class="text-center">FC5</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/5.png" width="100%">
                                                <h4 class="text-center">T7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/6.png" width="100%">
                                                <h4 class="text-center">P7</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/ica/7.png" width="100%">
                                                <h4 class="text-center">O1</h4>
                                            </div>
                                            <div class="col-lg-4">
                                                <img src="../img/ica/8.png" width="100%">
                                                <h4 class="text-center">O2</h4>
                                            </div>
                                            <div class="col-lg-4">
                                                <img src="../img/ica/9.png" width="100%">
                                                <h4 class="text-center">P8</h4>
                                            </div>
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/ica/10.png" width="100%">
                                                <h4 class="text-center">T8</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/11.png" width="100%">
                                                <h4 class="text-center">FC6</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/12.png" width="100%">
                                                <h4 class="text-center">F4</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                        <!-- /.row -->
                                        <div class="row">
                                            <div class="col-lg-4">
                                                <img src="../img/ica/13.png" width="100%">
                                                <h4 class="text-center">F8</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4"></div>
                                            <!-- /.col-lg-4 -->
                                            <div class="col-lg-4">
                                                <img src="../img/ica/14.png" width="100%">
                                                <h4 class="text-center">AF4</h4>
                                            </div>
                                            <!-- /.col-lg-4 -->
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="stationery-wavelet-transform">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/swt/a5.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Approximation 5</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/swt/d5.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Detail 5</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/swt/d4.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Detail 4</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/swt/d3.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Detail 3</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                            <div class="col-lg-10">
                                                <img src="../img/swt/d2.png" width="100%"  height="200px"> 
                                                <h4 class="text-center">Detail 2</h4>
                                            </div>
                                            <!-- /.col-lg-10 -->
                                            <div class="col-lg-1"></div>
                                            <!-- /.col-lg-1 -->
                                        </div>
                                    </div>
                                    <div class="tab-pane fade" id="prediction-result">
                                        <br/>
                                        <div class="row">
                                            <div class="col-lg-2"></div>
                                            <div class="col-lg-2">'''+strValence+'''</div>
                                            <div class="col-lg-4"></div>
                                            <div class="col-lg-2">'''+strArousal+'''</div>
                                            <div class="col-lg-2"></div>
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-4"></div>
                                            <div class="col-lg-4">'''+strClass+'''</div>
                                            <div class="col-lg-4"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /.panel-body -->
                        </div>
                        <!-- /.panel -->
                    </div>
                    <!-- /.col-lg-12 -->
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