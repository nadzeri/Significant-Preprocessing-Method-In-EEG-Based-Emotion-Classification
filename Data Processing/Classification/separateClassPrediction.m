function label = separateClassPrediction(project_path,method,class)
    kelas = csvread(strcat(project_path,'\Metadata\kelas_',method,'_',class,'.csv'));
    
    for i = 1:length(kelas)
        if(kelas(i)<=4)
            label(i) = 1;
        elseif (kelas(i)>=6)
            label(i) = 3;
        else
            label(i) = 2;
        end
    end
end

