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

function data = computeFFTPredict(raw_data,preprocessing_method,channel,fb,features)
    %define variable
    if strcmp(preprocessing_method,'ica_fft')
        raw_data = computeICAPredict(raw_data);
    end
    samplingFrequency=128;

    data = [];
    counter=1;
    for j = channel
        X = raw_data(j,:);

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
        
        if counter==1
            set(gcf,'Visible','off');
            plot(delta);
            print -dpng '../../Web App/img/fft/delta.png';
            
            set(gcf,'Visible','off');
            plot(theta);
            print -dpng '../../Web App/img/fft/theta.png';
            
            set(gcf,'Visible','off');
            plot(alpha);
            print -dpng '../../Web App/img/fft/alpha.png';
            
            set(gcf,'Visible','off');
            plot(beta);
            print -dpng '../../Web App/img/fft/beta.png';
            
            set(gcf,'Visible','off');
            plot(gamma);
            print -dpng '../../Web App/img/fft/gamma.png';
        end
        
        counter = 2;
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
end