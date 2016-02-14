%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Author : Muhammad Nadzeri Munawar
%         
%
%This code is to create absolute_power variable of subject no. 20 such as :
%delta, theta, alpha, beta, gamma with shape 32x5x40. 32 mean total of
%channel, 5 mean total absolute power, 40 mean 40 trial
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
function absolute_power = absolute(project_path,method)

    % define initial variable
    if strcmp(method,'fft') || strcmp(method,'swt')
        basePath = strcat(project_path,'\USED_EEG\');
    elseif strcmp(method,'ica_fft') || strcmp(method,'ica_swt')
        basePath = strcat(project_path,'\ICA_EEG\');
    end
    all_files = dir(basePath);
    all_files = all_files(3:end);
    all_dir = all_files([all_files(:).isdir]);
    subjects = numel(all_dir);
    channel = 14;%define total channel
    samplingFrequency = 128;

    for h = 1:subjects
        directory = sprintf('S%02d',h);

        allList = dir( strcat(basePath,directory ));
        allFiles = { allList(3:end).name };

        %looping trial for define absolut power for each trial
        for i = 1:length(allFiles)

            %looping channel for compute absolute power for each channel
            for j = 1:channel

                %open spesific file according trial and channel
                %Contain each channel per file (In this case subject no. 20)
                X = csvread(strcat(basePath,directory,'\T',num2str(i),'.csv'));
                X = X(j,:);
                
                if strcmp(method,'swt')||strcmp(method,'ica_swt')
                    [swa,swd] = swt(X,5,'db4');
                    
                    d2=swd(2,:);
                    d3=swd(3,:);
                    d4=swd(4,:);
                    d5=swd(5,:);
                    a5=swa(5,:);

                    absolute_power(h,j,1,i) = mean(d2)+std(d2)+min(d2)+max(d2);
                    absolute_power(h,j,2,i) = mean(d3)+std(d3)+min(d3)+max(d3);
                    absolute_power(h,j,3,i) = mean(d4)+std(d4)+min(d4)+max(d4);
                    absolute_power(h,j,4,i) = mean(d5)+std(d5)+min(d5)+max(d5);
                    absolute_power(h,j,5,i) = mean(a5)+std(a5)+min(a5)+max(a5);
%                     absolute_power(h,j,1,i) = sum(d2.^2);
%                     absolute_power(h,j,2,i) = sum(d3.^2);
%                     absolute_power(h,j,3,i) = sum(d4.^2);
%                     absolute_power(h,j,4,i) = sum(d5.^2);
%                     absolute_power(h,j,5,i) = sum(a5.^2);
                    
                elseif strcmp(method,'fft')||strcmp(method,'ica_fft')
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
                    beta = P1(L*13/Fs:L*30/Fs);
                    gamma = P1(L*30/Fs:L*50/Fs);

                    delta = mean(delta)+std(delta)+min(delta)+max(delta);
                    theta = mean(theta)+std(theta)+min(theta)+max(theta);
                    alpha = mean(alpha)+std(alpha)+min(alpha)+max(alpha);
                    beta  = mean(beta)+std(beta)+min(beta)+max(beta);
                    gamma = mean(gamma)+std(gamma)+min(gamma)+max(gamma);
                    
%                     delta = max(delta)+std(delta);
%                     theta = max(delta)+std(theta);
%                     alpha = max(delta)+std(alpha);
%                     beta  = max(delta)+std(beta);
%                     gamma = max(delta)+std(gamma);

                    %Create absolute power
                    %Each channel create absolute power (delta,theta,alpha,beta,gamma)
                    %from each trial
                    absolute_power(h,j,1,i) = delta;
                    absolute_power(h,j,2,i) = theta;
                    absolute_power(h,j,3,i) = alpha;
                    absolute_power(h,j,4,i) = beta;
                    absolute_power(h,j,5,i) = gamma;
                end
            end
        end
    end
end