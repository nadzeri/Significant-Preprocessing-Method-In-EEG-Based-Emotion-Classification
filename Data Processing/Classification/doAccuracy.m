function [jmlBenar,rata_rata,tp,tn,fp,fn] = doAccuracy(method,class,method_classification)
    project_path = strcat(pwd,'\..\..');
%     method='ica_swt';%'ica_fft','swt','ica_swt';
%     class='valence';%'valence';
%     method_classification='svm';%'svm';
    
    datasets = saveDatasets(project_path,method,class);
    label = separateClass(project_path,method,class);
    [datasets,label] = getTwoClass(datasets,label);
    [jmlBenar,rata_rata,tp,tn,fp,fn] = findAccuracy(datasets,label,method_classification);
end