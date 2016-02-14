function [sum_ch_arousal,sum_ch_valence,sum_fb_arousal,sum_fb_valence,sum_sb_arousal,sum_sb_valence] = processCorrelation(correlation_data)
    th = 0.35;

    subjects = size(correlation_data);
    subjects = subjects(1);

    fb_valence = zeros(subjects,5);
    fb_arousal = zeros(subjects,5);

    ch_valence = zeros(subjects,14);
    ch_arousal = zeros(subjects,14);

    correlation_data = abs(correlation_data);

    for i = 1:subjects
        correlation_value = reshape(correlation_data(i,1,:,:),14,5);
        idx_corr = correlation_value<th;
        correlation_value(idx_corr)=0;
        fb_valence(i,:) = sum(correlation_value);
    end

    for i = 1:subjects
        correlation_value = reshape(correlation_data(i,2,:,:),14,5);
        idx_corr = correlation_value<th;
        correlation_value(idx_corr)=0;
        fb_arousal(i,:) = sum(correlation_value);
    end

    for i = 1:subjects
        correlation_value = transpose(reshape(correlation_data(i,1,:,:),14,5));
        idx_corr = correlation_value<th;
        correlation_value(idx_corr)=0;
        ch_valence(i,:) = sum(correlation_value);
    end

    for i = 1:subjects
        correlation_value = transpose(reshape(correlation_data(i,2,:,:),14,5));
        idx_corr = correlation_value<th;
        correlation_value(idx_corr)=0;
        ch_arousal(i,:) = sum(correlation_value);
    end

    sum_ch_arousal = sum(ch_arousal);
    sum_ch_valence = sum(ch_valence);
    sum_fb_arousal = sum(fb_arousal);
    sum_fb_valence = sum(fb_valence);
    sum_sb_arousal = sum(fb_arousal,2);
    sum_sb_valence = sum(fb_valence,2);
end