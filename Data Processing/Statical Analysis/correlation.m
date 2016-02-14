function correlation_data = correlation(project_path,absolute_power)
    basePath = strcat(project_path,'\USED_EEG\');

    kuesioner = csvread(strcat(project_path,'\Metadata\newDataKuesioner.csv'));
    kuesioner = transpose(kuesioner);
    start = 0;
    stop = 0;
    
    subject = size(absolute_power);
    subject = subject(1);
    
    for h=1:subject
        directory = sprintf('S%02d',h);
        allList = dir( strcat(basePath,directory ));
        allFiles = { allList(3:end).name };
        trial = length(allFiles);

        start = stop+1;
        stop = stop + trial;

        for k=1:2
            for i=1:14
                for j=1:5
                    temp = corrcoef(kuesioner(k,start:stop), reshape(absolute_power(h,i,j,1:trial),1,trial));
                    correlation_data(h,k,i,j) = temp(1,2);
                end
            end
        end
    end
end