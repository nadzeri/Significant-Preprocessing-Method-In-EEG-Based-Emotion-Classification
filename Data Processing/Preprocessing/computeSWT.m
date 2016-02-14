%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Author : Muhammad Nadzeri Munawar
%         
%
%This code is to create absolute_power variable of subject no. 20 such as :
%delta, theta, alpha, beta, gamma with shape 32x5x40. 32 mean total of
%channel, 5 mean total absolute power, 40 mean 40 trial
%
% project_path -> 'D:\TUGAS AKHIR\Progress\24. (08-12-2015)'
% method -> swt;ica_swt
% subject -> [2,4,6,7,8,9,10,13,15,16,21,25,26,28,29,30];
% channel -> [2,3,4,5,6,7,8,14];
% fb -> 1.A5;2.D5;3.D4;4.D3;5.D2
% features -> 1. Min;2.Max;3.Std;4.Avg;5.Pow;6.Energy
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function computeSWT(project_path,method,class,subject,channel,fb,features)
    addpath(genpath('..\Global Code'));

    %define variable
    if strcmp(method,'swt')
        basePath = strcat(project_path,'\USED_EEG\');
        destination = strcat(project_path,'\SWT_EEG_',upper(class));
    elseif strcmp(method,'ica_swt')
        basePath = strcat(project_path,'\ICA_EEG\');
        destination = strcat(project_path,'\ICA_SWT_EEG_',upper(class));
    end
    kuesioner = csvread(strcat(project_path,'\Metadata\newDataKuesioner.csv'));
    kuesioner = transpose(kuesioner);
    samplingFrequency=128;
    counter =1;
    start = 1;
    stop = 0;
    kelas = [];
    
    if strcmp(class,'valence')
        kuesioner = kuesioner(1,:);
    elseif strcmp(class,'arousal')
        kuesioner = kuesioner(2,:);
    end
    
    if exist(destination, 'dir')
        system(strcat('rmdir /S /Q "',destination,'"'));
    end
    
    createFolder(length(subject),destination);
    
    all_files = dir(basePath);
    all_files = all_files(3:end);
    all_dir = all_files([all_files(:).isdir]);
    totalSubject = numel(all_dir);

    for h=1:totalSubject
        directory = sprintf('S%02d',h);
        direc = sprintf('S%02d',counter);
        allList = dir( strcat(basePath,directory ));
        allFiles = { allList(3:end).name };
        trial = length(allFiles);

        if h>1
            start = stop + 1;
        end
        stop = start + trial - 1;

        if ismember(h,subject)==0
            continue;
        end

        kelas = horzcat(kelas,kuesioner(start:stop));

        for i = 1:trial
            rawData = csvread(strcat(basePath,directory,'\T',num2str(i),'.csv'));
            data = [];
            for j = channel
                [swa,swd] = swt(rawData(j,:),5,'db4');
                d2=swd(2,:);
                d3=swd(3,:);
                d4=swd(4,:);
                d5=swd(5,:);
                a5=swa(5,:);
                
                data_feature = [];
                
                if ismember(1,fb)
                    if ismember(1,features)
                        data_feature = [data_feature,min(a5)];
                    end
                    if ismember(2,features)
                        data_feature = [data_feature,max(a5)];
                    end
                    if ismember(3,features)
                        data_feature = [data_feature,std(a5)];
                    end
                    if ismember(4,features)
                        data_feature = [data_feature,mean(a5)];
                    end
                    if ismember(5,features)
                        data_feature = [data_feature,mean(a5.^2)];
                    end
                    if ismember(6,features)
                        data_feature = [data_feature,sum(a5.^2)];
                    end
                end    
                if ismember(2,fb)
                    if ismember(1,features)
                        data_feature = [data_feature,min(d5)];
                    end
                    if ismember(2,features)
                        data_feature = [data_feature,max(d5)];
                    end
                    if ismember(3,features)
                        data_feature = [data_feature,std(d5)];
                    end
                    if ismember(4,features)
                        data_feature = [data_feature,mean(d5)];
                    end
                    if ismember(5,features)
                        data_feature = [data_feature,mean(d5.^2)];
                    end
                    if ismember(6,features)
                        data_feature = [data_feature,sum(d5.^2)];
                    end
                end
                if ismember(3,fb)
                    if ismember(1,features)
                        data_feature = [data_feature,min(d4)];
                    end
                    if ismember(2,features)
                        data_feature = [data_feature,max(d4)];
                    end
                    if ismember(3,features)
                        data_feature = [data_feature,std(d4)];
                    end
                    if ismember(4,features)
                        data_feature = [data_feature,mean(d4)];
                    end
                    if ismember(5,features)
                        data_feature = [data_feature,mean(d4.^2)];
                    end
                    if ismember(6,features)
                        data_feature = [data_feature,sum(d4.^2)];
                    end
                end
                if ismember(4,fb)
                    if ismember(1,features)
                        data_feature = [data_feature,min(d3)];
                    end
                    if ismember(2,features)
                        data_feature = [data_feature,max(d3)];
                    end
                    if ismember(3,features)
                        data_feature = [data_feature,std(d3)];
                    end
                    if ismember(4,features)
                        data_feature = [data_feature,mean(d3)];
                    end
                    if ismember(5,features)
                        data_feature = [data_feature,mean(d3.^2)];
                    end
                    if ismember(6,features)
                        data_feature = [data_feature,sum(d3.^2)];
                    end
                end
                if ismember(5,fb)
                    if ismember(1,features)
                        data_feature = [data_feature,min(d2)];
                    end
                    if ismember(2,features)
                        data_feature = [data_feature,max(d2)];
                    end
                    if ismember(3,features)
                        data_feature = [data_feature,std(d2)];
                    end
                    if ismember(4,features)
                        data_feature = [data_feature,mean(d2)];
                    end
                    if ismember(5,features)
                        data_feature = [data_feature,mean(d2.^2)];
                    end
                    if ismember(6,features)
                        data_feature = [data_feature,sum(d2.^2)];
                    end
                end
                data = horzcat(data,data_feature);
            end
            csvwrite(strcat(destination,'\',direc,'\T',num2str(i),'.csv'),data);
        end
        counter=counter+1;
    end
    if strcmp(method,'swt')
        csvwrite(strcat(project_path,'\Metadata\kelas_swt_',class,'.csv'),kelas);
    elseif strcmp(method,'ica_swt')
        csvwrite(strcat(project_path,'\Metadata\kelas_ica_swt_',class,'.csv'),kelas);
    end
end