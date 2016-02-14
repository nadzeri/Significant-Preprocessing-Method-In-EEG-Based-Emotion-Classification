%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Author : Muhammad Nadzeri Munawar
%         
%
%This code is to create absolute_power variable of subject no. 20 such as :
%delta, theta, alpha, beta, gamma with shape 32x5x40. 32 mean total of
%channel, 5 mean total absolute power, 40 mean 40 trial
%
% project_path -> 'D:\TUGAS AKHIR\Progress\24. (08-12-2015)'
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function computeICA(project_path)
    addpath(genpath('pca_ica'));
    addpath(genpath('..\Global Code'));
    basePath = strcat(project_path,'\USED_EEG\');
    all_files = dir(basePath);
    all_files = all_files(3:end);
    all_dir = all_files([all_files(:).isdir]);
    subject = numel(all_dir);
    
    if exist(strcat(project_path,'\ICA_EEG'), 'dir')
        system(strcat('rmdir /S /Q "',project_path,'\ICA_EEG"'));
    end
    
    createFolder(subject,strcat(project_path,'\ICA_EEG'));

    for h=1:subject
        directory = sprintf('S%02d',h);
        allList = dir( strcat(basePath,directory ));
        allFiles = { allList(3:end).name };
        trial = length(allFiles);

        for i = 1:trial
            rawData = csvread(strcat(basePath,directory,'\T',num2str(i),'.csv'));
            rawData = myICA(rawData,14);
            csvwrite(strcat(project_path,'\ICA_EEG\',directory,'\T',num2str(i),'.csv'),rawData);
        end
    end
end