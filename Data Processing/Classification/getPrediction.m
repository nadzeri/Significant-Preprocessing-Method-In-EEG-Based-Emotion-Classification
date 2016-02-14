function [valence,arousal] = getPrediction(file_path,preprocessing_method,classification_method)
    %%%%%%%%%%%%%%
    %file_path = 'D:\5112100136 - Muhammad Nadzeri Munawar\TUGAS AKHIR\Datasets\EEG\S04\S04-T13-10.11.15.11.40.03.csv';
    project_path = strcat(pwd,'\..\..');
    %preprocessing_method='fft';%'ica_fft','swt','ica_swt';
    %classification_method='knn';
    channel_v = [10,3,14,5,1,8,6,4,7,11];
    fb_v = [3,4,5];
    features_v = [2,3];
    
    channel_a = [3,13,10,2,1,12,4,7,8,11];
    fb_a = [3,4,5];
    features_a = [2,3];
    %%%%%%%%%%%%%%%
    
    addpath(genpath('..\Process Data'));
    addpath(genpath('..\Preprocessing'));
    
    raw_data = cutDataPredict(file_path);
    preprocessing_result_v = preProcessingPredict(raw_data,preprocessing_method,channel_v,fb_v,features_v);
    preprocessing_result_a = preProcessingPredict(raw_data,preprocessing_method,channel_a,fb_a,features_a);

    % Find Valence
    datasets = getDatasetsPrediction(project_path,preprocessing_method,'valence');
    label = separateClassPrediction(project_path,preprocessing_method,'valence');
    [datasets,label] = getTwoClass(datasets,label);
    valence = predictClassification(preprocessing_result_v,datasets,label,classification_method);
    
    % Find Arousal
    datasets = getDatasetsPrediction(project_path,preprocessing_method,'arousal');
    label = separateClassPrediction(project_path,preprocessing_method,'arousal');
    [datasets,label] = getTwoClass(datasets,label);
    arousal = predictClassification(preprocessing_result_a,datasets,label,classification_method);
end