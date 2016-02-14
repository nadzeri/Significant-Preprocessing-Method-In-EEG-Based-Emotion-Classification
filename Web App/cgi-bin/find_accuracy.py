#!/usr/bin/env python

# Import modules for CGI handling 
import cgi, cgitb
import matlab.engine


print "Content-type: text/html\n"

# Create matlab file
eng = matlab.engine.start_matlab()

# Classification matlab path
function_path = 'D:/TUGAS AKHIR/Progress/SIDANG/Source Code/Classification'

# Call matlab function
eng.eval("cd '"+function_path+"';",nargout=0)

#Valence FFT
(t,r,tp_valence_fft_knn,tn_valence_fft_knn,fp_valence_fft_knn,fn_valence_fft_knn) = eng.eval("doAccuracy('fft','valence','knn');",nargout=6);
(t,r,tp_valence_fft_svm,tn_valence_fft_svm,fp_valence_fft_svm,fn_valence_fft_svm) = eng.eval("doAccuracy('fft','valence','svm');",nargout=6);

#Valence ICA + FFT
(t,r,tp_valence_ica_fft_knn,tn_valence_ica_fft_knn,fp_valence_ica_fft_knn,fn_valence_ica_fft_knn) = eng.eval("doAccuracy('ica_fft','valence','knn');",nargout=6);
(t,r,tp_valence_ica_fft_svm,tn_valence_ica_fft_svm,fp_valence_ica_fft_svm,fn_valence_ica_fft_svm) = eng.eval("doAccuracy('ica_fft','valence','svm');",nargout=6);

#Valence SWT
(t,r,tp_valence_swt_knn,tn_valence_swt_knn,fp_valence_swt_knn,fn_valence_swt_knn) = eng.eval("doAccuracy('swt','valence','knn');",nargout=6);
(t,r,tp_valence_swt_svm,tn_valence_swt_svm,fp_valence_swt_svm,fn_valence_swt_svm) = eng.eval("doAccuracy('swt','valence','svm');",nargout=6);

#Valence ICA + SWT
(t,r,tp_valence_ica_swt_knn,tn_valence_ica_swt_knn,fp_valence_ica_swt_knn,fn_valence_ica_swt_knn) = eng.eval("doAccuracy('ica_swt','valence','knn');",nargout=6);
(t,r,tp_valence_ica_swt_svm,tn_valence_ica_swt_svm,fp_valence_ica_swt_svm,fn_valence_ica_swt_svm) = eng.eval("doAccuracy('ica_swt','valence','svm');",nargout=6);

#Arousal FFT
(t,r,tp_arousal_fft_knn,tn_arousal_fft_knn,fp_arousal_fft_knn,fn_arousal_fft_knn) = eng.eval("doAccuracy('fft','arousal','knn');",nargout=6);
(t,r,tp_arousal_fft_svm,tn_arousal_fft_svm,fp_arousal_fft_svm,fn_arousal_fft_svm) = eng.eval("doAccuracy('fft','arousal','svm');",nargout=6);

#Arousal ICA + FFT
(t,r,tp_arousal_ica_fft_knn,tn_arousal_ica_fft_knn,fp_arousal_ica_fft_knn,fn_arousal_ica_fft_knn) = eng.eval("doAccuracy('ica_fft','arousal','knn');",nargout=6);
(t,r,tp_arousal_ica_fft_svm,tn_arousal_ica_fft_svm,fp_arousal_ica_fft_svm,fn_arousal_ica_fft_svm) = eng.eval("doAccuracy('ica_fft','arousal','svm');",nargout=6);

#Arousal SWT
(t,r,tp_arousal_swt_knn,tn_arousal_swt_knn,fp_arousal_swt_knn,fn_arousal_swt_knn) = eng.eval("doAccuracy('swt','arousal','knn');",nargout=6);
(t,r,tp_arousal_swt_svm,tn_arousal_swt_svm,fp_arousal_swt_svm,fn_arousal_swt_svm) = eng.eval("doAccuracy('swt','arousal','svm');",nargout=6);

