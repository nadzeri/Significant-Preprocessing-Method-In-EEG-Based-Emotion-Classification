function [sum_ch_arousal,sum_ch_valence,sum_fb_arousal,sum_fb_valence,sum_sb_arousal,sum_sb_valence] = statisticalAnalysis(method)
    project_path = strcat(pwd,'\..\..');
    method = 'fft';%'ica_fft','swt','ica_swt';
    %%%%%%%%%%%%%%%
    
    if strcmp(method,'ica_fft')||strcmp(method,'ica_swt')
        if exist(strcat(project_path,'\ICA_EEG'), 'dir')==0
            addpath(genpath('..\Preprocessing'));
            computeICA(project_path);
        end
    end
    
    absolute_power = absolute(project_path,method);
    correlation_data = correlation(project_path,absolute_power);
    [sum_ch_arousal,sum_ch_valence,sum_fb_arousal,sum_fb_valence,sum_sb_arousal,sum_sb_valence] = processCorrelation(correlation_data);
end