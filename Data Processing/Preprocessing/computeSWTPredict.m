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

function data = computeSWTPredict(raw_data,preprocessing_method,channel,fb,features)
    %define variable
    if strcmp(preprocessing_method,'ica_swt')
        raw_data = computeICAPredict(raw_data);
    end
    
    counter=1;
    data=[];
    for j = channel
        [swa,swd] = swt(raw_data(j,:),5,'db4');
        d2=swd(2,:);
        d3=swd(3,:);
        d4=swd(4,:);
        d5=swd(5,:);
        a5=swa(5,:);
        
        if counter==1
            set(gcf,'Visible','off');
            plot(a5);
            print -dpng '../../Web App/img/swt/a5.png';
            
            set(gcf,'Visible','off');
            plot(d5);
            print -dpng '../../Web App/img/swt/d5.png';
            
            set(gcf,'Visible','off');
            plot(d4);
            print -dpng '../../Web App/img/swt/d4.png';
            
            set(gcf,'Visible','off');
            plot(d3);
            print -dpng '../../Web App/img/swt/d3.png';
            
            set(gcf,'Visible','off');
            plot(d2);
            print -dpng '../../Web App/img/swt/d2.png';
        end
        
        counter=2;

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
end