#Arousal ICA + SWT
(t,r,tp_arousal_ica_swt_knn,tn_arousal_ica_swt_knn,fp_arousal_ica_swt_knn,fn_arousal_ica_swt_knn) = eng.eval("doAccuracy('ica_swt','arousal','knn');",nargout=6);
(t,r,tp_arousal_ica_swt_svm,tn_arousal_ica_swt_svm,fp_arousal_ica_swt_svm,fn_arousal_ica_swt_svm) = eng.eval("doAccuracy('ica_swt','arousal','svm');",nargout=6);

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
    <link href="../css/accuracy.css" rel="stylesheet">

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
                <div class="col-lg-3">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Fast Fourier Transformation
                        </div>
                        <div class="panel-body">
                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    K-Neirest Neighbord
                                </div>
                                <!-- /.panel-heading -->
                                <div class="panel-body">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Valence
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_valence_fft_knn)+'''</td>
                                                            <td>FP : '''+str(fp_valence_fft_knn)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_valence_fft_knn)+'''</td>
                                                            <td>FN : '''+str(fn_valence_fft_knn)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_valence_fft_knn)+''' + '''+str(tn_valence_fft_knn)+''') / '''+str(tp_valence_fft_knn+fp_valence_fft_knn+tn_valence_fft_knn+fn_valence_fft_knn)+'''</p>
                                                <p>Acc = <b>'''+str((tp_valence_fft_knn+tn_valence_fft_knn)/(tp_valence_fft_knn+tn_valence_fft_knn+fp_valence_fft_knn+fn_valence_fft_knn))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->

                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Arousal
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_arousal_fft_knn)+'''</td>
                                                            <td>FP : '''+str(fp_arousal_fft_knn)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_arousal_fft_knn)+'''</td>
                                                            <td>FN : '''+str(fn_arousal_fft_knn)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_arousal_fft_knn)+''' + '''+str(tn_arousal_fft_knn)+''') / '''+str(tp_arousal_fft_knn+fp_arousal_fft_knn+tn_arousal_fft_knn+fn_arousal_fft_knn)+'''</p>
                                                <p>Acc = <b>'''+str((tp_arousal_fft_knn+tn_arousal_fft_knn)/(tp_arousal_fft_knn+tn_arousal_fft_knn+fp_arousal_fft_knn+fn_arousal_fft_knn))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->
                                </div>
                                <!-- /.panel-body -->
                            </div>
                            <!-- /.panel -->

                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    Support Vector Machine
                                </div>
                                <!-- /.panel-heading -->
                                <div class="panel-body">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Valence
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_valence_fft_svm)+'''</td>
                                                            <td>FP : '''+str(fp_valence_fft_svm)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_valence_fft_svm)+'''</td>
                                                            <td>FN : '''+str(fn_valence_fft_svm)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_valence_fft_svm)+''' + '''+str(tn_valence_fft_svm)+''') / '''+str(tp_valence_fft_svm+fp_valence_fft_svm+tn_valence_fft_svm+fn_valence_fft_svm)+'''</p>
                                                <p>Acc = <b>'''+str((tp_valence_fft_svm+tn_valence_fft_svm)/(tp_valence_fft_svm+tn_valence_fft_svm+fp_valence_fft_svm+fn_valence_fft_svm))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->

                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Arousal
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_arousal_fft_svm)+'''</td>
                                                            <td>FP : '''+str(fp_arousal_fft_svm)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_arousal_fft_svm)+'''</td>
                                                            <td>FN : '''+str(fn_arousal_fft_svm)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_arousal_fft_svm)+''' + '''+str(tn_arousal_fft_svm)+''') / '''+str(tp_arousal_fft_svm+fp_arousal_fft_svm+tn_arousal_fft_svm+fn_arousal_fft_svm)+'''</p>
                                                <p>Acc = <b>'''+str((tp_arousal_fft_svm+tn_arousal_fft_svm)/(tp_arousal_fft_svm+tn_arousal_fft_svm+fp_arousal_fft_svm+fn_arousal_fft_svm))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->
                                </div>
                                <!-- /.panel-body -->
                            </div>
                            <!-- /.panel -->
                        </div>
                    </div>
                </div>

                <div class="col-lg-3">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            ICA + Fast Fourier Transformation
                        </div>
                        <div class="panel-body">
                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    K-Neirest Neighbord
                                </div>
                                <!-- /.panel-heading -->
                                <div class="panel-body">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Valence
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_valence_ica_fft_knn)+'''</td>
                                                            <td>FP : '''+str(fp_valence_ica_fft_knn)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_valence_ica_fft_knn)+'''</td>
                                                            <td>FN : '''+str(fn_valence_ica_fft_knn)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_valence_ica_fft_knn)+''' + '''+str(tn_valence_ica_fft_knn)+''') / '''+str(tp_valence_ica_fft_knn+fp_valence_ica_fft_knn+tn_valence_ica_fft_knn+fn_valence_ica_fft_knn)+'''</p>
                                                <p>Acc = <b>'''+str((tp_valence_ica_fft_knn+tn_valence_ica_fft_knn)/(tp_valence_ica_fft_knn+tn_valence_ica_fft_knn+fp_valence_ica_fft_knn+fn_valence_ica_fft_knn))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->

                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Arousal
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_arousal_ica_fft_knn)+'''</td>
                                                            <td>FP : '''+str(fp_arousal_ica_fft_knn)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_arousal_ica_fft_knn)+'''</td>
                                                            <td>FN : '''+str(fn_arousal_ica_fft_knn)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_arousal_ica_fft_knn)+''' + '''+str(tn_arousal_ica_fft_knn)+''') / '''+str(tp_arousal_ica_fft_knn+fp_arousal_ica_fft_knn+tn_arousal_ica_fft_knn+fn_arousal_ica_fft_knn)+'''</p>
                                                <p>Acc = <b>'''+str((tp_arousal_ica_fft_knn+tn_arousal_ica_fft_knn)/(tp_arousal_ica_fft_knn+tn_arousal_ica_fft_knn+fp_arousal_ica_fft_knn+fn_arousal_ica_fft_knn))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->
                                </div>
                                <!-- /.panel-body -->
                            </div>
                            <!-- /.panel -->

                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    Support Vector Machine
                                </div>
                                <!-- /.panel-heading -->
                                <div class="panel-body">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Valence
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_valence_ica_fft_svm)+'''</td>
                                                            <td>FP : '''+str(fp_valence_ica_fft_svm)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_valence_ica_fft_svm)+'''</td>
                                                            <td>FN : '''+str(fn_valence_ica_fft_svm)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_valence_ica_fft_svm)+''' + '''+str(tn_valence_ica_fft_svm)+''') / '''+str(tp_valence_ica_fft_svm+fp_valence_ica_fft_svm+tn_valence_ica_fft_svm+fn_valence_ica_fft_svm)+'''</p>
                                                <p>Acc = <b>'''+str((tp_valence_ica_fft_svm+tn_valence_ica_fft_svm)/(tp_valence_ica_fft_svm+tn_valence_ica_fft_svm+fp_valence_ica_fft_svm+fn_valence_ica_fft_svm))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->

                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Arousal
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_arousal_ica_fft_svm)+'''</td>
                                                            <td>FP : '''+str(fp_arousal_ica_fft_svm)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_arousal_ica_fft_svm)+'''</td>
                                                            <td>FN : '''+str(fn_arousal_ica_fft_svm)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_arousal_ica_fft_svm)+''' + '''+str(tn_arousal_ica_fft_svm)+''') / '''+str(tp_arousal_ica_fft_svm+fp_arousal_ica_fft_svm+tn_arousal_ica_fft_svm+fn_arousal_ica_fft_svm)+'''</p>
                                                <p>Acc = <b>'''+str((tp_arousal_ica_fft_svm+tn_arousal_ica_fft_svm)/(tp_arousal_ica_fft_svm+tn_arousal_ica_fft_svm+fp_arousal_ica_fft_svm+fn_arousal_ica_fft_svm))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->
                                </div>
                                <!-- /.panel-body -->
                            </div>
                            <!-- /.panel -->
                        </div>
                    </div>
                </div>

                <div class="col-lg-3">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Stationery Wavelet Transformation
                        </div>
                        <div class="panel-body">
                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    K-Neirest Neighbord
                                </div>
                                <!-- /.panel-heading -->
                                <div class="panel-body">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Valence
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_valence_swt_knn)+'''</td>
                                                            <td>FP : '''+str(fp_valence_swt_knn)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_valence_swt_knn)+'''</td>
                                                            <td>FN : '''+str(fn_valence_swt_knn)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_valence_swt_knn)+''' + '''+str(tn_valence_swt_knn)+''') / '''+str(tp_valence_swt_knn+fp_valence_swt_knn+tn_valence_swt_knn+fn_valence_swt_knn)+'''</p>
                                                <p>Acc = <b>'''+str((tp_valence_swt_knn+tn_valence_swt_knn)/(tp_valence_swt_knn+tn_valence_swt_knn+fp_valence_swt_knn+fn_valence_swt_knn))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->

                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Arousal
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_arousal_swt_knn)+'''</td>
                                                            <td>FP : '''+str(fp_arousal_swt_knn)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_arousal_swt_knn)+'''</td>
                                                            <td>FN : '''+str(fn_arousal_swt_knn)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_arousal_swt_knn)+''' + '''+str(tn_arousal_swt_knn)+''') / '''+str(tp_arousal_swt_knn+fp_arousal_swt_knn+tn_arousal_swt_knn+fn_arousal_swt_knn)+'''</p>
                                                <p>Acc = <b>'''+str((tp_arousal_swt_knn+tn_arousal_swt_knn)/(tp_arousal_swt_knn+tn_arousal_swt_knn+fp_arousal_swt_knn+fn_arousal_swt_knn))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->
                                </div>
                                <!-- /.panel-body -->
                            </div>
                            <!-- /.panel -->

                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    Support Vector Machine
                                </div>
                                <!-- /.panel-heading -->
                                <div class="panel-body">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Valence
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_valence_swt_svm)+'''</td>
                                                            <td>FP : '''+str(fp_valence_swt_svm)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_valence_swt_svm)+'''</td>
                                                            <td>FN : '''+str(fn_valence_swt_svm)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_valence_swt_svm)+''' + '''+str(tn_valence_swt_svm)+''') / '''+str(tp_valence_swt_svm+fp_valence_swt_svm+tn_valence_swt_svm+fn_valence_swt_svm)+'''</p>
                                                <p>Acc = <b>'''+str((tp_valence_swt_svm+tn_valence_swt_svm)/(tp_valence_swt_svm+tn_valence_swt_svm+fp_valence_swt_svm+fn_valence_swt_svm))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->

                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Arousal
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_arousal_swt_svm)+'''</td>
                                                            <td>FP : '''+str(fp_arousal_swt_svm)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_arousal_swt_svm)+'''</td>
                                                            <td>FN : '''+str(fn_arousal_swt_svm)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_arousal_swt_svm)+''' + '''+str(tn_arousal_swt_svm)+''') / '''+str(tp_arousal_swt_svm+fp_arousal_swt_svm+tn_arousal_swt_svm+fn_arousal_swt_svm)+'''</p>
                                                <p>Acc = <b>'''+str((tp_arousal_swt_svm+tn_arousal_swt_svm)/(tp_arousal_swt_svm+tn_arousal_swt_svm+fp_arousal_swt_svm+fn_arousal_swt_svm))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->
                                </div>
                                <!-- /.panel-body -->
                            </div>
                            <!-- /.panel -->
                        </div>
                    </div>
                </div>

                <div class="col-lg-3">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            ICA + Stationery Wavelet Transformation
                        </div>
                        <div class="panel-body">
                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    K-Neirest Neighbord
                                </div>
                                <!-- /.panel-heading -->
                                <div class="panel-body">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Valence
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_valence_ica_swt_knn)+'''</td>
                                                            <td>FP : '''+str(fp_valence_ica_swt_knn)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_valence_ica_swt_knn)+'''</td>
                                                            <td>FN : '''+str(fn_valence_ica_swt_knn)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_valence_ica_swt_knn)+''' + '''+str(tn_valence_ica_swt_knn)+''') / '''+str(tp_valence_ica_swt_knn+fp_valence_ica_swt_knn+tn_valence_ica_swt_knn+fn_valence_ica_swt_knn)+'''</p>
                                                <p>Acc = <b>'''+str((tp_valence_ica_swt_knn+tn_valence_ica_swt_knn)/(tp_valence_ica_swt_knn+tn_valence_ica_swt_knn+fp_valence_ica_swt_knn+fn_valence_ica_swt_knn))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->

                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Arousal
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_arousal_ica_swt_knn)+'''</td>
                                                            <td>FP : '''+str(fp_arousal_ica_swt_knn)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_arousal_ica_swt_knn)+'''</td>
                                                            <td>FN : '''+str(fn_arousal_ica_swt_knn)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_arousal_ica_swt_knn)+''' + '''+str(tn_arousal_ica_swt_knn)+''') / '''+str(tp_arousal_ica_swt_knn+fp_arousal_ica_swt_knn+tn_arousal_ica_swt_knn+fn_arousal_ica_swt_knn)+'''</p>
                                                <p>Acc = <b>'''+str((tp_arousal_ica_swt_knn+tn_arousal_ica_swt_knn)/(tp_arousal_ica_swt_knn+tn_arousal_ica_swt_knn+fp_arousal_ica_swt_knn+fn_arousal_ica_swt_knn))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->
                                </div>
                                <!-- /.panel-body -->
                            </div>
                            <!-- /.panel -->

                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    Support Vector Machine
                                </div>
                                <!-- /.panel-heading -->
                                <div class="panel-body">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Valence
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_valence_ica_swt_svm)+'''</td>
                                                            <td>FP : '''+str(fp_valence_ica_swt_svm)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_valence_ica_swt_svm)+'''</td>
                                                            <td>FN : '''+str(fn_valence_ica_swt_svm)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_valence_ica_swt_svm)+''' + '''+str(tn_valence_ica_swt_svm)+''') / '''+str(tp_valence_ica_swt_svm+fp_valence_ica_swt_svm+tn_valence_ica_swt_svm+fn_valence_ica_swt_svm)+'''</p>
                                                <p>Acc = <b>'''+str((tp_valence_ica_swt_svm+tn_valence_ica_swt_svm)/(tp_valence_ica_swt_svm+tn_valence_ica_swt_svm+fp_valence_ica_swt_svm+fn_valence_ica_swt_svm))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->

                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            Arousal
                                        </div>
                                        <!-- /.panel-heading -->
                                        <div class="panel-body">
                                            <div class="table-responsive">
                                                <table class="table table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th>#</th>
                                                            <th>1</th>
                                                            <th>2</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <th>1</th>
                                                            <td>TP : '''+str(tp_arousal_ica_swt_svm)+'''</td>
                                                            <td>FP : '''+str(fp_arousal_ica_swt_svm)+'''</td>
                                                        </tr>
                                                        <tr>
                                                            <th>2</th>
                                                            <td>TN : '''+str(tn_arousal_ica_swt_svm)+'''</td>
                                                            <td>FN : '''+str(fn_arousal_ica_swt_svm)+'''</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                            <!-- /.table-responsive -->
                                            <h4>Accuracy : </h4>
                                            <blockquote>
                                                <p>Acc = (TP + TN) / Total Population</p>
                                                <p>Acc = ('''+str(tp_arousal_ica_swt_svm)+''' + '''+str(tn_arousal_ica_swt_svm)+''') / '''+str(tp_arousal_ica_swt_svm+fp_arousal_ica_swt_svm+tn_arousal_ica_swt_svm+fn_arousal_ica_swt_svm)+'''</p>
                                                <p>Acc = <b>'''+str((tp_arousal_ica_swt_svm+tn_arousal_ica_swt_svm)/(tp_arousal_ica_swt_svm+tn_arousal_ica_swt_svm+fp_arousal_ica_swt_svm+fn_arousal_ica_swt_svm))+'''</b></p>
                                            </blockquote>
                                        </div>
                                        <!-- /.panel-body -->
                                    </div>
                                    <!-- /.panel -->
                                </div>
                                <!-- /.panel-body -->
                            </div>
                            <!-- /.panel -->
                        </div>
                    </div>
                </div>
            </div>           
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
