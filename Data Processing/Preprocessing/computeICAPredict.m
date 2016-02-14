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

function ica_data = computeICAPredict(raw_data)
    addpath(genpath('pca_ica'));
    
    ica_data = myICA(raw_data,14);
    
    for i=1:14
        path = strcat('../../Web App/img/ica/',num2str(i),'.png');

        set(gcf,'Visible','off');
        plot(ica_data(i,:));
        print(path,'-dpng');
    end
end