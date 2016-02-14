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

function result = preProcessingPredict(raw_data,preprocessing_method,channel,fb,features)
    if strcmp(preprocessing_method,'fft') || strcmp(preprocessing_method,'ica_fft')
        result = computeFFTPredict(raw_data,preprocessing_method,channel,fb,features);
    elseif strcmp(preprocessing_method,'swt') || strcmp(preprocessing_method,'ica_swt')
        result = computeSWTPredict(raw_data,preprocessing_method,channel,fb,features);
    end
end