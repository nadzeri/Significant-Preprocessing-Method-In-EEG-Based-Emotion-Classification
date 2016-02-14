%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Author : Muhammad Nadzeri Munawar
%         
%
%This code is to create absolute_power variable of subject no. 20 such as :
%delta, theta, alpha, beta, gamma with shape 32x5x40. 32 mean total of
%channel, 5 mean total absolute power, 40 mean 40 trial
%
% project_path -> 'D:\TUGAS AKHIR\Progress\24. (08-12-2015)'
% method -> fft;ica_fft
% subject -> [2,4,6,7,8,9,10,13,15,16,21,25,26,28,29,30];
% channel -> [2,3,4,5,6,7,8,14];
% fb -> 1.Delta;2.Theta;3.Alpha;4.Beta;5.Gamma
% features -> 1. Min;2.Max;3.Std;4.Avg;5.Pow;6.Energy
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function computeFFT(project_path,method,class,subject,channel,fb,features)
    addpath(genpath('..\Global Code'));
    
    %define variable
    if strcmp(method,'fft')
        basePath = strcat(project_path,'\USED_EEG\');
        destination = strcat(project_path,'\FFT_EEG_',upper(class));
    elseif strcmp(method,'ica_fft')
        basePath = strcat(project_path,'\ICA_EEG\');
        destination = strcat(project_path,'\ICA_FFT_EEG_',upper(class));
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
    total_subject = numel(all_dir);
    
    for h=1:total_subject
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
                X = rawData(j,:);

                Fs = samplingFrequency;  % Sampling frequency
                L = length(X);             % Length of signal

                %compute fft from channel
                Y = fft(X);

                %Divide fft to get frequency
                P2 = abs(Y/L);
                P1 = P2(1:L/2+1);
                P1(2:end-1) = 2*P1(2:end-1);

                %divide froquency to get delta, theta, alpha, beta, gamma
                %And average all of each range (delta, theta, alpha, beta, gamma) 
                delta = P1(L*1/Fs:L*4/Fs);
                theta = P1(L*4/Fs:L*8/Fs);
                alpha = P1(L*8/Fs:L*13/Fs);
                beta  = P1(L*13/Fs:L*30/Fs);
                gamma = P1(L*30/Fs:L*50/Fs);
                
                data_feature = [];
                
                if ismember(1,fb)
                    if ismember(1,features)
                        data_feature = [data_feature,min(delta)];
                    end
                    if ismember(2,features)
                        data_feature = [data_feature,max(delta)];
                    end
                    if ismember(3,features)
                        data_feature = [data_feature,std(delta)];
                    end
                    if ismember(4,features)
                        data_feature = [data_feature,mean(delta)];
                    end
                    if ismember(5,features)
                        data_feature = [data_feature,mean(delta.^2)];
                    end
                    if ismember(6,features)
                        data_feature = [data_feature,sum(delta.^2)];
                    end
                end    
                if ismember(2,fb)
                    if ismember(1,features)
                        data_feature = [data_feature,min(theta)];
                    end
                    if ismember(2,features)
                        data_feature = [data_feature,max(theta)];
                    end
                    if ismember(3,features)
                        data_feature = [data_feature,std(theta)];
                    end
                    if ismember(4,features)
                        data_feature = [data_feature,mean(theta)];
                    end
                    if ismember(5,features)
                        data_feature = [data_feature,mean(theta.^2)];
                    end
                    if ismember(6,features)
                        data_feature = [data_feature,sum(theta.^2)];
                    end
                end
                if ismember(3,fb)
                    if ismember(1,features)
                        data_feature = [data_feature,min(alpha)];
                    end
                    if ismember(2,features)
                        data_feature = [data_feature,max(alpha)];
                    end
                    if ismember(3,features)
                        data_feature = [data_feature,std(alpha)];
                    end
                    if ismember(4,features)
                        data_feature = [data_feature,mean(alpha)];
                    end
                    if ismember(5,features)
                        data_feature = [data_feature,mean(alpha.^2)];
                    end
                    if ismember(6,features)
                        data_feature = [data_feature,sum(alpha.^2)];
                    end
                end
                if ismember(4,fb)
                    if ismember(1,features)
                        data_feature = [data_feature,min(beta)];
                    end
                    if ismember(2,features)
                        data_feature = [data_feature,max(beta)];
                    end
                    if ismember(3,features)
                        data_feature = [data_feature,std(beta)];
                    end
                    if ismember(4,features)
                        data_feature = [data_feature,mean(beta)];
                    end
                    if ismember(5,features)
                        data_feature = [data_feature,mean(beta.^2)];
                    end
                    if ismember(6,features)
                        data_feature = [data_feature,sum(beta.^2)];
                    end
                end
                if ismember(5,fb)
                    if ismember(1,features)
                        data_feature = [data_feature,min(gamma)];
                    end
                    if ismember(2,features)
                        data_feature = [data_feature,max(gamma)];
                    end
                    if ismember(3,features)
                        data_feature = [data_feature,std(gamma)];
                    end
                    if ismember(4,features)
                        data_feature = [data_feature,mean(gamma)];
                    end
                    if ismember(5,features)
                        data_feature = [data_feature,mean(gamma.^2)];
                    end
                    if ismember(6,features)
                        data_feature = [data_feature,sum(gamma.^2)];
                    end
                end
                data = horzcat(data,data_feature);
            end
            csvwrite(strcat(destination,'\',direc,'\T',num2str(i),'.csv'),data);
        end
        counter=counter+1;
    end
    if strcmp(method,'fft')
        csvwrite(strcat(project_path,'\Metadata\kelas_fft_',class,'.csv'),kelas);
    elseif strcmp(method,'ica_fft')
        csvwrite(strcat(project_path,'\Metadata\kelas_ica_fft_',class,'.csv'),kelas);
    end
    
end