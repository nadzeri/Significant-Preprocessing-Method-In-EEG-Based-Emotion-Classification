%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Author : Muhammad Nadzeri Munawar
%         
%
%This code is to create absolute_power variable of subject no. 20 such as :
%delta, theta, alpha, beta, gamma with shape 32x5x40. 32 mean total of
%channel, 5 mean total absolute power, 40 mean 40 trial
%
% project_path -> 'D:\TUGAS AKHIR\Progress\24. (08-12-2015)'
% method -> fft;ica_fft;swt;ica_swt
% subject -> [2,4,6,7,8,9,10,13,15,16,21,25,26,28,29,30];
% channel -> [2,3,4,5,6,7,8,14];
% fb -> for fft : 1.Delta;2.Theta;3.Alpha;4.Beta;5.Gamma - for swt : 1.A5;2.D5;3.D4;4.D3;5.D2
% features -> 1. Min;2.Max;3.Std;4.Avg;5.Pow;6.Energy
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function preProcessing(project_path,method,class,subject,channel,fb,features)
    
    %%%%%%%%%%%%%%
    project_path = strcat(pwd,'\..\..');
    method='fft';%'ica_fft','swt','ica_swt';
    
%     class='arousal';%'valence';
%     subject = 1:34;
    fb = 1:5;
    features = 3:4;
    channel = 1:14;
    
    %Arousal
    class='arousal';%'valence';
    subject = [16,13,10,28,11,7,6,2,20,26,29,15,4,30,5,34,9,24,8,23];
%     fb = [3,4,5];
%     features = [2,3];
%     channel = [3,13,10,2,1,12,4,7,8,11];

    %Valence
%     class='valence';%'valence';
%     subject = [16,25,34,9,5,4,20,28,2,6,32,29,15,10,22,11,8,1,31,13];
%     fb = [3,4,5];
%     features = [2,3];
%     channel = [10,3,14,5,1,8,6,4,7,11];

    %%%%%%%%%%%%%%%
      
    if strcmp(method,'fft')
        computeFFT(project_path,method,class,subject,channel,fb,features);
    elseif strcmp(method,'ica_fft')
        if exist(strcat(project_path,'\ICA_EEG'), 'dir')==0
            computeICA(project_path);
        end
        computeFFT(project_path,method,class,subject,channel,fb,features);
    elseif strcmp(method,'swt')
        computeSWT(project_path,method,class,subject,channel,fb,features);
    elseif strcmp(method,'ica_swt')
        if exist(strcat(project_path,'\ICA_EEG'), 'dir')==0
            computeICA(project_path);
        end
        computeSWT(project_path,method,class,subject,channel,fb,features);
    end
end